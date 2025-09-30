import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_experimental_option("prefs", {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False
    }
)

LOGIN_FILED = ("xpath", "//input[@id='user-name']")
PASSWORD = ("xpath", "//input[@id='password']")
LOGIN_BUTTIN = ("xpath", "//input[@id='login-button']")

driver = webdriver.Chrome(options=options)
driver.get("https://www.saucedemo.com")

driver.find_element(*LOGIN_FILED).send_keys("standard_user")
driver.find_element(*PASSWORD).send_keys("secret_sauce")
time.sleep(2)
driver.find_element(*LOGIN_BUTTIN).click()


url_inventory = driver.current_url
assert url_inventory == "https://www.saucedemo.com/inventory.html", f"Ожидался заголовок 'https://www.saucedemo.com/inventory.html', но получен '{url_inventory}'"


product_backpack = driver.find_element("xpath", "//button[@id='add-to-cart-sauce-labs-backpack']")
product_Bike_Light = driver.find_element("xpath", "//button[@id='add-to-cart-sauce-labs-bike-light']")
product_backpack.click()
product_Bike_Light.click()
time.sleep(2)

shopping_cart_link = driver.find_element("xpath", "//a[@data-test='shopping-cart-link']")
shopping_cart_link.click()

url_inventory2 = driver.current_url
assert url_inventory2 == "https://www.saucedemo.com/cart.html", f"Ожидался заголовок 'https://www.saucedemo.com/cart.html', но получен '{url_inventory2}'"
time.sleep(2)

chec_button = driver.find_element("xpath", "//button[@id='checkout']")
chec_button.click()

url_inventory3 = driver.current_url
assert url_inventory3 == "https://www.saucedemo.com/checkout-step-one.html", f"Ожидался заголовок 'https://www.saucedemo.com/checkout-step-one.html', но получен '{url_inventory3}'"
time.sleep(2)

first_name = driver.find_element("xpath", "//input[@id='first-name']")
last_name = driver.find_element("xpath", "//input[@id='last-name']")
zip = driver.find_element("xpath", "//input[@id='postal-code']")
input_tab = driver.find_element("xpath", "//input[@id='continue']")

first_name.send_keys("Nadua")
last_name.send_keys("Denisova")
zip.send_keys("140009")
time.sleep(2)
input_tab.click()
time.sleep(2)

url_inventory4 = driver.current_url
assert url_inventory4 == "https://www.saucedemo.com/checkout-step-two.html", f"Ожидался заголовок 'https://www.saucedemo.com/checkout-step-two.html', но получен '{url_inventory4}'"
time.sleep(2)

finish = driver.find_element("xpath", "//button[@id='finish']")
finish.click()
