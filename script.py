# user_autoplius = +37060403272
# user_pass_autoplius = 'LordNelson1'
#
# user_autogidas = 'rimti.senelyzai@gmail.com'
# user_pass_autogidas = 'LordNelson1'



from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc

options = uc.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-blink-features=AutomationControlled")

driver = uc.Chrome(options=options)

import os

user_autoplius = os.getenv("AUTO_USER")
user_pass_autoplius = os.getenv("AUTO_PASS")

user_autogidas = os.getenv("GIDAS_USER")
user_pass_autogidas = os.getenv("GIDAS_PASS")
wait = WebDriverWait(driver, 10)
# autopliusas
driver.get("https://autoplius.lt")

consent_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Sutinku"]'))
)
consent_button.click()

login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@title="Prisijungti"]')))
login_button.click()

username_input = wait.until(EC.visibility_of_element_located((By.ID, "username-lookup")))
username_input.send_keys(f"{user_autoplius}")

continue_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[normalize-space()="Tęsti"]')))
continue_button.click()

pass_input = wait.until(EC.visibility_of_element_located((By.ID, "password")))
pass_input.send_keys(f"{user_pass_autoplius}")

continue_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[normalize-space()="Prisijungti"]')))
continue_button.click()

# dummy wait
my_account_link = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, '//a[@title="Mano Autoplius.lt" and contains(@href, "/dashboard/announcements")]')
    )
)

driver.get("https://autoplius.lt/dashboard/announcements/autodalys/lengvuju-dalys")

renew_button = wait.until(EC.element_to_be_clickable(
    (By.XPATH, '//div[contains(@class, "js-renew-announcements-old") and contains(text(), "Atnaujinti visus")]')
))
renew_button.click()

# autogidas
driver.get('https://autogidas.lt/mano-gidas/')

accept_button = wait.until(
    EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
)
accept_button.click()

user_gidas_input = wait.until(
    EC.visibility_of_element_located((By.ID, "vartotojovardas"))
)
user_gidas_input.send_keys(f"{user_autogidas}")

password_gidas_input = wait.until(
    EC.visibility_of_element_located((By.ID, "vartotojoslaptazodis"))
)
password_gidas_input.send_keys(f"{user_pass_autogidas}")

login_button = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[type="submit"][value="Prisijungti"]'))
)
login_button.click()

renew_button = wait.until(
    EC.element_to_be_clickable((By.ID, "renew-advertisements-button"))
)
renew_button.click()

renew_link = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//a[@title="Atnaujinti" and contains(@href, "renew-all/proceed")]'))
)
driver.get('https://autogidas.lt/ajax/ad/renew-all/proceed?category_id=10')
