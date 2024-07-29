global f

f=0

def t_movie():
    global f
    f=f+1
    print("which movie do you want to watch?")
    print("1.KGF")
    print("2.Alaipayuthe")
    print("3.Garudan")
    print("4.back")

    movie=int(input("choose your movie:"))

    if movie==1:
        theatre()

    if movie==2:
        theatre()
        
    if movie==3:
        theatre()
    

    if movie==4:
        center()
        theatre()
        return 0

def theatre():
    print("which screen you want?")
    print("1.SCREEN 1")
    print("2.SCREEN 2")
    print("3.SCREEN 3")
    a=int(input("choose your screen:"))

    ticket=int(input("number of tickets you want:"))
    timing(a)

def timing(a):
    time1={
        "1":"10.00-01.00",
        "2":"02.00-05.00",
        "3":"06.00-08.00",
        "4":"09.00-11.00"
        }

    time2={
        "1":"10.10-01.00",
        "2":"02.30-05.00",
        "3":"06.40-08.00",
        "4":"09.50-11.00"
        }

    time3={
        "1":"07.00-09.00",
        "2":"10.00-12.00",
        "3":"01.00-03.00",
        "4":"04.00-5.00"
        }

    if a==1:
        print("choose your time:")
        print(time1)
        t=input("select your time:")
        x=time1[t]
        print("success,enjoy your movie at"+x)

    elif a==2:
        print("choose your time:")
        print(time2)
        t=input("select your time:")
        x=time2[t]
        print("success,enjoy your movie at"+x)

    elif a==3:
        print("choose your time:")
        print(time3)
        t=input("select your time:")
        x=time3[t]
        print("success,enjoy your movie at"+x)

    return 0

def movie(theatre):
    if theatre==1:

        t_movie()
    elif theatre==2:
        t_movie()

    elif theatre==3:
        t_movie()

    elif theatre==4:
        city()

    else:
        print("wrong choice")


def center():
    print("which theatre you want:")
    print("1.INOX")
    print("2.PVR")
    print("3.AGS")
    print("4.back")

    a=int(input("choose your option:"))
    movie(a)
    return 0

def city():
     print("HI...Wlcome to mivie ticket booking: ")
     print("1.chennai")
     print("2.kochi")
     print("3.Hydrabad")
     place=int(input("choose your option:"))

     if place==1:
         center()
     if place==2:
         center()
     if place==3:
         center()

     else:
         print("wrong choice")


city()  A     


        
           
          
    
    
