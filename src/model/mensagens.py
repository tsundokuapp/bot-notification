import time
import logging

from datetime import datetime

from src.dao.conexao_discord import ConexaoDiscord

class Mensagens:
    #Mensagens de indicação da execução de postagem
    @staticmethod
    def mensagem_inicio():
        time.sleep(5)
        logger_infos = logging.getLogger('logger_infos')
        logger_infos.info("*******************************************************")
        logger_infos.info("                Iniciando o programa...                ")
        logger_infos.info("*******************************************************\n")

        mensagem_log = "**Iniciando o programa...**"

        ConexaoDiscord.mensagem_de_log_discord(mensagem_log)


    @staticmethod
    def atualizando_diretorio_imagens():
        time.sleep(5)
        logger_infos = logging.getLogger('logger_infos')
        logger_infos.info("*******************************************************")
        logger_infos.info("      Atualizando Diretorio de Imagens...     ")
        logger_infos.info("*******************************************************\n")

        mensagem_log = "**Atualizando Diretorio de Imagens...**"

        ConexaoDiscord.mensagem_de_log_discord(mensagem_log)


    @staticmethod
    def recebendo_capitulos_mensagem():
        time.sleep(5)
        logger_infos = logging.getLogger('logger_infos')
        logger_infos.info("*******************************************************")
        logger_infos.info("         Recebendo capitulos dos ultimos dias...         ")
        logger_infos.info("*******************************************************\n")

        mensagem_log = "**Recebendo Capitulos dos ultimos dias...**"
        ConexaoDiscord.mensagem_de_log_discord(mensagem_log)

    
    @staticmethod
    def inicializando_validacao_arquivos_antigos():
        time.sleep(5)
        logger_infos = logging.getLogger('logger_infos')
        logger_infos.info("*******************************************************")
        logger_infos.info("       Validando registro de arquivos antigos...       ")
        logger_infos.info("*******************************************************\n")

        mensagem_log = "**Validando registro de arquivos antigos...**"

        ConexaoDiscord.mensagem_de_log_discord(mensagem_log)

    
    @staticmethod
    def inicializando_verificacao_postagem():
        time.sleep(5)
        logger_infos = logging.getLogger('logger_infos')
        logger_infos.info("*******************************************************")
        logger_infos.info("      Comparando lista recebida com do registro...     ")
        logger_infos.info("*******************************************************\n")

        mensagem_log = "**Comparando lista recebida com do registro...**"

        ConexaoDiscord.mensagem_de_log_discord(mensagem_log)

    
    @staticmethod    
    def conclusao_verificacao():
        time.sleep(5)
        logger_infos = logging.getLogger('logger_infos')
        logger_infos.info("*******************************************************")
        logger_infos.info("      Comparação concluída, iniciando postagem...      ")
        logger_infos.info("*******************************************************\n")
        
        mensagem_log = "**Comparação concluída, iniciando postagem...**"
        ConexaoDiscord.mensagem_de_log_discord(mensagem_log)


    @staticmethod
    def post_redes():
        time.sleep(5)
        logger_infos = logging.getLogger('logger_infos')
        logger_infos.info("*******************************************************")
        logger_infos.info("            Iniciando anúncio nas redes...              ")
        logger_infos.info("*******************************************************\n")

        mensagem_log = "**Iniciando anúncio nas redes...**"
        ConexaoDiscord.mensagem_de_log_discord(mensagem_log)


    @staticmethod
    def post_discord():
        time.sleep(5)
        logger_infos = logging.getLogger('logger_infos')
        logger_infos.info("*******************************************************")
        logger_infos.info("            Fazendo anúncio no Discord...              ")
        logger_infos.info("*******************************************************\n")

        mensagem_log = "**Fazendo anúncio no Discord...**"
        ConexaoDiscord.mensagem_de_log_discord(mensagem_log)

    
    @staticmethod
    def adicionando_anuncios_no_registro():
        time.sleep(5)
        logger_infos = logging.getLogger('logger_infos')
        logger_infos.info("*******************************************************")
        logger_infos.info("    Registrando Caps Anúnciados para ev.Repetição...     ")
        logger_infos.info("*******************************************************\n")

        mensagem_log = "**Registrando caps anúnciados para evitar repetição...**"
        ConexaoDiscord.mensagem_de_log_discord(mensagem_log)


    @staticmethod
    def mensagem_excluindo_relatorios_capitulos():
        time.sleep(5)
        logger_infos = logging.getLogger('logger_infos')
        logger_infos.info("*******************************************************")
        logger_infos.info("        Excluindo relatórios dos capítulos...          ")
        logger_infos.info("*******************************************************\n")

        mensagem_log = "**Excluindo relatórios dos capítulos...**"

        ConexaoDiscord.mensagem_de_log_discord(mensagem_log)


    @staticmethod
    def nao_foi_possivel_postar_discord():
        time.sleep(5)
        logger_infos = logging.getLogger('logger_infos')
        logger_infos.info("*******************************************************")
        logger_infos.info("      Não foi possível fazer o post no Discord...      ")
        logger_infos.info("*******************************************************\n")

        mensagem_log = "Não foi possível fazer o post no Discord... Tentaremos novamente mais tarde"

        ConexaoDiscord.mensagem_de_log_discord(mensagem_log)


    @staticmethod
    def nao_foi_possivel_postar_facebook():
        time.sleep(5)
        logger_infos = logging.getLogger('logger_infos')
        logger_infos.info("*******************************************************")
        logger_infos.info("      Não foi possível fazer o post no Facebook...      ")
        logger_infos.info("*******************************************************\n")

        mensagem_log = "Não foi possível fazer o post no Facebook... Tentaremos novamente mais tarde"

        ConexaoDiscord.mensagem_de_log_discord(mensagem_log)

    #Mensagens de aviso quanto a execucão principal
    @staticmethod
    def mensagem_obra_nao_tem_nenhum_capitulo(titulo_obra):
        mensagem_log = f"A seguinte obra não tem nenhum capitulo:  {titulo_obra}, ela será pulada!"
        logger_infos = logging.getLogger('logger_infos')
        logger_infos.info(mensagem_log)
        ConexaoDiscord.mensagem_de_log_discord(mensagem_log)


    @staticmethod
    def nao_existe_registro():
        time.sleep(5)
        mensagem_log = "O arquivo não existe, deve ter sido excluído recentemente. Criando arquivo vazio..."
        logger_infos = logging.getLogger('logger_infos')
        logger_infos.info(mensagem_log)
        ConexaoDiscord.mensagem_de_log_discord(mensagem_log)
        

    @staticmethod
    def mensagem_tempo_desde_exclusao(diferenca_dias):
        mensagem_log = "Tempo desde a última exclusão: " , diferenca_dias, " dias\n"

        logger_infos = logging.getLogger('logger_infos')
        logger_infos.info(mensagem_log)

        ConexaoDiscord.mensagem_de_log_discord(mensagem_log)


    @staticmethod
    def mensagem_lista_de_obras_para_verificar(lista_de_obras):
        mensagem_log = f"Lista de obras para verificar: {lista_de_obras}\n"

        logger_infos = logging.getLogger('logger_infos')
        logger_infos.info(mensagem_log)

        ConexaoDiscord.mensagem_de_log_discord(mensagem_log)


    @staticmethod
    def mensagem_lista_de_obras_para_fazer_anuncio(lista_de_obras):
        mensagem_log = f"Lista de obras para fazer anúncio: {lista_de_obras}"

        logger_infos = logging.getLogger('logger_infos')
        logger_infos.info(mensagem_log)

        ConexaoDiscord.mensagem_de_log_discord(mensagem_log)


    @staticmethod
    def mensagem_nenhum_post_obra(titulo_obra):
        mensagem_log = f"Nenhum post de {titulo_obra}. \n"

        logger_infos = logging.getLogger('logger_infos')
        logger_infos.info(mensagem_log)

        ConexaoDiscord.mensagem_de_log_discord(mensagem_log)

    
    @staticmethod
    def mensagem_obra_tem_n_posts(titulo_obra, quantidade):
        mensagem_log = f"{titulo_obra} tem {quantidade} capitulos postados no site. \n"

        logger_infos = logging.getLogger('logger_infos')
        logger_infos.info(mensagem_log)

        ConexaoDiscord.mensagem_de_log_discord(mensagem_log)


    @staticmethod
    def mensagen_realizando_post_obra(titulo_obra):
        mensagem_log = f"Realizando anúncio de {titulo_obra}"

        logger_infos = logging.getLogger('logger_infos')
        logger_infos.info(mensagem_log)
        
        ConexaoDiscord.mensagem_de_log_discord(mensagem_log)


    @staticmethod
    def post_facebook(titulo_obra):
        time.sleep(5)
        mensagem_log = f"**Fazendo anúncio de {titulo_obra} no Facebook...**"

        logger_infos = logging.getLogger('logger_infos')
        logger_infos.info(mensagem_log)
        
        ConexaoDiscord.mensagem_de_log_discord(mensagem_log)


    @staticmethod
    def informa_obras_sem_registro(lista_de_obras):
        mensagem_log = f"Existem obras dentre as postadas recentemente que não foram registradas.\n {lista_de_obras}\n \n CANCELANDO EXECUÇÃO... \n Use o comando /adicionar_obra para adicionar cada uma delas e depois use /forcar_postagem para a verificação ser feita novamente."

        ConexaoDiscord.mensagem_de_log_discord(mensagem_log)

        logger_infos = logging.getLogger('logger_infos')
        logger_infos.info(mensagem_log)

        time.sleep(10)

    
    @staticmethod
    def proxima_verificacao_capitulos():
        time.sleep(5)
        now = datetime.now()

        mensagem_log = "Envio concluído, a guarde a próxima verificação. São feitas 12h, 16h, 18h, 20h e 22h."

        logger_infos = logging.getLogger('logger_infos')
        logger_infos.info(mensagem_log)

        ConexaoDiscord.mensagem_de_log_discord(mensagem_log)


    #Mensagens de erros
    @staticmethod
    def erro_no_codigo(mensagem_erro_exception):
        time.sleep(5)

        mensagem_log = "Ocorreu uma exceção não catalogada: %s" % mensagem_erro_exception

        logger_erros = logging.getLogger('logger_erros')
        logger_erros.error(mensagem_log)

        ConexaoDiscord.mensagem_de_log_discord(mensagem_log)

    
    #Mensagens de erros
    @staticmethod
    def erro_no_banco_de_dados(mensagem_erro_exception):
        time.sleep(5)

        mensagem_log = "Não foi possível realizar a operação no banco de dados: %s" % mensagem_erro_exception

        logger_erros = logging.getLogger('logger_erros')
        logger_erros.error(mensagem_log)

        ConexaoDiscord.mensagem_de_log_discord(mensagem_log)


    @staticmethod
    def mensagem_nao_foi_possivel_postar_obra(titulo_obra):
        mensagem_log = f"Não foi possível fazer a postagem de {titulo_obra}, verifique se as informações dela foram cadastradas corretamente no JSON"
        
        logger_erros = logging.getLogger('logger_erros')
        logger_erros.error(mensagem_log)

        ConexaoDiscord.mensagem_de_log_discord(mensagem_log)
