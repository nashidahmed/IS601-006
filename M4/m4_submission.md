<table><tr><td> <em>Assignment: </em> M4-Simple-Calc</td></tr>
<tr><td> <em>Student: </em> Nashid Ahmed Shah Nashid Ahmed Shah (nn379)</td></tr>
<tr><td> <em>Generated: </em> 2/27/2023 6:50:57 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/m4-simple-calc/grade/nn379" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <p>Make sure you're working in an up to date branch</p><ul><li><code>git checkout dev</code></li><li><code>git pull origin dev</code></li><li><code>git checkout -b M4-Simple-Calc</code></li></ul><p>This will likely be started in class.</p><p>Steps:</p><ol><li>Create a new Folder called M4</li><li>Create a new file called MyCalc.py inside this folder</li><li>Create a MyCalc Class</li><li>Define basic addition / subtraction / multiplication / division functions<ol><li>These functions should update an internal variable as a running total/value called&nbsp;<code><b>ans</b></code></li><li>All functions must properly handle the math given standard math scenarios (i.e., show proper messages when trying to divide by zero for example)</li><li>Since you'll likely be taking screenshots of the code, make sure you add a comment with your ucid and the date</li></ol></li><li>Define a "main" logic to run when the program runs</li><li>This logic should ask for user input<ol><li>The input can be any valid number, any valid math operator, and any valid number (i.e., 2 * 2)<ol><li>This will do an immediate calculation, print it, and store the answer in the&nbsp;<code>ans</code>&nbsp;variable</li></ol></li><li>Alternatively, the input can be&nbsp;<code>ans</code>, any valid math operator, any valid number (i.e.,&nbsp;<code>ans</code>&nbsp;* 2)<ol><li>This will use the previous answer (or 0 if not set) as part of the calculation, print it, and will store the new answer in the&nbsp;<code>ans</code>&nbsp;variable</li></ol></li></ol></li><li>Create a test case for each scenario that utilize functions to have expected input and compare against expected output, all cases should pass (test cases should have a series of data passed into them)<ol><li>Test number-add-number</li><li>Test ans-add-number</li><li>Test number-sub-number</li><li>Test ans-sum-number</li><li>Test number-mult-number</li><li>Test ans-mult-number</li><li>Test number-div-number</li><li>Test ans-div-number</li></ol></li><li>Create a new file called m4_submission.md inside the M4 folder</li><li>Fill out the below deliverables</li><li>Generate the markdown and paste it into the m4_submission.md</li><li><code>git add .</code></li><li><code>git commit -m "adding m4 hw"</code></li><li><code>git push origin M4-Simple-Calc</code></li><li>Create a pull request M4-Simple-Calc to dev</li><li>Create a pull request dev to prod (after the previous one is merged)</li><li>Navigate to the prod branch on github, go to the M4 folder, click the m4_submission.md</li><li>Submit this link to Canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Code Snippets (Make sure each screenshot has a comment showing your ucid and the date it was written) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of valid Addition Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/219744030-3ff3fc46-9bad-4466-99e8-11e100df14d7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the addition function along with the _as_number function to convert the string<br>into a number<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of valid Subtraction Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/219744030-3ff3fc46-9bad-4466-99e8-11e100df14d7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the subtraction function along with the _as_number function to convert the string<br>into a number<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/219785090-4b6a3d4e-6249-432f-868a-87898556ef91.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Prepocessing of user entered string before the calc function is called<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of valid Multiplication Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/219744030-3ff3fc46-9bad-4466-99e8-11e100df14d7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the multiplication function along with the _as_number function to convert the string<br>into a number<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshot of valid division Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/219744030-3ff3fc46-9bad-4466-99e8-11e100df14d7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the division function along with the _as_number function to convert the string<br>into a number<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Test Case Validations </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of passing number-add-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/221714672-81531154-e987-4241-914c-ebc3fe59d826.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code snippet of the test helper function which is called by all test<br>cases<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/219784319-f108e475-0fe0-4961-9a97-e70b0a1873a9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code snippet of the test_number_add_number function calling the test_helper function<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/219780878-20472dde-4181-4052-88be-81ba8264d846.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the data_number fixture which is passed to the test cases which operate<br>on numbers only (no &#39;ans&#39;)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/221715333-e08a71bd-8f11-4356-9cb2-527ed39244a9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing passing test case for number add number<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of passing ans-add-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/221714672-81531154-e987-4241-914c-ebc3fe59d826.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code snippet of the test helper function which is called by all test<br>cases<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/219783086-b1852bee-e67e-4d28-88f9-160b7bd51b66.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code snippet of the test_ans_add_number function calling the test_helper function<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/219781356-2f1c2eb2-4029-4c50-8178-40b94b5504ac.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the data_ans fixture which is passed to the test cases which operate<br>on numbers where one or both of the operands are &#39;ans&#39;<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/221715333-e08a71bd-8f11-4356-9cb2-527ed39244a9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing passing test case for ans add number<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of passing number-sub-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/221714672-81531154-e987-4241-914c-ebc3fe59d826.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code snippet of the test helper function which is called by all test<br>cases<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/219783359-c8770c29-7851-4bc0-aa03-e5b460bc5131.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code snippet of the test_number_sub_number function calling the test_helper function<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/219780878-20472dde-4181-4052-88be-81ba8264d846.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the data_number fixture which is passed to the test cases which operate<br>on numbers only (no &#39;ans&#39;)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/221715333-e08a71bd-8f11-4356-9cb2-527ed39244a9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing passing test case for number sub number<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshots of passing ans-sub-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/221714672-81531154-e987-4241-914c-ebc3fe59d826.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code snippet of the test helper function which is called by all test<br>cases<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/219783464-5ae22969-e06c-4b87-9bf5-2a0b699b8a02.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code snippet of the test_ans_sub_number function calling the test_helper function<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/219781356-2f1c2eb2-4029-4c50-8178-40b94b5504ac.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the data_ans fixture which is passed to the test cases which operate<br>on numbers where one or both of the operands are &#39;ans&#39;<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/221715333-e08a71bd-8f11-4356-9cb2-527ed39244a9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing passing test case for ans sub number<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Screenshots of passing number-mult-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/221714672-81531154-e987-4241-914c-ebc3fe59d826.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code snippet of the test helper function which is called by all test<br>cases<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/219783699-694ee1e2-3770-4cd8-9783-ab7eabe6d8da.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code snippet of the test_number_mul_number function calling the test_helper function<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/219780878-20472dde-4181-4052-88be-81ba8264d846.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the data_number fixture which is passed to the test cases which operate<br>on numbers only (no &#39;ans&#39;)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/221715333-e08a71bd-8f11-4356-9cb2-527ed39244a9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing passing test case for number mul number<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Screenshots of passing ans-multi-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/221714672-81531154-e987-4241-914c-ebc3fe59d826.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code snippet of the test helper function which is called by all test<br>cases<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/219784644-facbe572-e23a-4f68-8edc-fd3018a8aeda.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code snippet of the test_ans_mul_number function calling the test_helper function<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/219781356-2f1c2eb2-4029-4c50-8178-40b94b5504ac.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the data_ans fixture which is passed to the test cases which operate<br>on numbers where one or both of the operands are &#39;ans&#39;<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/221715333-e08a71bd-8f11-4356-9cb2-527ed39244a9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing passing test case for ans mul number<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Screenshots of passing number-div-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/221714672-81531154-e987-4241-914c-ebc3fe59d826.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code snippet of the test helper function which is called by all test<br>cases<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/219784763-95a75f8b-6732-4acf-bcd7-b588906f0567.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code snippet of the test_number_div_number function calling the test_helper function<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/219780878-20472dde-4181-4052-88be-81ba8264d846.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the data_number fixture which is passed to the test cases which operate<br>on numbers only (no &#39;ans&#39;)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/221715333-e08a71bd-8f11-4356-9cb2-527ed39244a9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing passing test case for number div number<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 8: </em> Screenshots of passing ans-div-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/221714672-81531154-e987-4241-914c-ebc3fe59d826.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code snippet of the test helper function which is called by all test<br>cases<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/219784899-ddf2792c-5c8e-486d-b28b-21b6317f7de0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code snippet of the test_ans_div_number function calling the test_helper function<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/219781356-2f1c2eb2-4029-4c50-8178-40b94b5504ac.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the data_ans fixture which is passed to the test cases which operate<br>on numbers where one or both of the operands are &#39;ans&#39;<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/221715333-e08a71bd-8f11-4356-9cb2-527ed39244a9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing passing test case for ans div number<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Briefly talk about anything you learn during this assignment/module</td></tr>
<tr><td> <em>Response:</em> <ol><li>I learned how to better deal with decimal calculations with the Decimal function<br>from the decimal module accounting for floating point precision errors.Il&nbsp;</li><li>I learned more about<br>fixtures and how to use them improve the code readability as well as<br>to instantiate variables or classes common to all test cases.</li><li>I got comfortable with<br>the pytest syntax and with writing test cases on python in general.</li></ol><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Discuss how test cases work and anything new you learned about them while doing this assignment</td></tr>
<tr><td> <em>Response:</em> <p>There are 3 fixtures in my test case.<div><ul><li>my_calc: to instantiate the MyCalc class<br>and pass it to every test case.</li><li>data_number: a list of dictionaries mimicing user<br>input containing only numbers as strings</li><li>data_ans: a list of dictionairies mimicing user input<br>containing numbers and &#39;ans&#39;</li></ul><div>I have created a helper function for the test cases<br>so that all the test cases can just call this helper function with<br>the respective arguments. The helper function tests for both positive and negative test<br>cases as well as for any exceptions raised by the program. The parameters<br>for the helper function are&nbsp;</div></div><div><ul><li>&#39;my_calc&#39; class instance which is obtained through a fixture.<br></li><li>&#39;data&#39;<br>which is obtained through a fixture<br></li><li>&#39;operation&#39; which is passed in from the respective<br>test cases as per what operation needs to be performed on the two<br>numbers.<br></li><li>&#39;res&#39; which is the name of the key in the data list of<br>dictonaries for the result of the respective operation<br></li></ul></div><div>This helper function is then in<br>turn called by each test case along with the my_calc fixture, the data<br>depending on whether the test case is for number or for &#39;ans&#39;, the<br>operation (+, -, /, *, x) and the key name of the result<br>from &#39;data&#39; to check against response of the calc() function.</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the pull request of M4-Simple-Calc to Dev link</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/nashidahmed/IS601-006/pull/8">https://github.com/nashidahmed/IS601-006/pull/8</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/m4-simple-calc/grade/nn379" target="_blank">Grading</a></td></tr></table>
