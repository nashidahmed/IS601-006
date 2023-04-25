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
    if form.validate_on_submit:
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
