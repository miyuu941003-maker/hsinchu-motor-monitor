from playwright.sync_api import sync_playwright

URL = "https://www.mvdis.gov.tw/m3-emv-trn/exm/locations"


def check_booking():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            args=["--disable-blink-features=AutomationControlled"]
        )

        page = browser.new_page()

        page.goto(
            URL,
            wait_until="commit",
            timeout=90000
        )

        page.wait_for_timeout(10000)

        text = page.locator("body").inner_text()

        print(text[:500])

        browser.close()


check_booking()