---

## Source Repository

1. Project Folder

   The main folder which contain the core source code

2. Virtualusers Folder

   The extra folder which focus on the virtual testing all the functions of webiste

---

## 1. Project Folder

### 1.1 accounts folder

#### 1.1.1 static folder

##### 1.1.1.1 login folder

Css/js files for login page

##### 1.1.1.2 password_reset folder

Css file for reset-password page

##### 1.1.1.3 profile folder

Css file for edit profile page

##### 1.1.1.4 register folder

Css/js files for register page

#### 1.1.2 templates folder

##### 1.1.2.1 admin folder

base.html used for styling the admin panel.

##### 1.1.2.2 edit_profile.html file

the html file for edit-profile page

##### 1.1.2.3 home.html file

the html file for home page

##### 1.1.2.4 login.html file

the html file for sign in page

##### 1.1.2.5 password_reset_complete.html, password_reset_form.html, password_reset_sent.html files

the html files for reset-password page

##### 1.1.2.6 register.html

the html file for register page

#### 1.1.3 admin.py file

python file for admin site to register the models

#### 1.1.4 forms.py file

python file for forms using

#### 1.1.5 models.py

python file for models using

#### 1.1.6 decorators.py

python file for identify and authorised users functions

#### 1.1.7 tests.py

python file for testing the account

#### 1.1.8 urls.py

python file for urls list using

#### 1.1.9 views.py

python file for the functions used for account 



### 1.2 managelist folder

#### 1.2.1 static folder

##### 1.2.1.1 managelist folder

Css/js/png files for researcher managelist(home) page

##### 1.2.1.2 view folder

Css/js files for staff to view in managelist(home) page

#### 1.2.2 templates folder

##### 1.2.2.1 base.html

html file for home navigation bar

##### 1.2.2.2 managelist.html

html file for researcher managelist page

##### 1.2.2.3 viewNormal.html

html file for view the application

#### 1.2.3 tests.py file

python file for testing the managelist page

#### 1.2.4 urls.py file

python file including related urls for managelist page

#### 1.2.5 utils.py 

python file for converting to pdf function

#### 1.2.6 views.py

python file including all the functions related to managelist page



### 1.3 coversheet folder

#### 1.3.1 static folder

##### 1.3.1.1 coversheet folder

Css/js/png files used for coversheet page

#### 1.3.2 templates folder

##### 1.3.2.1 coversheet.html file

html file for coversheet page

##### 1.3.2.2 navbarcoversheet.html file

html file including two navigation bars in coversheet page

#### 1.3.3 coversheetquestion.txt file

txt file includings all the questions of coversheet page

#### 1.3.4 tests.py file

python file used for tesing the coversheet page

#### 1.3.5 urls.py file

python file including related urls for coversheet page

#### 1.3.6 views.py file

python file including all the functions related to coversheet page



### 1.4 questionnaire folder

#### 1.4.1 static folder

##### 1.4.1.1 questionnaire folder

Css/js/png files used for questionnaire page

#### 1.4.2 templates folder

##### 1.4.2.1 questionnaire.html file

html file for questionnaire page

#### 1.4.3 tests.py file

python file used for tesing the questionnaire page

#### 1.4.4 urls.py file

python file including related urls for questionnaire page

#### 1.4.5 views.py file

python file including all the functions related to questionnaire page



### 1.5 qualifier folder

#### 1.5.1 static folder

##### 1.5.1.1 welcome

Css file used for welcome page

##### 1.5.1.2 quiz folder

Css file used for qualifier quiz page

##### 1.5.1.3 failure

Css file used for High Risk (failure) page

#### 1.5.2 templates folder

##### 1.5.2.1 welcome.html file

html file for welcome page

##### 1.5.2.2 quiz.html file

html file for quiz page

##### 1.5.2.3 success.html file

html file for Low Risk (success) page

##### 1.5.2.4 failure.html file

html file for High Risk (failure) page

#### 1.5.3 tests.py file

python file used for tesing the qualifier quiz page

#### 1.5.4 urls.py file

python file including related urls for qualifier page

#### 1.5.5 views.py file

python file including all the functions related to qualifier page



### 1.6 upload folder (Not Used)

#### 1.6.1 templates folder

##### 1.6.2.1 upload.html file

html file for upload PIS/PCF page

#### 1.6.2 tests.py file

python file used for tesing the upload PIS/PCF  page

#### 1.6.3 urls.py file

python file including related urls for upload PIS/PCF  page

#### 1.6.4 views.py file

python file including all the functions related to upload PIS/PCF  page



### 1.7 PISform folder (Not Used)

#### 1.7.1 templates folder

##### 1.7.1.1 PISform.html file

html file for create PIS form page

#### 1.7.2 tests.py file

python file used for tesing the create PIS form page

#### 1.7.3 urls.py file

python file including related urls for create PIS form page

#### 1.7.4 utils.py file

python file including function for view PIS form page

#### 1.7.5 views.py file

python file including all the functions related to create/view PIS form page

#### 1.7.6 PISform.txt file

txt file including all the functions related to create PIS form page



### 1.8 consentform folder (Not Used)

#### 1.8.1 templates folder

##### 1.8.1.1 form.html file

html file for create PIS form page

#### 1.8.2 tests.py file

python file used for tesing the create PCF form page

#### 1.8.3 urls.py file

python file including related urls for create PCF form page

#### 1.8.4 utils.py file

python file including function for view PCF form page

#### 1.8.5 views.py file

python file including all the functions related to create/view PCF form page



### 1.9 approvelist folder

#### 1.9.1 static folder

##### 1.9.1.1 view folder

Css/js files for approvelist page

##### 1.9.1.2 css file

css file for approvelist page

#### 1.9.2 templates folder

##### 1.9.2.1 approvelist.html file

Html file for approvelist page

##### 1.9.2.2 view.html file

html file for view function in approvelist page

#### 1.9.3 tests.py file

python file used for tesing the approvelist page

#### 1.9.4 urls.py file

python file including related urls for approvelist page

#### 1.9.5 views.py file

python file including all the functions related to approvelist page



### 1.10 htmlcov folder

Html files is the coverage report of testing the project



### 1.11 viewforms folder

#### 1.11.1 static folder

##### 1.11.1.1 create folder

css file for create PIS/PCF forms pages

#### 1.11.2 templates

##### 1.11.2.1 consent_form.html file

html file for view PCF

##### 1.11.2.2 information_sheet.html file

html file for view PIS

##### 1.11.2.3 new_PCF.html

html file for create new PCF

##### 1.11.2.4 new_PIS.html

html file for create new PIS

#### 1.11.3 tests.py file

python file used for tesing the create/view PIS/PCF page

#### 1.11.4 urls.py file

python file including related urls for create/view PIS/PCF page

#### 1.11.5 utils.py file

python file used for converting to PDF for create/view PIS/PCF page

#### 1.11.6 views.py file

python file including all the functions related to create/view PIS/PCF page



### 1.12 Project folder

#### 1.12.1 settings.py file

python file used for setting the environment of the project and install library

the different apps created would register in this file

#### 1.12.2 urls.py

python file used for including all the urls for the project



### 1.13 add_questions.py file

python file used for admin to add the ethics questions to the database

### 1.14 add_templates.py file

python file used for admin to add the template ansewers to the database

### 1.15 manage.py file 

python file used for run command such as runserver, test

### 1.16 requirements.txt file

txt file listed the requirments of the project



---

## 2. Virtualusers Folder

### 2.1 AdminTests folder

Virtual test for Admin Panel

### 2.2 ApproveTests folder

Virtual test for Approvelist Page as ethics committee

### 2.3 Coversheet Test folder

Virtual test for Coversheet page

### 2.4 LoginTests folder

Virtual test for Login Page

### 2.5 ManagelistTest folder

Virtual test for Managelist Page as normal researcher

### 2.6 PCFTests folder

Virtual test for Create/ View PCF Pages

### 2.7 PISTests folder

Virtual test for Create/View PIS Pages

### 2.8 ProfileTests folder

Virtual test for Edit Profile Page

### 2.9 QualifierTests folder

Virtual test for Qualifier Quiz/Success/Failure Pages

### 2.10 RegisterTests folder

Virtual test for Register Page