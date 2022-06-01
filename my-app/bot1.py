import pyautogui
import time

#A cada dois segundos ele vai executar uma ação em cada linha de codígo
pyautogui.PAUSE = 2
#Passo 1 Abrir Sistema, preencher nome do programa
pyautogui.press("win")
pyautogui.write("Documentos: login.xlsx")
pyautogui.press("enter")
#Passo 2 - Clicar e preencher Login, preencher senha e fazer Login
pyautogui.doubleClick(button="left" ,x=437, y=267)
#Passo 3 -






