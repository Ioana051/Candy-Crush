import random


def creaza_matrice(dimensiune):
    
    matrice = []
    
    # se va crea o matrice cu 11 randuri
    for i in range(dimensiune):
        
        # adauga un rand nou
        matrice.append([])
        
        # in acest rand adauga 11 elemente
        for j in range(dimensiune):
            
            gasit_element = False
            
            # incercam sa gasim un element care nu este in stanga sau deasupra
            while not gasit_element:
                element = random.randint(1,4)
                
                # daca nu suntem pe prima coloana
                if j >= 1:
                    if element != matrice[i][j-1]:
                        # daca nu suntem pe primul rand
                        if i >= 1:
                            if element != matrice[i-1][j]:
                                matrice[i].append(element)
                                gasit_element = True
                
                # daca suntem pe prima coloana, compara doar cu elementul de deasupra
                if j == 0 and i >= 1: 
                    if element != matrice[i-1][j]:
                                matrice[i].append(element)
                                gasit_element = True
                
                # daca suntem pe primul rand, compara doar cu elementul din stanga
                if i == 0 and j >= 1:
                    if element != matrice[i][j-1]:
                                matrice[i].append(element)
                                gasit_element = True
                
                # daca suntem pe prima pozitie din matrice, doar adauga un element random
                if i==0 and j==0:
                    matrice[i].append(element)
                    gasit_element = True
    
    return matrice


def afiseaza_matrice(matrice):
    # afiseaza matricea
    for i in range(len(matrice)):
        for j in range(len(matrice)):
            print(matrice[i][j], end="  ")
        print("\n")


def muta_element(matrice, pozitie_initiala, pozitie_finala):
    a = pozitie_initiala[0]
    b = pozitie_initiala[1]
    x = pozitie_finala[0]
    y = pozitie_finala[1]
    
    temp = matrice[a][b]
    matrice[a][b] = matrice[x][y]
    matrice[x][y] = temp
    
    return matrice


def cauta_linie(matrice, lungime):
    #sa returneze un flag si pozitia initiala si cea finala a elem
    
    for i in range(len(matrice)):
        for j in range(len(matrice)):
            
            ### Daca gasim doua elemente alaturate pe rand
            if j < len(matrice) - 1:
                if matrice[i][j]==matrice[i][j+1]:
                    #Pentru lungimea 5
                    if lungime == 5:
                        #daca suntem pe o coloana pe care ar fi posibila o mutare fara sa iesim din matrice
                        if j < len(matrice[i]) - 4:
                            # daca urmatoarele 2 sunt tot egale
                            if matrice[i][j+3] == matrice[j+4] == matrice[i][j]:
                                if i>0:
                                    #daca gasim un element potrivit pe linia de mai sus
                                    if matrice[i-1][j+2] == matrice[i][j]:
                                        return True, [(i - 1, j + 2), (i, j+2)]
                                
                                if i < len(matrice)-1:
                                    #daca gasim un element potrivit pe linia de mai jos
                                    if matrice[i+1][j+2] == matrice[i][j]:
                                        return False, [(i + 1, j + 2), (i, j+2)]
                                
                
                    #Pentru lungimea 4
                    if lungime == 4:
                        #daca nu iesim din matrice
                        if j < len(matrice) - 3:
                            #Cautam in dreapta daca al 4-lea element este bun
                            if matrice[i][j+3] == matrice[i][j]:
                                #daca gasim un element potrivit pe linia de mai sus
                                if i > 0:
                                    if matrice[i-1][j+2] == matrice[i][j]:
                                        return True, [(i - 1, j + 2), (i, j+2)]
                                
                                #daca gasim un element potrivit pe linia de mai jos
                                if i < len(matrice) - 1:
                                    if matrice[i+1][j+2] == matrice[i][j]:
                                        return False, [(i + 1, j + 2), (i, j+2)]
                        
                        
                            #Cautam in stanga
                            if j >= 3:
                                if matrice[i][j-2] == matrice[i][j]:
                                    #daca gasim un element potrivit pe linia de mai sus
                                    if i>0:
                                        if matrice[i-1][j-1] == matrice[i][j]:
                                            return True, [(i-1, j-1), (i, j-1)]
                                    
                                    if i < len(matrice[i]) - 1:
                                        #daca gasim un element potrivit pe linia de mai jos
                                        if matrice[i+1][j-1] == matrice[i][j]:
                                            return False, [(i + 1, j - 1), (i, j-1)]
                    
                    
                    #Pentru lungimea 3
                    if lungime == 3:
                        #daca nu iesim din matrice
                        if j < len(matrice) - 3:
                            #daca elementul din dreapta este bun
                            if matrice[i][j+3] == matrice[i][j]:
                                return True, [(i, j + 3), (i, j+2)]
                        
                        if j >= 2:
                            #daca elementul din stanga este bun
                            if matrice[i][j-2] == matrice[i][j]:
                                return True, [(i, j-2), (i, j-1)]
                        
                        if j <= len(matrice)-3:
                            if i>0:
                                #daca elementul din dreapta sus este bun
                                if matrice[i-1][j+2] == matrice[i][j]:
                                    return True, [(i-1, j+2), (i, j+2)]
                            
                            if i < len(matrice)-1:
                                #daca elementul din dreapta jos este bun
                                if matrice[i+1][j+2] == matrice[i][j]:
                                    return True, [(i+1, j+2), (i, j+2)]
                        
                        if j>0:
                            if i>0:
                                #daca elementul din stanga sus este bun
                                if matrice[i-1][j-1] == matrice[i][j]:
                                    return True, [(i-1, j-1), (i, j-1)]
                            
                            if i < len(matrice) - 1:
                                #daca elementul din stanga jos este bun
                                if matrice[i+1][j-1] == matrice[i][j]:
                                    return True, [(i+1, j-1), (i, j-1)]
            
            if lungime == 3:
                #Pentru linia de 3 exista varianta de a adauga un element in mijloc
                if j <= len(matrice) - 3:
                    if matrice[i][j] == matrice[i][j+2]:
                        if i>0:
                            if matrice[i-1][j+1] == matrice[i][j]:
                                return True, [(i-1, j+1), (i, j+1)]
                        
                        if i < len(matrice)-1:
                            if matrice[i+1][j+1] == matrice[i][j]:
                                return True, [(i+1, j+1), (i, j+1)]
            
            
            ### Daca gasim doua elemente alaturate pe coloana
            if i < len(matrice) - 1:
                if matrice[i][j] == matrice[i+1][j]:
                    
                    #Pentru lungime 5
                    if lungime == 5:
                        if i < len(matrice) - 4:
                            if matrice[i+3][j]==matrice[i+4][j]:
                                # Cautam in dreapta
                                if j < len(matrice)- 1:
                                    if matrice[i+2][j+1]== matrice[i][j]:
                                        return True, [(i+2, j+1), (i+2, j)]
                                
                                #Cautam in stanga
                                if j > 0:
                                    if matrice[i+2][j-1]== matrice[i][j]:
                                        return True, [(i+2, j-1), (i+2, j)]
                    
                    #Pentru lungime 4
                    if lungime == 4:
                        #Cautam in jos
                        if i < len(matrice) - 3:
                            if matrice[i+3][j]==matrice[i][j]:
                                # Cautam in dreapta
                                if j < len(matrice)- 1:
                                    if matrice[i+2][j+1]== matrice[i][j]:
                                        return True, [(i+2, j+1), (i+2, j)]
                                
                                #Cautam in stanga
                                if j > 0:
                                    if matrice[i+2][j-1]== matrice[i][j]:
                                        return True, [(i+2, j-1), (i+2, j)]
                        
                        #cautam in sus
                        if i>1:
                            if matrice[i-2][j]==matrice[i][j]:
                                # Cautam in dreapta
                                if j < len(matrice)- 1:
                                    if matrice[i-1][j+1]== matrice[i][j]:
                                        return True, [(i-1, j+1), (i-1, j)]
                                
                                #Cautam in stanga
                                if j > 0:
                                    if matrice[i-1][j-1]== matrice[i][j]:
                                        return True, [(i-1, j-1), (i-1, j)]
                    
                    if lungime == 3:
                        #cautam in jos
                        if i < len(matrice) - 3:
                            if matrice[i+3][j]== matrice[i][j]:
                                return True, [(i+3, j), (i+2, j)]
                            
                        #cautam in sus
                        if i > 1:
                            if matrice[i-2][j]== matrice[i][j]:
                                return True, [(i-2, j), (i-1, j)]
                            
                        
                        if i>0:
                            #cautam stanga sus
                            if j>0:
                                if matrice[i-1][j-1]== matrice[i][j]:
                                    return True, [(i-1, j-1), (i-1, j)]
                            
                            #cautam in dreapta sus
                            if j < len(matrice)-1:
                                if matrice[i-1][j+1]== matrice[i][j]:
                                    return True, [(i-1, j+1), (i-1, j)]
                        
                        
                        if i < len(matrice)-2:
                            #cautam stanga jos
                            if j>0:
                                if matrice[i+2][j-1]== matrice[i][j]:
                                    return True, [(i+2, j-1), (i+2, j)]
                            
                            #cautam dreapta jos
                            if j < len(matrice)-1:
                                if matrice[i+2][j+1]== matrice[i][j]:
                                    return True, [(i+2, j+1), (i+2, j)]
        
        
            #Pentru linia de 3 exista varianta de a adauga un element in mijloc
            if lungime == 3:
                if i <= len(matrice) - 3:
                    if matrice[i][j] == matrice[i+2][j]:
                        if j>0:
                            if matrice[i+1][j-1] == matrice[i][j]:
                                return True, [(i+1, j-1), (i+1, j)]
                        
                        if j < len(matrice)-1:
                            if matrice[i+1][j+1] == matrice[i][j]:
                                return True, [(i+1, j+1), (i+1, j)]
    
    return False, []



def cauta_L(matrice):
    # cauta L
    for i in range(len(matrice)):
        for j in range(len(matrice[i])-1):
            #daca gasim o linie de 2 elemente, cautam sa vedem daca avem un L
            if matrice[i][j] == matrice[i][j+1]:
                #Cauta stanga sus
                if j > 0 and i < len(matrice) - 2:
                    if matrice[i][j] == matrice[i+1][j-1]== matrice[i+2][j-1]:
                        if j > 1 and matrice[i][j] == matrice[i][j-2]:
                            return True, [(i, j-2), (i, j-1)]
                        
                        if i > 0 and matrice[i][j] == matrice[i-1][j-1]:
                            return True, [(i-1, j-1), (i, j-1)]
                
                #cauta dreapta sus
                if i < len(matrice) - 2 and j < len(matrice) - 2:
                    if matrice[i][j] == matrice[i+1][j+2]== matrice[i+2][j+2]:
                        if j < len(matrice) - 3 and matrice[i][j] == matrice[i][j+3]:
                            return True, [(i, j+3), (i, j+2)]
                        
                        if i >0 and matrice[i][j] == matrice[i-1][j+2]:
                            return True, [(i-1, j+2), (i, j+2)]
                
                #cauta stanga jos
                if j > 0 and  i > 1:
                    if matrice[i][j] == matrice[i-1][j-1] == matrice[i-2][j-1]:
                        if j > 1 and matrice[i][j] == matrice[i][j-2]:
                            return True, [(i, j-2), (i, j-1)]
                        
                        if i < len(matrice) - 1 and matrice[i][j] == matrice[i+1][j-1]:
                            return True, [(i+1, j-1), (i, j-1)]
                
                #cauta dreapta jos
                if j < len(matrice) - 2 and i > 1:
                    if matrice[i][j] == matrice[i-1][j+2] == matrice[i-2][j+2]:
                        if j < len(matrice) - 3 and matrice[i][j] == matrice[i][j+3]:
                            return True, [(i, j+3), (i, j+2)]
                        
                        if i < len(matrice) - 1 and matrice[i][j] == matrice[i+1][j+2]:
                            return True, [(i+1, j+2), (i, j+2)]
        
    return False, []



def cauta_T(matrice):
    
    for i in range(len(matrice)-1):
        for j in range(len(matrice[i])-1):
            #daca gasim o linie de 2 elemente, cautam sa vedem daca avem un T
            if matrice[i][j] == matrice[i][j+1]:
                if j < len(matrice) - 3 and i > 0 and matrice[i][j] == matrice[i-1][j+2] == matrice[i+1][j+2] == matrice[i][j+3]:
                    return True, [(i, j+3), (i, j+2)]
            
                if j > 1 and i > 0 and matrice[i][j] == matrice[i-1][j-1] == matrice[i+1][j-1] == matrice[i][j-2]:
                    return True, [(i, j-2), (i, j-1)]
                
            #daca gasim o coloana de 2 elemente, cautam sa vedem daca avem un T
            if matrice[i][j] == matrice[i+1][j]:
                if i < len(matrice) - 3 and j > 0  and matrice[i][j] == matrice[i+2][j-1] == matrice[i+2][j+1] == matrice[i+3][j]:
                    return True, [(i+3, j), (i+2, j)]
                
                if i > 1 and j > 0 and matrice[i][j] == matrice[i-1][j-1] == matrice[i-1][j+1] == matrice[i-2][j]:
                    return True, [(i-2, j), (i-1, j)]
    
    return False, []



def distruge_linie(matrice, pozitie, lungime):
    for i in range(pozitie[0], 0, -1):
        for j in range(pozitie[1], pozitie[1] + lungime):
                matrice[i][j] = matrice[i-1][j]
            
    for column in range(pozitie[1], pozitie[1] + lungime):
        matrice[0][column] = random.randint(1,4)
    
    return matrice


def distruge_coloana(matrice, pozitie, lungime):
    for i in range(pozitie[0] + lungime - 1, 0, -1):
        if i >= lungime:
            matrice[i][pozitie[1]] = matrice[i - lungime][pozitie[1]]
        else:
            matrice[i][pozitie[1]] = random.randint(1,4)
    matrice[0][pozitie[1]] = random.randint(1,4)
    return matrice


def distruge_bomboane(matrice, pozitie, mod, lungime, figura):
    
    i = pozitie[0]
    j = pozitie[1]
    
    if figura == "linie":
        if mod == "dreapta":
            matrice_noua = distruge_linie(matrice, pozitie, lungime)
            
        elif mod == "jos":
            matrice_noua = distruge_coloana(matrice, pozitie, lungime)
    
    
    elif figura == "L":
        matrice_noua = distruge_linie(matrice, pozitie, 3)
        
        if mod == "sus-dr":
            matrice_noua = distruge_coloana(matrice,[i - 1, j+2], 2)
        
        elif mod == "sus-st":
            matrice_noua = distruge_coloana(matrice,[i - 1, j], 2)
        
        elif mod =="jos-dr":
            matrice_noua = distruge_coloana(matrice,[i+1, j+2], 2)
        
        elif mod == "jos-st":
            matrice_noua = distruge_coloana(matrice,[i+1, j], 2)
    
    
    elif figura == "T":
        matrice_noua = distruge_linie(matrice, pozitie, 3)
        
        if mod == "sus":
            matrice_noua = distruge_coloana(matrice,[i-1, j+1], 2)
        elif mod == "jos":
            matrice_noua = distruge_coloana(matrice,[i, j+1], 2)
        elif mod == "stanga":
            matrice_noua = distruge_coloana(matrice,[i, j+2], 2)
        elif mod == "dreapta":
            matrice_noua = distruge_coloana(matrice,[i, j], 2)
    
    matrice = matrice_noua[:]
    return matrice


def verifica_bomboane(matrice):
    # ----------------------------------------------------------------- #
    # cauta linie de 5
    for i in range(len(matrice)):
            for j in range(len(matrice[i])):
                #luam linie de 5 elemente
                if j <= len(matrice) - 5:
                    linie = matrice[i][j:j+5]
                    #daca toate elementele sunt identice
                    if linie.count(matrice[i][j]) == len(linie):
                        return True, (i,j), "dreapta", 5, "linie"
                
                #luam coloana de '5' elemente
                if i <= len(matrice) - 5:
                    linie = [matrice[x][j] for x in range(i, i+5)]
                    if linie.count(matrice[i][j]) == len(linie):
                        return True, (i,j), "jos", 5, "linie"
    
    
    # ----------------------------------------------------------------- #
    # cauta T
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            if j < len(matrice) - 2:
                #daca gasim o linie de 3 elemente, cautam sa vedem daca avem un T
                if matrice[i][j] == matrice[i][j+1] == matrice[i][j+2]:
                    if i > 1:
                        # cauta deasupra
                        if matrice[i][j+1] == matrice[i-1][j+1] == matrice[i-2][j+1]:
                            return True, (i, j), "sus", 0, "T"
                    
                    if i >=1 and i < len(matrice) - 1:
                        #cauta in dreapta
                        if matrice[i][j] == matrice[i-1][j] == matrice[i+1][j]:
                            return True, (i, j), "dreapta", 0, "T" 
                        
                        #cauta in stanga
                        if matrice[i][j+2] == matrice[i-1][j+2] == matrice[i+1][j+2]:
                            return True, (i, j), "stanga", 0, "T" 
                    
                    
                    #cauta sub
                    if i < len(matrice) - 2:
                        if matrice[i][j+1] == matrice[i+1][j+1] == matrice[i+2][j+1]:
                            return True, (i, j), "jos", 0, "T"       
    
    
    # ----------------------------------------------------------------- #
    # cauta L
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            if j < len(matrice) - 2:
                #daca gasim o linie de 3 elemente, cautam sa vedem daca avem un L
                if matrice[i][j] == matrice[i][j+1] == matrice[i][j+2]:
                    if i > 1:
                        # cauta deasupra
                        if matrice[i][j] == matrice[i-1][j] == matrice[i-2][j]:
                            return True, (i, j), "sus-st", 0, "L"       
                        
                        if matrice[i][j+2] == matrice[i-1][j+2] == matrice[i-2][j+2]:
                            return True, (i, j), "sus-dr", 0, "L" 
                    
                    #cauta sub
                    if i < len(matrice) - 2:
                        if matrice[i][j] == matrice[i+1][j] == matrice[i+2][j]:
                            return True, (i, j), "jos-st", 0, "L"       
                        
                        if matrice[i][j+2] == matrice[i+1][j+2] == matrice[i+2][j+2]:
                            return True, (i, j), "jos-dr", 0, "L"
    
    
    # ----------------------------------------------------------------- #
    # cauta linii de 4 si 3
    for lungime in range(4, 2, -1):
        for i in range(len(matrice)):
            for j in range(len(matrice[i])):
                #luam linie de 'lungime' elemente
                if j <= len(matrice) - lungime:
                    linie = matrice[i][j:j+lungime]
                    #daca toate elementele sunt identice
                    if linie.count(matrice[i][j]) == len(linie):
                        return True, (i,j), "dreapta", lungime, "linie"
                
                #luam coloana de 'lungime' elemente
                if i <= len(matrice) - lungime:
                    linie = [matrice[x][j] for x in range(i, i+lungime)]
                    if linie.count(matrice[i][j]) == len(linie):
                        return True, (i,j), "jos", lungime, "linie"
    
    return False, (), "", 0, None



def crush(matrice):
    flag = True
    scor_total = 0
    # 0-T, 1-L, restul-dimensiunile liniilor
    scor={5:50, 0:30, 1:20, 4:10, 3:5}
    
    while flag:
        flag, pozitie, mod, lungime, figura = verifica_bomboane(matrice)
        if flag:
            # print(f"Gasit figura {figura} de {lungime} bomboane la pozitia {pozitie}")
            matrice_noua = distruge_bomboane(matrice, pozitie, mod, lungime, figura)
            
            matrice = matrice_noua[:]
            scor_total += scor[lungime]
            
    return matrice, scor_total


def main():
    
    dimensiune = 11
    scor_total = 0
    mutari_totale = 0
    flag = True
    numar_jocuri = 1
    
    for i in range(numar_jocuri):
        matrice = creaza_matrice(dimensiune)
        print("########### MATRICE_INITIALA #############")
        afiseaza_matrice(matrice)
        print("#########################################")
        scor_joc = 0
        
        while flag:
            # print(f"\nRunda noua: mutari {mutari_totale}\n")
            
            gasit, pozitii = cauta_L(matrice)
            if gasit:
                # print(f"Gasit L la pozitia {pozitii[0]} - {pozitii[1]}")
                matrice_noua = muta_element(matrice, pozitii[0], pozitii[1])
                mutari_totale += 1
                matrice = matrice_noua[:]
                matrice_noua, scor = crush(matrice)
                scor_joc += scor
                matrice = matrice_noua[:]
                continue
            
            
            gasit, pozitii = cauta_T(matrice)
            if gasit:
                # print(f"Gasit T la pozitia {pozitii[0]} - {pozitii[1]}")
                matrice_noua = muta_element(matrice, pozitii[0], pozitii[1])
                matrice = matrice_noua[:]
                matrice_noua, scor = crush(matrice)
                scor_joc += scor
                mutari_totale += 1
                matrice = matrice_noua[:]
                continue
            
            for i in range(5, 2, -1):
                gasit, pozitii = cauta_linie(matrice, i)
                if gasit:
                    # print(f"Gasit linie de {i} la pozitia {pozitii[0]} - {pozitii[1]}")
                    matrice_noua = muta_element(matrice, pozitii[0], pozitii[1])
                    matrice = matrice_noua[:]
                    matrice_noua, scor = crush(matrice)
                    scor_joc += scor
                    mutari_totale += 1
                    matrice = matrice_noua[:]
                    break
                else:
                    continue
            
            
            if not gasit:
                print("Nu mai sunt miscari posibile.")
                flag = False
                break
            
            
            if scor_joc >= 10000:
                print(f"Game over: scor-{scor_joc}, mutari-{mutari_totale}.")
                print("########### MATRICE_FINALA #############")
                afiseaza_matrice(matrice)
                scor_total += scor_joc
                flag = False
                break
    
    print(f"Am jucat {numar_jocuri} jocuri: score mediu {scor_total / numar_jocuri}, media mutarilor {mutari_totale / numar_jocuri}.")


if __name__ == "__main__":
    main()