list2=["Placebo · 720p (119MB) ","Placebo · 720p (119MB) "]
list3=[]
for stor in list2: 
    print(stor)  
    for x in stor:
        if x=="(":
            break
        else: 
            stor=stor.replace(x,"")
        print(x)
    stor=stor.replace("(","").replace(")","").replace("M","").replace("B","")
    list3.append(int(stor))
print("The total storage is",sum(list3),"MB")