from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, NoSuchWindowException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()

driver.get('file:///E:/link/CCShoppingHaulAugust2022.html') # змінити шлях

action = ActionChains(driver)

time.sleep(5)

patreonToVisit = []

try:
    patreonToVisit = driver.find_elements(By.XPATH, "//a[contains(@href, 'patreon.com')]")
    for patreon in patreonToVisit:
        time.sleep(1)
        try:  
            action.key_down(Keys.CONTROL).click(patreon).key_up(Keys.CONTROL).perform()
            driver.switch_to.window(driver.window_handles[-1])
            time.sleep(1)
            try:
                next_window = driver.find_element(By.XPATH, "//a[contains(@href, 'patreon.com')]")
                next_window.click()
            except NoSuchElementException:
                pass
            time.sleep(5)
            try:
                links = driver.find_elements(By.XPATH, "//a[contains(@href, 'file')]")
                time.sleep(1)
                if(links is not None and len(links) > 0):
                    for link in links:
                        link.click()
                        time.sleep(0.1)
                else:
                    pass
                driver.close()
            except NoSuchElementException:
                pass
        except NoSuchWindowException:
            pass
        driver.switch_to.window(driver.window_handles[-1])
except NoSuchElementException:
    pass

input('Нажми Enter для завершення...')
