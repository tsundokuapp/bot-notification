from src.dao.Atlas_Dao import Atlas_DAO
from unittest.mock import MagicMock
from pymongo.errors import ServerSelectionTimeoutError

class TestDaoAtlasDao:
    def test_validar_conexao(self):
        atlas_dao = Atlas_DAO()

        assert atlas_dao.testar_conexao()

    
    def test_retorno_facebook_valido(self):
        atlas_dao = Atlas_DAO()

        print(atlas_dao.listar_obras_nao_permitidas_fb())