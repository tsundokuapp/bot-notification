from dao.Web_Screper_Site import Web_Screper_Site

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
            except ValueError:
                assert False, f"A data {data} está em um formato inválido"
            
            # Verifica se o mês da data está em português
            mes = dt.strftime('%B')
            assert mes.lower().startswith('julho'), f"A data {data} não está em português"