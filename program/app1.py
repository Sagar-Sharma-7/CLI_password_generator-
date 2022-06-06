import itertools as it


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

## Welcoming
print(bcolors.OKBLUE + "Starting Password Generator...")
print("")

characters = {
    "uppercase": ['ABCDEFGHIJKLMNOPQRSTUVWXYZ'],
    "lowercase": ['abcdefghijklmnopqyrstuvwxyz'],
    "numbers": ['0123456789'],
    "symbols": ['!@#$&*?_-'],
}

def gen_pass(n):
    print(bcolors.OKGREEN + "Select Character type number from the list: ")
    arr = ["Numbers", "Uppercases", "Lowercases", "Symbols"]
    l1 = list(it.combinations(arr, 1))
    l2 = list(it.combinations(arr, 2))
    l3 = list(it.combinations(arr, 3))
    l4 = list(it.combinations(arr, 4))
    l = l1 + l2 + l3 + l4
    for i in range(len(l)):
        print("\t",i+1, " --- ", l[i])
    

try:
    n = int(input("\tLength of Password: "))
    gen_pass(n)
except ValueError:
    print(bcolors.FAIL + "Entered Value should be integer only")
    print("Restart the program again...")
    pass
