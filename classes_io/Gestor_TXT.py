import os
from datetime import datetime, timedelta

class Gestor_TXT:

    def __init__(self):
        print("Construindo objeto ... {}".format(self))
        self.pasta_registro_horario = os.path.join(os.path.dirname(__file__), 'registro_horario/')
        self.caminho_arquivo_data = os.path.join(self.pasta_registro_horario, 'data_anterior.txt')

    
    def get_data_anterior(self):
        if os.path.isfile(self.caminho_arquivo_data):
            with open(self.caminho_arquivo_data, 'r') as f:
                 data_anterior = f.read().strip()
                 print("Data anterior recebida.")
                 return datetime.strptime(data_anterior, "%Y-%m-%d").date()

    
    def atualiza_data_anterior(self, data_anterior):
        with open(self.caminho_arquivo_data, 'w') as f:
            print("Data anterior atualizada.")
            f.write(str(data_anterior))

    
    def deleta_registro_capitulos(self):
        pasta_relatorios = os.path.join(os.path.dirname(__file__),'registro_capitulos/')
        caminho_completo_obras = os.path.join(pasta_relatorios, 'obras.json')
        if os.path.isfile(caminho_completo_obras):
            print(caminho_completo_obras + " Excluido!")
            os.remove(caminho_completo_obras)

    