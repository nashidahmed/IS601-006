from flask import Blueprint, redirect, request, render_template, url_for, flash
from sql.db import DB
from products.forms import SearchForm
from cart.forms import AddForm
from categories.forms import AddCategoryForm, EditCategoryForm
from admin.permissions import admin_owner_permission
categories = Blueprint('categories', __name__, url_prefix='/categories', template_folder='templates')

@categories.route('/add', methods=['GET', 'POST'])
@admin_owner_permission.require(http_exception=403)
def add():
    form = AddCategoryForm()
    if form.validate_on_submit():
        name = form.name.data
        if name:
            try:
                result = DB.insertOne(
                    "INSERT INTO IS601_Shop_Categories (name) VALUES(%s)", name)
                if result.status:
                    flash("Added new category", "success")
            except Exception as e:
                flash("Category already exists", "danger")

    return render_template("category.html", form=form)

@categories.route('/edit', methods=['GET', 'POST'])
@admin_owner_permission.require(http_exception=403)
def edit():
    id = request.args.get("id")
    form = EditCategoryForm()
    if form.validate_on_submit():
        name = form.name.data
        if name:
            try:
                result = DB.insertOne(
                    "UPDATE IS601_Shop_Categories SET name = %s WHERE id = %s", name, id)
                if result.status:
                    flash("Edited category", "success")
            except Exception as e:
                flash("Category already exists", "danger")
    try:
        result = DB.selectOne("SELECT name from IS601_Shop_Categories WHERE id = %s", id)
        if result.status and result.row:
            row = result.row
            form = EditCategoryForm(**row)
    except Exception as e:
        flash("Error getting category", "danger")
    return render_template("category.html", form=form)

@categories.route("/view", methods=["GET"])
@admin_owner_permission.require(http_exception=403)
def view():
    rows = [] 
    try:
        result = DB.selectAll("SELECT id, name FROM IS601_Shop_Categories",)
        if result.status and result.rows:
            rows = result.rows
    except Exception as e:
        print(e)
        flash("Error getting categories", "danger")

    return render_template("view_categories.html", rows=rows)

@categories.route("/delete", methods=["GET"])
@admin_owner_permission.require(http_exception=403)
def delete():
    id = request.args.get("id")
    if id:
        try:
            result = DB.delete("DELETE FROM IS601_Shop_Categories WHERE id = %s", id)
            if result.status:
                flash("Deleted category", "success")
        except Exception as e:
            print(e)
            flash("Could not delete category", "danger")
    else:
        flash("No id present", "warning")
    return redirect(url_for("categories.view"))
