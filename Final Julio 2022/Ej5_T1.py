def fun(ls,va):
    i=0
    while i < len(ls):
        if va==ls[i]:
            ls.pop(i)
        else:
            i+=1
def main():
    lst=["a","b","x","x","c"]
    fun(lst,"x")
    print(lst)
main()

#Resuelto