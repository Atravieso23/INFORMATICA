def fun (data,k):
    for key in data.keys():
        if data[key] ==data.get(k):
            data[key]="***"
        elif data.get(k)!=None:
            data[key]="###"
def main():
    d={(22,"go"):"Google",(7,"aa") : "Apple",(18,"mi"): "Microsoft"}
    fun(d,(7))
    print(d)
main()


#resuelto (que hace el data.get(k))