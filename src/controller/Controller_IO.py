import logging

from src.dao.Atlas_Dao import Atlas_DAO
from src.model.Mensagens import Mensagens

class Controller_IO:

    def valida_existencia_de_anuncios_anteriores():

        atlas_dao = Atlas_DAO()
        logger_infos = logging.getLogger('logger_infos')
        
        Mensagens.inicializando_verificacao_postagem()
        lista_de_obras_recebida = atlas_dao.receber_obras_anunciadas()

        if len(lista_de_obras_recebida) == 0:
            logger_infos.info("Não existe registro de anúncios!")
            return []
        else:
           return lista_de_obras_recebida