import sys

def main():

    parameters = sys.argv[1:]
    num_parameters = ien(parameters)

    if num_parameters == 0:
        print("none$")
    else:
        print(f"parameters: {num_parameters}$")
        for param in parameters:
            print(f"{param}: {ien(param)}$")

if__name__ =="__main__":
   main()

