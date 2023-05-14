from datetime import datetime, timedelta

class Mensagens:
    def mensagem_inicio():
        print("*******************************************************")
        print("                Iniciando o programa...                ")
        print("*******************************************************\n")

    
    def mensagem_excluindo_relatorios_capitulos():
        print("*******************************************************")
        print("        Excluindo relatórios dos capítulos...          ")
        print("*******************************************************\n")


    def inicializando_validacao_arquivos_antigos():
        print("*******************************************************")
        print("       Validando registro de arquivos antigos...       ")
        print("*******************************************************\n")

    
    def inicializando_verificacao_postagem():
        print("*******************************************************")
        print("      Comparando lista recebida com do registro...     ")
        print("*******************************************************\n")

    
    def conclusao_verificacao_postagem():
        print("*******************************************************")
        print("      Comparação concluída, iniciando postagem...      ")
        print("*******************************************************\n")


    def post_discord():
        print("*******************************************************")
        print("            Fazendo anúncio no Discord...              ")
        print("*******************************************************\n")


    def post_facebook():
        print("*******************************************************")
        print("            Fazendo anúncio no Facebook...             ")
        print("*******************************************************\n")


    
    def recebendo_capitulos_mensagem():
        print("*******************************************************")
        print("         Recebendo Capitulos dos ultimos dias.         ")
        print("*******************************************************\n")

    
    def adicionando_anuncios_no_registro():
        print("*******************************************************")
        print("    Registrando Caps Anúnciados para ev.Repetição.     ")
        print("*******************************************************\n")

    
    def proxima_verificacao_capitulos():
        now = datetime.now()
        print("\nA próxima verificação dos capítulos será {}:{}!\n".format(now.hour, now.minute))
        print("*******************************************************\n")
