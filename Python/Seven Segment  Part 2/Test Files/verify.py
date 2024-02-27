def verify(disp_Num, curVal, H1):
    if disp_Num == 1:
        if curVal == 0 or curVal==1:
            print(curVal)
        else: # curVal == (2 or 3 or 4 or 5 or 6 or 7 or 8 or 9):
            print("invalid") #invalid!o
    if disp_Num == 2:
        if H1 == 0:
            if curVal == 0:
                print("invalid")
            else:
                print(curVal)
        if H1 == 1:
            if curVal == 0 or curVal == 1 or curVal == 2:
                print(curVal)
            else: # curVal == 3 or 4 or 5 or 6 or 7 or 8 or 9:
                print("invalid") #invalid!
    if disp_Num == 3:
        if curVal == 0 or curVal == 1 or curVal == 2 or curVal == 3 or curVal == 4 or curVal == 5:
            print(curVal)
        else: # curVal == 6 or 7 or 8 or 9:
            print("invalid") #invalid!




verify(3,6,0)


