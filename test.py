import pyautogui as pg

answer1 = pg.confirm(
    "2 + 2 = ",
    buttons = [2, 22, 4]
)

answer2 = pg.confirm(
    "2 + 4 = ",
    buttons = [34, 2, 6]
)

answer3 = pg.confirm(
    "5 + 5 = ",
    buttons = [55, 3, 10, 43]
)

res = 0

if answer1 == "4":
    res += 1
if answer2 == "6":
    res +=1
if answer3 == "10":
    res +=1

pg.alert(res)