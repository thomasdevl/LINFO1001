import qcm 

if __name__ == '__main__':
    filename = 'QCM2.txt'

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
            print('''
\t\t\t Réponse unique: chiffre seul
\t\t\t ex: 1 ,3
\t\t\t 
\t\t\t Réponse à choix multiple: séparer la réponse par un tiret "-"
\t\t\t ex: 1-3-4
''')
            user_input = input("\t\t Choix: ").split("-")

            is_correct = True

            
            for words in user_input:
            
                if words.isnumeric(): #regarde si c'est numéro 
                    if int(words) < nmbr_de_choix+1: #regarde si dans les bornes 
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
\t\t\t mettre plusieurs numéros (ex: 123 , 32 , 13) 
''')

    list_choix_cotation = ["1","2","3"
                           ,"12","13","21","23","31","32"
                           ,"123","132","213","231","312","321"]
    
    while True:
        cotation = input("\t\t\t Choix:")
        if cotation.isnumeric(): #regarde si un numéro 
            if cotation in list_choix_cotation: #regarde si dans les bornes  
                break  
            else:
                print(f"\t\t\t'{user_input}' n'est pas une réponse valide")    
        else:
            print(f"\t\t\t'{user_input}' n'est pas un numéro")
        
    
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
            
           
