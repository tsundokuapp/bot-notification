import os
import logging

from datetime import datetime

class GestorTXT:

    def __init__(self):
        self.pasta_registro_horario = os.path.join('assets/', 'registro_horario/')
        self.caminho_arquivo_data = os.path.join(self.pasta_registro_horario, 'data_anterior.txt')

        self.logger_infos = logging.getLogger('logger_infos')
        
        self.validar_e_criar_pastas()


    def validar_e_criar_pastas(self):
        pastas = [self.pasta_registro_horario]

        for pasta in pastas:
            if not os.path.exists(pasta):
                os.makedirs(pasta)


    def get_data_anterior(self):
        if os.path.isfile(self.caminho_arquivo_data):
            with open(self.caminho_arquivo_data, 'r') as f:
                 data_anterior = f.read().strip()
                 self.logger_infos.info("Data anterior recebida.")
                 return datetime.strptime(data_anterior, "%Y-%m-%d").date()

    
    def atualiza_data_anterior(self, data_anterior):
        with open(self.caminho_arquivo_data, 'w') as f:
            self.logger_infos.info("Data anterior atualizada.")
            f.write(str(data_anterior))
    