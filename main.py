def on_button_pressed_a():
    for Y in range(5):
        for X in range(5):
            led.plot_brightness(X, Y, 51 * list2[Y][X])
    list2.unshift(list2.pop())
    basic.pause(100)
input.on_button_pressed(Button.A, on_button_pressed_a)

list2: List[List[number]] = []
list2 = [[0, 2, 0, 2, 0],
    [3, 0, 3, 0, 3],
    [0, 4, 0, 4, 0],
    [5, 0, 5, 0, 5],
    [0, 4, 0, 4, 0]]
while True:
    for Y2 in range(5):
        for X2 in range(5):
            led.plot_brightness(X2, Y2, 51 * list2[Y2][X2])
    list2.unshift(list2.pop())
    basic.pause(100)
while False:
    break

def on_forever():
    pass
basic.forever(on_forever)
