import sys
from datetime import datetime, timedelta
import time
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
pasta_relatorios_capitulos = os.path.join('..', '/classes_io/registro_capitulos')

from classes_io.Gestor_TXT import Gestor_TXT
from model.Mensagens import Mensagens
from dao.Web_Screper_Site import Web_Screper_Site
from controller.Controller_Postagem import Controller_Postagem

gestor_TXT = Gestor_TXT()
data_anterior = gestor_TXT.get_data_anterior()

Mensagens.mensagem_inicio()

while True:
    data_atual = datetime.now().date()

    Mensagens.inicializando_validacao_arquivos_antigos()
    if data_anterior:
        diferenca_dias = data_atual.toordinal() - data_anterior.toordinal()
        print("Tempo desde a última exclusão: " , diferenca_dias, " dias\n")

    if diferenca_dias >= 30 or diferenca_dias <= -30:
        Mensagens.mensagem_excluindo_relatorios_capitulos()
        gestor_TXT.deleta_registro_capitulos(pasta_relatorios_capitulos)

        data_anterior = data_atual
        gestor_TXT.atualiza_data_anterior(data_anterior)

    # executar ação a cada 15 minutos
    Controller_Postagem.execucao_principal()

    #validar_atualizacao_obras()
    Mensagens.proxima_verificacao_capitulos()
    time.sleep(5000)