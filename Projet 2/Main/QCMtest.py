import qcm 

if __name__ == '__main__':
    filename = 'QCM2.txt'

    choix = []
    score = 0
    nmbr_de_questions = 0
    
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
            #print(nmbr_de_choix)
            
        while True:
            print("")
            user_input = input("\t\t Choix: ")
            if user_input.isnumeric(): #regarde si un numéro 
                if int(user_input) < nmbr_de_choix+1: #regarde si dans les bornes
                    choix.append(user_input) 
                    break  
                else:
                    print(f"\t\t\t'{user_input}' n'est pas une réponse valide")    
            else:
                print(f"\t\t\t'{user_input}' n'est pas un numéro")
                
    #print(choix)
                
    #Choix de la cotation
    print('''
\t\t\t Type de cotation:
\t\t\t (1) +1 -0
\t\t\t (2) +1 -1
\t\t\t (3) indeterminé
''')
    
    while True:
        cotation = input("\t\t\t Choix:")
        if cotation.isnumeric(): #regarde si un numéro 
            if int(cotation) < 4: #regarde si dans les bornes  
                break  
            else:
                print(f"\t\t\t'{user_input}' n'est pas une réponse valide")    
        else:
            print(f"\t\t\t'{user_input}' n'est pas un numéro")
        


        
    #vérification des réponses

    #Premier système de cotation
    if int(cotation) == 1:
        for z in range(len(choix)):
                
            if questions[z][1][(int(choix[z])-1)][1]:
                    
                score = score + 1
                               
        print(f"\t\t\t Score de {score}/{nmbr_de_questions}")

    #deuxième système de cotation   
    elif int(cotation) == 2:
        for z in range(len(choix)):  
            if questions[z][1][(int(choix[z])-1)][1]:
                score = score + 1
            else:
                score = score - 1     
        print(f"\t\t\t Score de {score}/{nmbr_de_questions}")

    #troisième système de cotation
    elif int(cotation) == 3:
        print("en cours...")
            
           
