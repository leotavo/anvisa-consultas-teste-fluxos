import pytest
import logging
from undetected_playwright.sync_api import Page
import pytest_html

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # This hook is used to capture the result of each test
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

@pytest.fixture(autouse=True)
def log_on_failure(request, page: Page):
    yield
    # Execute this code after each test
    for phase in ("setup", "call", "teardown"):
        rep = getattr(request.node, "rep_" + phase, None)
        if rep and rep.failed:
            # Capture screenshot on failure
            screenshot_path = f"screenshots/{request.node.nodeid.replace('::', '_')}.png"
            page.screenshot(path=screenshot_path)
            logging.error(f"Screenshot saved to {screenshot_path}")

            # Capture page source on failure
            page_source_path = f"page_sources/{request.node.nodeid.replace('::', '_')}.html"
            with open(page_source_path, "w") as f:
                f.write(page.content())
            logging.error(f"Page source saved to {page_source_path}")

            # Attach screenshot and page source to the report
            if "pytest_html" in request.config.pluginmanager.get_plugins():
                extra = getattr(rep, "extra", [])
                extra.append(pytest_html.extras.image(screenshot_path))
                extra.append(pytest_html.extras.html(open(page_source_path).read()))
                rep.extra = extra
