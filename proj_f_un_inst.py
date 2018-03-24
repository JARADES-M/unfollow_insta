import numpy as np

POSICOES = 7
MAX_TAM_NOME = 200
ultimas_sete = ""
nao_segue = 0
i, j = 0, 0

#Followers
nome_insta_ers = []
nome_user_ers = []
eu_sigo_ers = []

#Following
nome_insta_ing = []
nome_user_ing = []
eu_sigo_ing = []

temp_nome_lista_ers = ""
temp_nome_lista_ing = ""

##############################################################################
arq_followers = open('followers.txt', 'r')
txt_followers = arq_followers.read()

#Iteração para pegar e guardar os dados
for i, caracter in enumerate(txt_followers):
    #forma uma palavra com as últimas 7 posiçoes
    if i > 7:
        ultimas_sete = txt_followers[(i-7):i]
    
    if ultimas_sete == 'title=\"':
        # salvar da posição atual até o proximo (') em nome_insta_ers[]
        for j in range (i, (i+MAX_TAM_NOME)):
            if txt_followers[j] == '\"':
                temp_nome_lista_ers = txt_followers[i:j]
                if temp_nome_lista_ers != 'Verified':
                    nome_insta_ers.append(temp_nome_lista_ers)
                break
            
    elif ultimas_sete == '2uju6\">':
        # salvar da posição atual até o proximo (<) em nome_user_ers[]
        for j in range (i, (i+MAX_TAM_NOME)):
            if txt_followers[j] == '<':
                temp_nome_lista_ers = txt_followers[i:j]
                nome_user_ers.append(temp_nome_lista_ers)
                break
        
    elif ultimas_sete == 'rmr7s\">':
        # salvar da posição atual até o proximo (<) em eu_sigo_ers[]
        for j in range (i, (i+MAX_TAM_NOME)):
            if txt_followers[j] == '<':
                temp_nome_lista_ers = txt_followers[i:j]
                eu_sigo_ers.append(temp_nome_lista_ers)
                break    
    #------------------------------------------------------------------------#

# unir os vetores em uma matriz
# unidos_ers = np.column_stack((nome_insta_ers, nome_user_ers))#, eu_sigo_ers))

arq_followers.close()
##############################################################################

##############################################################################
arq_following = open('following.txt', 'r')
txt_following = arq_following.read()

#Iteração para pegar e guardar os dados
for i, caracter in enumerate(txt_following):
    #forma uma palavra com as últimas 7 posiçoes
    if i > 7:
        ultimas_sete = txt_following[(i-7):i]
    
    if ultimas_sete == 'title=\"':
        # salvar da posição atual até o proximo (') em nome_insta_ing[]
        for j in range (i, (i+MAX_TAM_NOME)):
            if txt_following[j] == '\"':
                temp_nome_lista_ing = txt_following[i:j]
                if temp_nome_lista_ing != 'Verified':
                    nome_insta_ing.append(temp_nome_lista_ing)
                break
            
    elif ultimas_sete == '2uju6\">':
        # salvar da posição atual até o proximo (<) em nome_user_ing[]
        for j in range (i, (i+MAX_TAM_NOME)):
            if txt_following[j] == '<':
                temp_nome_lista_ing = txt_following[i:j]
                nome_user_ing.append(temp_nome_lista_ing)
                break
        
    elif ultimas_sete == 'rmr7s\">':
        # salvar da posição atual até o proximo (<) em eu_sigo_ing[]
        for j in range (i, (i+MAX_TAM_NOME)):
            if txt_following[j] == '<':
                temp_nome_lista_ing = txt_following[i:j]
                eu_sigo_ing.append(temp_nome_lista_ing)
                break    
    #------------------------------------------------------------------------#

# unir os vetores em uma matriz
#unidos_ing = np.column_stack((nome_insta_ing, nome_user_ing))#, eu_sigo_ing))

arq_following.close()
##############################################################################
'''
for i, nome in enumerate(nome_insta_ing):
    print(nome, end="--")
    print(nome_user_ing[i])
    
print(nome_user_ing)
print(nome_insta_ing)
print(len(nome_insta_ing))
print(len(nome_user_ing))
print(len(eu_sigo_ing))
print(len(unidos_ers))
#print(unidos_ing)

# infoma a 'matriz de seguidores' e 'quem' da matriz de quem sigo
'''
def segue_de_volta(matriz_me_segue, quem_eu_sigo):
    return quem_eu_sigo in matriz_me_segue

arq = open('Nao_Seguidores.txt', 'w')

arq.write("____________________ NÃO TE SEGUE _____________________\n\n-------------------------------------------------------\n")
for user in nome_insta_ing:
    if not segue_de_volta(nome_insta_ers, user):
        nao_segue += 1
        arq.write(str(user) + "\n-------------------------------------------------------\n")
arq.write("\nTOTAL = " + str(nao_segue))
arq.write("\n________________________________________________________\n")
arq.close()
