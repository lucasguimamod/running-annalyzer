def show_pace(time, dist):
    min = int(time)
    sec = (time % 1) * 60
    total_seconds = (min * 60) + sec
    pace_sec = total_seconds / dist
    pace_sfinal = pace_sec // 60
    pace_rest = pace_sec % 60
    pace_final = f'Pace: {int(pace_sfinal)}:{int(pace_rest):02}'
    return pace_final