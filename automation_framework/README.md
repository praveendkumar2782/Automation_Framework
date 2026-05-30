# Playwright Test Automation Suite with Allure Reporting

A production-grade test automation framework for `https://testautomationpractice.blogspot.com/` built with Playwright, pytest, and Allure reporting.

## Project Structure

```
automation_framework/
├── conftest.py                    # Pytest configuration and fixtures
├── pytest.ini                     # Pytest configuration file
├── requirements.txt               # Project dependencies
├── .gitignore                     # Git ignore rules
├── README.md                      # This file
├── data/
│   ├── __init__.py
│   └── test_profiles.csv          # Test data with user profiles
├── pages/
│   ├── __init__.py
│   └── playground_page.py         # Page Object Model (Synchronous)
├── tests/
│   ├── __init__.py
│   └── test_suite.py              # Test cases
├── utils/
│   ├── __init__.py
│   └── test_data_manager.py       # Test data utilities
├── reports/
│   ├── allure-results/            # Generated Allure data
│   ├── screenshots/               # Failure screenshots
│   └── logs/                      # Test logs
└── allure-report/                 # Generated static report
```

## Test Data Strategy

The framework uses a **CSV-based test data strategy** to avoid hardcoding values:

### Test Data File: `data/test_profiles.csv`

Contains realistic test user data with the following structure:
- **name**: Full name of the test user
- **email**: Email address
- **phone**: Phone number
- **address**: Full address
- **gender**: Male/Female
- **country**: Country name

Data is loaded dynamically via `TestDataManager` utility class.

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Install Playwright Browsers

```bash
playwright install chromium
```

### 3. Install Allure Command Line Tool

For Windows:
```bash
scoop install allure
```

Or download from: https://github.com/allure-framework/allure2/releases

## Running Tests

### Run All Tests

```bash
pytest
```

### Run Tests with Specific Markers

```bash
# Sanity tests only
pytest -m sanity

# UI tests only
pytest -m ui

# Datepicker tests only
pytest -m datepicker

# Keyboard tests only
pytest -m keyboard

# Mouse action tests only
pytest -m mouse

# Drag and drop tests only
pytest -m dragdrop
```

### Run Specific Test Class

```bash
pytest tests/test_suite.py::TestTextInputFields
```

### Run with Verbose Output

```bash
pytest -v
```

### Headless Mode

By default, tests run with `headless=False`. To run headless:

Edit `conftest.py`:
```python
browser = playwright.chromium.launch(headless=True)
```

## Generating Allure Report

### 1. Run Tests (Generates Allure Results)

```bash
pytest --alluredir=reports/allure-results
```

### 2. Generate HTML Report

```bash
allure generate reports/allure-results --clean -o reports/allure-report
```

### 3. View Report

```bash
allure open reports/allure-report
```

## Test Features

### Page Object Model (Synchronous)
- All code is **synchronous** (no async/await)
- Non-hardcoded locator mappings
- Descriptive action methods with `@allure.step()` decorators
- Playwright locators for efficiency

### Test Data Management
- CSV-based test data in `data/test_profiles.csv`
- `TestDataManager` utility for loading test data
- Parameterized tests using test data
- No hardcoded values

### Automatic Features
- **Screenshot Capture**: Automatically captures screenshots on test failures
- **Allure Reporting**: Step-by-step test execution tracking
- **Error Tracing**: Exception information attached to reports
- **Environment Info**: Browser, OS, URL tracked in reports

### Test Coverage
- Text input fields with test data
- Standard dropdowns
- Bootstrap dropdowns
- Search functionality
- Datepickers (static and dynamic)
- Checkboxes and radio buttons
- Mouse actions (click, double-click, right-click, hover)
- Drag and drop
- Keyboard actions
- Table interactions
- Image verification
- Form submission
- Page navigation

## Configuration

### Browser Options in `conftest.py`
- **Default**: Chromium (headless=False)
- **Viewport**: 1920x1080
- **Timeout**: 30 seconds (30000 ms)
- **Error Handling**: Ignore HTTPS errors

### Pytest Configuration in `pytest.ini`
- Auto-discovery patterns
- Allure report directory configuration
- Test markers definition
- Headed browser mode enabled

### Test Markers Available
- `@pytest.mark.sanity` - Critical sanity tests
- `@pytest.mark.ui` - UI component tests
- `@pytest.mark.datepicker` - Date picker tests
- `@pytest.mark.keyboard` - Keyboard interaction tests
- `@pytest.mark.mouse` - Mouse action tests
- `@pytest.mark.dragdrop` - Drag and drop tests

## Using Test Data

### Loading All Test Users
```python
from utils.test_data_manager import TestDataManager

test_users = TestDataManager.get_all_test_users()
```

### Getting Specific Test User
```python
user = TestDataManager.get_test_user(0)  # First user
name = user['name']
email = user['email']
```

### In Tests
```python
def test_fill_form_with_test_data(self, page, test_users):
    user = test_users[0]
    playground.fill_first_name(user['name'])
    playground.fill_email(user['email'])
```

## Reports and Artifacts

After test execution, the following are generated:

1. **`reports/allure-results/`** - Raw Allure test data
   - Multiple JSON files for each test
   - `environment.xml` - Test environment details
   - `categories.json` - Test categorization

2. **`reports/screenshots/`** - Failure screenshots
   - Named with test name and timestamp
   - Automatically attached to Allure reports

3. **`reports/logs/`** - Test execution logs

4. **`reports/allure-report/`** - Static HTML report
   - Visual dashboard with test results
   - Detailed test execution steps
   - Screenshot attachments
   - Failure analysis

## CI/CD Integration

### GitHub Actions Example

```yaml
name: Test Automation Suite

on: [push, pull_request]

jobs:
  test:
    runs-on: windows-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      
      - name: Install dependencies
        run: pip install -r automation_framework/requirements.txt
      
      - name: Install Playwright
        run: playwright install chromium
      
      - name: Run tests
        run: |
          cd automation_framework
          pytest --alluredir=reports/allure-results
      
      - name: Generate Allure report
        if: always()
        run: |
          allure generate automation_framework/reports/allure-results --clean -o automation_framework/reports/allure-report
      
      - name: Upload reports
        if: always()
        uses: actions/upload-artifact@v3
        with:
          name: allure-report
          path: automation_framework/reports/allure-report/
```

## Troubleshooting

### Browser Installation
```bash
# Reinstall Chromium
playwright install chromium --force
```

### Allure Report Not Generating
```bash
# Verify allure is installed
allure --version

# Check if results directory exists
dir reports\allure-results
```

### Tests Timing Out
Increase timeout in `conftest.py`:
```python
test_page.set_default_timeout(60000)  # 60 seconds
```

### Module Import Errors
```bash
# Run from automation_framework directory
cd automation_framework
pytest
```

## Best Practices

1. **Test Data**: Always use CSV-based data, never hardcode values
2. **Synchronous Code**: Use sync API only (not async)
3. **Page Objects**: Add new methods to `PlaygroundPage` class
4. **Decorators**: Use `@allure.feature()`, `@allure.story()`, `@allure.step()`
5. **Error Handling**: Let pytest capture failures and screenshots
6. **Test Independence**: Each test should be independent
7. **Locators**: Use descriptive, non-hardcoded selectors
8. **Waits**: Use Playwright's built-in wait mechanisms

## Adding New Tests

1. Create test method in appropriate class in `test_suite.py`
2. Add `@allure.feature()` and `@allure.story()` decorators
3. Create corresponding method in `PlaygroundPage` class
4. Decorate page methods with `@allure.step()`
5. Use test data from CSV via `TestDataManager`
6. Run tests to verify

## Contributing

When contributing:
1. Follow the POM pattern
2. Use synchronous code only
3. Add Allure decorators
4. Use test data from CSV
5. Update this README
6. Run full test suite before commit

## License

This project is provided as-is for testing purposes.

## Support

For issues or questions, review the test execution logs in `reports/logs/` and Allure report for detailed information.

