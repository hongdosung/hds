import pyautogui
import time

# pip install pyautogui
# pip install selenium

# #1. 화면크기출력
# print(pyautogui.size())

#2. 마우스위치출력
# time.sleep(2)
# print(pyautogui.position())

#3. 마우스이동
# pyautogui.moveTo(2804, 343)
# pyautogui.moveTo(2804, 343, 2)

#4. 마우스클릭
# pyautogui.click()
# pyautogui.click(button='right')
# pyautogui.doubleClick()
# pyautogui.click(clicks=3, interval=1) # 3번 클릭할건데 1초 마다

#5. 마우스 드래그
# 3291,65 -> 2903,65
pyautogui.moveTo(3291, 65, 2)

pyautogui.dragTo(2903, 65, 2)


pyautogui.dragTo(2903, 65, 2)
