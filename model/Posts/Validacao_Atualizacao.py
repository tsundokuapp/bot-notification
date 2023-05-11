def validar_atualizacao_obras():
    for numero_atual in [5,6,7,8]:
        print("Começando")

        dados_obra = receber_conteudo(numero_atual)

        titulo_obra = dados_obra[0]
        imagem_obra = dados_obra[3]
        url_obra = dados_obra[4]

        matriz_capitulos_postados_hoje = receber_capitulos_diarios_filtrados(url_obra) 

        data_atual = datetime.now().strftime('%d-%m-%Y')

        #Valida se a matriz esta vazia
        if not matriz_capitulos_postados_hoje:
            print("Nenhum capítulo novo hoje de: "+ titulo_obra+ ", seguindo para a próxima...")

            continue

        try:
            ##Recebe registro da ultima postagem no discord
            with open(f'{pasta_relatorios}matriz_capitulos_postados_{titulo_obra}{data_atual}.json', 'r') as arquivo:
                json_str = json.load(arquivo)

            dados = json.loads(json_str)
            matriz_carregada_capitulos_postados = dados["matriz_capitulos_postados_hoje"]
   
            try:
                testa = matriz_capitulos_postados_hoje[0][2]
                valida_identificacao = True
            except:
                valida_identificacao = False

            print("Registro Encontrado")

            print("Matriz recebida do site é: ")
            print(matriz_capitulos_postados_hoje)

            print("Matriz contida nos registros é: ")
            print(matriz_carregada_capitulos_postados)

            print(len(matriz_capitulos_postados_hoje))
            print(len(matriz_carregada_capitulos_postados))


            match (len(matriz_capitulos_postados_hoje), len(matriz_carregada_capitulos_postados)):
                case (1, 1): 
                    print("len 1 e 1")   
                    
                    if matriz_capitulos_postados_hoje[0] == matriz_carregada_capitulos_postados[0]:
                        print("Ultimo capítulo postado é o mesmo do registro, seguindo para o próximo...")
                        continue
                    else:
                        print("impossivel")

                case (2, 1):
                    print("len 2 e 1")

                    if valida_identificacao == True:
                        todos_capitulos_de_hoje = receber_capitulos_diarios_sem_filtro(url_obra)
     
                        print("no if")

                        print("todos os caps")
                        print(todos_capitulos_de_hoje)

                        print("carregada")         
                        print(matriz_carregada_capitulos_postados)     
                        

                        for i, sublist_anterior in enumerate(matriz_carregada_capitulos_postados):
                            for j, sublist_atual in enumerate(todos_capitulos_de_hoje):
                                if sublist_anterior[0] == sublist_atual[0]:
                                    del todos_capitulos_de_hoje[j:]
                                    del matriz_carregada_capitulos_postados[i:]
                                    break
                        
                        if len(todos_capitulos_de_hoje) == 1:
                            matriz_capitulos_postados_hoje = todos_capitulos_de_hoje

                        elif len(todos_capitulos_de_hoje) == 2: 
                            matriz_capitulos_postados_hoje = todos_capitulos_de_hoje

                        elif len(todos_capitulos_de_hoje) == 3:
                            matriz_capitulos_postados_hoje = todos_capitulos_de_hoje
                        
                        elif len(todos_capitulos_de_hoje) >= 4:
                            matriz_capitulos_postados_hoje[-1][1] = todos_capitulos_de_hoje[-1][1]
                            matriz_capitulos_postados_hoje[-1][0] = todos_capitulos_de_hoje[-1][0]

                    else:
                        print("no else")
                        for i, sublist_anterior in enumerate(matriz_carregada_capitulos_postados):
                            for j, sublist_atual in enumerate(matriz_capitulos_postados_hoje):
                                if sublist_anterior[0] == sublist_atual[0]:
                                    del matriz_capitulos_postados_hoje[j:]
                                    del matriz_carregada_capitulos_postados[i:]
                                    break
                                    
                    print("Matriz atualizada:")
                    print(matriz_capitulos_postados_hoje)

                    print("Capítulo novo, seguindo postagem...")

                case (2, 2):
                    print("len 2 e 2 ")

                    if matriz_capitulos_postados_hoje[0] == matriz_carregada_capitulos_postados[0]:
                        print("Ultimo capítulo postado é o mesmo do registro, seguindo para o próximo...")
                        continue
                        
                    elif valida_identificacao == True:
                        todos_capitulos_de_hoje = receber_capitulos_diarios_sem_filtro(url_obra)
     
                        print("no elif")

                        print("todos os caps")
                        print(todos_capitulos_de_hoje)

                        print("carregada")         
                        print(matriz_carregada_capitulos_postados)     
            
                        for i, sublist_anterior in enumerate(matriz_carregada_capitulos_postados):
                            for j, sublist_atual in enumerate(todos_capitulos_de_hoje):
                                if sublist_anterior[0] == sublist_atual[0]:
                                    del todos_capitulos_de_hoje[j:]
                                    del matriz_carregada_capitulos_postados[i:]
                                    break
                        
                        print("Tamanho da todos capitulos de hoje:")
                        print(len(todos_capitulos_de_hoje))
                        print(todos_capitulos_de_hoje)

                        if len(todos_capitulos_de_hoje) == 1:
                            matriz_capitulos_postados_hoje = todos_capitulos_de_hoje

                        elif len(todos_capitulos_de_hoje) == 2: 
                            matriz_capitulos_postados_hoje = todos_capitulos_de_hoje

                        elif len(todos_capitulos_de_hoje) == 3:
                            matriz_capitulos_postados_hoje = todos_capitulos_de_hoje
                        
                        elif len(todos_capitulos_de_hoje) >= 4:
                            matriz_capitulos_postados_hoje[-1][1] = todos_capitulos_de_hoje[-1][1]
                            matriz_capitulos_postados_hoje[-1][0] = todos_capitulos_de_hoje[-1][0]
                    else:
                        print("impossivel")
                    
                    print("Matriz atualizada:")
                    print(matriz_capitulos_postados_hoje)

                    print("Capítulo novo, seguindo postagem...")
                
                case (2, 3):
                    print("len 2 e 3 ")

                    if valida_identificacao == True:
                        todos_capitulos_de_hoje = receber_capitulos_diarios_sem_filtro(url_obra)
     
                        print("no if")

                        print("todos os caps")
                        print(todos_capitulos_de_hoje)

                        print("carregada")         
                        print(matriz_carregada_capitulos_postados)     
                        

                        for i, sublist_anterior in enumerate(matriz_carregada_capitulos_postados):
                            for j, sublist_atual in enumerate(todos_capitulos_de_hoje):
                                if sublist_anterior[0] == sublist_atual[0]:
                                    del todos_capitulos_de_hoje[j:]
                                    del matriz_carregada_capitulos_postados[i:]
                                    break

                        if len(todos_capitulos_de_hoje) == 1:
                            matriz_capitulos_postados_hoje = todos_capitulos_de_hoje

                        elif len(todos_capitulos_de_hoje) == 2: 
                            matriz_capitulos_postados_hoje = todos_capitulos_de_hoje

                        elif len(todos_capitulos_de_hoje) == 3:
                            matriz_capitulos_postados_hoje = todos_capitulos_de_hoje
                        
                        elif len(todos_capitulos_de_hoje) >= 4:
                            matriz_capitulos_postados_hoje[-1][1] = todos_capitulos_de_hoje[-1][1]
                            matriz_capitulos_postados_hoje[-1][0] = todos_capitulos_de_hoje[-1][0]
                    else:
                        print("impossivel")

                    print("Matriz atualizada:")
                    print(matriz_capitulos_postados_hoje)

                    print("Capítulo novo, seguindo postagem...")

                case (3, 1):
                    print("len 3 e 1 ")

                    for i, sublist_anterior in enumerate(matriz_carregada_capitulos_postados):
                        for j, sublist_atual in enumerate(matriz_capitulos_postados_hoje):
                            if sublist_anterior[0] == sublist_atual[0]:
                                del matriz_capitulos_postados_hoje[j:]
                                del matriz_carregada_capitulos_postados[i:]
                                break


                    print("Matriz atualizada:")
                    print(matriz_capitulos_postados_hoje)

                    print("Capítulo novo, seguindo postagem...")
                
                case (3, 2):
                    print("len 3 e 2 ")

                    for i, sublist_anterior in enumerate(matriz_carregada_capitulos_postados):
                        for j, sublist_atual in enumerate(matriz_capitulos_postados_hoje):
                            if sublist_anterior[0] == sublist_atual[0]:
                                del matriz_capitulos_postados_hoje[j:]
                                del matriz_carregada_capitulos_postados[i:]
                                break

                    print("Matriz atualizada:")
                    print(matriz_capitulos_postados_hoje)

                    print("Capítulo novo, seguindo postagem...")
                
                case (3, 3):
                    print("len 3 e 3 ")

                    if matriz_capitulos_postados_hoje[0] == matriz_carregada_capitulos_postados[0]:
                        print("Ultimo capítulo postado é o mesmo do registro, seguindo para o próximo...")
                        continue
                    else:
                        print("impossivel")

                case default:
                    print("Os comprimentos não correspondem")

        except Exception as e:
           print(f"Ocorreu um erro: {e}")
           print("Registro não encontrado")           

        postar_anuncio_discord(titulo_obra, imagem_obra, url_obra, matriz_capitulos_postados_hoje)

        dicionario = {"matriz_capitulos_postados_hoje": matriz_capitulos_postados_hoje}
        json_str = json.dumps(dicionario)
        with open(f'{pasta_relatorios}matriz_capitulos_postados_{titulo_obra}{data_atual}.json', 'w') as arquivo:
            json.dump(json_str, arquivo)
