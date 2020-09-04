import time
while 1==1 :
    print("==========================================")
    print("Please Choose option")
    print("1.Find the area of a rectangle")
    print("2.Find the area of a triangle")
    print("3.Find the area of a circle")
    try :
        inp = int(input("Choose option : "))
    except :
        print("[Program end]")
        break

    if inp == 1 :
        print("==========================================")
        try :
            lenght = float(input("Enter lenght : "))
            width = float(input("Enter width : "))
        except :
            print("[Program end]")
            break
        answer = (lenght*width)
        print("Area =",answer)
        time.sleep(1)
    if inp == 2 :
        print("==========================================")
        try :
            base = float(input("Enter base : "))
            height = float(input("Enter height : "))
        except :
            print("[Program end]")
            break
        answer = (base*height*0.5)
        print("Area =",answer)
        time.sleep(1)
    if inp == 3 :
        print("==========================================")
        print("Find the area of a circle")
        print("Please Choose option of a circle")
        print("1.Find it using pi = 3.14")
        print("2.Find it using pi = 22/7")
        try:
            circle_input = int(input("Choose option : "))
        except :
            print("[Program end]")
            break
        if circle_input == 1 :
            print("==========================================")
            print("Find the area of a circle")
            try :
                diameter_circle = float(input("Enter diameter : "))
            except :
                print("[Program end]")
                break
            answer = (diameter_circle*3.14)
            print("Area =",answer)
            time.sleep(1)
        if circle_input == 2 :
            print("==========================================")
            print("Find the area of a circle")
            try :
                diameter_circle = float(input("Enter diameter : "))
            except :
                print("[Program end]")
                break
            answer = (diameter_circle*(22/7))
            print("Area =",answer)
            time.sleep(1)
        else :
            print("==========================================")
            print("Error : Please enter the correct option")
            time.sleep(1)
    if inp >= 4 or inp <= 0 :
        print("==========================================")
        print("Error : Please enter the correct option")
        time.sleep(1)