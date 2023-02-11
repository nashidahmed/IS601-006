<table><tr><td> <em>Assignment: </em> IS601 - Mini Project 1 - Tracker App</td></tr>
<tr><td> <em>Student: </em> Nashid Ahmed Shah Nashid Ahmed Shah (nn379)</td></tr>
<tr><td> <em>Generated: </em> 2/10/2023 8:11:26 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-mini-project-1-tracker-app/grade/nn379" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout dev branch and pull any pending changes&nbsp;</li><ol><li>&nbsp;git checkout dev</li><li>&nbsp;git pull origin dev</li></ol><li>Create a new branch for this assignment (see Desired Branch Name)</li><ol><li>git checkout -b MP1-Tracker</li></ol><li>Create a new folder called MP1 in your local repository</li><li>Create a new file called tracker.py</li><li>Copy/paste the content from this template:&nbsp;&nbsp;<a href="https://gist.github.com/MattToegel/380e6baa24f6c25b74bf2ce99ccba6da">https://gist.github.com/MattToegel/380e6baa24f6c25b74bf2ce99ccba6da</a></li><li>Add/commit/push the template file</li><ol><li>git add --all</li><li>git commit -m "adding template"</li><li>git push origin MP1-Tracker</li></ol><li>Create a pull request from MP1-Tracker to dev (keep it open, do not close it until you're done)</li><li>Solve the various todo items (also noted below in the deliverables) and fill in the evidence</li><ol><li>Periodically add/commit; recommended after each solved item or every few items</li></ol><li>Save and copy/download the markdown</li><li>Create a new file mp1-submission.md in the MP1 folder</li><li>Add the markdown content</li><li>add/commit/push all the pending files for this assignment (tracker.py and mp1-submission.md)</li><li>If everything looks good on the pull request complete the merge</li><li>Create a new pull request from dev to prod and merge it to update prod (not used yet but you want to keep this up to date)</li><li>checkout dev locally and pull the changes to be up to date</li><li>Navigate to the prod branch on github and find the mp1-submission.md file and get the link to the file to submit to canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Add Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited add_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/218189918-abcfcf42-90dd-458f-a32e-5ea32f2a1628.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the implementation of the add_task function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of add_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/218190922-f78c8560-489f-4bbb-bbb6-d4bfa9d17c78.jpg"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the success/failure of the add_task functionality<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/218197514-50c5ac92-208e-49b4-bfb8-959aad8d29cf.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the success out add_task with the view<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for add_task()</td></tr>
<tr><td> <em>Response:</em> <ol><li><font size="2">update lastActivity with the current datetime value - assign current datetime (<b>datetime.now()</b>)<br>to the task's <b>lastActivity</b></font></li><li><font size="2">set the name, description, and due date (all must<br>be provided) - assigned the name, description and due date to the respective<br>arugements in the task list.</font></li><li><font size="2">due date must match one of the formats<br>mentioned in str_to_datetime() -&nbsp;due date is assigned in a <b>try</b> block to check<br>if it is a valid due date, if it is not, an excpetion<br>is thrown and the user is informed that the due date is of<br>an invalid format and the code will exit the function.<br></font></li><li><font size="2">add the new<br>task to the tasks list - task is added to the tasks list<br>using the <b>append</b> function.</font></li><li><font size="2">output a message confirming the new task was added<br>or if the addition was rejected due to missing data - using an<br><b>if</b> condition and <b>and</b>, check if all the arguments have been entered by<br>the user, if not, check which values have not been entered and inform<br>the user without adding the task to the tasks list.<br></font></li><li><font size="2">make sure save()<br>is still called last in this function - <b>save() </b>is called at the<br>end of the function.<br></font></li><li><font size="2">include your ucid and date as a comment of<br>when you implemented this, briefly summarize the solution - comments provided as needed.</font></li></ol><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Process Update Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited process_update() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/218191545-4b6c3199-5679-4f46-b584-180d437960ba.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the process_update functionality<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain the solutions to the checklist items for process_update()</td></tr>
<tr><td> <em>Response:</em> <ol><li><font size="2">get the task by index - access the task from the tasks<br>list using the index by <b style="">tasks[index]&nbsp;</b>&nbsp;and assign it to the <b style="">task</b>&nbsp;variable</font></li><li><font<br>size="2">consider index out of bounds scenarios and include appropriate message(s) for invalid index<br>- check if the index exists in the tasks list using the <b>if</b><br>condition <b>0 &lt;= index &lt; len(tasks)</b>, if it does not exist, inform the<br>user the user that the task does not exist.<br></font></li><li><font size="2">show the existing value<br>of each property where the TODOs are marked in the text of the<br>inputs (replace the TODO related text) - using the <b>task</b>&nbsp;variable, show the user<br>the existing values in the task.<br></font></li><li><font size="2">include your ucid and date as a<br>comment of when you implemented this, briefly summarize the solution - comments provided<br>as needed.</font></li></ol><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Update Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited update_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/218192330-8a991bbb-566a-4a27-9a9f-c07ecc0088b0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing update_task functionality<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of update_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/218194396-07f1fb80-2f28-4a99-8316-0e460b9b9aa0.jpg"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing success of update_task, failure when invalid date is provided and failure when<br>no data is entered<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for update_task()</td></tr>
<tr><td> <em>Response:</em> <ol><li><font size="2">find the task by index - access the task from the tasks<br>list using the index by&nbsp;<b>tasks[index]&nbsp;</b>&nbsp;and assign it to the&nbsp;<b>task</b>&nbsp;variable</font></li><li><font size="2">consider index out of<br>bounds scenarios and include appropriate message(s) for invalid index - check if the<br>index exists in the tasks list using the&nbsp;<b>if</b>&nbsp;condition&nbsp;<b>0 &lt;= index &lt; len(tasks)</b>, if<br>it does not exist, inform the user the user that the task does<br>not exist.</font></li><li><font size="2">update incoming task data if it's provided (if it's not provided<br>use the original task property value) - check if any value is provided<br>by the user for the name, description and due date using an&nbsp;<b>if </b>condition<br>(with <b>or</b>), if not inform the user that no input has been entered<br>and the task has not been updated.<br></font></li><li><font size="2">update lastActivity with the current datetime<br>value - assign current datetime (<b>datetime.now()</b>) to the task's <b>lastActivity</b><br></font></li><li><font size="2">output that the<br>task was updated if any items were changed, otherwise mention task was not<br>updated - if any value was entered by the user, first check if<br>the due date entered is a valid due date using a <b>try</b>&nbsp;block, if<br>it is valid, add the task and inform the user that the task<br>has been updated.<br></font></li><li><font size="2">make sure save() is still called last in this function<br>-&nbsp;<b style="">save()&nbsp;</b>is called at the end of the function.</font></li><li><font size="2">include your ucid and<br>date as a comment of when you implemented this, briefly summarize the solution<br>- comments provided as needed.</font></li></ol><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Mark Task Done/Complete Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited mark_done() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/218225227-a2c214c3-2d62-4cc2-8cbb-da8ae60f1fcf.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the mark_done functionality<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of mark_done()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/218198222-90f8bc19-0f21-46fd-8f43-5cd9fd2f220f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing success/failure of mark_done function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for mark_done()</td></tr>
<tr><td> <em>Response:</em> <ol><li><font size="2">find the task by index - access the task from the tasks<br>list using the index by&nbsp;<b>tasks[index]&nbsp;</b>&nbsp;and assign it to the&nbsp;<b>task</b>&nbsp;variable</font></li><li><font size="2">consider index out of<br>bounds scenarios and include appropriate message(s) for invalid index - check if the<br>index exists in the tasks list using the&nbsp;<b>if</b>&nbsp;condition&nbsp;<b>0 &lt;= index &lt; len(tasks)</b>, if<br>it does not exist, inform the user the user that the task does<br>not exist.</font></li><li><font size="2">if it's not done, record the current datetime as the value<br>- check if the task is not done using an <b>if</b>&nbsp;condition and negation<br>of the <b>task['done'] </b>value, then store the current datetime(<b>datetime.now()</b>) to <b>task['done'] </b>and inform<br>the user that the task has been marked as done.<br></font></li><li><font size="2">if it is<br>done, print a message saying it's already completed - if it is not<br>done, inform the user that the task has already been completed.<br></font></li><li><font size="2">make sure<br>save() is still called last in this function -&nbsp;<b>save()&nbsp;</b>is called at the end<br>of the function.</font></li><li><font size="2">include your ucid and date as a comment of when<br>you implemented this, briefly summarize the solution - comments provided as needed.</font></li></ol><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> View Task Logic (and list) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited view_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/218199958-243e6c13-6d50-4bdd-8a00-8ba9c696c98e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing view_task functionality<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of view_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/218200197-d634f0e5-57d3-401b-ac33-6ae3d6003d5b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing success/failure of view_task output<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add screenshot(s) of list_tasks() output showing a few examples</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/218200611-5b1fd6aa-936c-4800-80d7-9223aba43608.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing output of list_tasks function<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Delete Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited delete_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/218201519-854228e9-61c8-4dc1-9da4-38d03af98be2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing delete_task functionality<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of delete_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/218202826-61b16e0a-e4d9-41c9-bebd-92ce74bb41dc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing success/failure of delete_task<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for delete_task()</td></tr>
<tr><td> <em>Response:</em> <ol><li><font size="2">delete/remove task from list by index - delete or remove the task<br>from the list using the <b style="">pop</b>&nbsp;function.<br></font></li><li><font size="2">message should show if it was<br>successful or not - inform the user that the task has been deleted<br>using the <b>print</b>&nbsp;function.<br></font></li><li><font size="2">consider index out of bounds scenarios and include appropriate message(s)<br>for invalid index - check if the index exists in the tasks list<br>using the&nbsp;<b>if</b>&nbsp;condition&nbsp;<b>0 &lt;= index &lt; len(tasks)</b>, if it does not exist, inform the<br>user the user that the task does not exist.</font></li><li><font size="2">make sure save() is<br>still called last in this function -&nbsp;<b>save()&nbsp;</b>is called at the end of the<br>function.</font></li><li><font size="2">include your ucid and date as a comment of when you implemented<br>this, briefly summarize the solution - comments provided as needed.</font></li></ol><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Get Incomplete Tasks Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_incomplete_tasks() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/218203062-2ec0c03e-fb45-48cb-acb8-38245c128a48.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the get_incomplete_tasks functionality<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_incomplete_tasks()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/218203527-819b7f8a-9b94-4577-a49b-b39ab9fc53da.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing success/failure of get_incomplete_tasks output<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_incomplete_tasks()</td></tr>
<tr><td> <em>Response:</em> <ol><li><font size="2">generate a list of tasks where the task is not done -<br>get the list of tasks where the task is not done using the<br>list comprehension method passing an if condition checking <b>if</b> the task is <b<br>style="">not</b>&nbsp;done.<br></font></li><li><font size="2">pass that list into list_tasks() - the above list is assigned to<br>a variable <b>tasks</b>&nbsp;and this value is passed into the <b>list_tasks </b>function.<br></font></li><li><font size="2">include your<br>ucid and date as a comment of when you implemented this, briefly summarize<br>the solution - comments provided as needed.</font></li></ol><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Get Over Due Tasks Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_overdue_tasks() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/218204608-553da403-c935-470b-9442-c4be5077ca10.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing get_overdue_tasks functionality<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_overdue_tasks()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/218204882-064a11c1-9c5b-4692-89f3-54d6273fa1fc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing success/failure of get_overdue_tasks output<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_overdue_tasks()</td></tr>
<tr><td> <em>Response:</em> <ol><li><font size="2">generate a list of tasks where the task is not done -<br>get the list of tasks where the task is not done and where<br>the task due date is before the current datetime(<b>datetime.now()</b>) using the list comprehension<br>method passing an <b>if</b> condition checking if the task is&nbsp;<b style="">not</b>&nbsp;done and if<br>the due date is before the current datetime.<br></font></li><li><font size="2">pass that list into list_tasks()<br>- the above list is assigned to a variable&nbsp;<b>tasks</b>&nbsp;and this value is passed<br>into the&nbsp;<b>list_tasks&nbsp;</b>function.<br></font></li><li><font size="2">include your ucid and date as a comment of when you<br>implemented this, briefly summarize the solution - comments provided as needed.</font></li></ol><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Get Time Remaining Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_time_remaining() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/218207205-91cbd0a5-967c-4e1a-a1fa-1fa9e7c5e5a8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the get_time_remaining functionality<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_time_remaining()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/218207643-6cac063b-5abe-4cf0-bd11-969a587019cc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing output of remaining_time function. The time when this function was run was<br>at 2/10/23 17:03 approximately<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_time_remaining()</td></tr>
<tr><td> <em>Response:</em> <ol><li><font size="2">get the task by index - access the task from the tasks<br>list using the index by&nbsp;<b>tasks[index]&nbsp;</b>&nbsp;and assign it to the&nbsp;<b>task</b>&nbsp;variable</font></li><li><font size="2">consider index out of<br>bounds scenarios and include appropriate message(s) for invalid index - check if the<br>index exists in the tasks list using the&nbsp;<b>if</b>&nbsp;condition&nbsp;<b>0 &lt;= index &lt; len(tasks)</b>, if<br>it does not exist, inform the user the user that the task does<br>not exist.</font></li><li><font size="2">get the days, hours, minutes, seconds between the due date and<br>now - find the difference between the current datetime and the due date<br>and assign it to <b>remaining_time</b>&nbsp;(or due date and current datetime if due date<br>is later) and get the days and seconds using <b>remaining_time.days </b>and <b>remaining_time.seconds </b>respectively.<br>Using <b>remaining_time.seconds&nbsp;</b>calcaulte the remaining hours and and minutes using the formulae <b>remaining_time.seconds //<br>3600&nbsp;</b>and (<b>remaining_time.seconds // 60) % 60&nbsp;</b>&nbsp;respectively.</font></li><li><font size="2">display the remaining time via print in<br>a clear format showing days, hours, minutes, seconds - produce the string for<br>days, hours, minutes and seconds separately accounting for plural if days, minutes, hours<br>or seconds are more than one. If they are equal to 0, they<br>are given empty string as value so they can filtered out. Use join<br>and filter out the empty strings to get a clean output for the<br>days, hours, mintues and seconds.&nbsp;<br></font></li><li><font size="2">if the due date is in the past<br>print out how many days, hours, minutes, seconds the task is over due<br>(clearly note that it's over due, values should be positive) - check if<br>due date is more than the current time, if it is inform the<br>user that the task is due in <b>remaining_time</b>, else inform the user that<br>the task is overdue by <b>remaining_time</b>.</font></li><li><font size="2">include your ucid and date as a<br>comment of when you implemented this, briefly summarize the solution - comments provided<br>as needed.</font></li></ol><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of program output generated from filling in this deliverable (or close to it)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/218227864-66f91e8b-4712-42dd-9904-d276b1182ee0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing output of the entire program (part 1)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/218227937-9444dcd6-0a6f-4bdc-910c-199247c481ef.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing output of the entire program (part 2)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) of the saved JSON file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/218228520-200ce642-ac90-4122-9d3d-c1846de8208f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the saved json file tracker.json<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Discuss any issues and how they were overcome or learnings from this project</td></tr>
<tr><td> <em>Response:</em> <div><ul><li>dealing with datetime was challenging - When the user enters a new task<br>or updates the due date of an existing task, python stores the value<br>as a datetime object since the <b>str_to_datetime</b>&nbsp;function returns a datetime, if the program<br>is restarted, this issue does not arise, as python gets the value as<br>a string. To avoid the issue, where needed (<b>get_overdue </b>and<b> get_time_remaining</b>)&nbsp;the <b>due </b>value<br>was converted into a string before it was passed to the <b>str_to_datetime </b>function.</li><li>I<br>got pretty comfortable working my way around Python, the syntax is quite straightforward<br>and easier to get the hang of.</li><li>Calculating the remaining time was a little<br>challenging at first as I tried to find the&nbsp;difference between due date and<br>the current datetime even in the overdue case. The result turned out to<br>be incorrect as the the negative values were a day off. For example<br>if the due date is set to 2/10/23 4:0:0 and the current datetime<br>is 2/10/23 5:0:0, a simple <b>due - now </b>expression returned -1 day, even<br>though it was just 1 hour before. so I changed the condition to<br>check for which datetime was later and calculate the difference accordingly.</li></ul></div><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add pull request for this assignment (project branch to dev)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/nashidahmed/IS601-006/pull/6">https://github.com/nashidahmed/IS601-006/pull/6</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-mini-project-1-tracker-app/grade/nn379" target="_blank">Grading</a></td></tr></table>