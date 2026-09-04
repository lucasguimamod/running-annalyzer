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