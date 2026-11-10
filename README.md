# Playwright Python Automation

![Tests](https://github.com/knsupritha-kn/playwright-python-automation/actions/workflows/tests.yml/badge.svg)

UI and API test automation framework for the [Sauce Demo](https://www.saucedemo.com) e-commerce site, built with Playwright, PyTest, and the Page Object Model.

## Tech stack
- Python, Playwright, PyTest
- Page Object Model (POM)
- Requests (API testing)
- pytest-html reports
- GitHub Actions (CI)

## What's tested (21 tests)
| Area | Tests | Covers |
|---|---|---|
| Login | 7 | Valid users, locked user, wrong password, empty fields |
| Cart | 5 | Add one/multiple items, remove item, cart badge |
| Checkout | 4 | Full order flow, missing first name / last name / postal code |
| API | 5 | GET, POST, DELETE, 404 handling (JSONPlaceholder) |

## Framework features
- **Page Object Model**: locators and actions kept in page classes
- **Fixtures**: shared login setup in `conftest.py`
- **Parametrize**: data-driven tests with readable IDs
- **Markers**: run groups like `smoke`, `login`, `cart`, `checkout`, `api`
- **Reports**: HTML report, plus screenshots and videos on failure
- **CI**: all tests run automatically on every push

## Project structure
```
├── pages/            # Page classes (Login, Inventory, Cart, Checkout)
├── tests/            # Test files
├── conftest.py       # Shared fixtures
├── pytest.ini        # PyTest settings and markers
├── requirements.txt  # Dependencies
└── .github/workflows/tests.yml  # CI pipeline
```

## How to run
```bash
pip install -r requirements.txt
python -m playwright install
python -m pytest                 # all tests
python -m pytest -m smoke        # smoke tests