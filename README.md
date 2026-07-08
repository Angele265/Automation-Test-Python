# Automation Exercise Selenium Python Framework

## Project Overview

This project is a Selenium automation framework built using Python and Pytest.

The framework automates the main user workflows of the Automation Exercise e-commerce website:

https://automationexercise.com/

The project follows the Page Object Model (POM) design pattern to create reusable and maintainable test automation code.

---

## Technologies Used

* Python 3.12
* Selenium WebDriver
* Pytest
* WebDriver Manager
* Pytest HTML Reports
* GitHub Actions CI/CD

---

## Project Structure

```
Automation-Test-Python

├── pages/
│   ├── base_page.py
│   ├── home_page.py
│   ├── login_page.py
│   ├── signup_page.py
│   ├── products_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── tests/
│   ├── test_home_page.py
│   ├── test_signup.py
│   ├── test_login.py
│   ├── test_logout.py
│   ├── test_search_product.py
│   ├── test_add_to_cart.py
│   ├── test_remove_from_cart.py
│   ├── test_contact_us.py
│   └── test_place_order.py
│
├── utils/
│   ├── driver_factory.py
│   ├── logger.py
│   └── data_generator.py
│
├── data/
│   └── test_data.py
│
├── reports/
├── screenshots/
├── conftest.py
├── pytest.ini
└── requirements.txt
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Angele265/Automation-Test-Python.git
```

Navigate to the project:

```bash
cd Automation-Test-Python
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running Tests

Run all tests:

```bash
pytest
```

Run a specific test:

```bash
pytest tests/test_login.py
```

Generate HTML report:

```bash
pytest --html=reports/test_report.html --self-contained-html
```

---

## Test Coverage

| Test Case | Description              |
| --------- | ------------------------ |
| TC001     | Verify Home Page         |
| TC002     | Register New User        |
| TC003     | Login User               |
| TC004     | Logout User              |
| TC005     | Search Product           |
| TC006     | Add Product to Cart      |
| TC007     | Remove Product from Cart |
| TC008     | Contact Us Form          |
| TC009     | Verify Product Details   |
| TC010     | Place Order              |

---

## CI/CD

GitHub Actions automatically executes the Selenium test suite after every push to the main branch.

Pipeline:

```
Push Code
    ↓
GitHub Actions
    ↓
Install Dependencies
    ↓
Run Pytest
    ↓
Generate Result
```

---

## Author

Automation Test Framework created as a Selenium Python QA Automation portfolio project.
