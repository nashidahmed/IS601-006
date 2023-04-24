from flask import Blueprint, redirect, request, render_template, url_for, flash
from sql.db import DB
from products.forms import SearchForm
from cart.forms import AddForm
from products.forms import AddProductForm, EditProductForm, SearchForm
from admin.permissions import admin_owner_permission
shop = Blueprint('shop', __name__, url_prefix='/')

@shop.route('/', methods=['GET'])
def view_all():
    search = request.args.get('search')
    col = request.args.get('col')
    order = request.args.get('order')
    form = SearchForm(search = search, col = col, order = order)
    args = []
    query = "SELECT id, name, description, stock, cost, image from IS601_Shop_Products WHERE is_visible=1"
    if search:
        query += " AND name like %s"
        args.append(f"%{search}%")
    if col and order:
        if col in ["name","cost"] \
            and order in ["asc", "desc"]:
            query += f" ORDER BY {col} {order}"
    rows = []
    try:
        resp = DB.selectAll(query, *args)
        if resp.status:
            rows = resp.rows
    except Exception as e:
        # TODO make this user-friendly
        flash(str(e), "danger")
    
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
    if form.validate_on_submit:
        name = form.name.data
        description = form.description.data
        stock = form.stock.data
        cost = form.cost.data
        image = form.image.data
        if name and description and stock and cost:
            try:
                result = DB.insertOne("UPDATE IS601_Shop_Products SET name = %s, description = %s, stock = %s, cost = %s, image = %s WHERE id = %s", name, description, stock, cost, image, id)
                if result.status:
                    flash("Updated product", "success")
            except Exception as e:
                flash(f"Could not update product id: {id}", "danger")
    try:
        resp = DB.selectOne("SELECT id, name, description, stock, cost, image from IS601_Shop_Products WHERE id = %s", id)
        if resp.status:
            row = resp.row
            form = EditProductForm(**row)
    except Exception as e:
        flash(f"Could not get product id: {id}", "danger")

    return render_template("product.html", form=form, is_edit = True)
