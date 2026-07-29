from playwright.sync_api import sync_playwright

URL = "https://www.mvdis.gov.tw/m3-emv-trn/exm/locations"


def check_booking():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        page.goto(URL)

        page.wait_for_timeout(5000)

        text = page.locator("body").inner_text()

        if "額滿" not in text:
            print("可能有名額！")
        else:
            print("目前沒有名額")

        browser.close()


check_booking()
