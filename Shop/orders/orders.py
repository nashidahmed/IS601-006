import traceback
from flask import Blueprint, flash, render_template, request, redirect, url_for
from sql.db import DB
from orders.forms import PaymentForm
from flask_login import login_required, current_user
orders = Blueprint('orders', __name__, url_prefix='/orders',template_folder='templates')

@orders.route("/checkout", methods=["GET"])
@login_required
def view():
    form = PaymentForm()
    rows = []
    can_refresh = False
    try:
        result = DB.selectAll("""SELECT c.id, product_id, name, c.quantity, c.cost as cart_cost, p.cost as product_cost, (c.quantity * c.cost) as cart_subtotal, (c.quantity * p.cost) as actual_subtotal, image 
        FROM IS601_Shop_Cart c JOIN IS601_Shop_Products p on c.product_id = p.id
        WHERE c.user_id = %s
        """, current_user.get_id())
        if result and result.rows:
            rows = result.rows
            for product in rows:
                if product["cart_cost"] != product["product_cost"]:
                    can_refresh = True
    except Exception as e:
        print("Error getting cart", e)
        flash("Error fetching cart", "danger")

    if can_refresh:
        flash("The price for some items in your cart have changed, please refresh cart", "warning")
    
    return render_template("checkout.html", rows=rows, form=form, can_refresh=can_refresh)
    
@orders.route("/checkout", methods=["POST"])
@login_required
def pay():
    form = PaymentForm()
    cart = []
    total = 0
    quantity = 0
    order = {}
    amount = round((form.amount.data or 0) * 100)
    address = form.address.data
    method = form.method.data
    first_name = form.first_name.data
    last_name = form.last_name.data
    
    if form.validate_on_submit:
        try:
            DB.getDB().autocommit = False

            # Fetch cart data
            result = DB.selectAll("""SELECT c.id, product_id, name, quantity, stock, c.cost as cart_cost, p.cost as product_cost, (c.quantity * c.cost) as cart_subtotal, (c.quantity * p.cost) as actual_subtotal 
            FROM IS601_Shop_Cart c JOIN IS601_Shop_Products p on c.product_id = p.id
            WHERE c.user_id = %s
            """, current_user.get_id())
            if result.status and result.rows:
                cart = result.rows

            # Verify that there are enough products in stock or if the price has change for the cart items
            has_error = False
            for product in cart:
                if product["quantity"] > product["stock"]:
                    flash(f"There are only {product['stock']} of product {product['name']} left in stock", "warning")
                    has_error = True
                if product["cart_cost"] != product["product_cost"]:
                    flash(f"Product {product['name']}'s price has changed, please refresh cart", "warning")
                    has_error = True
                total += int(product["cart_subtotal"] or 0)
                quantity += int(product["quantity"])

            # Check if user has entered the right amount
            if not has_error:
                balance = int(amount)
                if total > balance:
                    flash("You can't afford to make this purchase", "danger")
                    has_error = True
                elif total < balance:
                    flash("You are paying an amount that is more than required", "danger")
                    has_error = True

            # Create order data
            order_id = -1
            if not has_error:
                result = DB.insertOne("""INSERT INTO IS601_Shop_Orders (user_id, total_price, number_of_products, address, payment_method, money_received, first_name, last_name)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""", current_user.get_id(), total, quantity, address, method, amount, first_name, last_name)
                if not result.status:
                    flash("Error generating order", "danger")
                    DB.getDB().rollback()
                    has_error = True
                else:
                    order_id = int(DB.db.fetch_eof_status()["insert_id"])
                    order["order_id"] = order_id
                    order["total"] = total
                    order["quantity"] = quantity

            # Record order history
            if order_id > -1 and not has_error:
                result = DB.insertOne("""INSERT INTO IS601_Shop_OrderProducts (quantity, cost, order_id, product_id, user_id)
                SELECT quantity, cost, %s, product_id, user_id FROM IS601_Shop_Cart c WHERE c.user_id = %s""",
                order_id, current_user.get_id())
                if not result.status:
                    flash("Error recording order history", "danger")
                    has_error = True
                    DB.getDB().rollback()

            # Update stock based on cart data
            if not has_error:
                result = DB.update("""
                UPDATE IS601_Shop_Products 
                SET stock = stock - (select IFNULL(quantity, 0) FROM IS601_Shop_Cart WHERE product_id = IS601_Shop_Products.id and user_id = %(uid)s) 
                WHERE id in (SELECT product_id from IS601_Shop_Cart where user_id = %(uid)s)
                """, { "uid": current_user.get_id() })
                if not result.status:
                    flash("Error updating stock", "danger")
                    has_error = True
                    DB.getDB().rollback()

            # Empty the cart for this user
            if not has_error:
                result = DB.delete("DELETE FROM IS601_Shop_Cart WHERE user_id = %s", current_user.get_id())

            if not has_error:
                DB.getDB().commit()
                flash("Payment successful!", "success")
            # else:
            #     return redirect(url_for("cart.view"))
                
        except Exception as e:
            print("Transaction exception", e)
            flash(str(e), "danger")
            flash("Something went wrong", "danger")
            traceback.print_exc()
    # TODO route to thank you / summary page
    # TODO add link from cart page to this route
    return redirect(f'/orders/confirmation/{order_id}')

@orders.route("/confirmation/<id>", methods=["GET"])
@orders.route("/<id>", methods=["GET"])
@login_required
def order(id):
    rows = []
    total = 0
    order = {}
    if not id:
        flash("Invalid order", "danger")
        return redirect(url_for("orders.history"))
    try:
        result = DB.selectAll("""
        SELECT name, o.cost as cost, quantity, (o.cost * quantity) as subtotal, image
        FROM IS601_Shop_OrderProducts o
        JOIN IS601_Shop_Products p on o.product_id = p.id
        WHERE order_id = %s AND user_id = %s 
        """, id, current_user.get_id())
        if result.status and result.rows:
            rows = result.rows
            total = sum(int(row["subtotal"]) for row in rows)

        result = DB.selectOne("""
        SELECT id, number_of_products, address, payment_method, money_received, first_name, last_name, created FROM IS601_Shop_Orders WHERE id = %s AND user_id = %s
        """, id, current_user.get_id())
        if result.status and result.row:
            order = result.row
        
    except Exception as e:
        print("Error getting order", e)
        flash(str(e), "danger")
        flash("Error fetching order", "danger")

    return render_template("order.html", rows=rows, order=order, total=total)

@orders.route("/history", methods=["GET"])
@login_required
def history():
    rows = []
    try:
        result = DB.selectAll("""
        SELECT id as order_id, number_of_products, address, payment_method, money_received, first_name, last_name FROM IS601_Shop_Orders WHERE user_id = %s
        """, current_user.get_id())
        if result.status and result.rows:
            rows = result.rows
    except Exception as e:
        print("Error getting orders", e)
        flash(str(e), "danger")
        flash("Error fetching orders", "danger")
    return render_template("history.html", rows=rows)
