<table><tr><td> <em>Assignment: </em> IS601 - Mini Project 2 - Burgers</td></tr>
<tr><td> <em>Student: </em> Nashid Ahmed Shah Nashid Ahmed Shah (nn379)</td></tr>
<tr><td> <em>Generated: </em> 3/5/2023 4:28:35 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-mini-project-2-burgers/grade/nn379" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Create a new branch per the desired branch name below</li><li>Add the baseline files from the following link:&nbsp;<a href="https://gist.github.com/MattToegel/028db0e3fd2b20c1fb8e284b341292bb">https://gist.github.com/MattToegel/028db0e3fd2b20c1fb8e284b341292bb</a>&nbsp;</li><li>Put them into a subfolder in your repository folder (I called my folder BurgerMachine)</li><li>git add .</li><li>git commit -m "baseline files"</li><li>git push origin (name of desired branch below)</li><li>You can go to github and open the pull request for evidence capturing later (don't close/merge the pull request until you're done with the assignment)</li><li>Do the below tasks and fill in the below entries</li><ol><li>git add/commit after any significant changes to build up history</li></ol><li>Save the input and generate the submission markdown file (copy to clipboard or download the file)</li><li>Name it something relevant to the assignment if it's not named already</li><li>git add the submission file</li><li>git commit the submission file</li><li>git push the submission file</li><li>Complete the pull request to dev</li><li>Create a pull request from dev to prod</li><li>Go to the prod branch on github, navigate to the submission file</li><li>Paste that link to Canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Code Changes - Add the calculate_cost() implementation </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of the updated method calculate_cost()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/222978791-5fa104a7-7f9d-4d14-a8a7-2cbee5cdd01f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the implementation of the calculate_cost function<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/222978890-90e5dc2a-fd3d-4cdb-bd35-26427bae2a9c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing that the input message correctly displays the value in currency format with<br>the $ symbol<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain the approach to implementing the calculation</td></tr>
<tr><td> <em>Response:</em> <ul><li>The calculate_cost function uses the inprogress_burger list and fetches the costs from them<br>through list comprehension. The resulting array is passed to the sum function to<br>get the sum of the costs.</li><li>The currency format was handled using string formatting<br>and ".2f" to display exactly two decimal places.</li></ul><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Exception Handling </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of adjusted code to handle exceptions</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/222979393-385a1904-9f09-4bd4-b08b-9dd7b620baeb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the exception message raised by OutOfStockException<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/222979461-6fc00c46-7bda-4af5-a633-20b9b5825298.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing how all the exceptions are handled in the run function<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/222979420-6dda90d3-2038-40a8-a591-a1b45b146fb6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the handling of InvalidChoiceException where choice is the chosen item&#39;s name and<br>the second variable gives the stage/category name<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each exception handling process</td></tr>
<tr><td> <em>Response:</em> <ul><li><span style="font-size: 13px;"><b>OutOfStockException - </b>Use <b>self</b> since it returns the name of the<br>item and <b>self.__class__.__name__ </b>to get the name of the category through the class<br>name to show relevant message of exactly which item from which category is<br>out of stock.</span><br></li><li><span style="font-size: 13px;"><b>NeedsCleaningException - </b>Use a while loop asking the user<br>to type 'clean' to clean the machine. If any other input is entered,<br>the user is informed that the machine was not cleaned and asked to<br>type again. When the user types clean, <b>clean_machine </b>is called and the user<br>is informed that the machine has been cleaned.<br></span></li><li><span style="font-size: 13px;"><b>InvalidChoiceException - </b>When the<br>user enters choices which don't exist in the category, the user is informed<br>that what they requested for is not a valid choice for that category.<br></span></li><li><span<br>style="font-size: 13px;"><b>ExceededRemainingChoicesException - </b>The user is informed that they cannot add any more<br>items in that category and the stage progresses to the next category.<br></span></li><li><span style="font-size:<br>13px;"><b>InvalidPaymentException - </b>The user is informed that they have entered an incorrect amount<br></span></li></ul><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Test Cases </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of test cases per the checklist</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/222978485-431d31c9-883c-41ed-83b7-18696ed8cd50.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the fixtures used in the tests as well as the implementation of<br>the first 3 test cases as listed in the above checklist<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/222978503-3037ca75-c441-40a2-8a60-2970d23e86ca.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing implementation of test cases 4 - 8<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/222978556-b61bdf17-2128-4259-bbb4-b13dff052a15.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing 3 more test cases which check if the machine handles the following<br>exceptions correclty - NeedsCleaningException, ExceededRemainingChoicesException and InvalidChoiceException<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/222986608-0fa7428f-1c48-4351-bfeb-e2f3d2d0a1e7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the test cases passing<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each test case logic</td></tr>
<tr><td> <em>Response:</em> <ul><li><b>Test 1 -&nbsp;</b>Check that <b>bun</b> is first by forcing the machine to handle<br>patty/topping when the stage is at the bun stage</li><li><b>Test 2 -&nbsp;</b>Check whether the<br>machine detects when the <b>patties</b> are out of stock by</li><ul><li>Decreasing the quantity of<br>the patty to be tested to 2 instead of 10 for easier testing</li><li>Creating<br>an order with 3 of those patties to trigger the out of stock<br>exception</li><li>Asserting that exception message shows the correct patty name</li></ul><li><b>Test 3 -&nbsp;</b>Check whether the<br>machine detects when the <b>toppings</b> are out of stock by</li><ul><li>Decreasing the quantity of<br>the topping to be tested to 2 instead of 10 for easier testing</li><li>Creating<br>an order with 3 of those toppings to trigger the out of stock<br>exception</li><li>Asserting that exception message shows the correct topping name</li></ul><li><b>Test 4 -&nbsp;</b>Check if the<br>user can enter 3 patties of any type by passing random patties and<br>verifying that 3 elements of <b>Patty</b> type exist in <b>inprogress_burger</b></li><li><b>Test 5 -&nbsp;</b>Check if<br>the user can enter 3 toppings of any type by passing random toppings<br>and verifying that 3 elements of&nbsp;<b>Topping</b>&nbsp;type exist in&nbsp;<b>inprogress_burger</b></li><li><b>Test 6 -&nbsp;</b>Create 3 burger orders<br>and construct a request along with the <b>total cost</b> of the 3 orders<br>and check whether the cost calculated by the machine is the same as<br>the expected value of the orders</li><li><b>Test 7 -&nbsp;</b>Complete 3 orders and calculate their<br>total cost and verify that the total cost matches the <b>total sales</b> completed<br>by the machine</li><li><b>Test 8 -&nbsp;</b>Complete 4 burger orders and verify that the machine<br>has sold a total of 4 burgers&nbsp;</li></ul><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add pull request for the assignment</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/nashidahmed/IS601-006/pull/12">https://github.com/nashidahmed/IS601-006/pull/12</a> </td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain any issues/difficulties or something you learned while doing this assignment</td></tr>
<tr><td> <em>Response:</em> <ul><li>I learned about the use of underscore (_) as a throwaway variable, for<br>example, in <b>[machine.handle_patty('beef') for _ in range(3)]</b>, we can use '_' instead of<br>defining a variable since we want to simply do something thrice.</li><li>I learned how<br>to use factories as fixtures so we can dynamically create a reusable function<br>as a fixture.</li><li>I got to know about the random.choice function which aids in<br>getting a random element from a list</li><li>I used the named arguement method for<br>the first time to call a function in order to skip passing the<br>first parameter.</li><li>I had some difficulty initially with factories as fixtures but rather than<br>the implementation of the my test cases, it was the BurgerMachine class which<br>needed to be changed. Since the variables in the class were not initialized<br>using an <b>__init__ </b>function, all my test cases shared the same class variables.<br>Instead I moved the variable initializations into an <b>__init__&nbsp;</b>function so that my test<br>cases used separate instances of BurgerMachine. This also intuitively made sense since a<br>new instance of a burger machine should have it's own new initial values<br>and not share values across instances since each instance is a separate machine.</li></ul><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of successful output</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/222986104-7cf73107-d735-4a68-922a-53d82e2af486.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of output for first burger order<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/222986145-1b5c4382-ce09-42a6-93dd-0732b493b111.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of output for second burger order<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/222986208-12d10253-63d1-499f-bc53-e1e0e07069cf.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of output for third burger order<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-mini-project-2-burgers/grade/nn379" target="_blank">Grading</a></td></tr></table>