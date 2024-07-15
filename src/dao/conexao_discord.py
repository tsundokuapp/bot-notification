import discord
import logging
import os
import sys

from dotenv import load_dotenv

class ConexaoDiscord:

    def postar_anuncio_discord(post_obra, e_um_teste):
        logger_infos = logging.getLogger('logger_infos')

        intents = discord.Intents.default()
        client = discord.Client(intents=intents)

        #Carregando as variaveis de ambiente
        load_dotenv()
        token = os.getenv('API_KEY')
        canal = int(os.getenv('CANAL_LANCAMENTOS'))
        canal_id = int(os.getenv('CANAL_TAGS'))

        if e_um_teste:
            canal = int(os.getenv('CANAL_TESTES'))

        @client.event
        async def on_ready():
            channel = client.get_channel(canal)
            tags = client.get_channel(canal_id)
            
            embed = discord.Embed()

            guild = channel.guild
            cargo_todas_obras = discord.utils.get(guild.roles, name="Todas as obras")

            cargo = discord.utils.get(guild.roles, name=post_obra.nome_no_anuncio)

            if cargo is None or cargo_todas_obras is None:
                logger_infos.error("Cargo não foi encontrado!")
                raise Exception("Cargo não foi encontrado!")
            
            mensagem_cargos = f'''
            {cargo.mention} {cargo_todas_obras.mention}
            '''

            embed = discord.Embed()
            embed.colour = post_obra.cor_int
            embed.add_field(name="", value=post_obra.retornar_mensagem_post(tags.mention))
            embed.set_image(url=post_obra.imagem_obra)

            await channel.send(content=mensagem_cargos,embed=embed)

            await client.close()

        @client.event
        async def on_error(event, *args, **kwargs):
            logger_infos.error(f"Ocorreu um erro ao postar capitulo")

            atlas_dao = AtlasDAO()
            atlas_dao.remover_capitulos_de_uma_obra(post_obra.titulo_obra, post_obra.lista_de_capitulos)
            
            channel = client.get_channel(int(os.getenv('CANAL_TESTES')))
            await channel.send(f"Ocorreu um erro ao postar capitulo, verifique se o cargo esta criado no servidor, ou tente novamente. ")

            await client.close()

        logger_infos.info("Post no Discord realizado!")
        client.run(token)


    def mensagem_de_log_discord(mensagem_log):

        handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

        intents = discord.Intents.default()
        client = discord.Client(intents=intents)

        # Carregando as variaveis de ambiente
        load_dotenv()
        token = os.getenv('API_KEY')
        canal = int(os.getenv('CANAL_TESTES'))

        @client.event
        async def on_ready():
            channel = client.get_channel(canal)

            await channel.send(mensagem_log)  # Envia a mensagem sem um embed
            await client.close()

        client.run(token, log_handler=handler, log_level=logging.WARNING, root_logger=False)


import os
import logging

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
class AtlasDAO:
    def __init__(self):
        #Carregando as variaveis de ambiente
        load_dotenv()
        self.uri = os.getenv("URI_ATLAS")

        #Recebe os loggers
        self.logger_erros = logging.getLogger('logger_erros')
        self.logger_infos = logging.getLogger('logger_infos')
        
        # Create a new client and connect to the server
        self.client = MongoClient(self.uri, server_api=ServerApi('1'))
        
    def remover_capitulos_de_uma_obra(self, titulo_obra, lista_de_capitulos):
        db = self.client.DadosPostagem
        colecao = db.registroObrasPostadas

        try:
            # Filtro para verificar se o documento já existe pelo titulo_obra
            filtro = {"titulo_obra": titulo_obra}

            # Remover os capitulos na coleção
            result = colecao.update_one(
                filtro,
                {
                    "$pull": {
                        "lista_de_capitulos": {
                            "numero_capitulo": {
                                "$in": [capitulo.numero_capitulo for capitulo in lista_de_capitulos]
                            }
                        }
                    }
                }
            )

            self.logger_infos.info(f"Registros removidos do MongoDB: {result.modified_count}")
        except Exception as e:
            print(f"Erro ao remover registros do MongoDB: {e}")