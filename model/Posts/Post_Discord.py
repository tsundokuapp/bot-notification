def postar_anuncio_discord(titulo_obra, imagem_obra, url_obra, capitulos_postados_hoje):
    intents = discord.Intents.default()
    client = discord.Client(intents=intents)
    
    print(capitulos_postados_hoje)

    nome_no_anuncio = dados_unicos_obras[titulo_obra]['cargo_discord']
    cor_int = int(dados_unicos_obras[titulo_obra]['cor'], 16)
    imagem_obra = dados_unicos_obras[titulo_obra]['url_imagem']
    print(imagem_obra)

    #Carregando as variaveis de ambiente
    load_dotenv()
    token = os.getenv('API_KEY')
    canal = int(os.getenv('CANAL_LANCAMENTOS'))
    canal_id = int(os.getenv('CANAL_TAGS'))

    try:
        testa = capitulos_postados_hoje[0][2]
        valida_identificacao = True
    except:
        valida_identificacao = False

    @client.event
    async def on_ready():
        channel = client.get_channel(canal)
        tags = client.get_channel(canal_id)
        
        embed = discord.Embed()

        guild = channel.guild
        cargo_todas_obras = discord.utils.get(guild.roles, name="Todas as obras")

        cargo = discord.utils.get(guild.roles, name=nome_no_anuncio)

        mensagem_cargos = f'''
        {cargo.mention} {cargo_todas_obras.mention}
        ''' 

        if len(capitulos_postados_hoje) == 1:
            print("postando: " + str(capitulos_postados_hoje))

            capitulo = capitulos_postados_hoje[0][0]
            url_capitulo = capitulos_postados_hoje[0][1]

            mensagem_final = '''
            
            **[{}]({})**
            
            **Yo Minna!!!**
            **Capítulo fresquinho para todos!**
            <:uhu:867903115469393980>

            **[{}]({})**
            
            Não esqueçam de ir na aba de {} e assinar as suas séries favoritas pra sempre receber notificação quando elas forem lançadas. <:anotadinho:970678923052613735>
            
            Boa leitura
            <:oi:845651532401475584>
            
            '''.format(titulo_obra,url_obra,capitulo,url_capitulo,tags.mention)

        elif len(capitulos_postados_hoje) == 2 and valida_identificacao == False:
            print("postando: " + str(capitulos_postados_hoje))

            segundo_capitulo = capitulos_postados_hoje[0][0]
            primeiro_capitulo = capitulos_postados_hoje[1][0]
            url_segundo_capitulo = capitulos_postados_hoje[0][1]
            url_primeiro_capitulo = capitulos_postados_hoje[1][1]

            mensagem_final = '''
            
            **[{}]({})**
            
            **Yo Minna!!!**
            **Capítulo fresquinho para todos!**
            <:uhu:867903115469393980>

            **[{}]({})** &
            **[{}]({})**

            Não esqueçam de ir na aba de {} e assinar as suas séries favoritas pra sempre receber notificação quando elas forem lançadas. <:anotadinho:970678923052613735>
            
            Boa leitura
            <:oi:845651532401475584>
            
            '''.format(titulo_obra,url_obra,primeiro_capitulo,url_primeiro_capitulo,segundo_capitulo,url_segundo_capitulo,tags.mention)

        elif len(capitulos_postados_hoje) == 3:
            print("postando: " + str(capitulos_postados_hoje))
            
            terceiro_capitulo = capitulos_postados_hoje[0][0]
            segundo_capitulo = capitulos_postados_hoje[1][0]
            primeiro_capitulo = capitulos_postados_hoje[2][0]
            
            url_terceiro_capitulo = capitulos_postados_hoje[0][1]
            url_segundo_capitulo = capitulos_postados_hoje[1][1]
            url_primeiro_capitulo = capitulos_postados_hoje[2][1]

            mensagem_final = '''
            
            **[{}]({})**
            
            **Yo Minna!!!**
            **Capítulo fresquinho para todos!**
            <:uhu:867903115469393980>

            **[{}]({})** &
            **[{}]({})** &
            **[{}]({})** 

            Não esqueçam de ir na aba de {} e assinar as suas séries favoritas pra sempre receber notificação quando elas forem lançadas. <:anotadinho:970678923052613735>
            
            Boa leitura
            <:oi:845651532401475584>
            
            '''.format(titulo_obra,url_obra,primeiro_capitulo,url_primeiro_capitulo,segundo_capitulo,url_segundo_capitulo,terceiro_capitulo,url_terceiro_capitulo,tags.mention)

        elif len(capitulos_postados_hoje[0]) > 2 and capitulos_postados_hoje[0][2] == "identificação":
            print("postando: " + str(capitulos_postados_hoje))

            ultimo_capitulo = capitulos_postados_hoje[0][0]
            primeiro_capitulo = capitulos_postados_hoje[1][0]
            url_ultimo_capitulo = capitulos_postados_hoje[0][1]
            url_primeiro_capitulo = capitulos_postados_hoje[1][1]

            mensagem_final = '''
            
            **[{}]({})**
            
            **Yo Minna!!!**
            **Capítulo fresquinho para todos!**
            <:uhu:867903115469393980>

            Postados capítulos de: **[{}]({})** -
            Até: **[{}]({})** 
            
            Não esqueçam de ir na aba de {} e assinar as suas séries favoritas pra sempre receber notificação quando elas forem lançadas. <:anotadinho:970678923052613735>
            
            Boa leitura
            <:oi:845651532401475584>
            
            '''.format(titulo_obra,url_obra,primeiro_capitulo,url_primeiro_capitulo,ultimo_capitulo,url_ultimo_capitulo,tags.mention)

        print(mensagem_final)
    
        embed = discord.Embed()
        embed.colour = cor_int
        embed.add_field(name="", value=mensagem_final)
        embed.set_image(url=imagem_obra)

        await channel.send(content=mensagem_cargos,embed=embed)

        await client.close()
    
    client.run(token)
