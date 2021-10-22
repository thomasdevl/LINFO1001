import qcm 

if __name__ == '__main__':
    

    def quiz(qcm):
        filename = '/Users/thomasdevlamminck/Documents/UNIF/Project en info /Projet 2/LibrairieLectureFichierQCM/Main/QCM2.txt'
        #filename = 'QCM2.txt'

        choix = []
        score = 0
        nmbr_de_questions = 0
        list_nmbr_choix= []

        # Chargement du questionnaire
        questions = qcm.build_questionnaire(filename)

        for q in range(len(questions)):
            
            print("\tQuestion " + str(q+1) + ": \"" + questions[q][0] + "\"")

            nmbr_de_choix = 0
            nmbr_de_questions = nmbr_de_questions + 1
            
            for r in range(len(questions[q][1])):
                print("\t\tReponses " + str(r+1) + ":")
                print("\t\t\t  '" + questions[q][1][r][0] + "\'")
                nmbr_de_choix = nmbr_de_choix + 1

                
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
            

            
        #print(choix)
                    
        #Choix de la cotation
        print('''
\t\t\t Type de cotation:
\t\t\t
\t\t\t En cas de question à choix multiple toutes les réponses correct 
\t\t\t sont demandées pour avoir le point
\t\t\t
\t\t\t (1) +1 -0
\t\t\t (2) +1 -1
\t\t\t (3) +1 -1/par le nombre de question fausse
\t\t\t 
\t\t\t Pour choisir plusieurs type de cotation vous pouvez
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
                
        
        #print(list_nmbr_choix)
            
        #vérification des réponses

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
                if questions[z][1][(int(choix[z])-1)][1]:
                    score = score + 1
                else:
                    #  - 1/ par le nombre de question fausse 
                    score = score - (1/(list_nmbr_choix[z]-1))
            return(f"\t\t\t (3) Score de {round(score,1)}/{nmbr_de_questions}")


        #Choix du type de cotation
        if "1" in cotation:
            print(cotation1(choix,questions,score))

        if "2" in cotation:
            print(cotation2(choix,questions,score))
        
        if "3" in cotation:
            print(cotation3(choix,questions,score,list_nmbr_choix))

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
\t\t\t En cas de question à choix multiple toutes les réponses correct 
\t\t\t sont demandées pour avoir le point
\t\t\t
\t\t\t (1) +1 -0 (cotation normal)
\t\t\t +1 Pour une bonne réponse
\t\t\t -0 si pas toutes les bonnes réponses sont choisient ou si il y a un choix faux
\t\t\t 
\t\t\t (2) +1 -1 (cotation dur)
\t\t\t +1 Pour une bonne réponse
\t\t\t -1 si pas toutes les bonnes réponses sont choisient ou si il y a un choix faux
\t\t\t 
\t\t\t (3) en cours.....
\t\t\t 
\t\t\t Pour choisir plusieurs type de cotation vous pouvez
\t\t\t mettre plusieurs numéros (ex: 1-2-3 , 3-2 , 1-3) 
        ''') 

        #retour au menu
        main_menu()


    def main_menu():

        #main menu
        print('''
\t\t\t (1) Lancer le QCM
\t\t\t (2) instructions
\t\t\t (3) Quit
\t\t\t 
        ''')

        #user input choix entre 1,2 ou 3
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


    def logo():
        print('''
-------------------------------------------------------------
 ____    __    __  ______  __  __  _____   __  __           
/\  _`\ /\ \  /\ \/\__  _\/\ \/\ \/\  __`\/\ \/\ \          
\ \ \L\ \ `\`\\/'/\/_/\ \/\ \ \_\ \ \ \/\ \ \ `\\ \         
 \ \ ,__/`\ `\ /'    \ \ \ \ \  _  \ \ \ \ \ \ , ` \        
  \ \ \/   `\ \ \     \ \ \ \ \ \ \ \ \ \_\ \ \ \`\ \       
   \ \_\     \ \_\     \ \_\ \ \_\ \_\ \_____\ \_\ \_\      
    \/_/      \/_/      \/_/  \/_/\/_/\/_____/\/_/\/_/      
                                                            
                                                            
 _____   ____                                               
/\  __`\/\  _`\    /'\_/`\                                  
\ \ \/\ \ \ \/\_\ /\      \                                 
 \ \ \ \ \ \ \/_/_\ \ \__\ \                                
  \ \ \\'\\ \ \L\ \\ \ \_/\ \                               
   \ \___\_\ \____/ \ \_\\ \_\                              
    \/__//_/\/___/   \/_/ \/_/                              
                                                            
-------------------------------------------------------------''')



    logo()
    main_menu()
