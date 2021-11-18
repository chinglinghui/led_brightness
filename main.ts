function type1 () {
    if (randint(0, 2) == 0) {
        list = [
        [
        0,
        1,
        2,
        3,
        4
        ],
        [
        1,
        2,
        3,
        4,
        5
        ],
        [
        2,
        3,
        4,
        5,
        0
        ],
        [
        3,
        4,
        5,
        0,
        1
        ],
        [
        4,
        5,
        0,
        1,
        2
        ]
        ]
    }
}
function type2 () {
    if (randint(0, 2) == 0) {
        list = [
        [
        randint(0, 5),
        randint(0, 5),
        randint(0, 5),
        randint(0, 5),
        randint(0, 5)
        ],
        [
        randint(0, 5),
        randint(0, 5),
        randint(0, 5),
        randint(0, 5),
        randint(0, 5)
        ],
        [
        randint(0, 5),
        randint(0, 5),
        randint(0, 5),
        randint(0, 5),
        randint(0, 5)
        ],
        [
        randint(0, 5),
        randint(0, 5),
        randint(0, 5),
        randint(0, 5),
        randint(0, 5)
        ],
        [
        randint(0, 5),
        randint(0, 5),
        randint(0, 5),
        randint(0, 5),
        randint(0, 5)
        ]
        ]
    }
}
input.onButtonPressed(Button.A, function () {
    _type = 1
})
function type3 () {
    if (randint(0, 2) == 0) {
        list = [
        [
        randint(0, 5),
        randint(0, 5),
        randint(0, 5),
        randint(0, 5),
        randint(0, 5)
        ],
        [
        randint(0, 5),
        randint(0, 5),
        randint(0, 5),
        randint(0, 5),
        randint(0, 5)
        ],
        [
        randint(0, 5),
        randint(0, 5),
        randint(0, 5),
        randint(0, 5),
        randint(0, 5)
        ],
        [
        randint(0, 5),
        randint(0, 5),
        randint(0, 5),
        randint(0, 5),
        randint(0, 5)
        ],
        [
        randint(0, 5),
        randint(0, 5),
        randint(0, 5),
        randint(0, 5),
        randint(0, 5)
        ]
        ]
    }
}
input.onButtonPressed(Button.AB, function () {
    _type = 3
})
input.onButtonPressed(Button.B, function () {
    _type = 2
})
function type0 () {
    list = [
    [
    0,
    5,
    0,
    5,
    0
    ],
    [
    5,
    0,
    5,
    0,
    5
    ],
    [
    0,
    5,
    0,
    5,
    0
    ],
    [
    5,
    0,
    5,
    0,
    5
    ],
    [
    0,
    5,
    0,
    5,
    0
    ]
    ]
}
let list: number[][] = []
let _type = 0
_type = 0
basic.forever(function () {
    for (let Y = 0; Y <= 4; Y++) {
        for (let X = 0; X <= 4; X++) {
            for (let Y = 0; Y <= 4; Y++) {
                for (let X = 0; X <= 4; X++) {
                    led.plotBrightness(X, Y, 51 * list[Y][X])
                }
            }
            list.unshift(list.pop())
            basic.pause(100)
            if (_type == 0) {
                type0()
            } else if (_type == 1) {
                type1()
            } else if (_type == 2) {
                type2()
            } else {
                if (_type == 3) {
                	
                }
            }
        }
    }
})
