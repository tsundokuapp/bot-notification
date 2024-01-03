from src.dao.Web_Screper_Site import Web_Screper_Site

import locale
import datetime

class TestWebScreper:
    def test_valida_se_esta_recebendo_dados_obras(self):
        web_screper = Web_Screper_Site()
        dados_obra = web_screper.receber_conteudo(5)

        assert len(dados_obra[0]) > 0
        assert len(dados_obra[1]) > 0
        assert len(dados_obra[2]) > 0
        assert len(dados_obra[3]) > 0
        assert len(dados_obra[4]) > 0


    def test_verifica_se_data_esta_em_portugues(self):
        web_screper = Web_Screper_Site()
        datas = web_screper.receber_datas()

        print(datas)

        locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')

        for data in datas:
            try:
                # Tenta fazer o parse da data
                dt = datetime.datetime.strptime(data, '%B %d, %Y')
                print(f"A data {dt} está em um formato válido")

            except ValueError:
                assert False, f"A data {data} está em um formato inválido"
            
            # Verifica se o nome do mês está em português
            mes_numero = dt.month
            nome_mes_portugues = datetime.date(1900, mes_numero, 1).strftime('%B').lower()

            assert nome_mes_portugues in [
                'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
                'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'
            ], f"A data {data} não está em português"