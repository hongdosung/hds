from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pyperclip
import pyautogui
# pip install selenium

#driver = webdriver.Chrome('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Chrome') # 크롬실행파일
#driver = webdriver.Chrome('c://chromedriver.exe') # 크롬실행파일
driver = webdriver.Chrome("C://chromedriver.exe") # 크롬실행파일
driver.get('https://nid.naver.com/nidlogin.login') # 로그인경로
driver.maximize_window() # 브라우져 창 최대화

# 아이디 입력창
id = driver.find_element(By.CSS_SELECTOR, "#id")
#id.send_keys("snoopy17") # 아이디 입력
id.click()
pyperclip.copy("snoopy17")
pyautogui.hotkey("crtl", "v")
time.sleep(2)

# 비번 입력창
pwd = driver.find_element(By.CSS_SELECTOR, "#pw")
#pwd.send_keys("snoopy17") # 비밀번호 입력
pwd.click()
pyperclip.copy("snoopy17")
pyautogui.hotkey("crtl", "v")
time.sleep(2)

# 로그인 버튼
driver.find_element(By.CSS_SELECTOR, "#log\.login").click()

