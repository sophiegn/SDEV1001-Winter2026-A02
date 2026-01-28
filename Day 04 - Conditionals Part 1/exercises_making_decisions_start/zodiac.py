year = int(input("Enter the year you'd like to find out the chinese zodiac for.  "))

zodiacyear = (year-1900)%12 

match zodiacyear:
    case 0:
        print("Rat")
    case 1:
        print("Ox")
    case 2:
        print("Tiger")
    case 3:
        print("Rabbit")
    case 4:
        print("Dragon")
    case 5:
        print("Snake")
    case 6:
        print("Horse")
    case 7:
        print("Sheep")
    case 8:
        print("Monkey")
    case 9:
        print("Rooster")
    case 10:
        print("Dog")
    case 11:
        print("Pig")
    case _:
        print("ERROR")