count = 1

for a in range(1,101):
    include = str(a).find("7")
    if a%7 != 0 and a%10 != 7 and a//10 != 7:#include == -1:
        print(a,end=" ")
    else:
        print(end="  ")  
    if count == 6:
        print("\n")
        count =0
    
    count +=1

