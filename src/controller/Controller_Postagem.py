from dao.Web_Screper_Site import Web_Screper_Site
from dao.Conexao_Discord import Conexao_Discord
from dao.Conexao_Facebook import Conexao_Facebook
from classes_io.Gestor_JSON import Gestor_JSON
from controller.Controller_IO import Controller_IO
from model.posts.Post_Discord import Post_Discord
from model.posts.Post_Facebook import Post_Facebook

from model.Mensagens import Mensagens

import time

class Controller_Postagem:

    def execucao_principal():

        gestor_json = Gestor_JSON()

        def remover_obras_que_nao_pode_postar(lista_de_obras_para_postar, lista_de_obras_nao_permitidas):
            obras_filtradas = [obra for obra in lista_de_obras_para_postar if obra.titulo_obra not in [obra_json.titulo_obra for obra_json in lista_de_obras_nao_permitidas]]
            return obras_filtradas

        def valida_lista_obras(lista_de_obras, lista_de_obras_contidas_no_registro):
            print("\n*******************************************************")
            Mensagens.mensagem_lista_de_obras_para_verificar(lista_de_obras)
            print(lista_de_obras_contidas_no_registro)

            for obra_atual in lista_de_obras:
                for obra_contida_no_registro in lista_de_obras_contidas_no_registro:
                    if obra_atual.titulo_obra == obra_contida_no_registro.titulo_obra:
                        capitulos_restantes = []
                        for capitulo_atual in obra_atual.lista_de_capitulos:
                            for capitulo_contido_no_registro in obra_contida_no_registro.lista_de_capitulos:
                                if capitulo_atual.numero_capitulo == capitulo_contido_no_registro.numero_capitulo:
                                    print(f"Removendo capitulo que já foi anunciado antes: {capitulo_atual}")
                                    break
                            else:
                                capitulos_restantes.append(capitulo_atual)

                        obra_atual.lista_de_capitulos = capitulos_restantes

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

            Mensagens.post_redes()
            for obra in lista_de_obras_atualizada:
                try:
                    Mensagens.post_discord()
                    post_obra_Discord = Post_Discord(obra, gestor_json.retornar_dados_unicos_obras())
                    Mensagens.mensagen_realizando_post_obra(post_obra_Discord.nome_no_anuncio)
                    Conexao_Discord.postar_anuncio_discord(post_obra_Discord, False)  
                
                except Exception as e:
                    print("Erro ocorrido: ",e)
                    Mensagens.erro_no_codigo(e)
                    Mensagens.nao_foi_possivel_postar_discord()
                    Mensagens.mensagem_nao_foi_possivel_postar_obra(obra.titulo_obra)

                time.sleep(10)

            lista_de_obras_nao_permitidas = gestor_json.receber_lista_obras_json_nao_permitidas_fb()
            lista_de_obras_facebook = remover_obras_que_nao_pode_postar(lista_de_obras_atualizada,lista_de_obras_nao_permitidas)
            for obra in lista_de_obras_facebook:
                try:
                    Mensagens.post_facebook(obra.titulo_obra)
                    post_obra_Facebook = Post_Facebook(obra, gestor_json.retornar_dados_unicos_obras())
                    #Conexao_Facebook.postar_anuncio_facebook(post_obra_Facebook)
                
                except Exception as e:
                    Mensagens.erro_no_codigo(e)
                    Mensagens.nao_foi_possivel_postar_facebook()
                    Mensagens.mensagem_nao_foi_possivel_postar_obra(obra.titulo_obra)

                time.sleep(10)
     
        #Envia os dados para post
        else:
            print("Nenhum registro encontrado, pulado para o anúncio!")
            Mensagens.conclusao_verificacao_postagem()
            
            lista_de_obras_atualizada = lista_de_obras

            Mensagens.post_redes()
            for obra in lista_de_obras:

                try:
                    Mensagens.post_discord()
                    post_obra_Discord = Post_Discord(obra, gestor_json.retornar_dados_unicos_obras())
                    Mensagens.mensagen_realizando_post_obra(post_obra_Discord.nome_no_anuncio)
                    Conexao_Discord.postar_anuncio_discord(post_obra_Discord, False)
                except:
                    Mensagens.nao_foi_possivel_postar_discord()
                    Mensagens.mensagem_nao_foi_possivel_postar_obra(obra.titulo_obra)

                time.sleep(10)
            
            lista_de_obras_nao_permitidas = gestor_json.receber_lista_obras_json_nao_permitidas_fb()
            
            lista_de_obras_facebook = remover_obras_que_nao_pode_postar(lista_de_obras,lista_de_obras_nao_permitidas)
            
            for obra in lista_de_obras_facebook:
                try:
                    Mensagens.post_facebook(obra.titulo_obra)
                    post_obra_Facebook = Post_Facebook(obra, gestor_json.retornar_dados_unicos_obras())
                    #Conexao_Facebook.postar_anuncio_facebook(post_obra_Facebook)
                except:
                    Mensagens.nao_foi_possivel_postar_facebook()
                    Mensagens.mensagem_nao_foi_possivel_postar_obra(obra.titulo_obra)

                time.sleep(10)
                
        for obra in lista_de_obras_atualizada:
            for obra_contida in lista_de_obras_contidas_no_registro:
                if obra.titulo_obra == obra_contida.titulo_obra:
                    for capitulo in obra.lista_de_capitulos:
                        if capitulo.numero_capitulo not in [c.numero_capitulo for c in obra_contida.lista_de_capitulos]:
                            obra_contida.adicionar_capitulo(capitulo.numero_capitulo, capitulo.link_capitulo, capitulo.data_postagem)
            else:
                lista_de_obras_contidas_no_registro.append(obra)

        
        Mensagens.adicionando_anuncios_no_registro()
        gestor_json.criar_json_com_lista_obras(lista_de_obras_contidas_no_registro)


        
        
                    



