def openRussianDoll(doll):
    if doll == 1:
        print("doll " + str(doll) + " opened.")
        print("All dolls are opened.")
    else:
        print("doll " + str(doll) + " opened.")
        openRussianDoll(doll - 1)

openRussianDoll(5)
