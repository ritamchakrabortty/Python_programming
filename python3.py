Llist=["Apple","Guava","Banana","Orange","Cherry","Grapes"] 
print("The list is:\n") 
i=1 
for item in Llist: 
    print("Item ",i,": ",item) 
    i=i+1 
i=0 
for item in Llist: 
    if item=="Banana": 
        Llist[i]="Blackcurrent" 
    if item=="Cherry": 
        Llist[i]="Watermelon" 
    i=i+1 
i=1 
print("The items of the list after change is:\n") 
for item in Llist: 
    print("Item ",i,": ",item) 
    i=i+1
