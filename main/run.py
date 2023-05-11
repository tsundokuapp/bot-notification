# carregar data anterior do arquivo, se existir
data_anterior = None

caminho_arquivo_data = os.path.join(pasta_registro_horario, 'data_anterior.txt')
if os.path.isfile(caminho_arquivo_data):
    with open(caminho_arquivo_data, 'r') as f:
        data_anterior = f.read().strip()

while True:
    # obter data atual
    data_atual = datetime.now().date()

    # verificar se a data atual é diferente da data anterior
    if str(data_atual) != str(data_anterior):
        # excluir todos os arquivos na pasta de relatórios
        for arquivo in os.listdir(pasta_relatorios):
            caminho_arquivo = os.path.join(pasta_relatorios, arquivo)
            if os.path.isfile(caminho_arquivo):
                os.remove(caminho_arquivo)

        # atualizar data anterior
        data_anterior = data_atual

        # salvar data anterior no arquivo
        with open(caminho_arquivo_data, 'w') as f:
            f.write(str(data_anterior))

    # executar ação a cada 15 minutos
    validar_atualizacao_obras()
    now = datetime.now()
    print("Executando ação às {}:{}!".format(now.hour, now.minute))
    time.sleep(1800)