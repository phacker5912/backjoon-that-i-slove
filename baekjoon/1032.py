n=int(input(""))
e=""
for i in range(n):
    line=input("")
    if i==0:
        e=line
    else:
        for j in range(len(e)):
            if e[j] != "?" and  e[j] != line[j]:
                e=e[:j]+"?"+e[j+1:]
print(e)