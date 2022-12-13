from Login.login_unico import logar_unico
from modulo_fiscal.selecionar_mod_fiscal import acessar_modulo_fiscal
from modulo_import_municipal.importacao_municipal import acessar_modulo_importacao_municipal
from janela_1_importacao_NFSe.primeiro_acesso import acesso_inicial_NFSe
from janela_2_importacao_NFSe.importacao_janela2 import importar_notas_final
from percorrer_pasta_xml.pasta_xml import navegar_pastas_xml_contratados as navegar_pasta_xml
import pyautogui
import os
DT_inicial = '01112022'
DT_final = '30112022'


if __name__ == '__main__':

    conjunto_clientes = navegar_pasta_xml()

    if not not conjunto_clientes:
        logar_unico()
        acessar_modulo_fiscal()
        acessar_modulo_importacao_municipal()

    for cliente in conjunto_clientes:
        acesso_inicial_NFSe(cliente, DT_inicial, DT_final)
        importar_notas_final(cliente)
        # os.rename(f'u:\\ISS\\xml\\{cliente}', f'u:\\ISS\\xml\\{cliente}OK')

    # finalizar unico
    if not not conjunto_clientes:

        pyautogui.click(x=979, y=309)
        pyautogui.click(x=1338, y=2)
        pyautogui.click(x=653, y=439)
        pyautogui.press('enter')
