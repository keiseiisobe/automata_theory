# P = program
# I = input
# --> P(I)

# H(P, I)
# --> P(I)が止まるか止まらないか
# --> このようなHが存在するか

def H(P, I):
    P(I)
    return "YES"

# P(P)が止まる時はQ(P)は止まらない
# P(P)が止まらない時はQ(P)は止まる
def Q(P):
    answer = H(P, P) # P(P)

    if answer == "YES":
        Loop_Forever()
    else:
        Halt()

Q(Q)
        
