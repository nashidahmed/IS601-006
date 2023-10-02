<table><tr><td> <em>Assignment: </em> IS601 Milestone1 Deliverable</td></tr>
<tr><td> <em>Student: </em> Nashid Ahmed Shah Nashid Ahmed Shah (nn379)</td></tr>
<tr><td> <em>Generated: </em> 4/12/2023 10:35:44 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-milestone1-deliverable/grade/nn379" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone1 branch</li><li>Create a milestone1.md file in your Project folder</li><li>Git add/commit/push this empty file to Milestone1 (you'll need the link later)</li><li>Ensure your images display correctly in the sample markdown at the bottom</li><ol><li>NOTE: You may want to try to capture as much checklist evidence in your screenshots as possible, you do not need individual screenshots and are recommended to combine things when possible. Also, some screenshots may be reused if applicable.</li></ol><li>Save the submission items</li><li>Copy/paste the markdown from the "Copy markdown to clipboard link" or via the download button</li><li>Paste the code into the milestone1.md file or overwrite the file</li><li>Git add/commit/push the md file to Milestone1</li><li>Double check the images load when viewing the markdown file (points will be lost for invalid/non-loading images)</li><li>Make a pull request from Milestone1 to dev and merge it (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku dev</li></ol></li><li>Make a pull request from dev to prod (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku prod</li></ol></li><li>Submit the direct link from github prod branch to the milestone1.md file (no other links will be accepted and will result in 0)</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Feature: User will be able to register a new account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/230747499-1b5336b0-f02b-4826-a361-7b25e5a2fffd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>showing email validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/230747561-197d4391-d5f1-4b55-b80b-3cfefbfcac57.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>showing password validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/230747569-958e993b-a92b-4a74-acc6-57994101ccc1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>showing password not match validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/230747624-d2769040-a9d9-4612-8104-d21688de2959.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>showing email not available validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/230747608-354a3a68-c709-40d3-a6cc-97c108225f26.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing username not available validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/230747663-633edb92-f23d-4b04-b2a6-b119c6015bb5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>showing the form with valid data filled in<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/230747707-3bcaacd9-cfcc-4528-b419-6abd58699991.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>showing the success message after registering<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Users table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/230747747-02f4c893-286c-4020-b29f-51fbfe192ccf.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the screenshow of the new valid user. The new user corresponds to<br>user id 5 in the screenshot<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/nashidahmed/IS601-006/pull/27">https://github.com/nashidahmed/IS601-006/pull/27</a> </td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/nashidahmed/IS601-006/pull/36">https://github.com/nashidahmed/IS601-006/pull/36</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <ol><li>The form is handled using WTForms, we declare a RegisterForm which inherits all<br>the fields from the AuthForm class which is in turn derived from FlaskForm.<br>All the fields are declared here along with the name and type of<br>the fields and the validator functions for that specific field. These fields are<br>then displayed in the HTML file.</li><li>The code uses the validate_on_submit function from FlaskForm<br>to check if all the fields pass the validations set in the previous<br>step. When the user enters the data and clicks on Register, the /register<br>route is called from auth.py and the validations are run. If there is<br>any duplicate username or email once the data is inserted into the db,<br>an exception is thrown and the user is informed that the email/username already<br>exists.</li><li>The password is handled using bcrypt. The generate_password_hash function is called by passing<br>the password entered by the user and it returns the hash which is<br>stored in the db.</li><li>Once the above steps are complete, the insertOne function of<br>the DB is called with an insert query, and the email, password, and<br>username values are passed to the db to get stored.</li></ol><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Feature: User will be able to login to their account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/231553688-2d8673fd-472c-49bc-bb3a-1a94358a9c0b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing the password mismatch validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/231553914-c56b79eb-b675-4c8e-a15c-e15489a853ec.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing validation based on non-existing user<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of successful login</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/231554360-1331c700-36ee-4cc5-bf70-39424fc7839f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshow showing flash message and redirect after successful login<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/nashidahmed/IS601-006/pull/27">https://github.com/nashidahmed/IS601-006/pull/27</a> </td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/nashidahmed/IS601-006/pull/36">https://github.com/nashidahmed/IS601-006/pull/36</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <ol><li>The form is handled using WTForms, we declare a LoginForm which inherits all<br>the fields from the AuthForm class which is in turn derived from FlaskForm.<br>All the fields are declared here along with the name and type of<br>the fields and the validator functions for that specific field. These fields are<br>then displayed in the HTML file.</li><li>The code uses the validate_on_submit function from FlaskForm<br>to check if all the fields pass the validations set in the previous<br>step. When the user enters the data and clicks on Login, the /login<br>route is called from auth.py and the validations are run. Then we first<br>check if the user/email exists in the db, if not, the user is<br>informed that the user does not exist. Else, the data is fetched from<br>the db for this user and the password is compared with the check_password_hash<br>function from bcrypt.&nbsp;If the password is incorrect, the user is informed that the<br>password entered is incorrect.<br></li><li>The password is handled using bcrypt. The generate_password_hash function is<br>called by passing the password entered by the user and it returns the<br>hash.</li><li>The db is used to get the data from the users table using<br>the email and it is also used to get the user roles from<br>the UserRoles table by passing in the id received in the Users query.<br></li></ol><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Feat: Users will be able to logout </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the successful logout message</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/231555166-cc48806a-c4a3-471d-bd46-0906a5a134f0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the successful logout message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the logged out user can't access a login-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/231568067-e6ad59fb-5ecc-422c-a80d-b82137ccfb84.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the logged out user can&#39;t access a login-protected page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/nashidahmed/IS601-006/pull/27">https://github.com/nashidahmed/IS601-006/pull/27</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <ul><li>The code uses the flask_login library to handle login. During login, the login_user<br>function is called passing in all the user data along with the user's<br>role. This will this user's data to current_user.</li><li>Then, we use an Identity Management<br>library, flask_principal, to store the identity of the user using the identity_changed.send function.<br>This function will trigger the identity_loaded function declared in our main.py which will<br>set the roles of the user to the identity.</li><li>Next, we store the user<br>details in the Flask session. Delegating this login functionality to flask_login allows us<br>to use the login_required function to check if the user is authenticated. This<br>function just needs to be called with the routes for which users need<br>to log in.</li><li>In order to log out, we simply need to call the<br>logout_user function from flask_login, remove the user session we set during login and<br>inform Flask-principal that the new user is anonymous.</li></ul><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Feature: Basic Security Rules Implemented / Basic Roles Implemented </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the logged out user can't access a login-protected page (may be the same as similar request)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/231568067-e6ad59fb-5ecc-422c-a80d-b82137ccfb84.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the logged out user can&#39;t access a login-protected page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing a user without an appropriate role can't access the role-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/231558203-bb9352fd-60f2-4e93-8d62-2396ee20dec5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing a user without an appropriate role can&#39;t access the role-protected page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Roles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/231558533-a4aa12bd-3a7f-459c-8bd1-a78367c85cde.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the Roles table with valid data<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a screenshot of the UserRoles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/231558784-f2f7bab5-1822-46c1-8b79-c961a5b1ac33.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the UserRoles table with valid data, user 1 (id:1) is assigned<br>to the admin role (-1)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/231559706-3de06c7f-e2d1-4f1a-b014-a3db00639a03.gif"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the Users table with valid data, the first user is the<br>admin as indicated in the screenshot<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add the related pull request(s) for these features</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/nashidahmed/IS601-006/pull/27">https://github.com/nashidahmed/IS601-006/pull/27</a> </td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/nashidahmed/IS601-006/pull/28">https://github.com/nashidahmed/IS601-006/pull/28</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Explain briefly how the process/code works for login-protected pages</td></tr>
<tr><td> <em>Response:</em> <p>The login_required function from the flask_login library is used to prevent unauthorized access<br>to login_protected pages. Flask_login keeps track of whether a user is logged in<br>since we call the login_user and logout_user functions of flask_login during login and<br>logout respectively. These functions set and unset various sessions related to the user<br>to handle the login and logout functionality.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 7: </em> Explain briefly how the process/code works for role-protected pages</td></tr>
<tr><td> <em>Response:</em> <p>When the user logs in to the application. The identity_changed.send function is called<br>with the user_id. This triggers the identity_loaded function defined in our main.py file<br>which in turn sets the roles of the user to the identity. When<br>the user tries to access a role-protected page, the Permission class from flask_principal<br>is used to make sure that the logged-in user contains the &#39;Admin&#39; role.<br>This is done by calling the admission_permission.require function which makes sure that the<br>identity has the permissions needed to access the function (in our case, the<br>&#39;Admin&#39; role). If the condition is not satisfied, a 403 permission denied exception<br>is thrown.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Feature: Site should have basic styles/theme applied; everything should be styled </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots to show examples of your site's styles/theme</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/231564976-83743b8e-d6e6-4844-a25c-e84efa8d14b2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing table styles and navigation styles<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/231565374-c4451812-d85a-4f57-9bac-f01ffd57481b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing form styles<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/nashidahmed/IS601-006/pull/27">https://github.com/nashidahmed/IS601-006/pull/27</a> </td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/nashidahmed/IS601-006/pull/28">https://github.com/nashidahmed/IS601-006/pull/28</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain your CSS at a high level</td></tr>
<tr><td> <em>Response:</em> <p>We use the various classes provided by Bootstrap to style our elements. For<br>example,<div><ul><li>in nav.html, we use the navbar class for the navigation bar. We also<br>use the bg color class to give a background color. The nav-item class<br>is used for the different items in the navigation menu and the nav-link<br>class is used for links. The navbar-collapse class helps to move the menu<br>items in a smaller screen to a dropdown from a hamburger menu.</li><li>in forms,<br>we use the form-control class to give the input fields a better-looking design<br>than the default styles for these fields.</li></ul><div>Using these classes helps us not worry<br>about trivial padding, margin, font sizes, etc. since Bootstrap takes care of them<br>for us.<br></div></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Feature: Any output messages/errors should be "user friendly" </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of some examples of errors/messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/231568067-e6ad59fb-5ecc-422c-a80d-b82137ccfb84.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing unauthorized access<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/231553688-2d8673fd-472c-49bc-bb3a-1a94358a9c0b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing invalid password validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/230747569-958e993b-a92b-4a74-acc6-57994101ccc1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing password mismatch validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/231558203-bb9352fd-60f2-4e93-8d62-2396ee20dec5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing permission denied error message for role-protected pages<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a related pull request</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/nashidahmed/IS601-006/pull/27">https://github.com/nashidahmed/IS601-006/pull/27</a> </td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/nashidahmed/IS601-006/pull/36">https://github.com/nashidahmed/IS601-006/pull/36</a> </td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/nashidahmed/IS601-006/pull/40">https://github.com/nashidahmed/IS601-006/pull/40</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how you made messages user friendly</td></tr>
<tr><td> <em>Response:</em> <p>We&#39;ve been using flash messages, which is a flask helper function to display<br>user-friendly errors. We make use of try, except blocks and if conditions where<br>needed to check if an error occurred and accordingly display a user-friendly message<br>to the users. The second parameter of the flash function also allows us<br>to give the type of error(eg: danger, info) which have been styled on<br>the client side to inform the user whether the message is a warning(warning),<br>error(danger) or just some information(info).&nbsp;<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Feature: Users will be able to see their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/231565374-c4451812-d85a-4f57-9bac-f01ffd57481b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing profile page with email and username prefilled properly<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/nashidahmed/IS601-006/pull/36">https://github.com/nashidahmed/IS601-006/pull/36</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Explain briefly how the process/code works (view only)</td></tr>
<tr><td> <em>Response:</em> <p>We first get the user id from current_user in flask_login. We then use<br>this id to get the user details from the Users table in the<br>DB. Then, we set the form object with the email and username received<br>from the previous query and pass the form object to profile.html using the<br>render_template function.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Feature: User will be able to edit their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page validation messages and success messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/231570717-44861fb1-4a90-4d01-8484-831c22f8e293.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing username validation message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/231570884-ead50d68-9b22-4a36-8f2f-bf06b02b17c3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshow showing email validation message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/231583720-4cecd449-3d8f-4d52-bc06-add9bd3e497f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing password validation message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/231571207-5b6b307e-610f-447f-b8b2-3dc5591559ec.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshow showing password mismatch validation message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/231591501-bbab88a5-fe77-47c8-80f7-a35777908c19.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing email not available validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/231591107-814b2f9b-54a0-46ee-97ba-d3f58fff1bab.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing username not available validation<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add before and after screenshots of the Users table when a user edits their profile</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/231595772-3c67951d-8de0-4974-a57d-0f341ccad017.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of Users table before update, the first user will be the one<br>changed<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/231595639-34c6cc3f-85ea-4ec1-981d-d52b1ed8b285.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of Users table after update, all fields of the first user were<br>changed. The username was changed from &#39;test2&#39; to &#39;nash&#39;, email from &#39;<a href="mailto:&#116;&#101;&#115;&#116;&#64;&#x74;&#x65;&#x73;&#x74;&#46;&#x63;&#111;&#109;">&#116;&#101;&#115;&#116;&#64;&#x74;&#x65;&#x73;&#x74;&#46;&#x63;&#111;&#109;</a>&#39; to<br>&#39;<a href="mailto:&#x6e;&#97;&#115;&#104;&#105;&#100;&#x40;&#x74;&#101;&#115;&#x74;&#x2e;&#x63;&#111;&#x6d;">&#x6e;&#97;&#115;&#104;&#105;&#100;&#x40;&#x74;&#101;&#115;&#x74;&#x2e;&#x63;&#111;&#x6d;</a>&#39; and password was also changed<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/nashidahmed/IS601-006/pull/36">https://github.com/nashidahmed/IS601-006/pull/36</a> </td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/nashidahmed/IS601-006/pull/37">https://github.com/nashidahmed/IS601-006/pull/37</a> </td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/nashidahmed/IS601-006/pull/41">https://github.com/nashidahmed/IS601-006/pull/41</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works (edit only)</td></tr>
<tr><td> <em>Response:</em> <p>When the user tries to save the profile with updated data, the code<br>first uses validate_on_submit to handle the validations which are set in the ProfileForm.<br>This will make sure the email is of email format, the username is<br>between 2 and 30 characters, and the new password and the confirm password<br>fields match. Then we fetch the user details using the user id received<br>from current_user. We use check_password_hash from bcrypt to compare the hash of the<br>password entered by the user with the password hash stored in the DB.<br>If they do not match, we inform the user that they have entered<br>the incorrect password. If it is the correct password, then the new password<br>is hashed using bcrypt&#39;s generate_password_hash and it is updated in the DB. I<br>have updated the code to set is_valid to false if the password check<br>failed so that there will not be a partial save(saving email and username<br>when the password they typed is incorrect). If is_valid is true, it will<br>update the email and username for that user. If the update fails, we<br>check if the user has entered any duplicate data for email or username<br>and inform the user about the error. Finally, we pass the newly updated<br>data to the template.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <ul><li>I learned in detail how the flask_principal library can be used effectively to<br>manage the identity for us, which makes it significantly easier to handle role-based<br>authorization.</li><li>I learned how flask_login can be used to manage the current user's session<br>data along with the helper functions which enable us to implement checks for<br>login-protected pages.</li><li>I learned how to abstract parts of our code so that our<br>code is reusable and versatile.</li><li>I learned about the use of WTForms, which helps<br>us to manage our forms and validations more effectively and concisely.</li><li>I improved my<br>debugging skills when I came across an issue with named parameters in my<br>SQL query. As it turned out, I was using the older version of<br>db.py which did not account for passing tuples as arguments.</li></ul><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Prod Application Link to Login Page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-nn379-prod.herokuapp.com/login">https://is601-nn379-prod.herokuapp.com/login</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-milestone1-deliverable/grade/nn379" target="_blank">Grading</a></td></tr></table>