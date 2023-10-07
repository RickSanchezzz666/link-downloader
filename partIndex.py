from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, NoSuchWindowException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import pygame

#3.10.8 python

driver = webdriver.Chrome()

pygame.mixer.init()
sound = pygame.mixer.Sound('alert.mp3')
sound.set_volume(1.0)

driver.get('file:///E:/link/CCShoppingHaulAugust2022.html') # змінити шлях

action = ActionChains(driver)

time.sleep(3)

#sims resources

simsToVisit = []

def checkIfDownloaded(max_attempts=5):
    attempts = 0
    while attempts < max_attempts:
        try:
            status = driver.find_element(By.XPATH, "//a[contains(@class, 'downloader')]")
            if(status):
                if(status.get_attribute("display") != None):
                    pass
                else:
                    time.sleep(1.5)
                    attempts += 1
        except NoSuchElementException:
            time.sleep(1.5)
            attempts += 1
    else:
        pass

try:
    simsToVisit = driver.find_elements(By.XPATH, "//a[contains(@href, 'thesimsresource.com')]")
    for sims in simsToVisit:
        time.sleep(1)
        try:
            action.key_down(Keys.CONTROL).click(sims).key_up(Keys.CONTROL).perform()
            driver.switch_to.window(driver.window_handles[-1])
            time.sleep(1)
            try:
                next_window = driver.find_element(By.XPATH, "//a[contains(@href, 'thesimsresource.com')]")
                next_window.click()
            except NoSuchElementException:
                pass
            try:
                time.sleep(5)
                first_button = driver.find_element(By.XPATH, "//a[contains(@title, 'Download')]")
                first_button.click()
                try:
                    time.sleep(0.5)
                    required = driver.find_element(By.XPATH, "//a[contains(@class, 'continue-download-button')]")
                    if(required):
                        required.click()
                    else:
                        pass
                except NoSuchElementException:
                    pass
                try:
                    time.sleep(2)
                    captcha = driver.find_element(By.XPATH, "//*[contains(text(), 'This is a once per session action')]")
                    if(captcha):
                        print('Введіть капчу вручну!')
                        sound.play()
                        if input('Після введення напишіть "q": ') == 'q':
                            sound.stop()
                            pass
                    else: 
                        pass
                except NoSuchElementException:
                    pass
                time.sleep(20)
                second_button = driver.find_element(By.XPATH, "//a[contains(@class, 'downloader')]")
                second_button.click()
                checkIfDownloaded()
                driver.close()
            except NoSuchElementException:
                pass
        except NoSuchWindowException:
            pass
        driver.switch_to.window(driver.window_handles[-1])
except NoSuchElementException:
    pass

input('Нажми Enter для завершення...')