import os
import logging

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv

from src.model.Obra import Obra
from src.model.Capitulo import Capitulo
from src.model.Mensagens import Mensagens

class Atlas_DAO:
    def __init__(self):
        #Carregando as variaveis de ambiente
        load_dotenv()
        self.uri = os.getenv("URI_ATLAS")

        #Recebe os loggers
        self.logger_erros = logging.getLogger('logger_erros')
        self.logger_infos = logging.getLogger('logger_infos')
        
        # Create a new client and connect to the server
        self.client = MongoClient(self.uri, server_api=ServerApi('1'))
        
        self.testar_conexao()


    def testar_conexao(self):        
        try:
            self.client.admin.command('ping')
            self.logger_infos.info("Pinged your deployment. You successfully connected to MongoDB!")

            return True
        except Exception as e:
            Mensagens.erro_no_banco_de_dados("Erro ao conectar com banco de dados: " + e)
            return False


    def adicionar_obras_anunciadas(self, lista_de_obras):
        db = self.client.DadosPostagem
        colecao = db.registroObrasPostadas

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

            try:
                # Filtro para verificar se o documento já existe pelo titulo_obra
                filtro = {"titulo_obra": obra.titulo_obra}

                # Atualizar ou inserir os dados na coleção
                result = colecao.update_one(
                    filtro,
                    {"$set": dicionario_obra},
                    upsert=True
                )

                self.logger_infos.info(f"Registros inseridos/atualizados no MongoDB: {result.upserted_id if result.upserted_id else result.modified_count}")
            except Exception as e:
                Mensagens.erro_no_banco_de_dados(f"Erro ao inserir/atualizar registros no MongoDB: {e}")

    
    def receber_obras_anunciadas(self):
        db = self.client.DadosPostagem
        colecao = db.registroObrasPostadas
        
        lista_de_obras = []

        try:
            cursor = colecao.find({}) # Recebe todos os documentos da coleção

            # Iterar sobre os documentos encontrados
            for documento in cursor:
                obra = Obra(
                    titulo_obra=documento["titulo_obra"],
                    imagem_obra=documento["imagem_obra"],
                    url_obra=documento["url_obra"]
                )
                
                for dicionario_capitulo in documento["lista_de_capitulos"]:
                    capitulo = Capitulo(
                        numero_capitulo=dicionario_capitulo["numero_capitulo"],
                        link_capitulo=dicionario_capitulo["link_capitulo"],
                        data_postagem=dicionario_capitulo["data_postagem"]
                    )
                    obra.lista_de_capitulos.append(capitulo)
                
                lista_de_obras.append(obra)
            
            self.logger_infos.info("Registros Recebidos do MongoDB!")
            self.logger_infos.info(lista_de_obras)
        except Exception as e:
            Mensagens.erro_no_banco_de_dados(f"Erro ao receber registros do MongoDB: {e}")
            lista_de_obras = []  
        return lista_de_obras
            

    def inserir_obra(self, dicionario_obra):
        db = self.client.DadosPostagem
        colecao = db.dadosObras

        # Inserir os dados na coleção
        for chave, valor in dicionario_obra.items():
            filtro = {'titulo': chave}
            novo_valor = {'$set': valor}
            
            try:
                colecao.update_one(filtro, novo_valor, upsert=True)
                self.logger_infos.info(f"Inserido com sucesso na coleção 'dadosObras' se não existir.")
            except Exception as e:
                Mensagens.erro_no_banco_de_dados(f"Erro ao inserir dados na coleção 'dadosObras': {e}")

    
    def inserir_obra_nao_permitida_fb(self, dicionario_obra):
        db = self.client.DadosPostagem
        colecao = db.obrasNaoPermitidasFB

        # Inserir os dados na coleção
        try:
            colecao.insert_one(dicionario_obra)
        except Exception as e:
            Mensagens.erro_no_banco_de_dados(f'Erro ao inserir obra não permitida: {e}')

        
    def receber_obras(self):
        try:
            db = self.client.DadosPostagem
            colecao = db.dadosObras
        
            # Definir projeção para excluir o campo '_id'
            projection = {'_id': 0}

            todos_documentos = colecao.find({}, projection=projection).sort('titulo', 1)

            return todos_documentos
        except Exception as e:
            Mensagens.erro_no_banco_de_dados(f"Erro ao receber obras do MongoDB: {e}")
            return []


    def listar_obras_nao_permitidas_fb(self):
        try:
            db = self.client.DadosPostagem
            colecao = db.obrasNaoPermitidasFB

            projection = {'_id': 0}

            todos_documentos = colecao.find({}, projection=projection).sort('titulo_obra', 1)
            
            # Convertendo o cursor em uma lista
            lista_documentos = list(todos_documentos)

            return lista_documentos
        except Exception as e:
            Mensagens.erro_no_banco_de_dados(f"Erro ao listar obras não permitidas do MongoDB: {e}")
            return []


    def excluir_obra_por_titulo(self, titulo_a_remover):
        db = self.client.DadosPostagem
        colecao = db.dadosObras

        # Remover todos os documentos com o título especificado
        filtro_remover = {'titulo': titulo_a_remover}

        try:
            resultado = colecao.delete_many(filtro_remover)
            self.logger_infos.info(f"Documentos com o título '{titulo_a_remover}' removidos com sucesso. Total de documentos removidos: {resultado.deleted_count}")
            return f"Documentos com o título '{titulo_a_remover}' removidos com sucesso. Total de documentos removidos: {resultado.deleted_count}"
        except Exception as e:
            Mensagens.erro_no_banco_de_dados(f"Erro ao remover documentos com o título '{titulo_a_remover}': {e}")
            return f"Erro ao remover documentos com o título '{titulo_a_remover}': {e}"


    def excluir_registros_de_obras_anunciadas(self):
        db = self.client.DadosPostagem
        colecao = db.registroObrasPostadas

        try:
            resultado = colecao.delete_many({})
            self.logger_infos.info(f"Todos os documentos foram removidos com sucesso. Total de documentos removidos: {resultado.deleted_count}")
            return f"Todos os documentos foram removidos com sucesso. Total de documentos removidos: {resultado.deleted_count}"
        except Exception as e:
            Mensagens.erro_no_banco_de_dados(f"Erro ao remover todos os documentos: {e}")
            return f"Erro ao remover todos os documentos: {e}"
