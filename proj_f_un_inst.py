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
arq_followers = open('followers.txt', 'r', encoding='utf8')
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
arq_following = open('following.txt', 'r', encoding='utf8')
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

followers = set(nome_insta_ers)
following = set(nome_insta_ing)
non_followers = following - followers

arq = open('Nao_Seguidores.txt', 'w')
arq.write("____________________ NÃO TE SEGUE _____________________\n\n-------------------------------------------------------\n")

for user in non_followers:
    arq.write(str(user) + "\n-------------------------------------------------------\n")
    
arq.write("\nTOTAL = " + str(len(non_followers)))
arq.write("\n________________________________________________________\n")
arq.close()
