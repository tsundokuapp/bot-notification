from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

class Atlas_DAO:
    def __init__(self):
        #Carregando as variaveis de ambiente
        load_dotenv()
        self.uri = os.getenv("URI_ATLAS")
        
        # Create a new client and connect to the server
        self.client = MongoClient(self.uri, server_api=ServerApi('1'))
        
        self.testar_conexao()


    def testar_conexao(self):        
        # Send a ping to confirm a successful connection
        try:
            self.client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")

            return True
        except Exception as e:
            print(e)
            return False

            
    def inserir_obra(self, dicionario_obra):
        # Selecionar o banco de dados e a coleção
        db = self.client.DadosPostagem  # Substitua pelo nome do seu banco de dados
        colecao = db.dadosObras    # Substitua pelo nome da sua coleção

        # Inserir os dados na coleção
        for chave, valor in dicionario_obra.items():
            filtro = {'titulo': chave}
            novo_valor = {'$set': valor}
            
            try:
                colecao.update_one(filtro, novo_valor, upsert=True)
                print(f"Inserido com sucesso na coleção 'dadosObras' se não existir.")
            except Exception as e:
                print(f"Erro ao inserir dados na coleção 'dadosObras': {e}")

        
    def receber_obras(self):
        # Selecionar o banco de dados e a coleção
        db = self.client.DadosPostagem  # Substitua pelo nome do seu banco de dados
        colecao = db.dadosObras    # Substitua pelo nome da sua coleção

        # Definir projeção para excluir o campo '_id'
        projection = {'_id': 0}

        # Recuperar todos os documentos da coleção sem o campo '_id' e ordená-los por um campo específico (ex: 'titulo') em ordem alfabética ascendente
        todos_documentos = colecao.find({}, projection=projection).sort('titulo', 1)

        return todos_documentos


    def excluir_obra_por_titulo(self, titulo_a_remover):
        # Selecionar o banco de dados e a coleção
        db = self.client.DadosPostagem  # Substitua pelo nome do seu banco de dados
        colecao = db.dadosObras    # Substitua pelo nome da sua coleção

        # Remover todos os documentos com o título especificado
        filtro_remover = {'titulo': titulo_a_remover}

        try:
            resultado = colecao.delete_many(filtro_remover)
            print(f"Documentos com o título '{titulo_a_remover}' removidos com sucesso. Total de documentos removidos: {resultado.deleted_count}")
            return f"Documentos com o título '{titulo_a_remover}' removidos com sucesso. Total de documentos removidos: {resultado.deleted_count}"
        except Exception as e:
            print(f"Erro ao remover documentos com o título '{titulo_a_remover}': {e}")
            return f"Erro ao remover documentos com o título '{titulo_a_remover}': {e}"