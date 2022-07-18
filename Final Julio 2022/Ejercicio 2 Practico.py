def obtenerLista(lstA):
    l=[]
    for linea in lstA:
        linea=linea[:-1]
        datos=linea.split(",")
        l.append(datos)
    return l
def ordenar (lst):
    for i in range (0,(len(lst)-1)):
        for j in range (i+1,len(lst)):
            if lst[i] < lst[j]:
                aux=lst[j]
                lst[j]=lst[i]
                lst[i]=aux
    return lst
def fun2t1(n):
    lsArch=["club,jugador,partidos,minutos,goles,tiros,año\n","(JUV),Cristiano Ronaldo,29,2634,25,162,2016\n","(PSG),Neymar,30,2694,13,105,2016\n","(BAR),Lionel Messi,32,2910,37,179,2016\n","(RMA),Eden Hazard,36,3101,16,77,2016\n","(TOT),Dele Alli,35,3182,18,95,2016\n","(BAR),Lionel Messi,32,3123,33,197,2017\n","(JUV),Cristiano Ronaldo,27,2375,26,178,2017\n","(BAR),Lionel Messi,29,2049,36,170,2018\n","(JUV),Cristiano Ronaldo,30,2857,21,177,2018\n","(PSG),Angel di Maria,28,2418,12,97,2018\n","(PSG),Neymar,16,1517,15,34,2018\n","(RMA),Eden Hazard,32,3115,16,93,2018\n","(PSG),Angel di Maria,23,2106,8,74,2019\n","(JUV),Cristiano Ronaldo,5,197,8,26,2020\n"]
    lst=obtenerLista(lsArch)
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