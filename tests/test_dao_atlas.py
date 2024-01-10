from src.dao.atlas_dao import AtlasDAO

class TestDaoAtlasDao:
    def test_validar_conexao(self):
        atlas_dao = AtlasDAO()

        assert atlas_dao.testar_conexao()