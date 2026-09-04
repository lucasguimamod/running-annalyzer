from functions import *

def main():
    time = float(input('Qual foi o tempo?: '))
    dist = float(input('Qual foi a distância?: '))
    print(f'Pace: {show_pace(time, dist)}')
    print(f'Velocidade média: {calculate_speed(time, dist):.2f} km/h')
    print(f'Tempo estimado para 10km no pace atual: {calculate_10km_time(time, dist)}')
    time_one = time
    dist_one = dist
    time_two = float(input('Qual foi o tempo da segunda corrida?: '))
    dist_two = float(input('Qual foi a distância da segunda corrida?: '))
    compare_runs(time_one, dist_one, time_two, dist_two)

if __name__ == '__main__':
    main()