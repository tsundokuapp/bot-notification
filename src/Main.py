#!/bin/python

import datetime
import time

from classes_io.Gestor_TXT import Gestor_TXT
from classes_io.Download_Imagens import Download_Imagens
from model.Mensagens import Mensagens
from dao.Web_Screper_Site import Web_Screper_Site
from controller.Controller_Postagem import Controller_Postagem

if __name__ == "__main__":    
    gestor_TXT = Gestor_TXT()
    data_anterior = gestor_TXT.get_data_anterior()

    Mensagens.mensagem_inicio()

    Mensagens.atualizando_diretorio_imagens()
    Download_Imagens.fazer_download_imagens_obras()

    data_atual = datetime.datetime.now().date()
    Mensagens.inicializando_validacao_arquivos_antigos()
    
    if data_anterior:
        diferenca_dias = data_atual.toordinal() - data_anterior.toordinal()
        Mensagens.mensagem_tempo_desde_exclusao(diferenca_dias)

    if diferenca_dias >= 30 or diferenca_dias <= -30:
        Mensagens.atualizando_diretorio_imagens()
        Download_Imagens.fazer_download_imagens_obras()
        Mensagens.mensagem_excluindo_relatorios_capitulos()
        gestor_TXT.deleta_registro_capitulos()
        data_anterior = data_atual
        gestor_TXT.atualiza_data_anterior(data_anterior)
    
    Controller_Postagem.execucao_principal()
    Mensagens.proxima_verificacao_capitulos()

