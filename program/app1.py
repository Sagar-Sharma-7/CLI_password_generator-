
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

def gen_pass(n):
    print(n)

try:
    n = int(input("\tLength of Password: "))
    gen_pass(n)
except ValueError:
    print(bcolors.FAIL + "Entered Value should be integer only")
    print("Restart the program again...")
    pass
