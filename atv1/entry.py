import numpy as np

# ENTRADA DE DADOS:
# RECEBE UMA STRING COMO PARÂMETRO, REFERENTE AO NOME DO ARQUIVO A SER BUSCADO, NA PASTA 'datasets'
# O MÉTODO 'numpy.loadtxt()' LÊ O ARQUIVO E RETORNA UMA MATRIZ DE INTEIROS
# RETORNA UMA MATRIZ
def data_entry(dataset):  
    caminho = 'datasets/' + dataset +'.txt' 
    file = open(caminho, "r")
    data = np.loadtxt(file, dtype=int)       
    file.close
    return data