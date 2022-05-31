import pyautogui
#Automação do teclado
#Aperta para baixo alt
pyautogui.keyDown('alt')
#Pressiona o Tab
pyautogui.press(['tab'])
#Solta a tecla alt
pyautogui.keyUp('alt')
#Digita o texto
pyautogui.write("Olá, Bom dia Jéssica!!")