def in_borne(prng,borne):  #vérifier si dans la borne
    
    for i in range(100):
        x = prng.next_int() 
    
        if x >= borne or x < 0:  #la valeur n'est pas dans la borne ou négative 
            return False
        
    return True


def check_seed(prng,borne,seed,PRNG):  #seed différent donne résultat diff
         
        for seed2 in range (50):
            
            if seed == seed2:
                pass
      
            if seed != seed2:
            
                prng2 = PRNG(seed2,borne)
                prng = PRNG(seed,borne)

                l1 = []
                l2 = []

                for i in range(50):
                    x=prng.next_int() 
                    l1.append(x)
                    y = prng2.next_int() 
                    l2.append(y)

                if l1 == l2:
                    return False

            return True
        
        
def global_num(prng,borne): #utiliser tous les numéros de la borne et +- une bonne moyenne entre tt 
   
    glob = []
    
    for i in range (borne): #creer une liste avec des zéros  
        glob.append(0)
    
    for i in range (300): #quand le numéro est tirer rajouter 1 a l'indice de ce numéro
        x = prng.next_int()
        glob[x] += 1  
        
    if 0 in glob: #si un des numéros de la liste est toujours a 0 revoyer False"
        return False

    return True


def is_correct(PRNG):
    
    for borne in range(20,100):
        for seed in range(100):
            
            prng = PRNG(seed, borne) #crée le PRNG pour chaque borne et chaque seed

            if not in_borne(prng,borne):
                return False

            if not check_seed(prng,borne,seed,PRNG): 
                return False

            if not global_num(prng,borne):
                return False

    return True

