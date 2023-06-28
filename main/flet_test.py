import flet as ft
from datetime import timedelta

def main(page):
    def handel_click(e):
        press_min = int(a.value)
        time_now = timedelta(hours=int((b.value)), minutes=int((c.value)))
        max_press_drop = round(press_min / 3)
        press_ctrl_exit = press_min - max_press_drop
        delta_time = timedelta(minutes=(round(max_press_drop * 6.8 / 45)))
        total_time = timedelta(minutes=(round(press_min * 6.8 / 45)))
        time_on_exit = time_now + delta_time
        comeback_time = time_now + total_time

        r.value = max_press_drop, press_ctrl_exit, delta_time, total_time, time_on_exit, comeback_time
        print(f' Pmax.пад = {max_press_drop}, Рк.вых =  {press_ctrl_exit}, Дельта Т = {delta_time}, Тобщ = {total_time}, Т вых = {time_on_exit}, Т возвр = {comeback_time}')

        page.update()


    a = ft.TextField(label='Мин.давление')
    b = ft.TextField(label='Час')
    c = ft.TextField(label='Минуты')
    r = ft.TextField(label='результат')
    s = ft.TextButton(text='рассчитать', on_click=handel_click)
    page.add(ft.Column([a,b,c,s,r]))
ft.app(target=main)

def calculator():
    press_min = int(input('Введите минимальное давление при включении:'))
    time_now = timedelta(hours=int(input('час: ')), minutes=(int(input('минуты: '))))
    max_press_drop = round(press_min / 3)
    press_ctrl_exit = press_min - max_press_drop
    delta_time = timedelta(minutes=(round(max_press_drop * 6.8 / 45)))
    total_time = timedelta(minutes=(round(press_min * 6.8 / 45)))
    time_on_exit = time_now + delta_time
    comeback_time = time_now + total_time
    return f' Pmax.пад = {max_press_drop}, Рк.вых =  {press_ctrl_exit}, Дельта Т = {delta_time}, Тобщ = {total_time}, Т вых = {time_on_exit}, Т возвр = {comeback_time}'