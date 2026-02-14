def Q(P):
    answer = H(P, P)
    if answer == "YES":
        LoopForever()
    else:
        Halt()