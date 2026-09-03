from functions import *

def main():
    time = float(input('Qual foi o tempo?: '))
    dist = float(input('Qual foi a distância?: '))
    print(show_pace(time, dist))

if __name__ == '__main__':
    main()