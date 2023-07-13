class Post_Facebook:

    def __init__(self, obra, dados_unicos_obras):
        self.titulo_obra = obra.titulo_obra
        self.imagem_obra = obra.imagem_obra
        self.url_obra = obra.url_obra

        self.lista_de_capitulos = obra.lista_de_capitulos

        self.imagem_obra = dados_unicos_obras[self.titulo_obra]['url_imagem']

        print(f"Construindo Post {self.titulo_obra }...")

    
    def retornar_mensagem_post(self):
        if len(self.lista_de_capitulos) == 1:

            print("postando: " + str(self.lista_de_capitulos))
            capitulo = self.lista_de_capitulos[0]

            mensagem_facebook = f'''
            
            Capítulo fresquinho para Todos!

            {self.titulo_obra}
            -- {capitulo.numero_capitulo}

            {capitulo.link_capitulo}

            Aproveita e passa lá no Discord para conversar com a gente:
            https://discord.gg/x4MyhMn3TQ

            Boa leitura a todos
            
            '''

        elif len(self.lista_de_capitulos) == 2:
            print("postando: " + str(self.lista_de_capitulos))
            
            primeiro_capitulo = self.lista_de_capitulos[1]
            segundo_capitulo = self.lista_de_capitulos[0]

            mensagem_facebook = f'''
            
            Capítulo fresquinho para Todos!

            {self.titulo_obra}
            -- {primeiro_capitulo.numero_capitulo} &
            -- {segundo_capitulo.numero_capitulo}

            {primeiro_capitulo.link_capitulo}

            Aproveita e passa lá no Discord para conversar com a gente:
            https://discord.gg/x4MyhMn3TQ

            Boa leitura a todos
            
            '''
        
        elif len(self.lista_de_capitulos) == 3:
            print("postando: " + str(self.lista_de_capitulos))
            
            primeiro_capitulo = self.lista_de_capitulos[2]
            segundo_capitulo = self.lista_de_capitulos[1]
            terceiro_capitulo = self.lista_de_capitulos[0]

            mensagem_facebook = f'''
            
            Capítulo fresquinho para Todos!

            {self.titulo_obra}
            -- {primeiro_capitulo.numero_capitulo} &
            -- {segundo_capitulo.numero_capitulo} &
            -- {terceiro_capitulo.numero_capitulo}

            {primeiro_capitulo.link_capitulo}

            Aproveita e passa lá no Discord para conversar com a gente:
            https://discord.gg/x4MyhMn3TQ

            Boa leitura a todos
            
            '''

        elif len(self.lista_de_capitulos) > 3:
            print("postando: " + str(self.lista_de_capitulos))
            
            primeiro_capitulo = self.lista_de_capitulos[0]
            ultimo_capitulo = self.lista_de_capitulos[-1]
    

            mensagem_facebook = f'''
            Capítulo fresquinho para Todos!

            {self.titulo_obra}
            Postados capítulos de:{ultimo_capitulo.numero_capitulo} -
            Até: {primeiro_capitulo.numero_capitulo}

            {ultimo_capitulo.numero_capitulo}

            Aproveita e passa lá no Discord para conversar com a gente:
            https://discord.gg/x4MyhMn3TQ

            Boa leitura a todos
            
            
            '''

        return mensagem_facebook