import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def wait_for_page_ready(driver: webdriver.Remote, timeout=15):
    """Wait until the document ready state is complete."""
    WebDriverWait(driver, timeout).until(
        lambda d: d.execute_script("return document.readyState") == "complete"
    )

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")  # required for some containerized runs
chrome_options.add_argument("--disable-extensions")  # keep Chrome lightweight for automation
chrome_options.add_argument("--disable-gpu")  # avoid GPU issues on headless servers
chrome_options.add_argument("--window-size=1080,720")  # ensure consistent viewport
chrome_options.add_argument("--ignore-certificate-errors")  # skip TLS warnings on demo sites
chrome_options.add_argument("--allow-insecure-localhost")  # permit self-signed localhost certs
# chrome_options.add_argument("--headless=new")  # uncomment if you don't need a visible browser

chrome_options.set_capability(
    "se:vncLocalAddress",
    "ws://localhost:7900",
)

driver = webdriver.Remote(
    command_executor="https://standalone-chrome.asia-east1.run.app/wd/hub",
    options=chrome_options,
)

url = "https://www.ptt.cc/bbs/index.html"

driver.get(url)

time.sleep(10)

wait_for_page_ready(driver)

driver.find_element(by=By.PARTIAL_LINK_TEXT, value="Gossiping").click()
wait_for_page_ready(driver)

time.sleep(5)

driver.find_element(by=By.CLASS_NAME, value="btn-big").click()
wait_for_page_ready(driver)

time.sleep(5)

html = driver.page_source
# print(driver.find_element(by=By.TAG_NAME, value="html").text)
print(html)
print("===")

cookie = driver.get_cookies()
print(cookie)

driver.quit()