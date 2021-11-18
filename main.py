def on_button_pressed_a():
    global list2
    list2 = [[0, 1, 0, 1, 0],
        [1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0],
        [1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0]]
    for Y in range(5):
        for X in range(5):
            if list2[Y][X] == 1:
                led.plot(X, Y)
            else:
                led.unplot(X, Y)
    list2.unshift(list2.pop())
    basic.pause(100)
input.on_button_pressed(Button.A, on_button_pressed_a)

list2: List[List[number]] = []
list2 = [[0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0]]
for Y2 in range(5):
    for X2 in range(5):
        if list2[Y2][X2] == 1:
            led.plot(X2, Y2)
        else:
            led.unplot(X2, Y2)

def on_forever():
    for Y3 in range(5):
        for X3 in range(5):
            if list2[Y3][X3] == 1:
                led.plot(X3, Y3)
            else:
                led.unplot(X3, Y3)
    list2.unshift(list2.pop())
    basic.pause(100)
basic.forever(on_forever)
