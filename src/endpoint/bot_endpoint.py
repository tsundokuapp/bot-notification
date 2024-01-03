import logging
import os
import subprocess

import discord
from discord import app_commands

from dotenv import load_dotenv
from typing import Optional

from src.dao.Atlas_Dao import Atlas_DAO
from src.endpoint.pagination import Pagination

#Carregando as variaveis de ambiente
load_dotenv()
token = os.getenv('API_KEY')
canal = int(os.getenv('CANAL_TESTES'))

MY_GUILD = discord.Object(id=697958499589554217)
atlas_dao = Atlas_DAO()

class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        self.tree.copy_global_to(guild=MY_GUILD)
        await self.tree.sync(guild=MY_GUILD)

intents = discord.Intents.default()
client = MyClient(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print('------')


#Adicionar obra no banco
@client.tree.command()
@app_commands.describe(
    titulo='Titulo que esta no site',
    cargo_discord='Cargo discord',
    capa_obra='URL da imagem',
    cor ='Cor em hexadecimal, ex:0xFFFFFF'
)
async def adicionar_obra(interaction: discord.Interaction, titulo: str, cargo_discord: str, capa_obra: str, cor: str):
    """Adicione uma obra nova na listagem."""
    try:
        dicionario_obra = {
            titulo: {
                "cargo_discord": cargo_discord,
                "url_imagem": capa_obra,
                "cor": cor
            }
        }

        atlas_dao.inserir_obra(dicionario_obra)

        await interaction.response.send_message(f'{titulo} adicionada com sucesso!')
    except Exception as e:
        await interaction.response.send_message(f'Erro ao adicionar {titulo}: {e}')


#Comando para remover obras do banco
@client.tree.command()
@app_commands.describe(
    titulo='Titulo que esta no site'
)
async def remover_obra(interaction: discord.Interaction, titulo: str):
    """Remova uma obra a partir do título."""

    res = atlas_dao.excluir_obra_por_titulo(titulo)

    await interaction.response.send_message(res)


#Comando para listar obras que estão no banco
@client.tree.command()
async def listar_obras(interaction: discord.Interaction):

    cursor_obras = atlas_dao.receber_obras()  # Recebendo o cursor do MongoDB
    colecao_obras = list(cursor_obras)  # Convertendo o cursor para uma lista de obras

    max_docs_por_pagina = 10

    async def get_page(page: int):
        emb = discord.Embed(title="Obras Registradas", description="Obras que estão salvas no banco de dados.")
        offset = (page - 1) * max_docs_por_pagina

        parte_documentos = colecao_obras[offset:offset + max_docs_por_pagina]

        formatted_collections = "\n".join([f"{index + 1}. {obra}" for index, obra in enumerate(parte_documentos)])
        emb.description = formatted_collections

        total_pages = Pagination.compute_total_pages(len(colecao_obras), max_docs_por_pagina)
        emb.set_footer(text=f"Página {page} de {total_pages}")
        
        return emb, total_pages

    await Pagination(interaction, get_page).navegate()


#Comando para forçar verificação de novos capitulos
@client.tree.command()
async def forcar_postagem(interaction: discord.Interaction):
    """Força a execução da postagem dos capitulos."""

    subprocess.run(["python", "src/Main.py"])

    await interaction.response.send_message(f'Postagem esta sendo iniciada... acompanhe pelo canal de logs')


#Comando que verifica quando um membro entrou no servidor
@client.tree.command()
@app_commands.describe(member='The member you want to get the joined date from; defaults to the user who uses the command')
async def joined(interaction: discord.Interaction, member: Optional[discord.Member] = None):
    """Diga quando um membro entrou no servidor"""
    # If no member is explicitly provided then we use the command user here
    member = member or interaction.user

    # The format_dt function formats the date time into a human readable representation in the official client
    await interaction.response.send_message(f'{member} entrou {discord.utils.format_dt(member.joined_at)}')


#Teste do banco de dados
@client.tree.command()
async def testar_banco(interaction: discord.Interaction):
    """Verifica conexão com banco de dados."""

    if(atlas_dao.testar_conexao()):
        await interaction.response.send_message(f'Ativo e operante!')
    else:
        await interaction.response.send_message(f'Moio o esquema, abre um chamado aí!')


#Teste conectividade do bot
@client.tree.command()
async def ping(interaction: discord.Interaction):
    """Verificar conectividade do bot."""
    await interaction.response.send_message(f'Olá, Latência: {round(client.latency,3)} ms')


client.run(token)