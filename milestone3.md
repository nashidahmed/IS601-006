<table><tr><td> <em>Assignment: </em> IS601 Milestone 3 Shop Project</td></tr>
<tr><td> <em>Student: </em> Nashid Ahmed Shah Nashid Ahmed Shah (nn379)</td></tr>
<tr><td> <em>Generated: </em> 5/2/2023 1:51:57 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-milestone-3-shop-project/grade/nn379" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone3 branch</li><li>Create a new markdown file called milestone3.md</li><li>git add/commit/push immediate</li><li>Fill in the below deliverables</li><li>At the end copy the markdown and paste it into milestone3.md</li><li>Add/commit/push the changes to Milestone3</li><li>PR Milestone3 to dev and verify</li><li>PR dev to prod and verify</li><li>Checkout dev locally and pull changes to get ready for Milestone 4</li><li>Submit the direct link to this new milestone3.md file from your GitHub prod branch to Canvas</li></ol><p>Note: Ensure all images appear properly on GitHub and everywhere else. Images are only accepted from dev or prod, not localhost. All website links must be from prod (you can assume/infer this by getting your dev URL and changing dev to prod).</p></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Orders will be able to be recorded </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the Orders table with valid data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/235538515-59041b8e-7e3d-446c-b872-2da57d9b95f6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the orders table with valid data shown<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of OrderItems table with validate data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/235538744-00e78962-4987-4838-932a-7bfee11cc3b5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the OrderProducts table with valid data shown, the table is called OrderProducts<br>in my project instead of OrderItems.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the purchase form UI from Heroku</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/235544252-ba3ea525-ec45-40c8-bee7-f4d790ea6b37.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the purchase form in the UI in heroku<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a screenshot showing the items pending purchase from Heroku</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/235544252-ba3ea525-ec45-40c8-bee7-f4d790ea6b37.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the filled purchase form in the UI<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/235551068-b25e1dcc-ef04-4f6d-8eb1-9d6f3dc507b4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the purchase form after a user tries to make a purchase. In<br>this scenario, I increased the price of the Nesquik product through the admin<br>profile in an incognito tab after the user went to the checkout page<br>and before they made the final payment.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a screenshot showing the Order Process validations from the code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/235593429-6d425da6-4ee6-427a-a0a9-81dc0d3b1bc4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the country and state validation, stock and cart vs paid amount validation<br>validation as well as payment amount validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/235591923-f2c9da28-ecbf-4deb-93c7-2d2f9de35a7f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the generate address function which combines the address fields into a single<br>string with line breaks of a particular format to store in the db<br>since the db has a single field for address.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/235595120-3420be59-7810-4595-ae2b-692878d66fcd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the payment method validation using wtforms&#39; radiofield along with DataRequired to make<br>sure it is entered by the user<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add a screenshot showing the Order Process validations from the UI (Heroku)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/235596506-932c3602-7c03-4103-ab99-e66599d49679.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the price difference message. This message shows up in the cart page<br>and the checkout page as soon as the user refreshes those pages after<br>the price changes in the db. Clicking on refresh cart, updates the cart<br>with the latest price.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/235598067-6e8b7452-915e-4e0e-abfc-c028799b6612.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing no stock message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/235598267-eac297f7-6af6-4b04-bcf0-9fbb2c50719a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing less money received message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/235598393-3e3374de-81a2-41bd-8cd7-e95e3a4922db.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing too much money sent message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Briefly describe the code flow/process of the purchase process</td></tr>
<tr><td> <em>Response:</em> <ul><li>Firstly, we need to set <b>autocommit</b> to false, this makes it possible for<br>us to interact with the db as a transaction since we will be<br>making multiple insert and update queries that should execute only if all the<br>queries are executed correctly. If any one of these queries fail, we will<br>set a variable <b>has_error </b>to <b>True&nbsp;</b>which will inform the code to stop executing<br>the other queries and <b>not</b> to commit&nbsp;what has been checked thus far into<br>the db.</li><li>Then, we fetch the cart data to create the purchase order.</li><li>WTForms takes<br>care of the validation for all the fields except the country and state<br>fields since we use pycountry for those fields. So we check if country<br>and state have been entered, if not set <b>has_error&nbsp;</b>to <b>True</b>.</li><li>If they have been<br>entered, we check that the values entered exist in <b>pycountry</b>, if not set&nbsp;<b>has_error&nbsp;</b>to&nbsp;<b>True.</b></li><li>Since<br>we are storing the address is a single field in the db and<br>using multiple fields in the UI to capture the input, we create a<br><b>generate_address </b>function that takes in the different address fields and returns the address<br>with line breaks.</li><li>Call&nbsp;<b>generate_address </b>to get the address and compare each product's stock with<br>the quantity requested by the user. Also, check if there were any changes<br>made to the price of the product after the user added the item<br>to their cart. If the price has changed, show a refresh button allowing<br>the user to refresh the cart instantly. The total price and total quantity<br>is also calculated here.</li><li>Compare the amount entered by the user with the product<br>total and inform the user if it is not equal.</li><li>Then create the order<br>data. If there was an error, rollback the transaction. else fetch some order<br>details including order id.</li><li>Then record the ordered items into the OrderProducts table (orderitems<br>in my project). Rollback if unsuccessful.</li><li>Update the stock in the products table based<br>on the quantity in the cart data. Rollback if unsuccessful.</li><li>Empty the cart for<br>this user. Rollback if unsuccessful.</li><li>If there have been no errors up till this<br>point, commit the changes into the db, if there were errors rerender the<br>checkout page, with the flash messages generated from the errors above.</li><li>If successful, render<br>the confirmation page.</li></ul><br></td></tr>
<tr><td> <em>Sub-Task 8: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/nashidahmed/IS601-006/pull/48">https://github.com/nashidahmed/IS601-006/pull/48</a> </td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/nashidahmed/IS601-006/pull/51">https://github.com/nashidahmed/IS601-006/pull/51</a> </td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/nashidahmed/IS601-006/pull/53">https://github.com/nashidahmed/IS601-006/pull/53</a> </td></tr>
<tr><td> <em>Sub-Task 9: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-nn379-prod.herokuapp.com/orders/checkout">https://is601-nn379-prod.herokuapp.com/orders/checkout</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Order Confirmation Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot showing the order details from the purchase form and the related items that were purchased with a thank you message</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/235585365-153d1a5a-7829-4ae5-ac20-3b4eaba0658a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the order details from the purchase form and the related items that<br>were purchased from the order confirmation page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain how this information is retrieved and displayed from a code logic perspective</td></tr>
<tr><td> <em>Response:</em> <ul><li>This route uses the same function defined for the route of the order<br>details page. It just uses different route for the same function. We check<br>if 'confirmation' exists in the route to tell our code that it is<br>the confirmation page.</li><li>Fetch the order details using the orderproducts table to fetch the<br>order details, and the products table to get the product details like name<br>and image.</li><li>Fetch the order details using the product id and the user id.</li><li>Show<br>the user an animated "Thank you for shopping with us" message along with<br>some confetti animation.&nbsp;</li></ul><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/nashidahmed/IS601-006/pull/50">https://github.com/nashidahmed/IS601-006/pull/50</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-nn379-prod.herokuapp.com/orders/confirmation/14">https://is601-nn379-prod.herokuapp.com/orders/confirmation/14</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> User will be able to see their Purchase History </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing purchase history for a user</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/235586432-d74c5547-7a6c-4880-8c72-2e1dc30aa3ce.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing a user&#39;s purchase history<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing full details of a purchase (Order Details Page)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/235586864-e56d03ce-4696-4a43-9c43-c096067e4863.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the full details of a specfic purchase<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the logic for showing the purchase list and click/displaying the Order Details</td></tr>
<tr><td> <em>Response:</em> <ul><li>Fetch all the rows from the orders table for that particular user id<br>and display them in a table.</li><li>Using javascript, capture clicks on a particular row<br>and get the order id from the table. Then navigate to the particular<br>order using <b>window.location.href</b></li><li>In the order details page, fetch the order details using the<br>orderproducts table to fetch the order details, and the products table to get<br>the product details like name and image.</li><li>Fetch the order details using the product<br>id and the user id.</li><li>If there is no such order for that user,<br>inform the user that the order may be unavailable or that they have<br>no permission to view the order.</li></ul><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/nashidahmed/IS601-006/pull/49">https://github.com/nashidahmed/IS601-006/pull/49</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-nn379-prod.herokuapp.com/orders/history">https://is601-nn379-prod.herokuapp.com/orders/history</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Store Owner Purchase History </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing purchase history from multiple users</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/235587121-e0213edd-c186-4193-9350-0eee79b508f7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the purchase history from multiple users for the admin view. Note: the<br>earlier orders show no formatting for the address since earlier in my development,<br>I had used a simple textarea for the address field and only later<br>did I change it to separate fields.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing full details of a purchase (Order Details Page)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/235587736-4343a2a0-5ff3-4c88-a4d6-adddc2328727.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the full details for a purchase for the admin. The user_id is<br>not required since we query the data using the order id alone.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the logic for showing the purchase list and click/displaying the Order Details (mostly how it differs from the user's purchase history feature)</td></tr>
<tr><td> <em>Response:</em> <ul><li>For the admin order history table, we use a similar idea and fetch<br>the orders from the orders table and left join it with the users<br>table to get the usernames of the users. Unlike the user purchase history,&nbsp;<br>we don't use a where clause on the user id since we want<br>to return all the users' purchases.</li><li>The order details part is essentially the same<br>as the user order details page except that we skip the user id<br>comparison in the where clause so the admin can view any order.</li><li>Similar to<br>the purchase history page, for the order details page we again join the<br>users table to get the username details.</li></ul><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/nashidahmed/IS601-006/pull/50">https://github.com/nashidahmed/IS601-006/pull/50</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-nn379-prod.herokuapp.com/admin/order-history">https://is601-nn379-prod.herokuapp.com/admin/order-history</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the Cart page showing the button to place an order</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/235554836-e0c5f98a-48f5-4a7a-9ba7-7c6802e77268.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the cart page along with the &quot;Checkout&quot; button which is used to<br>go to the checkout page where the user is asked for information regarding<br>their shipping and payment to place an order.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <ul><li>With this final Milestone, I now know how to build an entire flask<br>web application end to end from scratch.</li><li>I implemented some javascript for the purchase<br>history row click as well as made some changes to the old pycountry<br>file we used in the previous project.</li><li>I learned how to create my own<br>macros. I used one to display the price change when the admin changes<br>the price of an item that already exists in some users' carts. This<br>simply compares the old price to the new price and show the percent<br>difference between the two prices.</li><li>The last time I used Bootstrap, it was on<br>the 4th version. So I got reacquainted with Bootstrap and got comfortable using<br>version 5</li><li>Since the requirement was to have only an address field in the<br>DB. I implemented the address fields in such a way that the UI<br>contains multiple fields for the street address, city, country, state and zip which<br>are then validated and formulated into one string to store in the DB<br>with line breaks in the address field. This then allows us to display<br>the address neatly. This was implemented later on which is why some order<br>history screenshots contain addresses that are not valid as per my final design,<br>since the earlier design contained a simple textarea for the entire address field.</li></ul><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-milestone-3-shop-project/grade/nn379" target="_blank">Grading</a></td></tr></table>