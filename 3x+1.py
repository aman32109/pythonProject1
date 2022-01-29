#dumbass listen carefulno=int(input("enter odd number"))
no=int(input("enter odd number"))
if no%2==1:
    while no!=1:
        if no>1.7976931348623157e+308:
            exit()
        no=((no*3)+1)
        print(no)
        var_even=(no/2)
        print(var_even)
else:
    exit()