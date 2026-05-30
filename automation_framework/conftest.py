import pytest
import allure
from playwright.sync_api import sync_playwright
from pathlib import Path
from datetime import datetime


# Use pytest-playwright's built-in `page` fixture. This file provides
# reporting helpers (screenshot on failure, environment file) while
# avoiding re-defining the `page` fixture which would conflict with
# the pytest-playwright plugin.


def pytest_runtest_makereport(item, call):
    """
    pytest hook to capture screenshots on test failure and attach to Allure report.
    """
    if call.when == "call" and call.excinfo is not None:
        try:
            page = item.funcargs.get('page')
            if page and not page.is_closed():
                screenshot_dir = Path("reports/screenshots")
                screenshot_dir.mkdir(parents=True, exist_ok=True)
                screenshot_path = screenshot_dir / f"failure_{item.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
                page.screenshot(path=str(screenshot_path))

                with open(screenshot_path, 'rb') as f:
                    allure.attach(
                        f.read(),
                        name=f"failure_screenshot_{item.name}",
                        attachment_type=allure.attachment_type.PNG
                    )
        except Exception as e:
            pass


@pytest.fixture(scope="session", autouse=True)
def setup_allure_environment():
    """
    Setup Allure environment info and reports directory structure at session start.
    """
    reports_base = Path("reports")
    reports_base.mkdir(exist_ok=True)

    allure_results_dir = reports_base / "allure-results"
    allure_results_dir.mkdir(exist_ok=True)
    
    screenshots_dir = reports_base / "screenshots"
    screenshots_dir.mkdir(exist_ok=True)

    logs_dir = reports_base / "logs"
    logs_dir.mkdir(exist_ok=True)

    env_content = f"""<environment>
    <parameter>
        <key>Browser</key>
        <value>Chromium</value>
    </parameter>
    <parameter>
        <key>OS</key>
        <value>Windows</value>
    </parameter>
    <parameter>
        <key>Application URL</key>
        <value>https://testautomationpractice.blogspot.com/</value>
    </parameter>
    <parameter>
        <key>Framework</key>
        <value>Playwright + pytest + Allure</value>
    </parameter>
    <parameter>
        <key>Execution Date</key>
        <value>{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</value>
    </parameter>
</environment>"""

    env_file = allure_results_dir / "environment.xml"
    with open(env_file, 'w') as f:
        f.write(env_content)

    categories_content = """{
  "categories": [
    {
      "name": "Blocker",
      "matchedStatuses": ["broken"]
    },
    {
      "name": "Critical",
      "matchedStatuses": ["failed"]
    },
    {
      "name": "Minor",
      "matchedStatuses": ["skipped"]
    }
  ]
}"""

    categories_file = allure_results_dir / "categories.json"
    with open(categories_file, 'w') as f:
        f.write(categories_content)

