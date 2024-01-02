class Post_Discord:

    def __init__(self, obra, dados_unicos_obras):
        self.titulo_obra = obra.titulo_obra
        self.imagem_obra = obra.imagem_obra
        self.url_obra = obra.url_obra

        self.lista_de_capitulos = obra.lista_de_capitulos

        self.nome_no_anuncio = dados_unicos_obras[self.titulo_obra]['cargo_discord']
        self.cor_int = int(dados_unicos_obras[self.titulo_obra]['cor'], 16)
        self.imagem_obra = dados_unicos_obras[self.titulo_obra]['url_imagem']

    
    def retornar_mensagem_post(self, tag_aba):
        if len(self.lista_de_capitulos) == 1:
            print("postando: " + str(self.lista_de_capitulos))
            capitulo = self.lista_de_capitulos[0]

            mensagem_final = f'''
            
            **[{self.titulo_obra}]({self.url_obra})**
            
            **Yo Minna!!!**
            **Capítulo fresquinho para todos!**
            <:uhu:867903115469393980>

            **[{capitulo.numero_capitulo}]({capitulo.link_capitulo})**
            
            Não esqueçam de ir na aba de {tag_aba} e assinar as suas séries favoritas pra sempre receber notificação quando elas forem lançadas. <:anotadinho:970678923052613735>
            
            Boa leitura
            <:oi:845651532401475584>
            
            '''

        elif len(self.lista_de_capitulos) == 2:
            print("postando: " + str(self.lista_de_capitulos))
            
            primeiro_capitulo = self.lista_de_capitulos[0]
            segundo_capitulo = self.lista_de_capitulos[1]

            mensagem_final = f'''
            
            **[{self.titulo_obra}]({self.url_obra})**
            
            **Yo Minna!!!**
            **Capítulo fresquinho para todos!**
            <:uhu:867903115469393980>

            **[{primeiro_capitulo.numero_capitulo}]({primeiro_capitulo.link_capitulo})** &
            **[{segundo_capitulo.numero_capitulo}]({segundo_capitulo.link_capitulo})**

            Não esqueçam de ir na aba de {tag_aba} e assinar as suas séries favoritas pra sempre receber notificação quando elas forem lançadas. <:anotadinho:970678923052613735>
            
            Boa leitura
            <:oi:845651532401475584>
            
            '''
        
        elif len(self.lista_de_capitulos) == 3:
            print("postando: " + str(self.lista_de_capitulos))
            
            primeiro_capitulo = self.lista_de_capitulos[0]
            segundo_capitulo = self.lista_de_capitulos[1]
            terceiro_capitulo = self.lista_de_capitulos[2]

            mensagem_final = f'''
            
            **[{self.titulo_obra}]({self.url_obra})**
            
            **Yo Minna!!!**
            **Capítulo fresquinho para todos!**
            <:uhu:867903115469393980>

            **[{primeiro_capitulo.numero_capitulo}]({primeiro_capitulo.link_capitulo})** &
            **[{segundo_capitulo.numero_capitulo}]({segundo_capitulo.link_capitulo})**
            **[{terceiro_capitulo.numero_capitulo}]({terceiro_capitulo.link_capitulo})** 

            Não esqueçam de ir na aba de {tag_aba} e assinar as suas séries favoritas pra sempre receber notificação quando elas forem lançadas. <:anotadinho:970678923052613735>
            
            Boa leitura
            <:oi:845651532401475584>
            
            '''

        elif len(self.lista_de_capitulos) > 3:
            print("postando: " + str(self.lista_de_capitulos))
            
            primeiro_capitulo = self.lista_de_capitulos[0]
            ultimo_capitulo = self.lista_de_capitulos[-1]
    

            mensagem_final = f'''
            
            **[{self.titulo_obra}]({self.url_obra})**
            
            **Yo Minna!!!**
            **Capítulo fresquinho para todos!**
            <:uhu:867903115469393980>

            Postados capítulos de: **[{ultimo_capitulo.numero_capitulo}]({ultimo_capitulo.link_capitulo})** -
            Até: **[{primeiro_capitulo.numero_capitulo}]({primeiro_capitulo.link_capitulo})** 

            Não esqueçam de ir na aba de {tag_aba} e assinar as suas séries favoritas pra sempre receber notificação quando elas forem lançadas. <:anotadinho:970678923052613735>
            
            Boa leitura
            <:oi:845651532401475584>
            
            '''

        return mensagem_final