<table><tr><td> <em>Assignment: </em> IS601 Mini Project 3  Business Management</td></tr>
<tr><td> <em>Student: </em> Nashid Ahmed Shah Nashid Ahmed Shah (nn379)</td></tr>
<tr><td> <em>Generated: </em> 4/8/2023 1:03:30 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-mini-project-3-business-management/grade/nn379" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <div>Initial Preperation:</div><div><ol><li>Create two new dynos/VMs in Heroku:</li><ol><li>is601-ucid-mp3-dev</li><li>is601-ucid-mp3-prod</li></ol><li>Configure the heroku config vars and github secrets similar to how dev/prod were setup</li><li>Create two new secrets for github and set the values per the machine names in step 1</li><ol><li>HEROKU_APP_MP3_DEV</li><li>HEROKU_APP_MP3_PROD</li></ol><li>Duplicate your dev/prod yml files and have it listen to the mp3-dev and mp3-prod branches respectively</li><ol><li>Make sure you refer to the proper app secrets from step 3</li><li>You can merge these into regular dev/prod later but you'll want your final project to deploy over it (overwrite) on the normal dev/prod dynos/VM</li></ol><li>You can add this HW branch to the dev yml to test your deployments prior to the pull request to dev from step 4</li></ol></div><div><br></div><div><br></div><ol><li>checkout dev and pull any latest changes</li><li>Create a branch called mp3-prod and immediately push it</li><li>Create a branch called mp3-dev and immediately push it</li><li>Create a branch called MiniProject-3</li><li>Add all the baseline files first under a folder called BusinessManagement (included below)</li><li>Don't forget to copy your .env file from flask_sample into BusinessManagement</li><li>source the venv and pip install the requirements.txt</li><li>Run the BusinessManagement/sql/init_db.py script</li><li><b>Immediate add/commit/push to github</b></li><li>Open a pull request to mp3-dev and keep it open until you're done adding the submission file</li><li>Make your code changes per the following requirements</li><ol><li>Important: run the test files indiviudally as you're working/testing to save on query quota usage</li><li>&nbsp;pytest BusinessManagement/test/name_of_test.py -rA</li></ol><li>Add/commit periodically (recommended after you implement a TODO item or checlist item and add a related commit message for clarity)<br></li><ol><li>Do not delete any provided comments</li></ol><li>Anywhere relevant add your ucid and the date you added the code (best to do this as you go)</li><li>You'll be capturing website screenshots from dev and code snippet screenshots (ensure you upload these properly as pull request comments to the pull request from step 10</li><ol><li>Note: You don't need separate screenshots for each checklist item, when possible it's recommended to try to capture multiple items together and reuse the image</li><li>Ensure all screenshots are properly captioned in the deliverable section so it's clear what part you're trying to show</li></ol><li>Once done, copy the markdown or download the md file and save it under the BusinessManagement folder</li><li>Do a final add/commit/push</li><li>Verify everything looks ok in the pull request</li><li>Merge the pull request</li><li>Make a new pull request from mp3-dev to mp3-prod and merge it</li><ol><li>If you want to keep original dev/prod up to date you can merge the changes into those, but they will cause a deploy to occur for each so be mindful</li></ol><li>Navigate to the submission file under the BusinessManagement folder from mp3-prod</li><li>Copy the github url to the exact file and submit it to Canvas</li></ol><div>You'll be implementing a basic Business Management site.</div><div>There will be some provided files fully working as-is and some skeleton files you'll need to fill in.</div><div>The files you need to fill in will have TODO items or comments mentioning what's expected.</div><div>Some files will have "DO NOT EDIT" mentioned, please don't edit these. If there's a doubt about any of them ask.</div><div>There are provided test case files too that all must be passing for full credit. Do not edit these test case files.</div><div>If a test case isn't possible to complete, capture the failed test case locally via `pytest BusinessManagement -rA` first, then you can rename the function to `off_original_name`.</div><div>The site will handle CRUD operations for Companies and Employees as well as allowing import of Company/Employee data via a csv file.</div><div>Note: db.py has been updated to use pymysql instead of mysql-connector-python to aid in easier queries.</div><div><br></div><div>Baseline files:&nbsp;<a href="https://github.com/MattToegel/IS601/tree/F23-MiniProject-3">https://github.com/MattToegel/IS601/tree/F23-MiniProject-3</a>&nbsp;</div><div>May want to download branch as a zip, then copy/paste the files into your repo (if/when you do, please immediately do a git add/commit to record the baseline items)</div><div><br></div><div>Provided files you don't need to edit:</div><div><ul><li>000_create_table_companies.sql</li><li>001_create_table_employees.sql</li><li>db.py</li><li>init_db.py</li><li>flash.html</li><li>company_dropdown.html</li><li>country_state_selector.html</li><li>upload.html</li><li>sort_filter.html</li><li>all test files</li><li>geography.py</li><li>__init__.py (remains empty)</li><li>Dockerfile</li><li>main.py</li><li>index.py</li></ul><div>All other files likely have requirements to fill in.</div></div><div><br></div></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Identity Edits and Setup </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the index page being displayed (from dev)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/230681524-294dde1c-5ff0-4186-a738-49e9213985be.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of index page of app from heroku with identity edits<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/230681380-5064694d-0ab1-479a-a9aa-574df5719b1c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of url_for edits<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot from the DB extension of vs code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/230682268-20629406-ac4a-45bf-a3ce-3e0a59ee0796.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of DB extension showing both company and employee tables<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Upload / Import CSV File (provided data.csv) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of /import route (code)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/230683031-3be53c67-2249-427a-8922-db5fb4a2d4b6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of csv file check<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/230687175-c905f273-8735-4cfa-aacc-8a45aa6d68e8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of admin import code. Shows that companies and employees are imported only<br>if their respective fields exist using an if condition. The screenshot also shows<br>the flash messages for when companies/employees are inserted or not loaded.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of the website when uploading the data.csv file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/230690140-a5e157d1-3719-4199-9a6f-24daefa6fc9c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing error message when form was submitted without a file attached<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/230690150-a3d92472-8869-4452-9e28-3c74960e2c22.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing the error message when the file is not a .csv file<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/230690155-fb80659e-7892-4f88-9a17-374390a070a6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing the success message with the proper count of companies and employees<br>inserted<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data (basic summary/view)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/230682268-20629406-ac4a-45bf-a3ce-3e0a59ee0796.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing employee and company data was uploaded<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Add Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/230696154-70c9f2a4-6b23-4f3f-b739-86babbd1aed2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing the add employee code .py file<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/230703058-ef71f504-48d0-4914-95c0-032cfde0527b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing the add employee html file<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/230703167-605c86c9-9c0b-4df3-998c-651dac8ce829.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot to show filled in valid data prior to submission<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/230703290-4ae033ec-e615-4326-a0d4-7e17a5402a87.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot to show success message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/230703307-c2823691-a277-4c11-b5c4-cee1d9af1b31.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot to show first_name error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/230703330-4d44079a-61e6-4b17-959c-fc1c71eef886.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot to show last_name error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/230703363-44100ff7-a32b-439e-a107-fde68965425e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot to show email required error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/230703388-2234d9e4-96b8-43d7-acc1-9826f97cd2c0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot to show email format validation message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new employee DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/230703483-c422452a-db15-421c-9369-160a655e4a7c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the new employee in the VScode db along with it&#39;s company from<br>the companies table.<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> List/search Employees </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/230705142-965723fb-8366-4c4d-9c7c-51d4e0df038a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of search employee py file <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/230705257-aee6a768-9d1a-4107-afe4-b9fadb433437.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of list employee html file<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/230705470-ce2defc0-241d-4839-81ba-4a54c18aa18f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing results with first_name filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/230705584-f2920c7d-53fc-41a0-9447-0bb45fffdf76.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing results with last_name filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/230705606-15e771a7-641b-4dfc-961a-055db0f952c8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing results with email filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/230705627-ca6f364e-3440-41c2-8edf-d921a2257404.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing results with company filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/230705653-d953c1ed-98df-4427-a593-ed9637a7debd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing one asc filter applied (the first_name filter has been applied here)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/230705737-4a757b57-206a-424a-bf96-b857c5a53590.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing one desc filter applied (the company name filter has been applied<br>here)<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Edit Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/230706221-0c4106be-76af-4203-bd75-3ff57c76bcb6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of edit employee py file<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/230706270-1a643cd8-4229-494a-b212-bf053f4510ba.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of edit employee html file<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/230706509-55cb5dfc-f326-4ca9-a903-72b3b73fafac.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing data before an edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/230706590-96475cc7-2083-4de1-bbc2-033c137a190f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing data after editing data but before clicking save employee (all fields<br>have been changed to new values)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/230706597-0f61431d-c1ad-46ca-819a-a19022ae843e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing success after editing<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of employee data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/230706569-375b65d0-3af2-4dff-9650-918c7aaa93af.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing db in vs code showing the employee before editing all the<br>fields<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/230706644-4ad034f0-dd38-4651-bcfa-e8647847fd70.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing the same employee after the edit is complete<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/230708519-d1ada60f-c1e0-4e21-a020-c1c4dd1e90ce.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of add company py file<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/230708686-167439f6-a1f1-4700-9bac-554a3e12d4c3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of add employee html file<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/230708845-6f04e488-14e2-4f2c-a095-203097e97533.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing filled in valid data prior to submission<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/230708872-b224c19a-8736-48a8-b983-387df487e8c3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing success message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/230708932-c3b9f9bf-cb98-4071-9fe0-717a8becc8fc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing name error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/230708963-7b5644b0-f472-490d-89dd-3ce497107a0f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing address error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/230709026-6c091ecb-c044-4702-9391-d5615eaac021.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing city error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/230709088-66d19c41-c503-4520-803d-b5d450f74d9e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing zip error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/230709151-e95c22f3-c065-4431-ba09-e8f5781d1c19.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing country error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/230709186-0f73471f-356c-448e-93a0-1e9d2d73d1be.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing state error message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new company DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/230709293-e1600628-85c2-4673-aa93-dcc04b6de740.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of DB in vs code showing the newly added company<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> List/Search Comapny </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/230710337-be5007fd-2682-4387-b12b-887e454aecc6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of search company py file<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/230710589-f45fb4ac-06ae-45cc-9703-4879dd5d6200.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of list companies html file<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/230710637-19d62ef9-60f4-4eed-8e78-d13bdba777f2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing results with name filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/230710690-5d1ec5ae-a707-48e8-ad11-32e7d7173a61.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing results with country filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/230710705-10b5c74e-72db-485c-9409-2f84ae0b0616.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing results with state filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/230710734-e819a65f-c3a2-4760-b6d6-a1eba3b13020.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing one asc filter applied with city label chosen<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/230710828-ebf637c6-ffd7-4384-abd9-3009844dcf19.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing one desc filter applied with state label chosen<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Edit Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/230712700-2fa78264-5d1e-4db4-9390-acebb8321952.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of edit company py file<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/230712816-fefc1406-1cad-47e6-9866-5b8449460265.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of edit company html file<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/230712960-2e3fcdfc-cb72-47ee-9d0a-af20bbd0ece5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing data before an edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/230713076-39906be8-4ed1-4cea-87bf-214071a4fc10.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing data after a successfull edit<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of company  data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/230712982-51764e5a-4de9-4ba2-94a6-c1c107ac788f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of DB from vs code before editing the company<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/230713132-84cc5eb7-53f8-430c-a889-29b09bbdf2fa.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of DB from vs code after editing all fields in the company<br>except for the country field.<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Delete Employee and Delete Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /delete route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/230731034-d834e38a-0cd0-4f8f-ab42-04709400f867.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing the delete employee py file<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a before and after website screenshot of deleting an employee (search results)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/230731631-4deb8da0-e954-420f-aba7-15786d88c87e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot before deleting the employee. (The employee that will be deleted is employee<br>ID 10 which is the first employee shown in the screenshot)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/230731672-cfae8ae4-6440-46be-9acc-dbfe28700845.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot after deleting employee with id 10.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of code for /delete route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/230731557-ff900b05-5ca6-4d6f-8f8b-8194c35ee9e4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing the delete company py file<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a before and after website screenshot of deleting a company (search results)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/230731899-0a9d977c-0f20-4615-9dd0-669b8dd0b69c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of companies before deleting (The company to be deleted is company id<br>44, Abc Enterprises Inc, which is the 3rd company in the screenshot)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/230731943-50af3e44-71df-4dda-9d03-1936dd8c07de.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing the employee in Abc enterprises Inc. before deleting the company (Employee<br>id: 44, 6th employee in the screenshot). The second employee from this company<br>was deleted beforehand for the purspose of this example.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/230732096-b468a03d-7d4d-4f77-a502-d72fc5a92ae2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing companies after deletion. ID 44 no longer exists in the list<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/230732145-7a3fb80a-3d94-4d9a-9ab8-7e8e3fc2433b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the employee after deletion. Employee ID 44 who was previously allocated to<br>the now deleted company has been unallocated.<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Test Cases and Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot Test case Results</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/37153833/230732301-134d4663-9810-4791-99bf-63ada3d22fea.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing the response of pytest -rA<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Issues / Learnings / Interesting things to note</td></tr>
<tr><td> <em>Response:</em> <ul><li>I learned about <b>SimpleNamespace, </b>which helps convert an object into a namespace object<br>which in turn allows us to access parameters in an object using the<br>dot notation.</li><li>The delete functionality does not return the number of rows deleted which<br>causes an issue to arise when the user tries to delete an employee<br>through the URL. If the id passed to the delete function does not<br>exist in the database but is a valid number. The DB will simply<br>inform the user that the employee has been deleted. This does not cause<br>any harm to the database since nothing is maliciously deleted but it incorrectly<br>informs the user that an employee was deleted when it in fact doesn't<br>exist. This can be solved in the db.py <b>__runQuery</b> function, during DELETE, instead<br>of converting the status to true or false based on the number of<br>rows returned. we could just return the number and handle it in the<br>employee/company python file. If the number is 0, inform the user that the<br>employee id is invalid, else if &gt;0, it was successfully deleted</li><li>I initially faced<br>an issue with some of the test cases since I had forgotten to<br>make the check during import to ensure the database gets employees and companies<br>only if all fields are present. This caused my database to get corrupted<br>with incomplete data which forced me to dig through the test cases to<br>figure out the problem. This helped me get more acquainted with debugging in<br>python. A simple if condition to make sure all fields are present during<br>import for employees and companies fixed the issue.</li></ul><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-mini-project-3-business-management/grade/nn379" target="_blank">Grading</a></td></tr></table>
