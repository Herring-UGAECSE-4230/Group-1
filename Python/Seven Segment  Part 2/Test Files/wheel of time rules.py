#wheel of time rules
H1 = 0
H2 = 3
M1 = 0
M2 = 0
meridian = "PM"

def wheel_of_time():
    global H1
    global H2
    global M1
    global M2
    global meridian
    if M2 < 9:
        M2 = M2 + 1
    elif M2 == 9:
        M2 = 0
        if M1 < 5:
            M1 += 1
        elif M1 == 5:
            M1 = 0
            if H1 == 0:
                if H2 < 9:
                    H2 += 1
                elif H2 == 9:
                    H2 = 0
                    H1 = 1
            elif H1 == 1:
                if H2 < 2:
                    H2 += 1
                    if meridian == "AM":
                        meridian = "PM"
                    elif meridian == "AM":
                        meridian = "PM"
                elif H2 == 2:
                    H2 = 1
                    H1 = 0

for n in range(0,5):
    wheel_of_time() 
    print("The time is {",H1,"}{",H2,"}:{",M1,"}{",M2,"} {",meridian,"}")
