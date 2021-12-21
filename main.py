from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

while(True):
    print('hello geek!')
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    #chrome_options.add_argument('--headless')
    #chrome_options.add_argument('--disable-gpu')  # Last I checked this was necessary.

    driver = webdriver.Chrome(options=chrome_options)

    driver.maximize_window()

    driver.implicitly_wait(20) # seconds

    driver.get('https://t.co/kfV0oTpGNG')

    driver.execute_script("window.scrollTo(0, 1000);")


    #driver.find_element_by_id("PDI_answer50534733").click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'PDI_answer50534733'))).click()


    driver.find_element_by_id("pd-vote-button10997097").click()

    time.sleep(3)

    driver.close()

    time.sleep(20)



# identifying the radio button with xpath then click
#driver.find_element_by_xpath("//input[@value='50534733']").click()

