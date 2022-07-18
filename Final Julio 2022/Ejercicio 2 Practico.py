def cargar(lst):
    for i in range(len(lst)):
        lst[i]=(lst[i][:-1]).split(',')
    return lst
def ordenar (lst):    
    for j in range (0,len(lst)-1):
        for m in range(j+1,(len(lst))):
            if lst[j][1] < lst[m][1]:
                aux=lst[m]
                lst[m]=lst[j]
                lst[j]=aux
    return lst
def fun2t1(n):
    lstArch= ["club, jugador, partidos, minutos, goles, tiros, anio\n", "(JUV), Cristiano Ronaldo, 29, 2634, 25, 162, 2016\n", "(PSG), Neymar, 30, 2694, 13, 105, 2016\n", "(BAR), Lionel Messi, 32, 2910, 37, 179, 2016\n", "(RMA), Eden Hazard, 36, 3101, 16, 77, 2016\n", "(TOT), Dele Alli, 35, 3182, 18, 95, 2016\n", "(BAR), Lionel Messi, 32, 3123, 33, 197, 2017\n", "(JUV), Cristiano Ronaldo, 27, 2375, 26, 178, 2017\n", "(BAR), Lionel Messi, 29, 2849, 36, 170, 2018\n", "(JUV), Cristiano Ronaldo, 30, 2857, 21, 177, 2018\n", "(PSG), Angel Di Maria, 28, 2418, 12, 97, 2018\n", "(PSG), Neymar, 16, 1517, 15, 54, 2018\n", "(MNU), Edinson Cavani, 20, 1845, 11, 54, 2018\n", "(RMA), Eden Hazard, 32, 3115, 16, 93, 2018\n", "(BAR), Lionel Messi, 32, 3067, 25, 159, 2019\n", "(JUV), Cristiano Ronaldo, 33, 3127, 31, 208, 2019\n", "(INT), Lautaro Martinez, 29, 2581, 14, 82, 2019\n", "(PSG), Neymar, 15, 1396, 12, 71, 2019\n", "(PSG), Angel Di Maria, 23, 2106, 8, 74, 2019\n", "(BAR), Lionel Messi, 6, 501, 10, 39, 2020\n", "(JUV), Cristiano Ronaldo, 5, 397, 8, 26, 2020\n"]
    lst=cargar(lstArch)
    lstfinal=[]
    for i in range (1,len(lst)):
        jugador=lst[i][1]
        cantmin=0
        for j in range (1,len(lst)):
            minutos=int(lst[j][3])
            if lst[j][1]==jugador:
                cantmin+=minutos
        if [jugador,cantmin] not in lstfinal:
                lstfinal.append([jugador,cantmin])
    ordenar(lstfinal)
    return lstfinal[:n]
            
def main():
    print(fun2t1(0))
    print(fun2t1(1))
    print(fun2t1(2))
    print(fun2t1(3))
    print(fun2t1(4))
main()   