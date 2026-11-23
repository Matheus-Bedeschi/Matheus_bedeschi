import queue

ARQUIVO = "dados_sistema.txt"

produtos = []
pagamentos = queue.Queue()
historico = []
arvore = {}

def cadastrar_produto():
    codigo = input ("Codigo do produto: ")
    nome = input ("Nome do produto: ")
    preco = input ("Preco: ")
    departamento = input ("Departamento: ")
    categoria = input ("Categoria: ")
    subcategoria = input ("Subcategoria: ")
    produto = [codigo, nome, preco, departamento, categoria, subcategoria, "Ativo"]
    produtos.append(produto)
    print ("Produto cadastrado.")

def listar_produtos():
    if len(produtos) == 0:
        print ("Nao existem produtos cadastrados.")
    else:
        for produto in produtos:
            print (produto)

def pesquisar_produto():
    codigo = input ("Digite o codigo do produto: ")
    encontrado = False

    for produto in produtos:
        if produto[0] == codigo:
            print (produto)
            encontrado = True
    if encontrado == False:
        print ("Produto nao encontrado.")

def atualizar_produto():
    codigo = input("Codigo do produto que deseja atualizar: ")

    for produto in produtos:
        if produto[0] == codigo:
            produto[1] = input ("Novo nome: ")
            produto[2] = input ("Novo preco: ")
            produto[3] = input ("Novo departamento: ")
            produto[4] = input ("Nova categoria: ")
            produto[5] = input ("Nova subcategoria: ")
            produto[6] = input ("Status (Ativo/Inativo): ")
            print ("Produto atualizado.")
            return
    print ("Produto nao encontrado.")

def excluir_produto():
    codigo = input ("Codigo do produto que deseja excluir: ")
    for produto in produtos:
        if produto[0] == codigo:
            produtos.remove(produto)
            print ("Produto removido.")
            return
    print ("Produto nao encontrado.")

def menu_produtos():
    opcao = 0
    while opcao != 6:
        print ("1 - Cadastrar produto")
        print ("2 - Listar produtos")
        print ("3 - Pesquisar produto")
        print ("4 - Atualizar produto")
        print ("5 - Excluir produto")
        print ("6 - Voltar")
        opcao = input ("Escolha: ")
        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            pesquisar_produto()
        elif opcao == "4":
            atualizar_produto()
        elif opcao == "5":
            excluir_produto()

def cadastrar_pagamento():
    codigo = input ("Codigo do pagamento: ")
    cliente = input ("Nome do cliente: ")
    valor = input ("Valor: ")
    prioridade = input ("Prioridade (Normal/Alta): ")
    pagamento = [codigo, cliente, valor, prioridade, "Pendente"]
    pagamentos.put(pagamento)
    print ("Pagamento adicionado ao final da fila.")

def listar_pagamentos():
    if pagamentos.empty():
        print ("A fila de pagamentos esta vazia.")
        return
    temporaria = queue.Queue()
    while not pagamentos.empty():
        pagamento = pagamentos.get()
        print (pagamento)
        temporaria.put(pagamento)
    while not temporaria.empty():
        pagamentos.put(temporaria.get())

def processar_pagamento():
    if pagamentos.empty():
        print ("Nao existem pagamentos para processar.")
    else:
        pagamento = pagamentos.get()
        pagamento[4] = "Aprovado"
        print ("Pagamento processado:", pagamento)

def atualizar_pagamento():
    codigo = input ("Codigo do pagamento: ")
    temporaria = queue.Queue()
    encontrado = False
    while not pagamentos.empty():
        pagamento = pagamentos.get()
        if pagamento[0] == codigo:
            pagamento[1] = input ("Novo nome do cliente: ")
            pagamento[2] = input ("Novo valor: ")
            pagamento[3] = input ("Nova prioridade: ")
            encontrado = True
        temporaria.put(pagamento)
    while not temporaria.empty():
        pagamentos.put(temporaria.get())
    if encontrado:
        print ("Pagamento atualizado.")
    else:
        print ("Pagamento nao encontrado.")

def excluir_pagamento():
    codigo = input ("Codigo do pagamento que deseja excluir: ")
    temporaria = queue.Queue()
    encontrado = False
    while not pagamentos.empty():
        pagamento = pagamentos.get()
        if pagamento[0] == codigo and encontrado == False:
            encontrado = True
        else:
            temporaria.put(pagamento)
    while not temporaria.empty():
        pagamentos.put(temporaria.get())
    if encontrado:
        print ("Pagamento removido.")
    else:
        print ("Pagamento nao encontrado.")

def menu_pagamentos():
    opcao = ""
    while opcao != "6":
        print ("1 - Adicionar pagamento")
        print ("2 - Listar pagamentos")
        print ("3 - Processar proximo pagamento")
        print ("4 - Atualizar pagamento")
        print ("5 - Excluir pagamento")
        print ("6 - Voltar")
        opcao = input ("Escolha: ")
        if opcao == "1":
            cadastrar_pagamento()
        elif opcao == "2":
            listar_pagamentos()
        elif opcao == "3":
            processar_pagamento()
        elif opcao == "4":
            atualizar_pagamento()
        elif opcao == "5":
            excluir_pagamento()

def adicionar_historico():
    pagina = input ("Digite o produto ou pagina visitada: ")
    historico.append(pagina)
    print ("Pagina adicionada ao historico.")

def listar_historico():
    if len(historico) == 0:
        print ("Historico vazio.")
    else:
        print ("Historico (mais recente primeiro):")
        for i in range(len(historico) - 1, -1, -1):
            print (historico[i])

def voltar_pagina():
    if len(historico) == 0:
        print ("Nao existe pagina para voltar.")
    else:
        pagina = historico.pop()
        print ("Voltando da pagina:", pagina)

def menu_historico():
    opcao = ""
    while opcao != "4":
        print ("1 - Visitar pagina")
        print ("2 - Consultar historico")
        print ("3 - Voltar (remover ultima pagina)")
        print ("4 - Voltar ao menu principal")
        opcao = input ("Escolha: ")
        if opcao == "1":
            adicionar_historico()
        elif opcao == "2":
            listar_historico()
        elif opcao == "3":
            voltar_pagina()

def cadastrar_na_arvore():
    departamento = input ("Departamento: ")
    categoria = input ("Categoria: ")
    subcategoria = input ("Subcategoria: ")
    if departamento not in arvore:
        arvore[departamento] = {}
    if categoria not in arvore[departamento]:
        arvore[departamento][categoria] = {}
    if subcategoria not in arvore[departamento][categoria]:
        arvore[departamento][categoria][subcategoria] = {}
        print ("Categoria adicionada a arvore.")
    else:
        print ("Essa subcategoria ja existe.")

def listar_arvore():
    if len(arvore) == 0:
        print ("A arvore esta vazia.")
    else:
        for departamento in arvore:
            print (departamento)
            for categoria in arvore[departamento]:
                print ("  ", categoria)
                for subcategoria in arvore[departamento][categoria]:
                    print ("     ", subcategoria)

def pesquisar_arvore():
    departamento = input ("Departamento: ")
    categoria = input ("Categoria: ")
    subcategoria = input ("Subcategoria: ")
    if departamento in arvore:
        if categoria in arvore[departamento]:
            if subcategoria in arvore[departamento][categoria]:
                print ("Subcategoria encontrada na arvore.")
                return
    print ("Caminho nao encontrado.")

def atualizar_arvore():
    print ("1 - Renomear departamento")
    print ("2 - Renomear categoria")
    print ("3 - Renomear subcategoria")
    opcao = input ("Escolha: ")
    if opcao == "1":
        antigo = input ("Nome atual do departamento: ")
        if antigo in arvore:
            novo = input ("Novo nome: ")
            arvore[novo] = arvore.pop(antigo)
            print ("Departamento atualizado.")
        else:
            print ("Departamento nao encontrado.")
    elif opcao == "2":
        departamento = input ("Departamento: ")
        antigo = input ("Categoria atual: ")
        if departamento in arvore and antigo in arvore[departamento]:
            novo = input ("Novo nome: ")
            arvore[departamento][novo] = arvore[departamento].pop(antigo)
            print ("Categoria atualizada.")
        else:
            print ("Categoria nao encontrada.")
    elif opcao == "3":
        departamento = input ("Departamento: ")
        categoria = input ("Categoria: ")
        antigo = input ("Subcategoria atual: ")
        if departamento in arvore and categoria in arvore[departamento]:
            if antigo in arvore[departamento][categoria]:
                novo = input ("Novo nome: ")
                arvore[departamento][categoria][novo] = arvore[departamento][categoria].pop(antigo)
                print ("Subcategoria atualizada.")
            else:
                print ("Subcategoria nao encontrada.")
        else:
            print ("Caminho nao encontrado.")

def excluir_arvore():
    print ("1 - Excluir departamento")
    print ("2 - Excluir categoria")
    print ("3 - Excluir subcategoria")
    opcao = input ("Escolha: ")
    if opcao == "1":
        departamento = input ("Departamento: ")
        if departamento in arvore:
            del arvore[departamento]
            print ("Departamento e seus descendentes removidos.")
        else:
            print ("Departamento nao encontrado.")
    elif opcao == "2":
        departamento = input ("Departamento: ")
        categoria = input ("Categoria: ")
        if departamento in arvore and categoria in arvore[departamento]:
            del arvore[departamento][categoria]
            print ("Categoria e suas subcategorias removidas.")
        else:
            print ("Categoria nao encontrada.")
    elif opcao == "3":
        departamento = input ("Departamento: ")
        categoria = input ("Categoria: ")
        subcategoria = input ("Subcategoria: ")
        if departamento in arvore and categoria in arvore[departamento]:
            if subcategoria in arvore[departamento][categoria]:
                del arvore[departamento][categoria][subcategoria]
                print ("Subcategoria removida.")
            else:
                print ("Subcategoria nao encontrada.")
        else:
            print ("Caminho nao encontrado.")

def menu_arvore():
    opcao = ""
    while opcao != "6":
        print ("1 - Cadastrar departamento/categoria/subcategoria")
        print ("2 - Listar arvore")
        print ("3 - Pesquisar caminho")
        print ("4 - Atualizar nome")
        print ("5 - Excluir nivel")
        print ("6 - Voltar")
        opcao = input ("Escolha: ")
        if opcao == "1":
            cadastrar_na_arvore()
        elif opcao == "2":
            listar_arvore()
        elif opcao == "3":
            pesquisar_arvore()
        elif opcao == "4":
            atualizar_arvore()
        elif opcao == "5":
            excluir_arvore()

def salvar_dados():
    arquivo = open(ARQUIVO, "w", encoding="utf-8")
    for produto in produtos:
        arquivo.write("LISTA|" + "|".join(produto) + "\n")
    temporaria = queue.Queue()
    while not pagamentos.empty():
        pagamento = pagamentos.get()
        arquivo.write("FILA|" + "|".join(pagamento) + "\n")
        temporaria.put(pagamento)
    while not temporaria.empty():
        pagamentos.put(temporaria.get())
    for pagina in historico:
        arquivo.write("PILHA|" + pagina + "\n")
    for departamento in arvore:
        for categoria in arvore[departamento]:
            for subcategoria in arvore[departamento][categoria]:
                arquivo.write("ARVORE|" + departamento + "|" + categoria + "|" + subcategoria + "\n")
    arquivo.close()
    print ("Dados salvos em", ARQUIVO)

def carregar_dados():
    produtos.clear()
    while not pagamentos.empty():
        pagamentos.get()
    historico.clear()
    arvore.clear()
    try:
        arquivo = open(ARQUIVO, "r", encoding="utf-8")
        for linha in arquivo:
            dados = linha.strip().split("|")
            if dados[0] == "LISTA" and len(dados) == 8:
                produtos.append(dados[1:])
            elif dados[0] == "FILA" and len(dados) == 6:
                pagamentos.put(dados[1:])
            elif dados[0] == "PILHA" and len(dados) == 2:
                historico.append(dados[1])
            elif dados[0] == "ARVORE" and len(dados) == 4:
                departamento = dados[1]
                categoria = dados[2]
                subcategoria = dados[3]
                if departamento not in arvore:
                    arvore[departamento] = {}
                if categoria not in arvore[departamento]:
                    arvore[departamento][categoria] = {}
                arvore[departamento][categoria][subcategoria] = {}
        arquivo.close()
        print ("Dados carregados.")
    except FileNotFoundError:
        print ("Arquivo ainda nao existe. O sistema iniciara vazio.")

def menu_principal():
    opcao = ""
    while opcao != "7":
        print ("1 - Catalogo de produtos (Lista)")
        print ("2 - Pagamentos (Fila)")
        print ("3 - Historico de navegacao (Pilha)")
        print ("4 - Departamentos e categorias (Arvore)")
        print ("5 - Salvar dados (arquivo proprio txt)")
        print ("6 - Carregar dados")
        print ("7 - Encerrar")
        opcao = input ("Escolha uma das opcoes: ")
        if opcao == "1":
            menu_produtos()
        elif opcao == "2":
            menu_pagamentos()
        elif opcao == "3":
            menu_historico()
        elif opcao == "4":
            menu_arvore()
        elif opcao == "5":
            salvar_dados()
        elif opcao == "6":
            carregar_dados()
        elif opcao == "7":
            print ("Sistema encerrado.")
        else:
            print ("Opcao invalida.")

menu_principal()