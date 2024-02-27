file = open("allCon.txt","r")

lst = []

for i in range(1,9023):
    data = file.readline().replace("\n","")
    lst.append(data)

lst = list(set(lst))

a = 0
file1 = open("finalContact.txt","w")
for i in lst:
    a = a + 1
    file1.write(f"{i}\n")


file1.close()
file.close()