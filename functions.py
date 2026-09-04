def show_pace(time, dist):
    min = int(time)
    sec = (time % 1) * 60
    total_seconds = (min * 60) + sec
    pace_sec = total_seconds / dist
    pace_sfinal = pace_sec // 60
    pace_rest = pace_sec % 60
    pace_final = f'{int(pace_sfinal)}:{int(pace_rest):02}'
    return pace_final

def calculate_speed(time, dist):
    min = int(time)
    sec = (time % 1) * 60
    total_seconds = (min * 60) + sec
    hours = total_seconds / 3600
    speed = dist / hours
    return speed

def calculate_10km_time(time, dist):
    min = int(time)
    sec = (time % 1) * 60
    total_seconds = (min * 60) + sec
    ten_km = (total_seconds / dist) * 10
    min_ten = int(ten_km // 60)
    sec_ten_km = ten_km % 60
    time_ten_km = f'{min_ten}:{int(sec_ten_km):02}'
    return time_ten_km

def compare_runs(time_one, dist_one, time_two, dist_two):
    pacerun1 = show_pace(time_one, dist_one)
    pacerun2 = show_pace(time_two, dist_two)
    vel_run1 = calculate_speed(time_one, dist_one)
    vel_run2 = calculate_speed(time_two, dist_two)
    partes1 = pacerun1.split(':')
    partes2 = pacerun2.split(':')
    min1 = int(partes1[0])
    sec1 = int(partes1[1])
    min2 = int(partes2[0])
    sec2 = int(partes2[1])
    total_seconds1 = (min1 * 60) + sec1
    total_seconds2 = (min2 * 60) + sec2
    print(f'--- Corrida 1 ---\n'
          f'Pace: {pacerun1} min/km\n'
          f'Velocidade média: {vel_run1:.2f} km/h\n'
          f'\n'
          f'--- Corrida 2 ---\n'
          f'Pace: {pacerun2} min/km\n'
          f'Velocidade média: {vel_run2:.2f} km/h\n'
          f'\n'
          f'--- Comparação ---')
    if total_seconds1 < total_seconds2:
        subtraction = total_seconds2 - total_seconds1
        minsubtraction = subtraction // 60
        secsubtraction = subtraction % 60
        print(f'Você foi mais rápido na corrida 1!\n'
              f'Diferença de pace: {minsubtraction}:{secsubtraction:02} min/km')

    elif total_seconds1 == total_seconds2:
        print('O pace das duas corridas foi exatamente igual!')

    else:
        subtraction = total_seconds1 - total_seconds2
        minsubtraction = subtraction // 60
        secsubtraction = subtraction % 60
        print(f'Você foi mais rápido na corrida 2!\n'
              f'Diferença de pace: {minsubtraction}:{secsubtraction:02} min/km')

def hist_run():
    hist = []
    user = int(input('Quantas corridas você gostaria de registrar?: '))
    for count in range(1, user + 1, 1):
        runs = {}
        runs['dist'] = float(input(f'Qual a distância da {count}ª corrida?: '))
        runs['time'] = float(input(f'Qual o tempo da {count}ª corrida?: '))
        hist.append(runs)
    print('==== HISTÓRICO DE CORRIDAS ====')
    count2 = 0
    for run in hist:
        count2 += 1
        print(f'Corrida {count2} -> {run['dist']:.2f} | {show_pace(run['time'], run['dist'])} | {calculate_speed(run['time'], run['dist'])}')

def data_analysis():
    hist = []
    user = int(input('Quantas corridas você gostaria de registrar?: '))
    km_total = 0
    seconds = 0
    for count in range(1, user + 1, 1):
        runs = {}
        runs['dist'] = float(input(f'Qual a distância da {count}ª corrida?: '))
        runs['time'] = float(input(f'Qual o tempo da {count}ª corrida?: '))
        runs['pace'] = show_pace(runs['time'], runs['dist'])
        km_total += runs['dist']
        seconds += (int(runs['time']) * 60) + ((runs['time'] % 1) * 60)
        hist.append(runs)
    general_pace = show_pace(seconds / 60, km_total)
    general_vel = calculate_speed(seconds / 60, km_total)
    smaller_pace = 10000
    bigger_dist = 0
    count_pace = 0
    count_vel = 0
    counter = 0
    for run in hist:
        counter += 1
        if ((int(run['time']) * 60) + ((run['time'] % 1) * 60)) / run['dist'] < smaller_pace:
            smaller_pace = ((int(run['time']) * 60) + ((run['time'] % 1) * 60)) / run['dist']
            count_pace = counter

        if run['dist'] > bigger_dist:
            count_vel = counter
            bigger_dist = run['dist']
    print(f'==== ANÁLISE GERAL ====\n'
          f'Distância total: {km_total}\n'
          f'Tempo total: {seconds // 60}:{seconds%60:02} min\n'
          f'Pace médio geral: {general_pace}\n'
          f'Velocidade média geral: {general_vel}\n'
          f'\n'
          f'Corrida mais rápida: Corrida {count_pace}\n'
          f'Pace: {smaller_pace // 60}:{smaller_pace % 60:02}\n'
          f'\n'
          f'Corrida mais longa: {count_vel}\n'
          f'Distância: {bigger_dist}')