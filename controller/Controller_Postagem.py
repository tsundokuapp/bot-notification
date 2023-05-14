from dao.Web_Screper_Site import Web_Screper_Site
from classes_io.Gestor_JSON import Gestor_JSON

class Controller_Postagem:
     
    def execucao_principal():
        web_screper = Web_Screper_Site()
        lista_de_obras = web_screper.recebe_capitulos_diarios()

        Gestor_JSON.criar_json_com_lista_obras(lista_de_obras)
        print(lista_de_obras)

        lista_de_obras_recebida = Gestor_JSON.receber_lista_obras_json()
        obra = lista_de_obras_recebida[1]
        print(lista_de_obras_recebida)
        print(obra)
        


