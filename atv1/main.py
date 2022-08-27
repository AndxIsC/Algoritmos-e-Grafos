
#IMPORTANDO OS ARQUIVOS DO NECESSÁRIOS
import entry as ent
import save as sv

#=================================================================
# TO.DO: Implementar um protótipo de software com funções para: 
#       - entrada de dados.     
#       - saída dos resultados.
#=================================================================

# main
if __name__== "__main__":

    name = input('Digite o nome do arquivo: ')
    arq = ent.data_entry(name)
    print()
    print(arq)
    print()
    sv.save(name,arq)
  

    
    