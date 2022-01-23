from TwitchLinuxListener import Chat
import pyautogui

# The most cursed Twitch chat bot ever. do NOT run this on anything you care about

MyChat = Chat()

while True:
    user, message = MyChat.listen()
    if message != None or '':
        if '^' in message:
            pyautogui.hotkey(*message.split('^'))
        else:
            pyautogui.write(message, interval = 0.1)
            pyautogui.press('enter')


