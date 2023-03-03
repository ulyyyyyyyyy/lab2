color1 = input("enter the first color")
color2 = input("enter the second color")

if (color1 != "red") or (color1 != "yellow") or (color1 != "blue") or (color2 != "red") or (color2 != "yellow") or (color2 != "blue"):
    print("not found")
elif (color1 == "red") and (color2 == "blue"):
    print("purple")
elif (color1 == "blue") and (color2 == "red"):
    print("purple")
elif (color1 == "red") and (color2 == "yellow"):
    print("orange")
elif (color1 == "yellow") and (color2 == "red"):
    print("orange")
elif (color1 == "blue") and (color2 == "yellow"):
    print("green")
elif (color1 == "yellow") and (color2 == "blue"):
    print("green")
