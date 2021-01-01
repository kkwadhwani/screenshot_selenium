from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import datetime as dt
import os
import time
from selenium.webdriver.common.keys import Keys

op= webdriver.ChromeOptions()
op.binary_location=os.environ.get("GOOGLE_CHROME_BIN")
op.add_argument("--headless")
op.add_argument("--no-sandbox")
op.add_argument("--disable-dev-sh-usage  ")
to_continue= True
# chrome_driver_path = "/Users/Kunal/Documents/ChromeDriver/chromedriver"

driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=op)

num = 1


this_hour= dt.datetime.now().hour
this_minute= dt.datetime.now().minute

while to_continue:
    driver.get("https://www.google.com/")
    time.sleep(5)
    driver.delete_all_cookies()
    driver.refresh()
    driver.save_screenshot(f"image{num}_{this_hour}.{this_minute}.png")
    num += 1
    # driver.get("chrome://settings/clearBrowserData")
    # time.sleep(3)
    # clear_history= driver.find_element_by_css_selector('* /deep/ #clearBrowsingDataConfirm')


    def delete_cache():
        driver.execute_script("window.open('');")
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(2)
        driver.get('chrome://settings/cleardriverData')
        time.sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB * 3 + Keys.DOWN * 3)  # send right combination
        actions.perform()
        time.sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB * 4 + Keys.ENTER)  # confirm
        actions.perform()
        time.sleep(5)  # wait some time to finish
        driver.close()  # close this tab
        driver.switch_to.window(driver.window_handles[0])  # switch back


    delete_cache()
    print("I found it")

    time.sleep(2)









