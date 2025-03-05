import pytest
from undetected_playwright.async_api import async_playwright

@pytest.fixture(scope="session")
async def browser():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)  # Altere para True se não quiser ver o navegador
        yield browser
        await browser.close()

@pytest.fixture(scope="function")
async def page(browser):
    context = await browser.new_context(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
        extra_http_headers={
            "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
            "Referer": "https://consultas.anvisa.gov.br/",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-origin"
        },
        viewport={"width": 1280, "height": 720},
        ignore_https_errors=True,
        java_script_enabled=True
    )
    page = await context.new_page()
    yield page
    await page.close()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
async def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page")
        if page:
            screenshot_path = f"screenshots/{item.name}.png"
            await page.screenshot(path=screenshot_path)
            print(f"Screenshot saved to {screenshot_path}")
