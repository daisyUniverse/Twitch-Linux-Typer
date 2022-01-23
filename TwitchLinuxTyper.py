from TwitchLinuxListener import Chat
import pyautogui

# The most cursed Twitch chat bot ever. do NOT run this on anything you care about

MyChat = Chat()

while True:
    user, message = MyChat.listen()
    if message != None or '':
        if '^' in message:
            prog = ('pyautogui.hotkey("' + '", "'.join(str(v) for v in message.split('^')) + '")')
            exec(prog)
        else:
            pyautogui.write(message, interval = 0.2)
            pyautogui.press('enter')


