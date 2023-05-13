from datetime import datetime, timedelta

class Mensagens:
    def mensagem_inicio():
        print("*****************************************")
        print("         Iniciando o programa...         ")
        print("*****************************************\n")

    
    def mensagem_excluindo_relatorios_capitulos():
        print("*****************************************")
        print("  Excluindo relatórios dos capítulos...  ")
        print("*****************************************\n")


    def inicializando_validacao_arquivos_antigos():
        print("*****************************************")
        print("Validando registro de arquivos antigos...")
        print("*****************************************\n")

    
    def inicializando_verificacao_postagem():
        print("*****************************************")
        print("  Inicializando verificação postagem...  ")
        print("*****************************************\n")

    
    def proxima_verificacao_capitulos():
        now = datetime.now()
        print("A próxima verificação dos capítulos será {}:{}!".format(now.hour, now.minute))
        print("*********************************************************\n")