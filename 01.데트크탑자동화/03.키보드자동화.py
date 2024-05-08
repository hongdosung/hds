import pyautogui
import pyperclip

#1. 키보드입력(문자)
# pyautogui.write('hds go', interval=0.25) # 한글은 입력안됨

#2. 키도드입력(키)
# pyautogui.press('enter')
# pyautogui.press('up')

#3. 키보드입력(동시에 입력)
pyautogui.hotkey('ctrl', 'c') # 복사(copy) mac = command

#4. 한글입력방법
pyperclip.copy('한글입력잘되나?')
pyautogui.hotkey('ctrl', 'v') # 붙여넣기(paste)



