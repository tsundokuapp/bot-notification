from dao.Conexao_Discord import Conexao_Discord

from datetime import datetime, timedelta
import time

class Mensagens:
    def mensagem_inicio():
        time.sleep(5)
        print("*******************************************************")
        print("                Iniciando o programa...                ")
        print("*******************************************************\n")

        mensagem_log = "**Iniciando o programa...**"

        Conexao_Discord.mensagem_de_log_discord(mensagem_log)

    
    def mensagem_tempo_desde_exclusao(diferenca_dias):
        print("Tempo desde a última exclusão: " , diferenca_dias, " dias\n")

        mensagem_log = "Tempo desde a última exclusão: " , diferenca_dias, " dias\n"

        Conexao_Discord.mensagem_de_log_discord(mensagem_log)

    def mensagem_lista_de_obras_para_verificar(lista_de_obras):
        print(f"Lista de obras para verificar: {lista_de_obras}\n")

        mensagem_log = f"Lista de obras para verificar: {lista_de_obras}\n"

        Conexao_Discord.mensagem_de_log_discord(mensagem_log)

    def mensagem_lista_de_obras_para_fazer_anuncio(lista_de_obras):
        print(f"Lista de obras para fazer anúncio: {lista_de_obras}")

        mensagem_log = f"Lista de obras para fazer anúncio: {lista_de_obras}"

        Conexao_Discord.mensagem_de_log_discord(mensagem_log)


    def mensagem_nenhum_post_obra(titulo_obra):
        print(f"Nenhum post de {titulo_obra}. \n")

        mensagem_log = f"Nenhum post de {titulo_obra}. \n"

        Conexao_Discord.mensagem_de_log_discord(mensagem_log)


    def mensagem_excluindo_relatorios_capitulos():
        time.sleep(5)
        print("*******************************************************")
        print("        Excluindo relatórios dos capítulos...          ")
        print("*******************************************************\n")

        mensagem_log = "**Excluindo relatórios dos capítulos...**"

        Conexao_Discord.mensagem_de_log_discord(mensagem_log)


    def inicializando_validacao_arquivos_antigos():
        time.sleep(5)
        print("*******************************************************")
        print("       Validando registro de arquivos antigos...       ")
        print("*******************************************************\n")

        mensagem_log = "**Validando registro de arquivos antigos...**"

        Conexao_Discord.mensagem_de_log_discord(mensagem_log)

    
    def inicializando_verificacao_postagem():
        time.sleep(5)
        print("*******************************************************")
        print("      Comparando lista recebida com do registro...     ")
        print("*******************************************************\n")

        mensagem_log = "**Comparando lista recebida com do registro...**"

        Conexao_Discord.mensagem_de_log_discord(mensagem_log)

    
    def atualizando_diretorio_imagens():
        time.sleep(5)
        print("*******************************************************")
        print("      Atualizando Diretorio de Imagens...     ")
        print("*******************************************************\n")

        mensagem_log = "**Atualizando Diretorio de Imagens...**"

        Conexao_Discord.mensagem_de_log_discord(mensagem_log)


    def nao_foi_possivel_postar_discord():
        time.sleep(5)
        print("*******************************************************")
        print("      Não foi possível fazer o post no Discord...      ")
        print("*******************************************************\n")

        mensagem_log = "Não foi possível fazer o post no Discord... Tentaremos novamente mais tarde"

        Conexao_Discord.mensagem_de_log_discord(mensagem_log)


    def nao_foi_possivel_postar_facebook():
        time.sleep(5)
        print("*******************************************************")
        print("      Não foi possível fazer o post no Facebook...      ")
        print("*******************************************************\n")

        mensagem_log = "Não foi possível fazer o post no Facebook... Tentaremos novamente mais tarde"

        Conexao_Discord.mensagem_de_log_discord(mensagem_log)

    
    def conclusao_verificacao_postagem():
        time.sleep(5)
        print("*******************************************************")
        print("      Comparação concluída, iniciando postagem...      ")
        print("*******************************************************\n")
        
        mensagem_log = "**Comparação concluída, iniciando postagem...**"
        Conexao_Discord.mensagem_de_log_discord(mensagem_log)


    def post_discord():
        time.sleep(5)
        print("*******************************************************")
        print("            Fazendo anúncio no Discord...              ")
        print("*******************************************************\n")

        mensagem_log = "**Fazendo anúncio no Discord...**"
        Conexao_Discord.mensagem_de_log_discord(mensagem_log)


    def post_redes():
        time.sleep(5)
        print("*******************************************************")
        print("            Iniciando anúncio nas redes...              ")
        print("*******************************************************\n")

        mensagem_log = "**Iniciando anúncio nas redes...**"
        Conexao_Discord.mensagem_de_log_discord(mensagem_log)


    def mensagen_realizando_post_obra(titulo_obra):
        print(f"Realizando anúncio de {titulo_obra}")
        mensagem_log = f"Realizando anúncio de {titulo_obra}"
        Conexao_Discord.mensagem_de_log_discord(mensagem_log)

    def post_facebook():
        time.sleep(5)
        print("            Fazendo anúncio no Facebook...             ")
        mensagem_log = "**Fazendo anúncio no Facebook...**"
        Conexao_Discord.mensagem_de_log_discord(mensagem_log)


    
    def recebendo_capitulos_mensagem():
        time.sleep(5)
        print("*******************************************************")
        print("         Recebendo capitulos dos ultimos dias...         ")
        print("*******************************************************\n")

        mensagem_log = "**Recebendo Capitulos dos ultimos dias...**"
        Conexao_Discord.mensagem_de_log_discord(mensagem_log)

    
    def adicionando_anuncios_no_registro():
        time.sleep(5)
        print("*******************************************************")
        print("    Registrando Caps Anúnciados para ev.Repetição...     ")
        print("*******************************************************\n")

        mensagem_log = "**Registrando caps anúnciados para evitar repetição...**"
        Conexao_Discord.mensagem_de_log_discord(mensagem_log)


    
    def proxima_verificacao_capitulos():
        time.sleep(5)
        now = datetime.now()
        next_execution = now + timedelta(seconds=18000)

        print("\nA próxima verificação dos capítulos será {}:{}!\n".format(next_execution.hour, next_execution.minute))
        print("*******************************************************\n")

        mensagem_log = "\n**A próxima verificação dos capítulos será {}:{}!**\n".format(next_execution.hour, next_execution.minute)
        Conexao_Discord.mensagem_de_log_discord(mensagem_log)
