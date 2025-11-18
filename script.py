import asyncio
import random
import pyperclip
import pyautogui
import pygetwindow

# Координаты поля ввода всплывающего окна Steam о конфликте сессий.
x_pass, y_pass = random.randint(50, 400), random.randint(250, 260)
# Координаты кнопки "Войти" всплывающего окна Steam о конфликте сессий.
x_ent, y_ent = random.randint(40, 200), random.randint(340, 360)

async def steam_login():
    while True:
        try:
            win = pygetwindow.getWindowsWithTitle('Войдите в аккаунт снова')[0]
            win.activate()

            pyautogui.click(x=x_pass+win.left, y=y_pass+win.top)
            await asyncio.sleep(0.3)

            pyautogui.write('d10Cjgdncu')
            await asyncio.sleep(0.2)
            pyautogui.write('1979')
            await asyncio.sleep(0.3)

            pyautogui.click(x=x_ent + win.left, y=y_ent + win.top)
            await asyncio.sleep(3)
            print('Вход выполнен!')

        except:
            print('Ожидаю окно ...')
            await asyncio.sleep(1)


async def steam_login_alt(inf: str):
    while True:
        try:
            win = pygetwindow.getWindowsWithTitle('Войдите в аккаунт снова')[0]
            win.activate()

            pyautogui.click(x=x_pass+win.left, y=y_pass+win.top)
            await asyncio.sleep(0.3)

            pyperclip.copy(inf)
            await asyncio.sleep(0.1)

            pyautogui.write(pyperclip.paste())
            await asyncio.sleep(0.3)

            pyautogui.click(x=x_ent + win.left, y=y_ent + win.top)
            await asyncio.sleep(3)
            print('Вход выполнен!')

        except:
            print('Ожидаю окно ...')
            await asyncio.sleep(1)

async def main():
    while True:
        inf = input('Вставьте пароль для автовхода: ')
        wei = input('Выберите способ автоматизации входа: ')
        if wei == '1':
            await steam_login()
            break
        elif wei == '2':
            await steam_login_alt(inf)
            break
        else:
            print('Неверное значение.')


if __name__ == '__main__':
    asyncio.run(main())