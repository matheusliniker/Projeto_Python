import pyautogui

#Como usar a função click
pyautogui.click(x=1446, y=744,clicks=1000,interval=0.1,button='left',duration=2)
#click na posição atual (com botão esquerdo)
pyautogui.click()
pyautogui.click(button='left')
pyautogui.click(button='right')
pyautogui(button= 'middle')
#cliclar X vezes
pyautogui.click(clicks=10)
# Funções prontas para clicks
pyautogui.doubleClick()
pyautogui.rightClick()
pyautogui.middleClick()
