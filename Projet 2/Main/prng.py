from math import pi

def prng_rep(seed, borne):
    nbr = None
    global prng_final
    prng_final = []
    pi_lst = []

    def prng(seed, borne):
        global nbr
        
        global pi_lst
        pass

    #   création pi_list
        pi_lst = []
        for p in range(4+len(prng_final)):
            if str(pi)[p] != '.':
                pi_lst.append(int(str(pi)[p]))
        # print(pi_lst)

    #   délimitation des bornes
        bornes = []
        for i in range(1, borne+1):
            bornes.append(i)

    #   nbr aléatoire
        pi_nbr = 0
        for i in (pi_lst[-2:]):
            pi_nbr += i
        if len(prng_final) == 0:
            nbr = pi_nbr*seed
        else:
            nbr = pi_nbr*pi_lst[-1]*seed

            
    #   attribution du prochain chiffre    
        while nbr > bornes[-1]:
            nbr -= borne
        nbr = int(nbr)
        
        
        prng_final.append(nbr)
        return(nbr)

    seed2 = seed
    borne2 = borne
    nbr_gen = 14
    while len(prng_final) != nbr_gen:
        print(prng(seed2, borne2))
    prng_final = list(dict.fromkeys(prng_final))
    
    return prng_final


print(prng_rep(41,5))
