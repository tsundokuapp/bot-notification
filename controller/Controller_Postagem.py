from dao.Web_Screper_Site import Web_Screper_Site
from dao.Conexao_Discord import Conexao_Discord
from classes_io.Gestor_JSON import Gestor_JSON
from controller.Controller_IO import Controller_IO
from model.posts.Post_Discord import Post_Discord
from model.posts.Post_Facebook import Post_Facebook

from model.Mensagens import Mensagens

import time

class Controller_Postagem:

    def execucao_principal():
        def valida_lista_obras(lista_de_obras, lista_de_obras_contidas_no_registro):
            print("\n*******************************************************")
            Mensagens.mensagem_lista_de_obras_para_verificar(lista_de_obras)

            for obra_atual in lista_de_obras:
                for obra_contida_no_registro in lista_de_obras_contidas_no_registro:
                    if obra_atual.titulo_obra == obra_contida_no_registro.titulo_obra:
                        for capitulo_atual in obra_atual.lista_de_capitulos:
                            for capitulo_contido_no_registro in obra_contida_no_registro.lista_de_capitulos:
                                if capitulo_atual.numero_capitulo == capitulo_contido_no_registro.numero_capitulo:
                                    print(f"Removendo capitulo que já foi anunciado antes: {capitulo_atual}")
                                    obra_atual.lista_de_capitulos.remove(capitulo_atual)

            lista_de_obras = [obra for obra in lista_de_obras if obra.lista_de_capitulos]

            Mensagens.mensagem_lista_de_obras_para_fazer_anuncio(lista_de_obras)
            print("*******************************************************\n")

            return lista_de_obras
        
        web_screper = Web_Screper_Site()
        lista_de_obras = web_screper.recebe_capitulos_diarios()

        lista_de_obras_contidas_no_registro = Controller_IO.valida_existencia_de_anuncios_anteriores()
        existe_registro = len(lista_de_obras_contidas_no_registro) != 0

        #Faz validação dos capítulos e depois envia os dados para post
        if existe_registro:
            lista_de_obras_atualizada = valida_lista_obras(lista_de_obras, lista_de_obras_contidas_no_registro)
            Mensagens.conclusao_verificacao_postagem()

            Mensagens.post_discord()
            for obra in lista_de_obras_atualizada:
                post_obra_Discord = Post_Discord(obra, Gestor_JSON.retornar_dados_unicos_obras())
                Mensagens.mensagen_realizando_post_obra(post_obra_Discord.nome_no_anuncio)
                Conexao_Discord.postar_anuncio_discord(post_obra_Discord)  

                #Aqui vai a parte do facebook
                #Mensagens.post_facebook()
                #post_obra_Facebook = Post_Facebook(obra, Gestor_JSON.retornar_dados_unicos_obras())
                #Conexao_Facebook.postar_anuncio_facebook(post_obra_Facebook)
     
        #Envia os dados para post
        else:
            print("Nenhum registro encontrado, pulado para o anúncio!")
            Mensagens.conclusao_verificacao_postagem()

            Mensagens.post_discord()
            for obra in lista_de_obras:
                Mensagens.post_discord()
                post_obra_Discord = Post_Discord(obra, Gestor_JSON.retornar_dados_unicos_obras())
                Conexao_Discord.postar_anuncio_discord(post_obra_Discord)  
                
                #Aqui vai a parte do facebook

                time.sleep(300)
                
        for obra in lista_de_obras_atualizada:
            for obra_contida in lista_de_obras_contidas_no_registro:
                if obra.titulo_obra == obra_contida.titulo_obra:
                    for capitulo in obra.lista_de_capitulos:
                        if capitulo.numero_capitulo not in [c.numero_capitulo for c in obra_contida.lista_de_capitulos]:
                            obra_contida.adicionar_capitulo(capitulo.numero_capitulo, capitulo.link_capitulo, capitulo.data_postagem)
            else:
                lista_de_obras_contidas_no_registro.append(obra)

        
        Mensagens.adicionando_anuncios_no_registro()
        Gestor_JSON.criar_json_com_lista_obras(lista_de_obras_contidas_no_registro)


        
        
                    



