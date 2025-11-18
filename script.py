import asyncio
import random
import pyperclip
import pyautogui
import pygetwindow

x_pass, y_pass = random.randint(50, 400), random.randint(250, 260)
x_ent, y_ent = random.randint(40, 200), random.randint(340, 360)

async def steam_login(inf: str):
    while True:
        try:
            win = pygetwindow.getWindowsWithTitle('Войдите в аккаунт снова')[0]
            win.activate()

            pyautogui.click(x=x_pass+win.left, y=y_pass+win.top)
            await asyncio.sleep(0.3)

            pyperclip.copy(inf)
            pyautogui.write(pyperclip.paste())
            await asyncio.sleep(0.3)

            pyautogui.click(x=x_ent + win.left, y=y_ent + win.top)
            await asyncio.sleep(3)

        except:
            print('Ожидаю окно ...')
            await asyncio.sleep(1)

async def main():
    inf = input('Вставьте пароль для автовхода: ')
    await steam_login(inf)

if __name__ == '__main__':
    asyncio.run(main())