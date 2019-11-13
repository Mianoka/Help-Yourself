collection = ["\b\t80cm\t60cm\n", "\b\t81cm\t51cm\n", "\b\t105cm\t145cm\n"]
c=[]
for i in range(0,len(collection)):
    c = collection[i].split("\b\t")
    del c[0]
    for j in range(0,1):
        v = c[j].split("cm\t")
        val = v[1].split("cm\n")
        if v[0]>v[1]:
            print(v[0])
















