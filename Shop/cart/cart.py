from flask import Blueprint, flash, render_template, request, redirect, url_for
from sql.db import DB
from cart.forms import AddForm
from werkzeug.datastructures import MultiDict
from admin.permissions import admin_permission
from flask_login import login_required, current_user
cart = Blueprint('cart', __name__, url_prefix='/cart',template_folder='templates')

@cart.route("/add", methods=["POST"])
@login_required
def add():
    form = AddForm()
    if form.validate_on_submit:
        product_id = form.product_id.data
        quantity = form.quantity.data
        user_id = current_user.get_id()
        try:
            result = DB.selectOne("SELECT cost,name from IS601_Shop_Products WHERE id = %s", product_id)
            if result.status and result.row:
                cost = result.row["cost"]
                name = result.row["name"]
                result = DB.insertOne("""
                INSERT INTO IS601_Shop_Cart (product_id, quantity, cost, user_id)
                VALUES(%(product_id)s, %(quantity)s, %(cost)s, %(user_id)s)
                ON DUPLICATE KEY UPDATE
                quantity = quantity + %(quantity)s,
                cost = %(cost)s
                """,{
                    "product_id":product_id,
                    "quantity": quantity,
                    "cost":cost,
                    "user_id":user_id
                })
                if result.status:
                    flash(f"Added {quantity} {name} to cart", "success")
        except Exception as e:
            print("Error adding to cart" ,e)
            flash("Error adding to cart", "danger")
        
    return redirect(url_for('shop.view', id = product_id))

@cart.route('/', methods=['GET'])
@login_required
def view():
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
    
    return render_template("cart.html", rows=rows, can_refresh=can_refresh)

@cart.route('/update', methods=['POST'])
@login_required
def update():
    product_id = request.form.get("product_id")
    quantity = request.form.get("quantity", 1, type=int)
    user_id = current_user.get_id()
    if quantity > 0:
        try:
            result = DB.selectOne("SELECT cost,name from IS601_Shop_Products WHERE id = %s", product_id)
            if result.status and result.row:
                cost = result.row["cost"]
                name = result.row["name"]
                result = DB.insertOne("""
                UPDATE IS601_Shop_Cart SET
                quantity = %s,
                cost = %s
                WHERE product_id = %s and user_id = %s
                """, quantity, cost, product_id, user_id)
                if result.status:
                    flash(f"Updated quantity for {name} to {quantity}", "success")
        except Exception as e:
            print("Error updating cart" ,e)
            flash("Error updating cart", "danger")
    elif quantity == 0:
        flash('Quantity cannot be 0, if you want to remove the product, use the delete button', 'danger')
    else:
        flash('Quantity must be more than 0', 'danger')

    return redirect(url_for('cart.view'))

@cart.route('/delete', methods=['POST'])
@login_required
def delete():
    product_id = request.form.get("product_id")
    name = request.form.get("name")
    user_id = current_user.get_id()
    try:
        result = DB.delete("DELETE FROM IS601_Shop_Cart where product_id = %s and user_id = %s", product_id, user_id)
        if result.status:
            flash(f"Deleted {name.lower()} from cart", "success")
    except Exception as e:
        print("Error deleting item", e)
        flash("Error deleting item from cart", "danger")

    return redirect(url_for('cart.view'))

@cart.route('/clear', methods=['POST'])
@login_required
def clear():
    user_id = current_user.get_id()
    try:
        result = DB.delete("DELETE FROM IS601_Shop_Cart WHERE user_id = %s", user_id)
        if result.status:
            flash("Cleared cart", "success")
    except Exception as e:
        print("Error clearing cart", e)
        flash("Error clearing cart", "danger")

    return redirect(url_for('cart.view'))

@cart.route('/refresh/<int:is_cart>', methods=['GET'])
@login_required
def refresh(is_cart):
    user_id = current_user.get_id()
    try:
        result = DB.delete("""
        UPDATE IS601_Shop_Cart c, IS601_Shop_Products p
        SET c.cost = p.cost
        WHERE c.product_id = p.id AND user_id = %s
        """, user_id)
        if result.status:
            flash("Refreshed cart", "success")
    except Exception as e:
        print("Error refreshing cart", e)
        flash(str(e), "danger")
        flash("Error refreshing cart", "danger")

    if is_cart == 1:
        return redirect(url_for('cart.view'))
    elif is_cart == 0:
        return redirect(url_for('orders.view'))
        