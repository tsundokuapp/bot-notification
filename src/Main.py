#!/bin/python

import datetime
import logging

from src.classes_io.Gestor_TXT import Gestor_TXT
from src.classes_io.Download_Imagens import Download_Imagens
from src.model.Mensagens import Mensagens
from src.model.Logger_Config import Logger_Config
from src.dao.Atlas_Dao import Atlas_DAO
from src.dao.Web_Screper_Site import Web_Screper_Site
from src.controller.Controller_Postagem import Controller_Postagem

if __name__ == "__main__":

    logger_config = Logger_Config()
    atlas_dao = Atlas_DAO()

    try:
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
            atlas_dao.excluir_registros_de_obras_anunciadas()
            data_anterior = data_atual
            gestor_TXT.atualiza_data_anterior(data_anterior)

        Controller_Postagem.execucao_principal()
        Mensagens.proxima_verificacao_capitulos()

    except Exception as e:
        Mensagens.erro_no_codigo(e)