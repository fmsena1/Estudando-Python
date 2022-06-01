import pyautogui
import time
#A cada dois segundos ele vai executar uma ação em cada linha de codígo
pyautogui.PAUSE = 2
#Passo 1 Abrir Sistema, preencher nome do programa
pyautogui.press("win")
pyautogui.write("Documentos: login.xlsx")
pyautogui.press("enter")
time.sleep(3)
post = pyautogui.position()
print(post)

#time.sleep = para saber a posição no desktop

#time.sleep(3)
#post = pyautogui.position()
#print(post)