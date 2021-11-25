def type1():
    global list2
    while _type == 1:
        list2 = [[0, 1, 2, 3, 4],
            [1, 2, 3, 4, 5],
            [2, 3, 4, 5, 0],
            [3, 4, 5, 0, 1],
            [4, 5, 0, 1, 2]]
def type2():
    global list2
    list2 = [[randint(0, 5),
            randint(0, 5),
            randint(0, 5),
            randint(0, 5),
            randint(0, 5)],
        [randint(0, 5),
            randint(0, 5),
            randint(0, 5),
            randint(0, 5),
            randint(0, 5)],
        [randint(0, 5),
            randint(0, 5),
            randint(0, 5),
            randint(0, 5),
            randint(0, 5)],
        [randint(0, 5),
            randint(0, 5),
            randint(0, 5),
            randint(0, 5),
            randint(0, 5)],
        [randint(0, 5),
            randint(0, 5),
            randint(0, 5),
            randint(0, 5),
            randint(0, 5)]]
    while _type == 2:
        if randint(0, 2) == 0:
            list2 = [[randint(0, 5),
                    randint(0, 5),
                    randint(0, 5),
                    randint(0, 5),
                    randint(0, 5)],
                [randint(0, 5),
                    randint(0, 5),
                    randint(0, 5),
                    randint(0, 5),
                    randint(0, 5)],
                [randint(0, 5),
                    randint(0, 5),
                    randint(0, 5),
                    randint(0, 5),
                    randint(0, 5)],
                [randint(0, 5),
                    randint(0, 5),
                    randint(0, 5),
                    randint(0, 5),
                    randint(0, 5)],
                [randint(0, 5),
                    randint(0, 5),
                    randint(0, 5),
                    randint(0, 5),
                    randint(0, 5)]]

def on_button_pressed_a():
    global _type
    _type = 1
    type1()
input.on_button_pressed(Button.A, on_button_pressed_a)

def type3():
    global list2
    list2 = [[randint(0, 5),
            randint(0, 5),
            randint(0, 5),
            randint(0, 5),
            randint(0, 5)],
        [randint(0, 5),
            randint(0, 5),
            randint(0, 5),
            randint(0, 5),
            randint(0, 5)],
        [randint(0, 5),
            randint(0, 5),
            randint(0, 5),
            randint(0, 5),
            randint(0, 5)],
        [randint(0, 5),
            randint(0, 5),
            randint(0, 5),
            randint(0, 5),
            randint(0, 5)],
        [randint(0, 5),
            randint(0, 5),
            randint(0, 5),
            randint(0, 5),
            randint(0, 5)]]
    while _type == 3:
        if randint(0, 2) == 0:
            list2 = [[randint(0, 5),
                    randint(0, 5),
                    randint(0, 5),
                    randint(0, 5),
                    randint(0, 5)],
                [randint(0, 5),
                    randint(0, 5),
                    randint(0, 5),
                    randint(0, 5),
                    randint(0, 5)],
                [randint(0, 5),
                    randint(0, 5),
                    randint(0, 5),
                    randint(0, 5),
                    randint(0, 5)],
                [randint(0, 5),
                    randint(0, 5),
                    randint(0, 5),
                    randint(0, 5),
                    randint(0, 5)],
                [randint(0, 5),
                    randint(0, 5),
                    randint(0, 5),
                    randint(0, 5),
                    randint(0, 5)]]

def on_button_pressed_ab():
    global _type
    _type = 3
    type3()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global _type
    _type = 2
    type2()
input.on_button_pressed(Button.B, on_button_pressed_b)

def type0():
    global list2
    while _type == 0:
        list2 = [[0, 5, 0, 5, 0],
            [5, 0, 5, 0, 5],
            [0, 5, 0, 5, 0],
            [5, 0, 5, 0, 5],
            [0, 5, 0, 5, 0]]
list2: List[List[number]] = []
_type = 0
_type = 0
type0()

def on_forever():
    for Y in range(5):
        for X in range(5):
            led.plot_brightness(X, Y, 51 * list2[Y][X])
basic.forever(on_forever)
