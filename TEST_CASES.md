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


## TC005 – Search Product

### Objective

Verify that a user can search for a product successfully.

### Preconditions

* The Automation Exercise website is available.

### Test Data

* Search term: Blue Top

### Test Steps

1. Open https://automationexercise.com.
2. Click **Products**.
3. Verify that the Products page is displayed.
4. Enter **Blue Top** in the search field.
5. Click the **Search** button.
6. Verify that the search results are displayed.
7. Verify that the product **Blue Top** appears in the results.

### Expected Result

The Products page displays the search results, including the product "Blue Top".


## TC006 – Add Product to Cart

### Objective

Verify that a user can add a product to the shopping cart successfully.

### Priority

High

### Preconditions

* The Automation Exercise website is available.

### Test Data

* Product: Blue Top

### Test Steps

1. Launch the browser.
2. Navigate to https://automationexercise.com.
3. Click **Products**.
4. Verify that the Products page is displayed.
5. Locate the product **Blue Top**.
6. Click **Add to Cart**.
7. In the confirmation modal, click **View Cart**.
8. Verify that the Cart page is displayed.
9. Verify that **Blue Top** is present in the cart.

### Expected Result

The selected product is successfully added to the shopping cart and appears on the Cart page.


## TC007 – Remove Product from Cart

### Objective

Verify that a user can remove a product from the shopping cart.

### Priority

High

### Preconditions

* The shopping cart contains at least one product.

### Test Data

* Product: Blue Top

### Test Steps

1. Launch the browser.
2. Navigate to https://automationexercise.com.
3. Add the product **Blue Top** to the cart.
4. Open the shopping cart.
5. Verify that **Blue Top** is present.
6. Click the **Delete (X)** button for the product.
7. Verify that the product is removed from the shopping cart.

### Expected Result

The selected product is successfully removed from the shopping cart.
