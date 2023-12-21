import json
import os

from model.Capitulo import Capitulo
from model.Obra import Obra
from model.Mensagens import Mensagens

class Gestor_JSON:

    def __init__(self):
        self.pasta_relatorios_capitulos = os.path.join('assets/',"registro_capitulos")
        self.pasta_dados_obras = os.path.join('assets/', "dados_obras")
        self.validar_e_criar_pastas()

    def validar_e_criar_pastas(self):
        pastas = [self.pasta_relatorios_capitulos, self.pasta_dados_obras]

        for pasta in pastas:
            if not os.path.exists(pasta):
                os.makedirs(pasta)

    def criar_json_com_lista_obras(self, lista_de_obras):
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

        with open(f"{self.pasta_relatorios_capitulos}/obras.json", "w") as arquivo_json:
            arquivo_json.write(json_obras)
            print("Registro Concluído!")
        
    
    def receber_lista_obras_json(self):
        arquivo_json = os.path.join(self.pasta_relatorios_capitulos, "obras.json")

        if not os.path.exists(arquivo_json):
            Mensagens.nao_existe_registro()
            with open(arquivo_json, "w") as arquivo:
                arquivo.write("[]")
            return []

        with open(f"{self.pasta_relatorios_capitulos}/obras.json", "r") as arquivo_json:
            json_obras = arquivo_json.read()
        
        lista_de_obras = []

        try:
            lista_de_dicionarios = json.loads(json_obras)

        except Exception as e:
            print("Não existe arquivo para receber os dados.")
            with open(f"{self.pasta_relatorios_capitulos}/obras.json", "w") as arquivo_json:
                arquivo_json.write(json_obras)
            return []
            

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
        print("Registro Recebido!")
        return lista_de_obras


    def retornar_dados_unicos_obras(self):
        print(os.getcwd())

        with open(f"{self.pasta_dados_obras}/dadosObras.json", "r") as arquivo_json:
            dados_unicos_obras = json.load(arquivo_json)

        return dados_unicos_obras

    def receber_lista_obras_json_nao_permitidas_fb(self):
        with open(f"{self.pasta_dados_obras}/obras_nao_permitidas.json", "r") as arquivo_json:
            json_obras = arquivo_json.read()
        
        lista_de_obras = []

        try:
            lista_de_dicionarios = json.loads(json_obras)

        except Exception as e:
            print("Não existe arquivo para receber os dados.")
            with open(f"{self.pasta_relatorios_capitulos}/obras.json", "w") as arquivo_json:
                arquivo_json.write(json_obras)
            return []
            

        for dicionario_obra in lista_de_dicionarios:
            obra = Obra(
                titulo_obra=dicionario_obra["titulo_obra"],
                imagem_obra="",
                url_obra=""
            )
            
            lista_de_obras.append(obra)
        print("Registro Recebido!")
        return lista_de_obras
        
