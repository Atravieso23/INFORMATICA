def fun(t,a):
    i=len(t)
    while i < len(t) and t[i] > a:
        t[i]=a
        i+=1
    return t[:i]
def main():
    x=[10,20,30,40,50]
    x=fun(x,1)
    print(x)
main()