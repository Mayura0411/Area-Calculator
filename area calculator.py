def areacalculator():
    user=input("Enter the shape you want calculate the area of:").lower()
    area=0
    pi=3.14
    if user=="square":
        side=int(input("Enter the side of the square:"))
        area=area+(side**2)
    elif user=="circle":
        radius=int(input("Enter the radius of the circle:"))
        area=area+(pi*(radius**2))
    elif user=="rectangle":
        length=int(input("Enter the length of the rectangle:"))
        breadth=int(input("Enter the breadth of the rectangle:"))
        area=area+(length*breadth)
    elif user=="triangle":
        base=int(input("Enter the base of the triangle:"))
        height=int(input("Enter the height of the triangle:"))
        area=area+(0.5*base*height)
    else:
        print("select a valid shape")
    print("%.2f"%area)

areacalculator()




