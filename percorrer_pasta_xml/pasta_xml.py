import os
pasta = 'u:\\ISS\\xml_contratados'


def navegar_pastas_xml_contratados():

    conjunto_clientes = set()
    for diretorio, subpastas, arquivos in os.walk(pasta):

        for arquivo in arquivos:

            # print(os.path.join(diretorio, arquivo))
            cod_cliente = os.path.join(
                diretorio, arquivo).split('\\')[3]
            if 'OK' not in cod_cliente:
                conjunto_clientes.add(cod_cliente)

    return conjunto_clientes


if __name__ == '__main__':
    conjunto_clientes = navegar_pastas_xml_contratados()
    for conjunto in conjunto_clientes:
        print(conjunto)
