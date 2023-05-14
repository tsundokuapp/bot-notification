import json

from model.Capitulo import Capitulo
from model.Obra import Obra

class Gestor_JSON:

    def criar_json_com_lista_obras(lista_de_obras):
        lista_de_dicionarios = []

        for obra in lista_de_obras:
            dicionario_obra = {
                "titulo_obra": obra.titulo_obra,
                "imagem_obra": obra.imagem_obra,
                "url_obra": obra.url_obra,
                "lista_de_capitulos": [
                    {
                        "numero_capitulo": capitulo.numero_capitulo,
                        "link_capitulo": capitulo.link_capitulo,
                        "data_postagem": capitulo.data_postagem
                    }
                    for capitulo in obra.lista_de_capitulos
                ]
            }
            lista_de_dicionarios.append(dicionario_obra)

        # Converter a lista de dicionários para JSON
        json_obras = json.dumps(lista_de_dicionarios, indent=4)

        with open("obras.json", "w") as arquivo_json:
            arquivo_json.write(json_obras)
        
    
    def receber_lista_obras_json():
        with open("obras.json", "r") as arquivo_json:
            json_obras = arquivo_json.read()
        
        lista_de_dicionarios = json.loads(json_obras)

        lista_de_obras = []

        for dicionario_obra in lista_de_dicionarios:
            obra = Obra(
                titulo_obra=dicionario_obra["titulo_obra"],
                imagem_obra=dicionario_obra["imagem_obra"],
                url_obra=dicionario_obra["url_obra"]
            )
            
            for dicionario_capitulo in dicionario_obra["lista_de_capitulos"]:
                capitulo = Capitulo(
                    numero_capitulo=dicionario_capitulo["numero_capitulo"],
                    link_capitulo=dicionario_capitulo["link_capitulo"],
                    data_postagem=dicionario_capitulo["data_postagem"]
                )
                obra.lista_de_capitulos.append(capitulo)
            
            lista_de_obras.append(obra)
        return lista_de_obras


        
        
