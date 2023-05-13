from classes_io.Gestor_TXT import Gestor_TXT
from model.Mensagens import Mensagens
from dao.Web_Screper_Site import Web_Screper_Site

from datetime import datetime, timedelta
import time

pasta_relatorios = '/home/ginfo/_dev/bot-tsun/gestor_postagem_tsun/classes_io/registro_capitulos'

gestor_TXT = Gestor_TXT()
data_anterior = gestor_TXT.get_data_anterior()

Mensagens.mensagem_inicio()

while True:
    # obter data atual
    data_atual = datetime.now().date()

    # verificar se a data atual é diferente da data anterior
    Mensagens.inicializando_validacao_arquivos_antigos()
    diferenca_dias = data_atual.toordinal() - data_anterior.toordinal()
    print("Tempo desde a última exclusão: " , diferenca_dias, " dias\n")

    if diferenca_dias >= 10 or diferenca_dias <= -10:
        Mensagens.mensagem_excluindo_relatorios_capitulos()
        gestor_TXT.deleta_registro_capitulos(pasta_relatorios)

        data_anterior = data_atual
        gestor_TXT.atualiza_data_anterior(data_anterior)

    # executar ação a cada 15 minutos
    Mensagens.inicializando_verificacao_postagem()
    web_Screper_site = Web_Screper_Site()
    web_Screper_site.recebe_capitulos_diarios()

    #validar_atualizacao_obras()
    Mensagens.proxima_verificacao_capitulos()
    time.sleep(1800)