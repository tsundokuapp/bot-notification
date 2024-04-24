import time
import logging

from src.dao.web_screper_site import WebScreperSite
from src.dao.conexao_discord import ConexaoDiscord
from src.dao.atlas_dao import AtlasDAO
#from src.dao.conexao_facebook import ConexaoFacebook
from src.controller.controller_io import ControllerIO
from src.controller.controller_obras import ControllerObras
from src.model.posts.post_discord import PostDiscord
from src.model.posts.post_facebook import PostFacebook

from model.mensagens import Mensagens

class ControllerPostagem:

    def execucao_principal():
        atlas_dao = AtlasDAO()
        logger_infos = logging.getLogger('logger_infos')
        web_screper = WebScreperSite()

        #Recebe obras posta no site e remove as que não estão registradas
        lista_de_obras = ControllerObras.remove_obras_nao_registradas(web_screper.recebe_capitulos_diarios(), atlas_dao.receber_obras())

        #Verifica se existe registro de anúncios anteriores
        lista_de_obras_contidas_no_registro = ControllerIO.valida_existencia_de_anuncios_anteriores()
        existe_registro = len(lista_de_obras_contidas_no_registro) != 0

        #Faz validação dos capítulos e depois envia os dados para post
        if existe_registro:
            lista_de_obras_atualizada = ControllerObras.valida_lista_obras(lista_de_obras, lista_de_obras_contidas_no_registro)
            Mensagens.conclusao_verificacao_postagem()

            Mensagens.post_redes()
            for obra in lista_de_obras_atualizada:
                try:
                    Mensagens.post_discord()
                    post_obra_Discord = PostDiscord(obra, atlas_dao.receber_obras())
                    Mensagens.mensagen_realizando_post_obra(post_obra_Discord.nome_no_anuncio)
                    ConexaoDiscord.postar_anuncio_discord(post_obra_Discord, False)  
                
                except Exception as e:
                    Mensagens.erro_no_codigo(e)
                    Mensagens.nao_foi_possivel_postar_discord()
                    Mensagens.mensagem_nao_foi_possivel_postar_obra(obra.titulo_obra)

                time.sleep(10)

            lista_de_obras_nao_permitidas = atlas_dao.listar_obras_nao_permitidas_fb()
            lista_de_obras_facebook = ControllerObras.remover_obras_que_nao_pode_postar(lista_de_obras_atualizada,lista_de_obras_nao_permitidas)
            for obra in lista_de_obras_facebook:
                try:
                    Mensagens.post_facebook(obra.titulo_obra)
                    post_obra_Facebook = PostFacebook(obra, atlas_dao.receber_obras())
                    #Conexao_Facebook.postar_anuncio_facebook(post_obra_Facebook)
                
                except Exception as e:
                    Mensagens.erro_no_codigo(e)
                    Mensagens.nao_foi_possivel_postar_facebook()
                    Mensagens.mensagem_nao_foi_possivel_postar_obra(obra.titulo_obra)

                time.sleep(10)
     
        #Envia os dados para post
        else:
            logger_infos.info("Nenhum registro encontrado, pulado para o anúncio!")
            Mensagens.conclusao_verificacao_postagem()
            
            lista_de_obras_atualizada = lista_de_obras

            Mensagens.post_redes()
            for obra in lista_de_obras:

                try:
                    Mensagens.post_discord()
                    post_obra_Discord = PostDiscord(obra, atlas_dao.receber_obras())
                    Mensagens.mensagen_realizando_post_obra(post_obra_Discord.nome_no_anuncio)
                    ConexaoDiscord.postar_anuncio_discord(post_obra_Discord, False)
                except:
                    Mensagens.nao_foi_possivel_postar_discord()
                    Mensagens.mensagem_nao_foi_possivel_postar_obra(obra.titulo_obra)

                time.sleep(10)
            
            lista_de_obras_nao_permitidas = atlas_dao.listar_obras_nao_permitidas_fb()
            
            lista_de_obras_facebook = remover_obras_que_nao_pode_postar(lista_de_obras,lista_de_obras_nao_permitidas)
            
            for obra in lista_de_obras_facebook:
                try:
                    Mensagens.post_facebook(obra.titulo_obra)
                    post_obra_Facebook = PostFacebook(obra, atlas_dao.receber_obras())
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
        atlas_dao.adicionar_obras_anunciadas(lista_de_obras_contidas_no_registro)