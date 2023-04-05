from flask import Blueprint, redirect, render_template, request, flash, url_for
from sql.db import DB
import re
employee = Blueprint('employee', __name__, url_prefix='/employee')


@employee.route("/search", methods=["GET"])
def search():
    rows = []
    # DO NOT DELETE PROVIDED COMMENTS
    # TODO search-1 retrieve employee id as id, first_name, last_name, email, company_id, company_name using a LEFT JOIN
    query = "SELECT e.id, first_name, last_name, email, company_id, name FROM IS601_MP3_Employees as e LEFT JOIN IS601_MP3_Companies as c ON company_id = c.id WHERE 1=1"
    args = {} # <--- add values to replace %s/%(named)s placeholders
    allowed_columns = ["first_name", "last_name", "email", "company_name"]
    # TODO search-2 get fn, ln, email, company, column, order, limit from request args
    # TODO search-3 append like filter for first_name if provided
    # TODO search-4 append like filter for last_name if provided
    # TODO search-5 append like filter for email if provided
    # TODO search-6 append equality filter for company_id if provided
    # TODO search-7 append sorting if column and order are provided and within the allowed columns and order options (asc, desc)
    # TODO search-8 append limit (default 10) or limit greater than 1 and less than or equal to 100
    # TODO search-9 provide a proper error message if limit isn't a number or if it's out of bounds
    fn = request.args.get('fn')
    ln = request.args.get('ln')
    email = request.args.get('email')
    company = request.args.get('company')
    col = request.args.get("column")
    order = request.args.get("order")
    limit = request.args.get("limit", 10) # TODO change this per the above requirements

    if fn:
      query += " AND first_name like %(first_name)s"
      args['first_name'] = f"%{fn}%"
    if ln:
      query += " AND last_name like %(last_name)s"
      args['last_name'] = f"%{ln}%"
    if email:
      query += " AND email like %(email)s"
      args['email'] = f"%{email}%"
    if company:
      query += " AND company_id = %(company)s"
      args['company'] = company
    if col and order:
        if col in allowed_columns and order in ["asc", "desc"]:
            query += f" ORDER BY {col} {order}"

    if limit and int(limit) >= 1 and int(limit) <= 100:
        # technically this should follow the same rules as col/order
        # but it seems to work with the placeholder mapping with
        # this connector
        query += " LIMIT %(limit)s"
        args['limit'] = int(limit)
    else:
        flash('Limit out of bounds (Limit bound: 0 < Limit <= 100)', 'danger')
        return render_template("list_employees.html", rows=rows, allowed_columns=allowed_columns)
    print("query",query)
    print("args", args)
    try:
        result = DB.selectAll(query, args)
        if result.status:
            rows = result.rows
            print(rows)
    except Exception as e:
        # TODO search-10 make message user friendly
        flash(e, "error")
    # hint: use allowed_columns in template to generate sort dropdown
    # hint2: convert allowed_columns into a list of tuples representing (value, label)
    # do this prior to passing to render_template, but not before otherwise it can break validation
   
    return render_template("list_employees.html", rows=rows, allowed_columns=allowed_columns)

@employee.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        # TODO add-1 retrieve form data for first_name, last_name, company, email
        # TODO add-2 first_name is required (flash proper error message)
        # TODO add-3 last_name is required (flash proper error message)
        # TODO add-4 company (may be None)
        # TODO add-5 email is required (flash proper error message)
        # TODO add-5a verify email is in the correct format
        has_error = False # use this to control whether or not an insert occurs
        fn = request.form.get('fn')
        ln = request.form.get('ln')
        email = request.form.get('email')
        company = request.form.get('company')

        if not fn or not ln or not email or not re.match(r"^\S+@\S+\.\S+$", email):
            if not fn: flash('First name is required', 'danger')
            if not ln: flash('Last name is required', 'danger')
            flash('Email is required', 'danger') if not email else flash('Incorrect email address format', 'danger')
            has_error = True
            
        if not has_error:
            try:
                result = DB.insertOne("INSERT INTO IS601_MP3_Employees (first_name, last_name, company_id, email) VALUES (%s, %s, %s, %s)",
                fn, ln, company, email) # <-- TODO add-6 add query and add arguments
                if result.status:
                    flash("Created Employee Record", "success")
            except Exception as e:
                # TODO add-7 make message user friendly
                flash('Employee was not inserted. Check your input.', "danger")
    return render_template("add_employee.html", request=request)

@employee.route("/edit", methods=["GET", "POST"])
def edit():
    # TODO edit-1 request args id is required (flash proper error message)
    id = request.args.get('id')
    if not id: # TODO update this for TODO edit-1
        flash('Invalid Employee ID', "danger")
        return redirect(url_for('employee.search'))
    else:
        if request.method == "POST":
            
            # TODO edit-1 retrieve form data for first_name, last_name, company, email
            # TODO edit-2 first_name is required (flash proper error message)
            # TODO edit-3 last_name is required (flash proper error message)
            # TODO edit-4 company (may be None)
            # TODO edit-5 email is required (flash proper error message)
            # TODO edit-5a verify email is in the correct format
            has_error = False # use this to control whether or not an insert occurs
            fn = request.form.get('fn')
            ln = request.form.get('ln')
            email = request.form.get('email')
            company = request.form.get('company', None)

            if not fn or not ln or not email or not re.match(r"^\S+@\S+\.\S+$", email):
                if not fn: flash('First name is required', 'danger')
                if not ln: flash('Last name is required', 'danger')
                flash('Email is required', 'danger') if not email else flash('Incorrect email address format', 'danger')
                has_error = True
            
                
            if not has_error:
                try:
                    # TODO edit-6 fill in proper update query
                    result = DB.update("UPDATE IS601_MP3_Employees SET first_name = %s, last_name = %s, email = %s, company_id = %s WHERE id = %s", fn, ln, email, company, int(id))
                    if result.status:
                        flash("Updated record", "success")
                except Exception as e:
                    # TODO edit-7 make this user-friendly
                    print(str(e))
                    flash('Employee was not updated', "danger")
        row = {}
        try:
            # TODO edit-8 fetch the updated data 
            result = DB.selectOne("SELECT first_name, last_name, company_id, email FROM IS601_MP3_Employees as e LEFT JOIN IS601_MP3_Companies as c ON company_id = c.id WHERE e.id = %s", int(id))
            if result.status:
                row = result.row
            if row is None:
                flash('Invalid Employee ID', "danger")
                return redirect(url_for('employee.search'))
        except Exception as e:
            # TODO edit-9 make this user-friendly
            print(str(e))
            flash('Could not fetch updated data', "danger")
            
    # TODO edit-10 pass the employee data to the render template
    return render_template("edit_employee.html", employee=row)

@employee.route("/delete", methods=["GET"])
def delete():
    # TODO delete-1 delete employee by id
    # TODO delete-2 redirect to employee search
    # TODO delete-3 pass all argument except id to this route
    # TODO delete-4 ensure a flash message shows for successful delete
    # TODO delete-5 if id is missing, flash necessary message and redirect to search
    pass