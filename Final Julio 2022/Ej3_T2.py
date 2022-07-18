def aMay(x):
    if x[0] in "abcdefghaijklmnñopqrstuvwxyz":
        x[0]= chr(ord(x[0])-32)
    return x
def fun(var):
    i=0
    while i<len(var):
        var[i]=aMay(var[i])
        i+=1
def main():
    miVar = ["belen","andres","diego"]
    fun(miVar)
    print(miVar)
main()