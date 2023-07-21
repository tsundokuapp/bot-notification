from dotenv import load_dotenv
import discord
import os

class Conexao_Discord:

    def postar_anuncio_discord(post_obra, e_um_teste):
        intents = discord.Intents.default()
        client = discord.Client(intents=intents)

        #Carregando as variaveis de ambiente
        load_dotenv()
        token = os.getenv('API_KEY')
        canal = int(os.getenv('CANAL_LANCAMENTOS'))
        canal_id = int(os.getenv('CANAL_TAGS'))

        if e_um_teste:
            canal = os.getenv('CANAL_TESTES')

        @client.event
        async def on_ready():
            channel = client.get_channel(canal)
            tags = client.get_channel(canal_id)
            
            embed = discord.Embed()

            guild = channel.guild
            cargo_todas_obras = discord.utils.get(guild.roles, name="Todas as obras")

            cargo = discord.utils.get(guild.roles, name=post_obra.nome_no_anuncio)
            
            
            mensagem_cargos = f'''
            {cargo.mention} {cargo_todas_obras.mention}
            ''' 

            embed = discord.Embed()
            embed.colour = post_obra.cor_int
            embed.add_field(name="", value=post_obra.retornar_mensagem_post(tags.mention))
            embed.set_image(url=post_obra.imagem_obra)

            await channel.send(content=mensagem_cargos,embed=embed)

            await client.close()
        print("Post no Discord realizado!")
        client.run(token)


    def mensagem_de_log_discord(mensagem_log):
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

        client.run(token)
