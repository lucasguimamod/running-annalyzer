def show_pace(time, dist):
    min = int(time)
    sec = (time % 1) * 60
    total_seconds = (min * 60) + sec
    pace_sec = total_seconds / dist
    pace_sfinal = pace_sec // 60
    pace_rest = pace_sec % 60
    pace_final = f'Pace: {int(pace_sfinal)}:{int(pace_rest):02}'
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