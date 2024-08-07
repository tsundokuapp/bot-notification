import locale
import datetime
import logging

from src.dao.web_screper_site import WebScreperSite

class TestWebScreper:
    def test_valida_se_esta_recebendo_dados_obras(self):
        web_screper = WebScreperSite()
        dados_obra = web_screper.receber_conteudo(5)

        [print(dado) for dado in dados_obra ]

        assert len(dados_obra[0]) > 0
        assert len(dados_obra[1]) > 0
        assert len(dados_obra[2]) > 0
        assert len(dados_obra[3]) > 0
        assert len(dados_obra[4]) > 0


    def test_valida_se_esta_recebendo_capitulos_obras(self):
        web_screper = WebScreperSite()
        dados_obra = web_screper.recebe_capitulos_diarios()

        [print(obra) for obra in dados_obra ]

        assert len(dados_obra) > 0


    def test_verifica_se_data_esta_em_portugues(self):
        web_screper = WebScreperSite()
        datas = web_screper.receber_datas()

        logger_infos = logging.getLogger('logger_infos')
        logger_infos.info(datas)

        locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')

        for data in datas:
            try:
                # Tenta fazer o parse da data
                dt = datetime.datetime.strptime(data, '%B %d, %Y')
                logger_infos.info(f"A data {dt} está em um formato válido")

            except ValueError:
                assert False, f"A data {data} está em um formato inválido"
            
            # Verifica se o nome do mês está em português
            mes_numero = dt.month
            nome_mes_portugues = datetime.date(1900, mes_numero, 1).strftime('%B').lower()

            assert nome_mes_portugues in [
                'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
                'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'
            ], f"A data {data} não está em português"