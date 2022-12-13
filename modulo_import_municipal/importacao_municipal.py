import pyautogui
import time


def acessar_modulo_importacao_municipal():
    pyautogui.hotkey('alt', 'i')
    pyautogui.click(x=724, y=409)


if __name__ == '__main__':
    acessar_modulo_importacao_municipal()
