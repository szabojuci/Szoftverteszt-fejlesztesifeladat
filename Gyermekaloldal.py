from distutils.spawn import find_executable
from lib2to3.pgen2 import driver
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

bongeszo = webdriver.Chrome(executable_path=ChromeDriverManager().install())
bongeszo.get('http://127.0.0.1:5500/gyermekruha.html')
time.sleep(2)
minimumar = bongeszo.find_element(By.ID,'min-price')
minimumar.click()
time.sleep(2)
minimumar.send_keys("2000")
time.sleep(2)
KeresesGomb = bongeszo.find_element(By.XPATH,'/html/body/div[1]/button')
KeresesGomb.click()
time.sleep(2)
minimumar = bongeszo.find_element(By.ID,'color')
minimumar.click()
time.sleep(2)
minimumar.send_keys("fekete")
time.sleep(2)
KeresesGomb = bongeszo.find_element(By.XPATH,'/html/body/div[1]/button')
KeresesGomb.click()
time.sleep(2)
bongeszo.save_screenshot('MinimumosKereses.png')
time.sleep(2)
bongeszo.save_screenshot('Gyermekaloldal.png')
time.sleep(2)
Gomb = bongeszo.find_element(By.ID,'dropdownMenuButton')
Gomb.click()
time.sleep(2)
bongeszo.save_screenshot('FiuRuhak.png')
time.sleep(2)
KovetkezoGomb = bongeszo.find_element(By.ID,'next-btn')
KovetkezoGomb.click()
time.sleep(2)
bongeszo.save_screenshot('FiuRuhakKovetkezo.png')
time.sleep(2)
ElozoGomb = bongeszo.find_element(By.ID,'prev-btn')
ElozoGomb.click()
time.sleep(2)
bongeszo.save_screenshot('FiuRuhakElozo.png')
time.sleep(2)








