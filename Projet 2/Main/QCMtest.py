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

        list_nmbr_choix.append(nmbr_de_choix)

           
    #print(choix)
                
    #Choix de la cotation
    print('''
\t\t\t Type de cotation:
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
        
    

        
    #vérification des réponses

    #Premier système de cotation
    def cotation1(choix,questions,score):
        for z in range(len(choix)):
                
            if questions[z][1][(int(choix[z])-1)][1]:
                    
                score = score + 1
                               
        return(f"\t\t\t (1) Score de {score}/{nmbr_de_questions}")

    #deuxième système de cotation     
    def cotation2(choix,questions,score):
        for z in range(len(choix)):  
            if questions[z][1][(int(choix[z])-1)][1]:
                score = score + 1
            else:
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
            
           
