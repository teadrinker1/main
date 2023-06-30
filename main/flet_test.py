import flet as ft
from datetime import timedelta


def main(page):
    def calculator(e):
        press_min = int(min_press.value)
        time_now = timedelta(hours=int(hours.value), minutes=int(minutes.value))
        max_press_drop = round(press_min / 3)
        press_ctrl_exit = press_min - max_press_drop
        delta_time = timedelta(minutes=(round(max_press_drop * 6.8 / 45)))
        total_time = timedelta(minutes=(round(press_min * 6.8 / 45)))
        time_on_exit = time_now + delta_time
        comeback_time = time_now + total_time
        d.value = f' Pmax.пад = {max_press_drop};  Рк.вых =  {press_ctrl_exit};  Дельта Т = {delta_time};  Тобщ = {total_time};  Т вых = {time_on_exit};  Т возвр = {comeback_time}'

        page.update()


    min_press = ft.TextField(label='введите минимальное давление:', width=280, helper_text='Введите время включения в НДС:')
    hours = ft.TextField(label='Введите часы:', width=280, hint_text='от 0 до 24')
    minutes = ft.TextField(label='Введите минуты:', width=280,hint_text='от 0 до 60')



    d = ft.TextField(label='Результат')
    c = ft.ElevatedButton(text='Рассчитать', on_click=calculator,
                          bgcolor=ft.colors.BLACK, color=ft.colors.WHITE)

    page.controls.append(ft.Text('Калькулятор ГДЗС v1.0',style=ft.TextThemeStyle.DISPLAY_SMALL))
    # page.controls.pop()
    page.add(ft.Column([min_press, hours, minutes, c, d]))
    page.update()



ft.app(target=main)
