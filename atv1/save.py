import dimensions as dim

# MOSTRAR O RESULTADO DESEJADO E SALVAR EM UM ARQUIVO
# 'results.txt' NA PASTA 'results'
# RECEBE 'name' REFERENTE AO NOME DA MATRIZ E A MATRIZ COMO PARÂMETROS
# RECEBE NÚMEROS DE COLUNAS E LINHAS ATRAVÉS DE FUNÇÕES IMPLEMENTADAS NO ARQUIVO ''dimensions.py
# CONCATENA O NOME + OS OUTROS DADOS E OS MOSTRA NA TELA
# E SALVA O ARQUIVO NO CAMINHO DESEJADO

def save(name,arq):
    rows = str(dim.numRows(arq))
    cols = str(dim.numCols(arq)) 
    result = ('Matriz '.upper() + name + ': Dimensao(linhas,colunas) = ' +  '(' + rows + ',' + cols + ')\n')
    print(result)
    file = open('results/results.txt', 'a')
    file.write(result)
    file.close
    