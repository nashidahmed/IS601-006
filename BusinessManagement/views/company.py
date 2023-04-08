from flask import Blueprint, redirect, render_template, request, flash, url_for
from sql.db import DB
import pycountry
company = Blueprint('company', __name__, url_prefix='/company')

@company.route("/search", methods=["GET"])
def search():
    rows = []
    # DO NOT DELETE PROVIDED COMMENTS
    # TODO search-1 retrieve id, name, address, city, country, state, zip, website, employee count as employees for the company
    # don't do SELECT *
    
    # nn379 Apr 4 2023
    query = """SELECT c.id, name, address, city, country, state, zip, IFNULL(website, 'N/A') as website, IFNULL(count(e.id), '0') as employees
    FROM IS601_MP3_Companies as c
    LEFT JOIN IS601_MP3_Employees as e
    ON c.id = e.company_id
    WHERE 1=1"""
    args = {} # <--- add values to replace %s/%(named)s placeholders
    allowed_columns = ["name", "city", "country", "state"]
    # TODO search-2 get name, country, state, column, order, limit request args
    # TODO search-3 append a LIKE filter for name if provided
    # TODO search-4 append an equality filter for country if provided
    # TODO search-5 append an equality filter for state if provided
    # TODO search-6 append sorting if column and order are provided and within the allows columsn and allowed order asc,desc
    # TODO search-7 append limit (default 10) or limit greater than 1 and less than or equal to 100
    # TODO search-8 provide a proper error message if limit isn't a number or if it's out of bounds
    name = request.args.get('name')
    country = request.args.get('country')
    state = request.args.get('state')
    col = request.args.get("column")
    order = request.args.get("order")
    limit = request.args.get("limit", 10) # TODO change this per the above requirements

    # If any of the data has been entered append it to the end of the query and populate the args object. Add group by after appending all the conditions, this will be used to get the count of employees in that particular company
    if name:
      query += " AND name like %(name)s"
      args['name'] = f"%{name}%"
    if country:
      query += " AND country = %(country)s"
      args['country'] = country
    if state:
      query += " AND state = %(state)s"
      args['state'] = state
    query += " GROUP BY c.id"
    if col and order:
        if col in allowed_columns and order in ["asc", "desc"]:
            query += f" ORDER BY {col} {order}"

    # Convert allowed_columns after the 'column' validation is complete so it can be passed to the templates for sort filter function
    allowed_columns = list(map(lambda c: (c, c), allowed_columns))
    # Check if limit that has been entered is a number and within 1 to 100, if not raise an exception informing the user through a flash message.
    try:
        if limit and int(limit) >= 1 and int(limit) <= 100:
            query += " LIMIT %(limit)s"
            args['limit'] = int(limit)
        else:
            raise Exception
    except:
        flash('Limit must be a number between 1 to 100', 'danger')
        return render_template("list_companies.html", rows=rows, allowed_columns=allowed_columns)

    try:
        result = DB.selectAll(query, args)
        #print(f"result {result.rows}")
        if result.status:
            rows = result.rows
    except Exception as e:
        # TODO search-9 make message user friendly
        flash("Company could not be found.", "danger")
        print(str(e))
    
    return render_template("list_companies.html", rows=rows, allowed_columns=allowed_columns)

@company.route("/add", methods=["GET","POST"])
def add():
    data = {}
    if request.method == "POST":
        # TODO add-1 retrieve form data for name, address, city, state, country, zip, website
        # TODO add-2 name is required (flash proper error message)
        # TODO add-3 address is required (flash proper error message)
        # TODO add-4 city is required (flash proper error message)
        # TODO add-5 state is required (flash proper error message)
        # TODO add-5a state should be a valid state mentioned in pycountry for the selected state
        # hint see geography.py and pycountry documentation
        # TODO add-6 country is required (flash proper error message)
        # TODO add-6a country should be a valid country mentioned in pycountry
        # hint see geography.py and pycountry documentation
        # TODO add-7 website is not required
        # TODO add-8 zipcode is required (flash proper error message)
        # note: call zip variable zipcode as zip is a built in function it could lead to issues
        # nn379 Apr 5 2023
        has_error = False # use this to control whether or not an insert occurs
        data['name'] = request.form.get('name')
        data['address'] = request.form.get('address')
        data['city'] = request.form.get('city')
        data['country'] = request.form.get('country')
        data['state'] = request.form.get('state')
        data['website'] = request.form.get('website') or None
        data['zipcode'] = request.form.get('zip')

        # Check if the required fields are all entered. If the data is a country or a state, check if it exists in pycountry for the selected country
        for k, v in data.items():
            if k != 'website' and not v:
                flash(f"{k.capitalize() if k != 'zipcode' else 'Zip'} is required", 'danger')
                has_error = True
            elif k == 'country' and v not in list(map(lambda c: c.alpha_2, pycountry.countries)):
                flash('Country does not exist', 'danger')
                has_error = True
            elif k == 'state' and v not in list(map(lambda s: s.code.split("-")[1], pycountry.subdivisions.get(country_code=data['country'].strip()))):
                flash('State does not exist', 'danger')
                has_error = True

        # If no error, we can proceed to insert the company into the database. 
        if not has_error:
            try:
                result = DB.insertOne("""INSERT INTO IS601_MP3_Companies (name, address, city, state, country, website, zip)
                VALUES (%(name)s, %(address)s, %(city)s, %(state)s, %(country)s, %(website)s, %(zipcode)s)"""
                , data) # <-- TODO add-8 add query and add arguments
                if result.status:
                    flash("Added Company", "success")
            except Exception as e:
                # TODO add-9 make message user friendly
                flash('Company could not be inserted. Check your input.', "danger")
                print(str(e))
        
    from types import SimpleNamespace
    return render_template("add_company.html", company=SimpleNamespace(**data))

@company.route("/edit", methods=["GET", "POST"])
def edit():
    # TODO edit-1 request args id is required (flash proper error message)
    # nn379 Apr 5 2023
    id = request.args.get('id')
    if not id: # TODO update this for TODO edit-1
        flash('Invalid Company ID', "danger")
        return redirect(url_for('company.search'))
    else:
        if request.method == "POST":
            data = {"id": id} # use this as needed, can convert to tuple if necessary
            # TODO edit-1 retrieve form data for name, address, city, state, country, zip, website
            # TODO edit-2 name is required (flash proper error message)
            # TODO edit-3 address is required (flash proper error message)
            # TODO edit-4 city is required (flash proper error message)
            # TODO edit-5 state is required (flash proper error message)
            # TODO edit-5a state should be a valid state mentioned in pycountry for the selected state
            # hint see geography.py and pycountry documentation
            # TODO edit-6 country is required (flash proper error message)
            # TODO edit-6a country should be a valid country mentioned in pycountry
            # hint see geography.py and pycountry documentation
            # TODO edit-7 website is not required
            # TODO edit-8 zipcode is required (flash proper error message)
            
            # note: call zip variable zipcode as zip is a built in function it could lead to issues
            # populate data dict with mappings
            has_error = False # use this to control whether or not an insert occurs
            data['name'] = request.form.get('name')
            data['address'] = request.form.get('address')
            data['city'] = request.form.get('city')
            data['state'] = request.form.get('state')
            data['country'] = request.form.get('country')
            data['website'] = request.form.get('website') or None
            data['zipcode'] = request.form.get('zip')

            # Check if the required fields are all entered. If the data is a country or a state, check if it exists in pycountry for the selected country
            for k, v in data.items():
                if k != 'website' and not v:
                    flash(f"{k.capitalize() if k != 'zipcode' else 'Zip'} is required", 'danger')
                    has_error = True
                elif k == 'country' and v not in list(map(lambda c: c.alpha_2, pycountry.countries)):
                    flash('Country does not exist', 'danger')
                    has_error = True
                elif k == 'state' and v not in list(map(lambda s: s.code.split("-")[1], pycountry.subdivisions.get(country_code=data['country'].strip()))):
                    flash('State does not exist', 'danger')
                    has_error = True
            
            # If no error, we can proceed to update the company in the database. 
            if not has_error:
                try:
                    # TODO edit-9 fill in proper update query
                    # name, address, city, state, country, zip, website
                    result = DB.update("""UPDATE IS601_MP3_Companies
                    SET name = %(name)s, address = %(address)s, city = %(city)s, state = %(state)s, country = %(country)s, website = %(website)s, zip = %(zipcode)s
                    WHERE id = %(id)s"""
                    , data)
                    if result.status:
                        flash("Updated record", "success")
                except Exception as e:
                    # TODO edit-10 make this user-friendly
                    print(str(e))
                    flash('Company could not be updated', "danger")
        row = {}
        try:
            # TODO edit-11 fetch the updated data
            result = DB.selectOne("""SELECT name, address, city, state, country, website, zip
            FROM IS601_MP3_Companies
            WHERE id = %s"""
            , int(id))
            if result.status:
                row = result.row
            # DB does not throw exception if company does not exist in the db, so if no rows are returned, company was not found, return user to search screen.
            if row is None:
                flash('Company ID does not exist', "danger")
                return redirect(url_for('company.search'))
        except Exception as e:
            # TODO edit-12 make this user-friendly
            print(str(e))
            flash('Could not fetch updated data', "danger")
    # TODO edit-13 pass the company data to the render template
    return render_template("edit_company.html", company = row)

@company.route("/delete", methods=["GET"])
def delete():
    # TODO delete-1 delete company by id (unallocate any employees see delete-5)
    # TODO delete-2 redirect to company search
    # TODO delete-3 pass all argument except id to this route
    # TODO delete-4 ensure a flash message shows for successful delete
    # TODO delete-5 for all employees assigned to this company set their company_id to None/null
    # TODO delete-6 if id is missing, flash necessary message and redirect to search
    id = request.args.get('id')
    args = {**request.args}
    print(args)
    if not id: # TODO update this for TODO edit-1
        flash('Invalid Company ID', "danger")
    else:
        try:
            result = DB.delete("""UPDATE IS601_MP3_Employees
            SET company_id = %s
            WHERE company_id = %s"""
            , None, int(id))
            if result.status:
                print('Unallocated employees')
        except Exception as e:
            print(str(e))
            flash('Could not set employees\' company to null')
        try:
            result = DB.delete("""DELETE FROM IS601_MP3_Companies
            WHERE id = %s"""
            , int(id))
            if result.status:
                flash(f'Company id: {id}  deleted', "success")
        except Exception as e:
            print(str(e))
            flash('Could not delete company.', "danger")

        del args['id']
    return redirect(url_for('company.search', **args))

    