import math

nbr = None
prng_final = []

def prng(seed, borne):
    global nbr
    global prng_final
    pass

    # création pi_list
    pi_lst = []
    for p in range(len(prng_final)+2):
        if str(math.pi)[p] != '.':
            pi_lst.append(int(str(math.pi)[p]))
    print(pi_lst)


    # délimitation des bornes
    bornes = []
    for i in range(1, borne+1):
        bornes.append(i)

    # nbr aléatoire ( à retravailler car pas assez random)
    pi_nbr = 0
    for i in (pi_lst[-3:]):
        pi_nbr += i
    nbr = pi_nbr*seed
    # attribution du prochain chiffre    
    while nbr > bornes[-1]:
        nbr /= 10
    nbr = int(nbr)
    prng_final.append(nbr)
    
    return nbr


seed = 47
borne = 50

print(prng(seed, borne))


# bornes = []
# for i in range(1, borne+1):
#     bornes.append(i)
#     
# print(bornes)
