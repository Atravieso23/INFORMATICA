def obtenerLista(lstA):
    l=[]
    for linea in lstA:
        linea=linea[:-1]
        datos=linea.split(",")
        l.append(datos)
    return l

def fun1t1(anInf,anSup):
    lsArch=["club,jugador,partidos,minutos,goles,tiros,año\n","(JUV),Cristiano Ronaldo,29,2634,25,162,2016\n","(PSG),Neymar,30,2694,13,105,2016\n","(BAR),Lionel Messi,32,2910,37,179,2016\n","(RMA),Eden Hazard,36,3101,16,77,2016\n","(TOT),Dele Alli,35,3182,18,95,2016\n","(BAR),Lionel Messi,32,3123,33,197,2017\n","(JUV),Cristiano Ronaldo,27,2375,26,178,2017\n","(BAR),Lionel Messi,29,2049,36,170,2018\n","(JUV),Cristiano Ronaldo,30,2857,21,177,2018\n","(PSG),Angel di Maria,28,2418,12,97,2018\n","(PSG),Neymar,16,1517,15,34,2018\n","(RMA),Eden Hazard,32,3115,16,93,2018\n","(PSG),Angel di Maria,23,2106,8,74,2019\n","(JUV),Cristiano Ronaldo,5,197,8,26,2020\n"]
    maxtiros=0
    lst=obtenerLista(lsArch)
    for i in range (1,len(lst)):
        anio=int(lst[i][6])
        tiros=int(lst[i][5])
        if anio>=anInf and anio<=anSup and tiros>maxtiros:
            maxtiros=tiros
            club=lst[i][0]
            maxanio=anio
    if maxtiros!=0:
        dic= {lst[0][6]:maxanio,lst[0][0]:club,lst[0][5]:maxtiros}
    else:
        dic={}
    return dic
            
    

def main():
    print(fun1t1(2016,2020))
    print(fun1t1(2010,2016))
    print(fun1t1(2020,2020))
    print(fun1t1(2025,2029))
main()
