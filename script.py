import os
import time

from playwright.sync_api import sync_playwright

AUTO_USER = os.getenv("AUTO_USER")
AUTO_PASS = os.getenv("AUTO_PASS")
GIDAS_USER = os.getenv("GIDAS_USER")
GIDAS_PASS = os.getenv("GIDAS_PASS")


def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            args=["--disable-blink-features=AutomationControlled"] 
        )
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
            locale="lt-LT",
            extra_http_headers={
                "Referer": "https://autogidas.lt/",
                "Accept-Language": "lt-LT,lt;q=0.9,en-US;q=0.8,en;q=0.7"
            }
        )
        context.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

        page = context.new_page()

        # 1. AUTOPLIUS
        page.goto("https://autoplius.lt", timeout=5000)
        # page.click('button[aria-label="Sutinku"]', timeout=5000)

        page.click('a[title="Prisijungti"]', timeout=10000)
        page.fill('#username-lookup', AUTO_USER, timeout=5000)
        page.click('button:has-text("Tęsti")', timeout=5000)
        page.fill('#password', AUTO_PASS, timeout=5000)
        page.click('button:has-text("Prisijungti")', timeout=5000)
        page.wait_for_selector('a[title="Mano Autoplius.lt"]', timeout=10000)
        page.goto("https://autoplius.lt/dashboard/announcements/autodalys/lengvuju-dalys", timeout=5000)

        page.click('div.js-renew-announcements-old:has-text("Atnaujinti visus")', timeout=10000)

        # 2. AUTOGIDAS
        time.sleep(2)
        page.goto("https://autogidas.lt/mano-gidas/", timeout=30000)
        time.sleep(2)
        page.click("#onetrust-accept-btn-handler", timeout=5000)
        time.sleep(2)
        page.fill("#vartotojovardas", GIDAS_USER, timeout=5000)
        time.sleep(2)
        page.fill("#vartotojoslaptazodis", GIDAS_PASS)
        time.sleep(2)
        page.click('input[type="submit"][value="Prisijungti"]', timeout=5000)
        time.sleep(2)
        # page.wait_for_selector("#renew-advertisements-button", timeout=10000)
        # time.sleep(2)
        # page.click("#renew-advertisements-button", timeout=5000)
        # time.sleep(2)
        page.goto("https://autogidas.lt/ajax/ad/renew-all/proceed?category_id=10", timeout=5000)
        time.sleep(2)

        print("✅ Ads renewed successfully.")

        context.close()
        browser.close()

if __name__ == "__main__":
    run()