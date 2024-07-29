def calculator():
    val1=int(input("enter 1st value: "))
    val2=int(input("enter 2nd value: "))
    val3=int(input("enter 3rd value: "))

    print("enter your choice")
    print("1.add")
    print("2.sub")
    print("3.multi")
    print("4.div")

    choice=int(input("enter your choice(1/2/3/4): "))
    if choice==1:
        result=val1+val2+val3
        operation="add"
    elif choice==2:
        result=val1-val2-val3
        operation="sub"
    elif choice==3:
        result=val1*val2*val3
        operation="multi"
    elif choice==4:
        if val2==0 or val3==0:
            print("error:divide by 0 is not allowed")
            return
        result=val1/val2/val3
        operation="div"
    else:
        print("invalid choice")
        return
    print(f"the result of {operation} is: {result}")

    
calculator()    
               
          

    
    
