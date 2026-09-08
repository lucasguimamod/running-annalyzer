import json

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
        print('-' * 34)
        runs['dist'] = float(input(f'Qual a distância da {count}ª corrida?: '))
        runs['time'] = float(input(f'Qual o tempo da {count}ª corrida?: '))
        print('-' * 34)
        hist.append(runs)
    print('\n')
    print('==== HISTÓRICO DE CORRIDAS ====')
    count2 = 0
    for run in hist:
        count2 += 1
        print(f'Corrida {count2} -> {run['dist']:.2f} km | {show_pace(run['time'], run['dist'])} min | {calculate_speed(run['time'], run['dist'])} km/h')
    return hist

def data_analysis(hist):
    km_total = 0
    seconds = 0
    smaller_pace = 10000
    bigger_dist = 0
    count_pace = 0
    count_longest = 0
    counter = 0
    for run in hist:
        counter += 1
        km_total += run['dist']
        seconds += ((int(run['time']) * 60) + ((run['time'] % 1) * 60))
        if ((int(run['time']) * 60) + ((run['time'] % 1) * 60)) / run['dist'] < smaller_pace:
            smaller_pace = ((int(run['time']) * 60) + ((run['time'] % 1) * 60)) / run['dist']
            count_pace = counter

        if run['dist'] > bigger_dist:
            count_longest = counter
            bigger_dist = run['dist']
    general_pace = show_pace(seconds / 60, km_total)
    general_vel = calculate_speed(seconds / 60, km_total)
    print('\n')
    print(f'==== ANÁLISE GERAL ====\n'
          f'Distância total: {km_total:.2f} km\n'
          f'Tempo total: {int(seconds // 60)}:{int(seconds%60):02} min\n'
          f'Pace médio geral: {general_pace}\n'
          f'Velocidade média geral: {general_vel:.2f}\n'
          f'\n'
          f'Corrida mais rápida: Corrida {count_pace}\n'
          f'Pace: {int(smaller_pace // 60)}:{int(smaller_pace % 60):02}\n'
          f'\n'
          f'{'-' * 34}\n'
          f'Corrida mais longa: {count_longest}\n'
          f'Distância: {bigger_dist:.2f} km\n')

def goal_dist(hist):
    goal = float(input('Qual sua meta de distÂncia percorrida total?: '))
    km_total = 0
    for run in hist:
        km_total += run['dist']
    if goal <= km_total:
        print('Parabéns, sua meta já foi batida!')
        print('-' * 34)
    else:
        print(f'Ainda temos um trabalho a fazer! Faltam {goal - km_total:.2f} km')
        print('-' * 34)

def best_run(hist):
    smaller_pace = 1000
    counter = 0
    count_pace = 0
    count_vel = 0
    bigger_vel = 0
    for run in hist:
        counter += 1
        if ((int(run['time']) * 60) + ((run['time'] % 1) * 60)) / run['dist'] < smaller_pace:
            smaller_pace = ((int(run['time']) * 60) + ((run['time'] % 1) * 60)) / run['dist']
            count_pace = counter
        if calculate_speed(run['time'], run['dist']) > bigger_vel:
            count_vel = counter
            bigger_vel = calculate_speed(run['time'], run['dist'])
    print('=' * 30)
    print('MELHOR DESEMPENHO'.center(30))
    print('=' * 30)
    print('\n')
    print(f'Melhor pace:\n'
          f'Corrida {count_pace}\n'
          f'Pace: {int(smaller_pace // 60)}:{int(smaller_pace % 60):02} min/km\n'
          f'\n'
          f'Maior velocidade:\n'
          f'Corrida {count_vel}\n'
          f'Velocidade: {bigger_vel:.2f} km/h')

def show_history(hist):
    counter = 0
    for run in hist:
        counter += 1
        print(f'Corrida {counter} -> {run['dist']:.2f} | {show_pace(run['time'], run['dist'])} min/km | {calculate_speed(run['time'], run['dist']):.2f} km/h')

def add_run(hist):
    runs = {}
    runs['dist'] = float(input('Qual a distância da corrida?: '))
    runs['time'] = float(input('Qual o tempo da corrida?: '))
    hist.append(runs)
    print('Corrida adicionada com sucesso!')

def remove_run(hist):
    counter = 0
    user = int(input('Qual o número da corrida a ser removida?: '))
    for run in hist:
        counter +=1
        if user == counter:
            hist.remove(run)
            print(f'Corrida {counter} removida com sucesso!')
            break
    if user > counter:
        print('Corrida não existente!')

def filter_runs(hist):
    user = int(input('Qual o filtro desejado?\n'
                     '1 - Corridas acima de x km\n'
                     '2 - Corridas abaixo de x km\n'
                     '3 - Corridas com pace melhor que x\n'
                     '0 - Voltar ao menu inicial\n'
                     'Escolha uma opção: '))
    if user == 1:
        useroption = float(input('Distância de filtragem: '))
        counter = 0
        for run in hist:
            counter += 1
            if run['dist'] > useroption:
                print(f'Corrida {counter} -> {run['dist']:.2f} km | {show_pace(run['time'], run['dist'])} min/km | {calculate_speed(run['time'], run['dist']):.2f} km/h')

    elif user == 2:
        useroption = float(input('Distância de filtragem: '))
        counter = 0
        for run in hist:
            counter += 1
            if run['dist'] < useroption:
                print(f'Corrida {counter} -> {run['dist']:.2f} km | {show_pace(run['time'], run['dist'])} min/km | {calculate_speed(run['time'], run['dist']):.2f} km/h')

    elif user == 3:
        useroption = str(input('Distância de filtragem: (Ex: X:XX)'))
        counter = 0
        partes = useroption.split(':')
        minutes = int(partes[0])
        seconds = int(partes[1])
        total_seconds = minutes * 60 + seconds
        for run in hist:
            pace = show_pace(run['time'], run['dist'])
            partes_run = pace.split(':')
            minutes_run = int(partes_run[0])
            seconds_run = int(partes_run[1])
            total_seconds_run = minutes_run * 60 + seconds_run
            counter += 1
            if total_seconds_run < total_seconds:
                print(f'Corrida {counter} -> {run['dist']:.2f} km | {show_pace(run['time'], run['dist'])} min/km | {calculate_speed(run['time'], run['dist']):.2f} km/h')

    elif user == 0:
        menu(hist)

def performance_evolution(hist):
    print('=' * 30)
    print('EVOLUÇÃO DE DESEMPENHO'.center(30))
    print('=' * 30)
    counter1 = 0
    for runs in hist:
        counter1 += 1
    counter2 = 0
    for run in hist:
        counter2 += 1
        if counter2 == 1:
            print(f'Primeira corrida:\n'
                  f'Distância: {run['dist']:.2f} km\n'
                  f'Pace: {show_pace(run['time'], run['dist'])} min/km\n'
                  f'Velocidade: {calculate_speed(run['time'], run['dist']):.2f}\n'
                  f'\n')
            partes1 = show_pace(run['time'], run['dist']).split(':')
            minutes1 = int(partes1[0])
            seconds1 = int(partes1[1])
            total_seconds = minutes1 * 60 + seconds1
            speed1 = calculate_speed(run['time'], run['dist'])
        if counter2 == counter1:
            print(f'Última corrida:\n'
                  f'Distância: {run['dist']:.2f} km\n'
                  f'Pace: {show_pace(run['time'], run['dist'])} min/km\n'
                  f'Velocidade: {calculate_speed(run['time'], run['dist']):.2f}\n'
                  f'\n')
            partes2 = show_pace(run['time'], run['dist']).split(':')
            minutes2 = int(partes2[0])
            seconds2 = int(partes2[1])
            total_seconds2 = minutes2 * 60 + seconds2
            speed2 = calculate_speed(run['time'], run['dist'])
            print('-' * 30)
            print('\n')
            print(f'Evolução do pace: {total_seconds2 - total_seconds} segundos/km')
            print(f'Evolução da velocidade: {speed2 - speed1:.2f} km/h')


def save_history(hist):
    arquivo = open('historico.json', 'w')
    json.dump(hist, arquivo)
    arquivo.close()

def menu(hist):
    print('=' * 30)
    print('RUNNING ANALYZER'.center(30))
    print('=' * 30)
    while True:
        try:
            user = int(input('\n'        
              '1 - Adicionar corrida\n'
              '2 - Remover corrida\n'
              '3 - Ver histórico\n'
              '4 - Análise geral\n'
              '5 - Meta de distância\n'
              '6 - Melhor desempenho\n'
              '7 - Filtrar corridas\n'
              '8 - Exibir melhoria de performance\n'
              '0 - Sair'
              '\n'
              'Escolha uma opção: '))
        except:
            print('Opção não disponível, tente novamente!')
            continue
        if user == 1:
            add_run(hist)
        elif user == 2:
            remove_run(hist)
        elif user == 3:
            show_history(hist)
        elif user == 4:
            data_analysis(hist)
        elif user == 5:
            goal_dist(hist)
        elif user == 6:
            best_run(hist)
        elif user == 7:
            filter_runs(hist)
        elif user == 8:
            performance_evolution(hist)
        elif user < 0 or user >= 7:
            print('Opção não disponível, tente novamente!')
        elif user == 0:
            print('Encerrando Running Analyzer...\n'
                  'Até a próxima!')
            break