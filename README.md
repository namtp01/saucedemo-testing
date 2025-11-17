# Project

This repository is a complete Software Quality Assurance portfolio demonstrating the full testing lifecycle. It includes a formal Test Plan, manually executed Test Cases, professional Bug Reports, and a data-driven Test Automation script.
This project tests the saucedemo.com e-commerce practice website.

## 1. Project Deliverables
This project is broken down into four key deliverables, representing the core artifacts of a QA process.

## 2. Test Plan (SauceDemo_Test_Plan.md)

What it is: The strategic "blueprint" for the entire testing effort.

Contains:

Project objectives and scope (in-scope and out-of-scope features).

Test strategy (manual, automation, and cross-browser).

Tools and technologies to be used.

Bug severity definitions and entry/exit criteria.

## 3. Manual Test Cases (SauceDemo_Test_Cases.md)

What it is: A complete, step-by-step checklist of 24+ test cases used for manual execution.

Contains:

A grid of all test cases for Login, Inventory, Cart, and Checkout modules.

Test data (e.g., standard_user, problem_user).

The "Actual Result" and "Status" from the manual test run, showing 3 failed tests.

## 4. Bug Reports (SauceDemo_Bug_Reports.md)

What it is: A formal report documenting the bugs found during the manual test run.

Contains:

1 detailed bug reports with severity, steps to reproduce, and expected vs. actual results.

Bug #1 (Medium): problem_user cannot remove items out the cart.


## 5. Test Automation (test_saucedemo.py)

What it is: A Python script that automatically runs the most critical login tests.

Contains:

test_successful_login: A "happy path" test to ensure a standard user can log in.

test_invalid_logins: A powerful, data-driven test (using pytest.mark.parametrize) that runs 4 different invalid login scenarios, including the bug found in TC-005.

## 6. Tools & Technologies

Automation Library: Selenium

Language: Python

Testing Framework: PyTest

Browser: Google Chrome

Version Control: Git & GitHub

## 7. How to Run the Automation Script

You can run these automated tests on your own machine.

Prerequisites

Python 3+ installed

Google Chrome browser installed

Git (optional, can also download ZIP)

Step 1: Get the Code

Clone this repository to your local machine:
```
git clone [URL_to_your_github_repo]
cd [your-repo-name]
```

Step 2: Create a Virtual Environment

It is highly recommended to use a virtual environment.

# Create the environment
```
python -m venv venv
```

# Activate the environment
# On Windows:
```
.\venv\Scripts\activate
```

# On Mac/Linux:
```
source venv/bin/activate
```

Step 3: Install Dependencies

The requirements.txt file contains the necessary Python libraries.

# Install selenium and pytest
```
pip install -r requirements.txt
```

(Note: You will need to create a file named requirements.txt and put selenium and pytest in it.)

Step 4: Run the Tests

With your virtual environment active, simply run pytest.
```
pytest
```

4. Expected Test Results

When you run pytest, you should see 5 tests run.

test_successful_login will PASS.

test_invalid_logins will run 4 times:

3 tests will PASS.


1 test (for TC-005, the blank password) will FAIL.

This failure is intentional! The automation script correctly catches the bug ("Expected: ...Password is required" but "Got: ...Username is required"), proving that the test suite is effective at finding regressions.
