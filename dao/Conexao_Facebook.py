
def postar_anuncio_facebook(titulo_obra, imagem_obra, capitulos_postados_hoje):
    load_dotenv()
    token_de_acesso_fb = os.getenv('API_TOKEN_PAGINA')
    id_pagina_fb = os.getenv("API_ID_PAGINA_FACEBOOK")
    imagem_obra = dados_unicos_obras[titulo_obra]['url_imagem']
    print(imagem_obra)

    graph = facebook.GraphAPI(access_token=token_de_acesso_fb, version="3.0")

    #try:
    #    response = requests.get(imagem_obra)
    #with open('{pasta_imagens_volumes}{url_obra}', 'wb') as f:
    #    f.write(response.content)

    try:
        testa = capitulos_postados_hoje[0][2]
        valida_identificacao = True
    except:
        valida_identificacao = False

    if len(capitulos_postados_hoje) == 1:
        print("postando No Facebook: " + str(capitulos_postados_hoje))

        capitulo = capitulos_postados_hoje[0][0]
        url_capitulo = capitulos_postados_hoje[0][1]

        mensagem_facebook = '''
        
        Capítulo fresquinho para Todos!

        {}
        -- {}

        {}

        Aproveita e passa lá no Discord para conversar com a gente:
        https://discord.gg/x4MyhMn3TQ

        Boa leitura a todos
        
        '''.format(titulo_obra,capitulo,url_capitulo)

    elif len(capitulos_postados_hoje) == 2 and valida_identificacao == False:
        print("postando: " + str(capitulos_postados_hoje))

        segundo_capitulo = capitulos_postados_hoje[0][0]
        primeiro_capitulo = capitulos_postados_hoje[1][0]
        url_primeiro_capitulo = capitulos_postados_hoje[1][1]
        
        mensagem_facebook = '''
        
        Capítulo fresquinho para Todos!

        {}
        -- {} &
        -- {}

        {}

        Aproveita e passa lá no Discord para conversar com a gente:
        https://discord.gg/x4MyhMn3TQ

        Boa leitura a todos
        
        '''.format(titulo_obra,primeiro_capitulo,segundo_capitulo,url_primeiro_capitulo)

    elif len(capitulos_postados_hoje) == 3:
        print("postando: " + str(capitulos_postados_hoje))
        
        terceiro_capitulo = capitulos_postados_hoje[0][0]
        segundo_capitulo = capitulos_postados_hoje[1][0]
        primeiro_capitulo = capitulos_postados_hoje[2][0]
        
        url_primeiro_capitulo = capitulos_postados_hoje[2][1]
        
        mensagem_facebook = '''
        
        Capítulo fresquinho para Todos!

        {}
        -- {} &
        -- {} &
        -- {}

        {}

        Aproveita e passa lá no Discord para conversar com a gente:
        https://discord.gg/x4MyhMn3TQ

        Boa leitura a todos
        
        '''.format(titulo_obra,primeiro_capitulo,segundo_capitulo,terceiro_capitulo,url_primeiro_capitulo)

    elif len(capitulos_postados_hoje[0]) > 2 and capitulos_postados_hoje[0][2] == "identificação":
        print("postando: " + str(capitulos_postados_hoje))
        ultimo_capitulo = capitulos_postados_hoje[0][0]
        primeiro_capitulo = capitulos_postados_hoje[1][0]
        url_primeiro_capitulo = capitulos_postados_hoje[1][1]

        mensagem_facebook = '''
        Capítulo fresquinho para Todos!

        {}
        Postados capítulos de:{} -
        Até: {}

        {}

        Aproveita e passa lá no Discord para conversar com a gente:
        https://discord.gg/x4MyhMn3TQ

        Boa leitura a todos
        
        
        '''.format(titulo_obra,primeiro_capitulo,ultimo_capitulo,url_primeiro_capitulo)

    #Recebendo imagem

    #with open('{pasta_imagens_volumes}{url_obra}', 'rb') as image_file:
    #    image_id = graph.put_photo(image=image_file, album_path='me/photos', published=False)['id']

    # Faz a postagem
    graph.put_object(parent_object=id_pagina_fb, connection_name='feed', message=mensagem_facebook)
