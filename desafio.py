# Navegar até o site https://cursoautomacao.netfly.app/
import webbrowser
import pyautogui
from time import sleep

# webbrowser.open('https://cursoautomacao.netlify.app/')

# Encontre e clique no campo "digite seu nome" dentro de "exemplos Alertas" e digite seu nome
pyautogui.moveTo(1393,347,duration=2)
pyautogui.scroll(-2500)
pyautogui.click(1036,298)
pyautogui.typewrite('Matheus Liniker')
sleep(1)

#Clique em alerta, para gerar a alerta

pyautogui.click(1069,358)

sleep(1)
# Feche a alerta

pyautogui.click(1699,285)

# Suba a página totalmente para cima

pyautogui.scroll(2500)

'''Desça apenas o suficiente para conseguir chegar até 
 a secção que contém os arquivos para o quais irá 
 fazer o download e click no botão de download para
realizar o download dos arquivos excel e pdf.'''

pyautogui.scroll(-3800)

# Download excel

pyautogui.click(1146,480)

sleep(2)
# Download PDF

pyautogui.click(1157,650)

sleep(2)

# Alerta que fala "Você terminou"

pyautogui.alert(text='Terminou', button='Ok')