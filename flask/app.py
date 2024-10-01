from flask import Flask, request, jsonify, render_template, redirect, url_for, session
from flask_cors import CORS
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from Classes.Database import db  
from Classes.Employees import Employees
from Classes.Wfh_Request import WFHRequests
from Classes.Login import Login
from werkzeug.security import check_password_hash
import os
from datetime import timedelta


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:8889/spmtest1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.urandom(24)  # Set a random secret key for security
db.init_app(app)  # Initialize the db with the Flask app
CORS(app, supports_credentials=True)

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login_route'  # Redirect to login if not authenticated

app.config['SESSION_PERMANENT'] = True  # Make sessions permanent
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=1)  # Set session lifetime (1 day)
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'  # Use 'Lax' or 'None' depending on your needs
app.config['SESSION_COOKIE_SECURE'] = False  # Set to True only if using HTTP

# Define User class
class User(UserMixin):
    pass

@login_manager.user_loader
def load_user(user_id):
    return Employees.query.get(user_id)

# Route for login
# @app.route('/login', methods=['GET', 'POST'])
# def login_route():
#     if request.method == 'POST':
#         user_id = request.form.get('user_ID')
#         input_password = request.form.get('password')

#         # Create an instance of Login to check user credentials
#         login1 = Login()
#         if login1.check_user_password(user_id, input_password):
#             user = User()
#             user.id = user_id  # or get the user ID from the Employees model if necessary
#             login_user(user)  # Log in the user
#             return redirect(url_for('homepage'))  # Redirect to the employees page
#         else:
#             return render_template("Login.html", error="Invalid credentials")  # Show an error if login fails
#     return render_template("Login.html")  # Display the login form

@app.route('/login', methods=['GET', 'POST'])
def login_route():
    data = request.get_json()  # Receive the data as JSON
    user_id = data.get('user_ID')
    input_password = data.get('password')

    # Assuming you have a login checker in Login class
    login1 = Login()
    
    # Check if the user credentials are valid
    if login1.check_user_password(user_id, input_password):
        # Fetch user details from Employees model or the relevant table
        user_details = Employees.query.filter_by(Staff_ID=user_id).first()

        if not user_details:
            return jsonify({"status": "failure", "message": "User not found"}), 404
        
        user = User()
        user.id = user_id
        login_user(user)
        
        session.permanent = True

        # Set session values based on the user details
        session['employee_id'] = user_id
        session['name'] = user_details.Staff_FName  # Fetch from DB
        session['supervisor'] = user_details.Reporting_Manager
        session['position'] = user_details.Position  # Fetch from DB for position


        # Determine role based on the job title (Position)
        role = "Staff"  # Default role
        if user_details.Position in ['MD', 'Director', 'Account Manager', 'Sales Manager']:
            role = "Manager"
        elif user_details.Position == 'HR Team':
            role = "HR"

        # Return a JSON response with the determined role
        return jsonify({"status": "success", "message": "Login successful", "role": role, "staffId": user_id, "supervisor": user_details.Reporting_Manager }), 200
    else:
        return jsonify({"status": "failure", "message": "Invalid credentials"}), 401

# Logout route
@app.route("/logout")
@login_required
def logout():
    logout_user()  # Log out the user
    return redirect(url_for('login_route'))  # Redirect to login page

@app.route("/homepage")
@login_required
def homepage():
    return render_template("homepage.html")


# Define a protected route
@app.route("/test_employees")
@login_required  # Protect this route
def retrieve_employees():
    """Retrieve and display all employees."""
    emp_name=session['name']
    employees_list = Employees.get_all()  # Retrieve all employees from the database
    return render_template('employees.html', employees=employees_list, emp_name=emp_name)  # Render the employees in the template


@app.route("/wfh_request")
def wfh_request():
    emp_name=session['name']
    emp_sup=session['supervisor']
    emp_id=session['employee_id']
    return render_template("wfh_request.html", emp_name=emp_name, emp_sup=emp_sup,emp_id=emp_id)

# @app.route("/submit_wfh_request", methods=["POST"])
# @login_required
# def submit_wfh_request():
#     """Submit a new WFH request to the database."""
#     start_date = request.form['start_date']
#     end_date = request.form['end_date']
#     monday = request.form['monday']
#     tuesday = request.form['tuesday']
#     wednesday = request.form['wednesday']
#     thursday = request.form['thursday']
#     friday = request.form['friday']
#     saturday = request.form['saturday']
#     sunday = request.form['sunday']
#     requester_id = request.form['requester_id']
#     requester_supervisor = request.form['requester_supervisor']
#     request_status = request.form['request_status']

#     # Create a new WFH request instance
#     new_request = WFHRequests(
#         Requester_ID=requester_id,
#         Requester_Supervisor=requester_supervisor,
#         Request_Status=request_status,
#         start_date = start_date,
#         end_date = end_date,
#         Monday = monday,
#         Tuesday = tuesday,
#         Wednesday = wednesday,
#         Thursday = thursday,
#         Friday = friday,
#         Saturday = saturday,
#         Sunday = sunday
#     )

#     try:
#         # Add the new request to the session and commit it to the database
#         db.session.add(new_request)
#         db.session.commit()
#         return redirect(url_for('success'))  # Redirect to the success page
#     except Exception as e:
#         print(f"Error: {e}")  # Log the error
#         return redirect(url_for('failure'))  # Redirect to the failure page

@app.route("/submit_wfh_request", methods=["POST"])
<<<<<<< Updated upstream
def submit_wfh_request():
    """Submit a new WFH request to the database."""
    selected_date = request.form['selected_date']
    day_of_week = request.form['day_of_week']
    requester_id = request.form['requester_id']
    requester_supervisor = request.form['requester_supervisor']
    request_status = request.form['request_status']
=======
# @login_required
def submit_wfh_request():
    """Submit a new WFH request to the database."""
    data = request.get_json()  # Receive JSON data from the frontend

    start_date = data.get('start_date')
    end_date = data.get('end_date')
    monday = data.get('monday')
    tuesday = data.get('tuesday')
    wednesday = data.get('wednesday')
    thursday = data.get('thursday')
    friday = data.get('friday')
    saturday = data.get('saturday')
    sunday = data.get('sunday')
    requester_id = data.get('requester_id')
    requester_supervisor = data.get('requester_supervisor')
    request_status = data.get('request_status')
>>>>>>> Stashed changes

    # Create a new WFH request instance
    new_request = WFHRequests(
        selected_date=selected_date,
        day_of_week=day_of_week,
        Requester_ID=requester_id,
        Requester_Supervisor=requester_supervisor,
<<<<<<< Updated upstream
        Request_Status=request_status
=======
        Request_Status=request_status,
        start_date=start_date,
        end_date=end_date,
        Monday=monday,
        Tuesday=tuesday,
        Wednesday=wednesday,
        Thursday=thursday,
        Friday=friday,
        Saturday=saturday,
        Sunday=sunday
>>>>>>> Stashed changes
    )

    try:
        # Add the new request to the session and commit it to the database
        db.session.add(new_request)
        db.session.commit()
        return jsonify({"status": "success", "message": "Request submitted successfully"}), 200
    except Exception as e:
        print(f"Error: {e}")  # Log the error
        return jsonify({"status": "failure", "message": "Request submission failed"}), 500

@app.route("/wfh_viewer")
def retrieve_wfh():
    """Retrieve and display all wfh."""
    wfh_list = WFHRequests.get_all()  # Retrieve all employees from the database
    return  render_template('WFH.html',wfh_li=wfh_list) # Render the employees in the 


@app.route("/update_wfh_request/<int:request_id>", methods=["GET", "POST"])
def update_wfh_request(request_id):
    """Update a WFH request."""
    wfh_request = WFHRequests.get_by_id(request_id)
    if request.method == "POST":
        # Update the WFH request with the form data
        selected_date = request.form['selected_date']
        day_of_week = request.form['day_of_week']
        requester_id = request.form['requester_id']
        requester_supervisor = request.form['requester_supervisor']
        request_status = request.form['request_status']

        success = WFHRequests.update_request(request_id, selected_date, day_of_week, requester_id, requester_supervisor, request_status)
        if success:
            return redirect(url_for('wfh_request'))  # Redirect to the WFH requests page
        else:
            return redirect(url_for('failure'))  # Redirect to the failure page if update fails

    return render_template('update_wfh_request.html', wfh_request=wfh_request)


<<<<<<< Updated upstream
=======
#Note, this function most likely can delete, with the homepage button reroute to manager view, was trialling some session based logic for handling data.
#Might try to integrate a function where if session["managecount"] == 0 redirect back to homepage since no need to approve anything.
@app.route("/manager_view_processing")
def retrieve_staff_wfh_for_manager():
    #sql = text("Select * from WFH_requests where Requester_Supervisor = " + str(session['employee_id']) + " AND Request_Status = 'Pending'")
    #processed = db.session.execute(sql)
    #turn the object into a list
    #pending_list = processed.fetchall()
    #session["manager_pending_list"] = pending_list
    return redirect(url_for('managerview'))

@app.route("/managerview")
def managerview():
    sql = text("Select * from WFH_requests where Requester_Supervisor = " + str(session['employee_id']) + " AND Request_Status = 'Pending'")
    processing = db.session.execute(sql) 
    #list_of_pending_requests = session.get('manager_pending_list', [])   
    return render_template('managerview.html', requests=processing)


# @app.route("/viewownrequests")
# @login_required
# def viewownrequests():
#     sql = text("Select * from WFH_requests where Requester_ID = " + str(session['employee_id']))
#     sqldonepog = db.session.execute(sql)
#     return render_template('viewownrequests.html', ownreq = sqldonepog)
@app.route("/viewownrequests", methods=['GET'])
def viewownrequests():
    # Retrieve employee_id from cookies
    employee_id = request.cookies.get('Staff_ID')

    # Check if 'Staff_ID' exists in the cookies
    if not employee_id:
        return jsonify({"status": "failure", "message": "User not logged in"}), 401
    
    # Fetch the requests from the database
    sql = text("SELECT * FROM WFH_requests WHERE Requester_ID = :requester_id")
    sqldonepog = db.session.execute(sql, {'requester_id': employee_id}).mappings().all()

    # Convert the SQL result to a list of dictionaries
    requests = [dict(row) for row in sqldonepog]

    # Return the data as JSON
    return jsonify(requests), 200

@app.route("/managerview_active")
@login_required
def managerview_active():
    sql = text("Select * from WFH_requests where Requester_Supervisor = " + str(session['employee_id']) + " AND Request_Status = 'Approved'")
    sql_processed = db.session.execute(sql)  
    return render_template('managerview_active.html', active=sql_processed)
>>>>>>> Stashed changes


if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables if they don't exist
    app.run(host='0.0.0.0', port=5000, debug=True)