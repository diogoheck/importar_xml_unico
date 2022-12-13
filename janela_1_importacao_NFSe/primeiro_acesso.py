import pyautogui
import time


def acesso_inicial_NFSe(cod_cliente, DT_inicial, DT_final):

    time.sleep(3)
    pyautogui.write(cod_cliente)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.write(DT_inicial)
    time.sleep(1)
    pyautogui.write(DT_final)
    time.sleep(1)
    pyautogui.press('enter')
    pyautogui.press('enter')
    pyautogui.press('enter')
    pyautogui.press('enter')
    pyautogui.press('enter')
    pyautogui.press('enter')
    pyautogui.press('enter')
    pyautogui.press('enter')
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.write(f'x:\\ISS\\xml_contratados\\{cod_cliente}')
    pyautogui.press('enter')
    pyautogui.press('enter')
