# Test Cases

## TC001 - Verify Home Page Loads Successfully

**Objective**
Verify that the Automation Exercise home page loads successfully.

**Preconditions**
- Google Chrome is installed.
- Internet connection is available.

**Test Steps**
1. Open the browser.
2. Navigate to https://automationexercise.com
3. Verify the page title.

**Expected Result**
The page title should be:

Automation Exercise

## TC002 - Register a New User Successfully

**Objective**
Verify that a new user can successfully register on the Automation Exercise website.

**Preconditions**

- The Automation Exercise website is accessible.
- A unique email address is available for registration.

**Test Data**

- **Name**: Test User
- **Email**: A unique email address (generated during test execution)
- **Password**: Password123

**Test Steps**

1. Launch Google Chrome.
2. Navigate to https://automationexercise.com.
3. Verify that the home page is displayed.
4. Click Signup / Login.
5. Verify that the New User Signup! section is displayed.
6. Enter a valid name.
7. Enter a unique email address.
8. Click the Signup button.
9. Verify that the Enter Account Information page is displayed.
10. Complete all the required registration fields.
11. Click the Create Account button.
12. Verify that the ACCOUNT CREATED! message is displayed.
13. Click the Continue button.
14. Verify that Logged in as username is displayed.

**Expected Result**

- The account is created successfully.
- The ACCOUNT CREATED! confirmation message is displayed.
- The user is logged into the application.

## TC003 – Login User with Valid Credentials

**Preconditions**:
- User account already exists.
- User has valid email and password.

**Test Steps**:
1. Open https://automationexercise.com
2. Click Signup / Login
3. Enter registered email address
4. Enter registered password
5. Click Login button
6. Verify that "Logged in as username" is displayed

**Expected Result**:
User should be successfully logged in.

## TC004 – Logout User Successfully

### Objective

Verify that a logged-in user can successfully log out of the application.

### Preconditions

* A valid user account exists.
* The user is not logged in.

### Test Data

* Email: Registered user email
* Password: Registered user password

### Test Steps

1. Open https://automationexercise.com.
2. Click **Signup / Login**.
3. Enter a valid email address.
4. Enter a valid password.
5. Click **Login**.
6. Verify that **Logged in as username** is displayed.
7. Click **Logout**.
8. Verify that the **Login to your account** page is displayed.

### Expected Result

The user is logged out successfully and is redirected to the Login page.
