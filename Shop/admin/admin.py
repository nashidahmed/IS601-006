from flask import Blueprint, flash, render_template, request, redirect, url_for
from sql.db import DB
from products.forms import AddProductForm, SearchForm
from werkzeug.datastructures import MultiDict
from admin.permissions import admin_owner_permission
admin = Blueprint('admin', __name__, url_prefix='/admin',template_folder='templates')

@admin.route('product/add', methods=['GET', 'POST'])
@admin_owner_permission.require(http_exception=403)
def add():
    form = AddProductForm(is_visible = True)
    if request.method == 'POST' and form.validate_on_submit:
      name = form.name.data
      description = form.description.data
      category = form.category.data
      stock = form.stock.data
      cost = round((form.cost.data or 0) * 100)
      image = form.image.data
      is_visible = 1 if form.is_visible.data else 0
      if name and description and category and stock and cost:
          try:
              result = DB.insertOne("INSERT INTO IS601_Shop_Products (name, description, stock, cost, image, is_visible) VALUES(%s, %s, %s, %s, %s, %s)", name, description, stock, cost, image, is_visible)
              if result.status:
                  flash("Added product", "success")
          except Exception as e:
              print(e.args[0])
              if '1062' in str(e):
                  flash('Duplicate data. Product name may already exist', 'danger')
              else:
                  flash("Unable to add product", "danger")
      elif stock == 0:
            flash('Stock cannot be 0', 'danger')
      elif cost == 0:
          flash('Cost cannot be 0', 'danger')
      else:
          flash('Please check your input', 'danger')
      
    categories = []
    try:
      result = DB.selectAll("SELECT id, name FROM IS601_Shop_Categories",)
      if result.status and result.rows:
          categories = [(category['id'], category['name']) for category in result.rows]
          form.category.choices.extend(categories)
    except Exception as e:
      print(e)
      flash("Unable to get categories", "danger")

    return render_template("product.html", form=form)

@admin.route("/products", methods=["GET"])
@admin_owner_permission.require(http_exception=403)
def products():
    search = request.args.get('search')
    category = request.args.get('category')
    col = request.args.get('col')
    order = request.args.get('order')
    form = SearchForm(search = search, category = category, col = col, order = order)
    args = []
    query = "SELECT id, name, description, stock, cost, image, is_visible from IS601_Shop_Products WHERE 1=1"
    if search:
        query += " AND name like %s"
        args.append(f"%{search}%")
    if category:
        query += " AND category_id = %s"
        args.append(f"{category}")
    if col and order:
        if col in ["name","cost"] \
            and order in ["asc", "desc"]:
            query += f" ORDER BY {col} {order}"
    rows = []
    categories = []
    try:
        print(query)
        resp = DB.selectAll(query, *args)
        if resp.status:
            rows = resp.rows
    except Exception as e:
        flash("Unable to retieve products", "danger")
    
    try:
        result = DB.selectAll("SELECT id, name FROM IS601_Shop_Categories",)
        if result.status and result.rows:
            categories = [(category['id'], category['name']) for category in result.rows]
            form.category.choices.extend(categories)
    except Exception as e:
        print(e)
        flash("Error getting categories", "danger")

    return render_template("view_products.html", resp=rows, form=form, is_admin = True)

@admin.route('/set/visibility/<is_visible>/<product_id>/<name>', methods=['GET'])
@admin_owner_permission.require(http_exception=403)
def set_visibility(is_visible, product_id, name):
    print(is_visible, product_id, name)
    try:
        result = DB.update("""
        UPDATE IS601_Shop_Products SET
        is_visible = %s
        WHERE id = %s
        """, is_visible, product_id)
        if result.status:
            flash(f"{name} is now {'visible' if int(is_visible) else 'invisible'}", "success")
    except Exception as e:
        flash("Could not toggle visibility", "danger")

    return redirect(url_for('admin.products'))

@admin.route("/order-history", methods=["GET"])
@admin_owner_permission.require(http_exception=403)
def order_history():
    rows = []
    try:
        result = DB.selectAll("""
        SELECT o.id as order_id, number_of_products, address, payment_method, money_received, first_name, last_name, u.username
        FROM IS601_Shop_Orders o
        LEFT JOIN IS601_Users u ON o.user_id = u.id
        """)
        if result.status and result.rows:
            rows = result.rows
    except Exception as e:
        print("Error getting orders", e)
        flash(str(e), "danger")
        flash("Error fetching orders", "danger")
    return render_template("history.html", rows=rows)

@admin.route("order/<id>", methods=["GET"])
@admin_owner_permission.require(http_exception=403)
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
        WHERE order_id = %s
        """, id)
        if result.status and result.rows:
            rows = result.rows
            total = sum(int(row["subtotal"]) for row in rows)

        result = DB.selectOne("""
        SELECT o.id, number_of_products, address, payment_method, money_received, first_name, last_name, o.created, u.username
        FROM IS601_Shop_Orders o
        LEFT JOIN IS601_Users u ON o.user_id = u.id
        WHERE o.id = %s
        """, id)
        if result.status and result.row:
            order = result.row
        
    except Exception as e:
        print("Error getting order", e)
        flash(str(e), "danger")
        flash("Error fetching order", "danger")

    return render_template("order.html", rows=rows, order=order, total=total)
