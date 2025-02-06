def solve(numheads, numlegs):
    for rabits in range(numheads + 1):
        chickens = numheads - rabits
        if 2*chickens + 4*rabits == numlegs:
            print(f"We have {rabits} rabits and {chickens} chickens.")
solve(35, 94)
            