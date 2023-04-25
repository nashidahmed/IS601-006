<table><tr><td> <em>Assignment: </em> IS601 Milestone 2 Shop Project</td></tr>
<tr><td> <em>Student: </em> Nashid Ahmed Shah Nashid Ahmed Shah (nn379)</td></tr>
<tr><td> <em>Generated: </em> 4/24/2023 10:03:42 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-milestone-2-shop-project/grade/nn379" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone2 branch</li><li>Create a new markdown file called milestone2.md</li><li>git add/commit/push immediate</li><li>Fill in the below deliverables</li><li>At the end copy the markdown and paste it into milestone2.md</li><li>Add/commit/push the changes to Milestone2</li><li>PR Milestone2 to dev and verify</li><li>PR dev to prod and verify</li><li>Checkout dev locally and pull changes to get ready for Milestone 3</li><li>Submit the direct link to this new milestone2.md file from your GitHub prod branch to Canvas</li></ol><p>Note: Ensure all images appear properly on github and everywhere else. Images are only accepted from dev or prod, not local host. All website links must be from prod (you can assume/infer this by getting your dev URL and changing dev to prod).</p></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Users with admin or shop owner will be able to add products </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of admin create item page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/234118201-52498b0e-8bfa-4c6e-a282-2345f1a3db5b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing admin add product page with valid data filled in<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot of populated Products table clearly showing the columns</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/234118386-8d35a94c-f056-496c-b2a9-f85963634b15.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing populated products table <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly describe the code flow for creating a Product</td></tr>
<tr><td> <em>Response:</em> <ul><li>A user enters the valid data into the form and clicks on the<br>"Add Product" button</li><li>WTForms validates the data for us, if the data is valid,<br>it is inserted into the DB.</li><li>The user enters the price in $ (decimal<br>format). This is then updated in the code by converting it to pennies<br>by multiplying by 100 and rounding off to the nearest integer since our<br>database stores the price as pennies.</li><li>If there was no error (the user could<br>enter a product name that already exists), the user is informed of the<br>same. Else a success message is displayed informing the user that the product<br>was added successfully.</li></ul><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/nashidahmed/IS601-006/pull/45">https://github.com/nashidahmed/IS601-006/pull/45</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-nn379-prod.herokuapp.com/admin/product/add">https://is601-nn379-prod.herokuapp.com/admin/product/add</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Any user can see visible products on the Shop Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the Shop page showing 10 items without filters/sorting applied</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/234122283-21f6d166-371f-4888-816c-175266cc0934.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing product screenshots on the shop page (only showing 8 since 10 don&#39;t<br>fit with my design). All products can be viewed using the prod url<br>associated with this deliverable<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Shop page showing both filters and a different sorting applied (should be more than 1 sample product)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/234119946-faa28f3f-5ca8-4f4c-8038-b94b9aff6718.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing search filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/234120044-cfe0b33c-2f1a-4428-b320-5cff272b6765.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing category filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/234120296-1873212d-e5f9-4874-b25d-4848a373dd6b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing sorting applied in ascending order of cost<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the filter/sort logic from the code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/234121097-92ab2097-76cc-410e-a168-ea8c4dbff8a8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the sorting/filter logic from the code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Briefly explain how the results are shown and how the filters are applied</td></tr>
<tr><td> <em>Response:</em> <ul><li>When the user navigates to the products page, a query is made to<br>the DB to fetch the products which are visible (is_visible = 1)</li><li>If any<br>search filters are passed, it will update the URL and the code will<br>fetch these params from the url and append it to the query to<br>get the filtered data from the DB</li><li>For the filters, a call is also<br>made to the categories table to fetch the different categories present in the<br>categories table.</li><li>If the query was successful, the products are displayed on the screen<br>else the user is informed that the products could not be retrieved.</li></ul><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/nashidahmed/IS601-006/pull/45">https://github.com/nashidahmed/IS601-006/pull/45</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-nn379-prod.herokuapp.com/">https://is601-nn379-prod.herokuapp.com/</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Show Admin/Shop Owner Product List (this is not the Shop page and should show visibility status) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of the Admin List page/results</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/234121564-1cfeb902-cbe4-483a-b75a-6fe95726675f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the admin products page, the visibility is indicated using the &quot;eye&quot; icon,<br>a slashed eye indicates non-visible products<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain how the results are shown</td></tr>
<tr><td> <em>Response:</em> <ul><li>When the admin navigates to the admin products page, a query is made<br>to the DB to fetch all the products regardless of visibility status (no<br>where clause with is_visible)</li><li>If any search filters are passed, it will update the<br>URL and the code will fetch these params from the url and append<br>it to the query to get the filtered data from the DB</li><li>For the<br>filters, a call is also made to the categories table to fetch the<br>different categories present in the categories table.</li><li>If the query was successful, the products<br>are displayed on the screen else the user is informed that the products<br>could not be retrieved.</li><li>The same template is used for both the products page<br>and admin products page with a conditional rendering of certain elements based on<br>the role of the user and the type of the page (admin/products or<br>just products)</li></ul><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/nashidahmed/IS601-006/pull/45">https://github.com/nashidahmed/IS601-006/pull/45</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-nn379-prod.herokuapp.com/admin/products">https://is601-nn379-prod.herokuapp.com/admin/products</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Admin/Shop Owner Edit button </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the edit button visible to the Admin on the Shop page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/234119324-ff241957-754f-4233-abdb-dc60fe40ec64.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the edit button visible to the admin on the shop page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the edit button visible to the Admin on the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/234122540-e9aef6f3-54d7-41f9-8b56-1587a521a2aa.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing edit button for the admin on the product details page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot showing the edit button visible to the Admin on the Admin Product List Page (The admin page)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/234121564-1cfeb902-cbe4-483a-b75a-6fe95726675f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the edit button for admin in the admin product list page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a before and after screenshot of Editing a Product via the Admin Edit Product Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/234123097-b41197f8-f1d5-4517-befd-48e698d9e464.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the edit product page before update<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/234123488-72721fdc-cb19-4d95-9317-f4df06708c0b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the edit product page after update, all the fields were updated<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Briefly explain the code process/flow</td></tr>
<tr><td> <em>Response:</em> <ul><li>The admin can view the edit button in the product list page and<br>the product details page through a conditional rendering of the edit button based<br>on whether the user is authenticated and if the authenticated user is an<br>admin/owner.</li><li>When the user clicks on the edit button, they are redirected to the<br>edit product page and they can make an edit.&nbsp;</li><li>The edit functionality is similar<br>to the add page since it essentially uses the same template. The code<br>updates the db based on the product id.</li><li>If the edit was successful, the<br>user is informed of the same else, they are informed that the product<br>was not updated.</li><li>A call is also made to the categories table in the<br>edit page to display the categories for the admin to select for the<br>product in the edit product page.</li><li>The admin product list page contains the same<br>edit button on products and the edit functionality is the same as that<br>mentioned in the previous steps. A different URL was not used for the<br>edit page since either way no other user has access to this page<br>except for the admin and the owner.</li></ul><br></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/nashidahmed/IS601-006/pull/45">https://github.com/nashidahmed/IS601-006/pull/45</a> </td></tr>
<tr><td> <em>Sub-Task 7: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-nn379-prod.herokuapp.com/">https://is601-nn379-prod.herokuapp.com/</a> </td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-nn379-prod.herokuapp.com/edit/5">https://is601-nn379-prod.herokuapp.com/edit/5</a> </td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-nn379-prod.herokuapp.com/admin/products">https://is601-nn379-prod.herokuapp.com/admin/products</a> </td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-nn379-prod.herokuapp.com/edit/4">https://is601-nn379-prod.herokuapp.com/edit/4</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Product Details Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the button (clickable item) that directs the user to the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/234122283-21f6d166-371f-4888-816c-175266cc0934.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The image is the clickable item in my project. Clicking on the image<br>of a product will redirect a user to the product details page (Same<br>as Amazon)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the result of the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/234125342-aba34ccd-95a6-4210-88db-27d1d09dc9d8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing product details page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the code process/flow</td></tr>
<tr><td> <em>Response:</em> <ul><li>The image of the product is used as the clickable item for the<br>user to access the product details page.</li><li>When the product details page is requested,<br>a call is made to the DB fetching the product based on the<br>product id.</li><li>If the data was successfully retrieved, the user is shown the details<br>of the product along with the quantity field and the add to cart<br>button.</li></ul><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/nashidahmed/IS601-006/pull/45">https://github.com/nashidahmed/IS601-006/pull/45</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file (can be any specific item)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-nn379-prod.herokuapp.com/">https://is601-nn379-prod.herokuapp.com/</a> </td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-nn379-prod.herokuapp.com/product/2">https://is601-nn379-prod.herokuapp.com/product/2</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add to Cart </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the success message of adding to cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/234125626-af35e44d-4f84-417f-a623-e4400d858c07.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the add to cart success message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the error message of adding to cart (i.e., when not logged in)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/234125842-0775b245-75da-4440-8fa2-9516199d15a6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>When a user is not logged in and they try to add something<br>to their cart. My application redirects the user to the login page asking<br>them to login to continue.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Cart table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/234126151-1e769cc2-935c-4c03-be1d-0e1819f46978.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the cart table with data in it<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Tell how your cart works (1 cart per user; multiple carts per user)</td></tr>
<tr><td> <em>Response:</em> <p>The cart allows only a single cart per user. The cart details for<br>a particular user are fetched from the DB based on the user_id.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Explain the process of add to cart</td></tr>
<tr><td> <em>Response:</em> <ul><li>The quantity field in the product details page contains validation to verify that<br>the quantity is an integer and is more than or equal to 0.</li><li>Once<br>the user enters a valid value and clicks add to cart, the product<br>cost is fetched from the products table and the product is inserted into<br>the cart with the quantity, if the user already has the same product<br>in their cart, the quantity they entered is added to the quantity they<br>previously had for that product.</li><li>If the product was added to the cart successfully,<br>the user is informed of the same, else the user is informed that<br>there was an error adding their product to the cart.</li></ul><br></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/nashidahmed/IS601-006/pull/45">https://github.com/nashidahmed/IS601-006/pull/45</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> User will be able to see their Cart </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the Cart View</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/234126514-a914dbde-cfb4-4fa5-8a2d-fb4859ec8cf7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the cart of a user along with the line subtotal, cart total<br>at the bottom right and &#39;View&#39; button to view the product<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain how the cart is being shown from a code perspective along with the subtotal and total calculations</td></tr>
<tr><td> <em>Response:</em> <ul><li>When the user navigates to the cart page, a query is made to<br>the DB. This query joins the cart table with the product table to<br>return the details of the product along with the cart for that specific<br>user.&nbsp;</li><li>The subtotal for each item is calculated on the fly in the query<br>by multiplying the quantity of the product in the cart by its cost.</li><li>In<br>the template, we perform the conversion of the price from pennies to $<br>using <b>set.</b>&nbsp;</li><li>We also calculate the total of the cart in the template using<br>the namespace trick which allows us to set a variable <b>total&nbsp;</b>and add the<br>subtotal of each item as we loop over the products in the template.&nbsp;</li><li>This<br>total is eventually displayed to the user.</li><li>Each product also contains a "View" button<br>which redirects the user to the product details page for that specific product.</li></ul><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/nashidahmed/IS601-006/pull/45">https://github.com/nashidahmed/IS601-006/pull/45</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-nn379-prod.herokuapp.com/cart/">https://is601-nn379-prod.herokuapp.com/cart/</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> User can update cart quantity </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Show a before and after screenshot of Cart Quantity update</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/234126514-a914dbde-cfb4-4fa5-8a2d-fb4859ec8cf7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the cart before update,  the purified drinking water item will be<br>updated.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/234127167-d6cb0dd6-7cb8-4f84-8363-c69d32f4b367.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the updated cart. As seen in the message, the water item was<br>updated to a count of 3<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Show a before and after screenshot of setting Cart Quantity to 0</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/234127167-d6cb0dd6-7cb8-4f84-8363-c69d32f4b367.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the cart before setting cart quantity to 0<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/234153572-69073246-2f7a-41d9-88bd-e4f888af1af3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the cart after setting cart quantity of bananas to 0, the application<br>will not allow this change and inform the user that quantity must be<br>more than 0 and that if they want to remove the product, they<br>should use the delete button.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Show how a negative quantity is handled</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/234127389-63a707a2-7730-472a-831d-bf9d37f20492.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing how negative value is handled. the user is informed that quantity must<br>be more than 0. the screenshot above was after trying to update the<br>quantity of snickers to -1<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain the update process including how a value of 0 and negatives are handled</td></tr>
<tr><td> <em>Response:</em> <ul><li>When the user tries to update the quantity of a particular product from<br>their cart, first validation is done to make sure that the quantity is<br>more than 0, if it is negative the user is informed that only<br>positive values are accepted, if it is 0, the user is informed to<br>remove the item from cart instead.</li><li>If the quantity is positive, fetch the product<br>details to inform the user which product was changed and to update the<br>price in case the price of the product changed when it was in<br>their cart.</li><li>Then insert the updated quantity and cost into the cart table and<br>inform the user of the successful update.</li></ul><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/nashidahmed/IS601-006/pull/45">https://github.com/nashidahmed/IS601-006/pull/45</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Cart Item Removal </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a before and after screenshot of deleting a single item from the Cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/234127389-63a707a2-7730-472a-831d-bf9d37f20492.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the cart before delete. The item to be deleted will the snickers<br>item<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/234127943-032a5a41-1e18-4933-947f-0fb2d6665174.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the cart after delete. As seen the snickers product has been removed<br>from cart<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a before and after screenshot of clearing the cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/234140889-f73063bf-3490-4311-9525-aa66ae18bed7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing clear cart before update. Note: This button does not apper in the<br>previous cart screenshots since I was unaware earlier this was required and I<br>added the functionality once I reached this point. I also updated the css.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/234140937-e04cfc0a-59a9-4df5-9b13-bc3fe39b54b1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the cart after being cleared. The user is informed that the cart<br>was cleared and an option to go to the view products page is<br>shown<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how each delete process works</td></tr>
<tr><td> <em>Response:</em> <ul><li>When the user tries to delete the product, we use the product_id and<br>the user_id to make a call to the DB to delete the item<br>in the cart for that specific product and user.</li><li>Inform the user if the<br>deletion was successful or not.</li><li>For the clear cart functionality, instead of selecting a<br>specific product, we delete all rows in the cart table for that specific<br>user and inform the user of the status of the deletion.</li></ul><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/nashidahmed/IS601-006/pull/45">https://github.com/nashidahmed/IS601-006/pull/45</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <ul><li>I learned how to make an application from scratch using Flask.</li><li>I got more<br>comfortable using WTForms by creating a form helper for the <b>SelectField</b> which helped<br>to display the categories. For this, I had to read the docs to<br>understand how to handle key-value pairs in a select dropdown.</li><li>Initially, I was not<br>aware that we have to use categories and I created my entire application<br>without it, when I was filling in the deliverables, I found out about<br>the categories field and I updated my entire codebase to accommodate it. I<br>also created a separate CRUD flow for the admin/owner for categories.</li><li>I learned more<br>about jinja templates and how to dynamically assign variables in the template using<br>the namespace trick.</li></ul><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a link to your herok prod project's login page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-nn379-prod.herokuapp.com/login">https://is601-nn379-prod.herokuapp.com/login</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-milestone-2-shop-project/grade/nn379" target="_blank">Grading</a></td></tr></table>