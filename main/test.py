from datetime import timedelta


def calculator():
    press_min = 260
    time_now = timedelta(hours=16, minutes=25)
    max_press_drop = round(press_min / 3)
    press_ctrl_exit = press_min - max_press_drop
    delta_time = timedelta(minutes=(round(max_press_drop * 6.8 / 45)))
    total_time = timedelta(minutes=(round(press_min * 6.8 / 45)))
    time_on_exit = time_now + delta_time
    comeback_time = time_now + total_time
    return f' Pmax.пад = {max_press_drop}, Рк.вых =  {press_ctrl_exit}, Дельта Т = {delta_time}, Тобщ = {total_time}, Т вых = {time_on_exit}, Т возвр = {comeback_time}'

print(calculator())



