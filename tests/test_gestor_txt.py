from src.classes_io.gestor_txt import GestorTXT
from datetime import datetime, date

class TestGestorTXT:
    def test_valida_recebimento_data_anterior(self):
        gestor_TXT = GestorTXT()

        print(gestor_TXT.get_data_anterior())

        assert isinstance(gestor_TXT.get_data_anterior(), date)  # Use date em vez de datetime.date


    def test_valida_modo_teste_e_boolean(self):
        gestor_TXT = GestorTXT()

        print(gestor_TXT.get_mode())

        assert isinstance(gestor_TXT.get_mode(), bool)

    
    def test_valida_modo_teste_nao_null(self):
        gestor_TXT = GestorTXT()

        print(gestor_TXT.get_mode())

        assert gestor_TXT.get_mode() != None


