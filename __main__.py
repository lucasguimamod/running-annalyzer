from functions import *

def main():
    time = float(input('Qual foi o tempo?: '))
    dist = float(input('Qual foi a distância?: '))
    print(show_pace(time, dist))
    print(f'Velocidade média: {calculate_speed(time, dist):.2f} km/h')
    print(f'Tempo estimado para 10km no pace atual: {calculate_10km_time(time, dist)}')

if __name__ == '__main__':
    main()