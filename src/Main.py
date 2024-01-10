#!/bin/python

import datetime
import logging

from src.classes_io.gestor_txt import GestorTXT
from src.classes_io.download_imagens import DownloadImagens
from src.model.mensagens import Mensagens
from src.model.logger_config import LoggerConfig
from src.dao.atlas_dao import AtlasDAO
from src.controller.controller_postagem import ControllerPostagem

if __name__ == "__main__":

    logger_config = LoggerConfig()
    atlas_dao = AtlasDAO()

    try:
        gestor_TXT = GestorTXT()
        data_anterior = gestor_TXT.get_data_anterior()

        Mensagens.mensagem_inicio()

        Mensagens.atualizando_diretorio_imagens()
        DownloadImagens.fazer_download_imagens_obras()

        data_atual = datetime.datetime.now().date()
        Mensagens.inicializando_validacao_arquivos_antigos()

        if data_anterior:
            diferenca_dias = data_atual.toordinal() - data_anterior.toordinal()
            Mensagens.mensagem_tempo_desde_exclusao(diferenca_dias)

        if diferenca_dias >= 30 or diferenca_dias <= -30:
            Mensagens.atualizando_diretorio_imagens()
            DownloadImagens.fazer_download_imagens_obras()
            Mensagens.mensagem_excluindo_relatorios_capitulos()
            atlas_dao.excluir_registros_de_obras_anunciadas()
            data_anterior = data_atual
            gestor_TXT.atualiza_data_anterior(data_anterior)

        ControllerPostagem.execucao_principal()
        Mensagens.proxima_verificacao_capitulos()

    except Exception as e:
        Mensagens.erro_no_codigo(e)