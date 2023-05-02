from flask import Blueprint, redirect, request, render_template, url_for, flash
from sql.db import DB
from products.forms import SearchForm
from cart.forms import AddForm
from products.forms import AddProductForm, EditProductForm, SearchForm
from admin.permissions import admin_owner_permission
shop = Blueprint('shop', __name__, url_prefix='/')

# nn379 Apr 24 2023
@shop.route('/', methods=['GET'])
def view_all():
    search = request.args.get('search')
    category = request.args.get('category')
    col = request.args.get('col')
    order = request.args.get('order')
    form = SearchForm(search = search, category = category, col = col, order = order)
    args = []
    query = "SELECT id, name, description, stock, cost, image from IS601_Shop_Products WHERE is_visible=1"
    # Do the filering here by appending the search values to the query.
    # Search and category are done by using where clauses while col and order are used for the sorting logic
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
    print(query)
    try:
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
    
    return render_template("view_products.html", resp=rows, form=form, is_admin = False)


@shop.route('/product/<id>', methods=['GET'])
def view(id):
    form = AddForm(product_id = id)
    try:
        resp = DB.selectOne("SELECT id, name, description, stock, cost, image from IS601_Shop_Products WHERE is_visible=1 AND id = %s", id)
        if resp.status:
            row = resp.row
            print(row)
    except Exception as e:
        flash(f"Could not get product id: {id}", "danger")

    return render_template("view_product.html", resp=row, form=form)
    
@shop.route('edit/<id>', methods=['GET', 'POST'])
@admin_owner_permission.require(http_exception=403)
def edit(id):
    form = EditProductForm()
    if request.method == 'POST' and form.validate_on_submit:
        name = form.name.data
        description = form.description.data
        category = form.category.data
        stock = form.stock.data
        cost = round((form.cost.data or 0) * 100)
        image = form.image.data
        is_visible = 1 if form.is_visible.data else 0
        if name and description and stock and cost:
            try:
                result = DB.insertOne("UPDATE IS601_Shop_Products SET name = %s, description = %s, category_id = %s, stock = %s, cost = %s, image = %s, is_visible = %s WHERE id = %s", name, description, category, stock, cost, image, is_visible, id)
                if result.status:
                    flash("Updated product", "success")
            except Exception as e:
                flash(str(e), 'danger')
                if '1062' in str(e):
                    flash('Duplicate data. Product name may already exist', 'danger')
                else:
                    flash(f"Could not update product id: {id}", "danger")
        elif stock == 0:
            flash('Stock cannot be 0', 'danger')
        elif cost == 0:
            flash('Cost cannot be 0', 'danger')
        else:
            flash('Please check your input', 'danger')

    try:
        resp = DB.selectOne("SELECT id, name, description, category_id as category, stock, cost, image, is_visible from IS601_Shop_Products WHERE id = %s", id)
        if resp.status:
            row = resp.row
            form = EditProductForm(**row)
            form.cost.data = form.cost.data / 100
    except Exception as e:
        flash(f"Could not get product id: {id}", "danger")

    categories = []
    try:
      result = DB.selectAll("SELECT id, name FROM IS601_Shop_Categories",)
      if result.status and result.rows:
          categories = [(category['id'], category['name']) for category in result.rows]
          form.category.choices.extend(categories)
    except Exception as e:
      print(e)
      flash("Could not get categories", "danger")

    return render_template("product.html", form=form, is_edit = True)
