import qcm 
from math import pi
from prng import prng_rep

if __name__ == '__main__':
    
    def quiz(qcm):

        print('''

        ---Qcm python---

        ''')
        
        while True:
            filename = input('''Choix du fichier: ''')
            print("")
            
            try :
                choix = []
                score = 0
                nmbr_de_questions = 0
                list_nmbr_choix= []

                # ---Chargement du questionnaire---

                questions = qcm.build_questionnaire(filename)

                for q in range(len(questions)):
                    
                    print("\tQuestion " + str(q+1) + ": \"" + questions[q][0] + "\"")

                    nmbr_de_choix = 0
                    nmbr_de_questions = nmbr_de_questions + 1

                    rep_list = prng_rep(23,len(questions[q][1]))
                    num_quest=1

                    for r in rep_list:
                        
                        r = r-1
                        print("\t\tReponses " + str(num_quest) + ":")
                        print("\t\t\t  '" + questions[q][1][r][0] + "\'")
                        nmbr_de_choix = nmbr_de_choix + 1
                        num_quest = num_quest + 1

                    while True:
                        user_input = input("\t\t Choix: ").split("-")
                        is_correct = True
                        for words in user_input:
                            if words.isnumeric(): #regarde si c'est numéro 
                                if 0 < int(words) < nmbr_de_choix+1: #regarde si dans les bornes 
                                    continue  
                                else:
                                    print(f"\t\t\t'{user_input}' n'est pas une réponse valide")
                                    is_correct = False
                                    break   
                            else:
                                print(f"\t\t\t'{user_input}' n'est pas un numéro")
                                is_correct = False
                                break
                        if is_correct:
                            for num in range(len(user_input)):
                                user_input[num] = int(user_input[num])
                            
                            choix.append(user_input)
                            break

                    list_nmbr_choix.append(nmbr_de_choix)
                    
            
                #---Choix de la cotation---
                print('''
\t\t\t Type de cotation:
\t\t\t
\t\t\t En cas de question à choix multiple toutes les réponses correctes 
\t\t\t sont demandées pour avoir le point
\t\t\t
\t\t\t (1) +1 -0
\t\t\t (2) +1 -1
\t\t\t (3) +1 -0.5 (si score négatif ->0)
\t\t\t 
\t\t\t Pour choisir plusieurs types de cotation vous pouvez
\t\t\t mettre plusieurs numéros (ex: 1-2-3 , 3-2 , 1-3) 
                ''')

                list_choix_cotation = ["1","2","3"]

                while True:

                    cotation = input("\t\t\t Choix:").split("-")
                    
                    is_correct = True

                    for h in cotation:
                        
                        if h.isnumeric(): #regarde si un numéro 
                            if h in list_choix_cotation: #regarde si dans les bornes  
                                continue  
                            else:
                                print(f"\t\t\t'{user_input}' n'est pas une réponse valide")
                                is_correct = False
                                break  
                        else:
                            print(f"\t\t\t'{user_input}' n'est pas un numéro")
                            is_correct = False
                            break
                        
                    if is_correct:
                        break
                        
                    
                #----vérification des réponses------

                #Premier système de cotation
                        
                def cotation1(choix,questions,score):
                    
                    for z in range(len(choix)):

                        rep_correct = 0
                        count_right = 0

                        good = True

                        #compteur de réponse correct a la question
                        for right in range(int(list_nmbr_choix[z])):
                            if questions[z][1][right][1]:
                                count_right = count_right + 1

                        #compteur du nombre de réponse correct donné par l'utilisateur
                        for a in choix[z]:
                            if questions[z][1][(a-1)][1]:
                                rep_correct = rep_correct + 1
                            else:   
                                good = False
                                break
                    
                        #le nombre de rep correct et le nombre de rep correct donné
                        # par l'utilisateur doivent être les mêmes pour recevoir le point
                        if rep_correct == count_right and good == True:
                            score = score + 1
                            
                        else:#si un des choix est faux pas de changement de score
                            score = score
                                                        
                    return(f"\t\t\t (1) Score de {score}/{nmbr_de_questions}")

                
                #deuxième système de cotation     
                def cotation2(choix,questions,score):
                    for z in range(len(choix)):

                        rep_correct = 0
                        count_right = 0

                        good = True

                        #compteur de réponse correct a la question
                        for right in range(int(list_nmbr_choix[z])):
                            if questions[z][1][right][1]:
                                count_right = count_right + 1

                    

                        #compteur du nombre de réponse correct donné par l'utilisateur
                        for a in choix[z]:
                            if questions[z][1][(a-1)][1]:
                                rep_correct = rep_correct + 1
                            else:   
                                good = False
                                break
                    

                        #le nombre de rep correct et le nombre de rep correct donné
                        # par l'utilisateur doivent être les mêmes pour recevoir le point
                        if rep_correct == count_right and good == True:
                            score = score + 1
                            
                        else:#si un des choix est faux pas de changement de score
                            score = score - 1
                                                        
                    return(f"\t\t\t (2) Score de {score}/{nmbr_de_questions}")

                
                #troisième système de cotation
                def cotation3(choix,questions,score,list_nmbr_choix):

                    for z in range(len(choix)):

                        rep_correct = 0
                        count_right = 0

                        good = True

                        #compteur de réponse correct a la question
                        for right in range(int(list_nmbr_choix[z])):
                            if questions[z][1][right][1]:
                                count_right = count_right + 1

                    

                        #compteur du nombre de réponse correct donné par l'utilisateur
                        for a in choix[z]:
                            if questions[z][1][(a-1)][1]:
                                rep_correct = rep_correct + 1
                            else:   
                                good = False
                                break
                    

                        #le nombre de rep correct et le nombre de rep correct donné
                        # par l'utilisateur doivent être les mêmes pour recevoir le point
                        if rep_correct == count_right and good == True:
                            score = score + 1
                            
                        else:#si un des choix est faux pas de changement de score
                            score = score - 0.5

                    if score > 0:                                    
                        return(f"\t\t\t (3) Score de {score}/{nmbr_de_questions}")
                    else:
                        return(f"\t\t\t (3) Score de 0/{nmbr_de_questions}")

                #Choix du type de cotation
                if "1" in cotation:
                    print(cotation1(choix,questions,score))

                if "2" in cotation:
                    print(cotation2(choix,questions,score))
                
                if "3" in cotation:
                    print(cotation3(choix,questions,score,list_nmbr_choix))

                #choix après la fin du quizz (menu,restart,quit)
                print('''
\t\t\t Continue?
\t\t\t
\t\t\t(1) menu
\t\t\t(2) Restart
\t\t\t(3) Quit     
                ''')

                while True:
                    choix_end_game = input("\t\t Choix: ")

                    is_correct = True
                    
                    if choix_end_game.isnumeric(): #regarde si c'est numéro 
                        if 0 < int(choix_end_game) < 4: #regarde si dans les bornes 
                            break 
                        else:
                            print(f"\t\t\t'{choix_end_game}' n'est pas une réponse valide")
                            is_correct = False      
                    else:
                        print(f"\t\t\t'{choix_end_game}' n'est pas un numéro")
                        is_correct = False

                if is_correct:
                    if "1" in choix_end_game:
                        main_menu()
                    if "2" in choix_end_game:
                        quiz(qcm)
                    if "3" in choix_end_game:
                        quit()

            except:
                print("ERROR : not a valid file")


    #afficher les instructions
    def instructions(): 
        print('''
\t\t\t Instruction :
\t\t\t 
\t\t\t Réponse:
\t\t\t
\t\t\t Réponse unique: chiffre seul
\t\t\t ex: 1 ,3
\t\t\t 
\t\t\t Réponse à choix multiple: séparer la réponse par un tiret "-"
\t\t\t ex: 1-3-4
\t\t\t 
\t\t\t Cotation:
\t\t\t 
\t\t\t En cas de question à choix multiple toutes les réponses correctes 
\t\t\t sont demandées pour avoir le point
\t\t\t
\t\t\t (1) +1 -0 (cotation normalle)
\t\t\t +1 Pour une bonne réponse
\t\t\t -0 si toutes les bonnes réponses ne sont pas choisies ou si un des choix est faux
\t\t\t 
\t\t\t (2) +1 -1 (cotation dure)
\t\t\t +1 Pour une bonne réponse
\t\t\t -1 si toutes les bonnes réponses ne sont pas choisies ou si un des choix est faux
\t\t\t 
\t\t\t (3) +1 -0.5 (cotation intermédiaire) 
\t\t\t +1 Pour une bonne réponse
\t\t\t -0.5 si toutes les bonnes réponses ne sont pas choisies ou si un des choix est faux
\t\t\t Attention : si le score est négatif la note de 0 sera attribuée
\t\t\t 
\t\t\t Pour choisir plusieurs types de cotation vous pouvez
\t\t\t mettre plusieurs numéros (ex: 1-2-3 , 3-2 , 1-3) 
        ''') 

        #retour au menu
        main_menu()

    #menu du programme
    def main_menu():

        #main menu
        print('''
\t\t\t (1) Lancer le QCM
\t\t\t (2) instructions
\t\t\t (3) Quit
\t\t\t 
        ''')

        #user input choix entre 1,2 ou 3(lancer le quizz, instructions, quit)
        while True:
            choix_menu = input("\t\t Choix: ")

            is_correct = True
            
            if choix_menu.isnumeric(): #regarde si c'est numéro 
                if 0 < int(choix_menu) < 4: #regarde si dans les bornes 
                    break 
                else:
                    print(f"\t\t\t'{choix_menu}' n'est pas une réponse valide")
                    is_correct = False      
            else:
                print(f"\t\t\t'{choix_menu}' n'est pas un numéro")
                is_correct = False

        if is_correct:
            if "1" in choix_menu:
                quiz(qcm)
            if "2" in choix_menu:
                instructions()
            if "3" in choix_menu:
                quit()

    #logo du programme
    def logo():
        print('''
-------------------------------------------------------------

██████╗ ██╗   ██╗████████╗██╗  ██╗ ██████╗ ███╗   ██╗
██╔══██╗╚██╗ ██╔╝╚══██╔══╝██║  ██║██╔═══██╗████╗  ██║
██████╔╝ ╚████╔╝    ██║   ███████║██║   ██║██╔██╗ ██║
██╔═══╝   ╚██╔╝     ██║   ██╔══██║██║   ██║██║╚██╗██║
██║        ██║      ██║   ██║  ██║╚██████╔╝██║ ╚████║
╚═╝        ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
                                                     
 ██████╗  ██████╗███╗   ███╗                         
██╔═══██╗██╔════╝████╗ ████║                         
██║   ██║██║     ██╔████╔██║                         
██║▄▄ ██║██║     ██║╚██╔╝██║                         
╚██████╔╝╚██████╗██║ ╚═╝ ██║                         
 ╚══▀▀═╝  ╚═════╝╚═╝     ╚═╝                         
                                                     
                             
-------------------------------------------------------------''')


    #---Lancement du programme---

    logo()
    main_menu()
