import pyautogui
import pandas as pd
import time

pyautogui.PAUSE = 1

pyautogui.press("win")
pyautogui.write("firefox")
pyautogui.press("enter")
time.sleep(2)
pyautogui.hotkey("alt", "d")
pyautogui.hotkey("ctrl", "a")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)

pyautogui.click(x=765, y=502)
pyautogui.write("narnia@gmail.com")
pyautogui.press("tab")
pyautogui.write("123456")
pyautogui.click(x=963, y=700)
time.sleep(3)


tabela = pd.read_csv("produtos.csv")

print(tabela)

for linha in tabela.index:
    pyautogui.click(x=708, y=357)
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(10000)
