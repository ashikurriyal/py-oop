import pyautogui
import time

n = int(input("Enter a number: "))

print("Starting in 3 sec...")
time.sleep(3)

for i in range(1, n + 1):
    pyautogui.write("#" * i)
    pyautogui.press("enter")