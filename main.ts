input.onButtonPressed(Button.A, function () {
    list = [
    [
    0,
    1,
    0,
    1,
    0
    ],
    [
    1,
    0,
    1,
    0,
    1
    ],
    [
    0,
    1,
    0,
    1,
    0
    ],
    [
    1,
    0,
    1,
    0,
    1
    ],
    [
    0,
    1,
    0,
    1,
    0
    ]
    ]
    for (let Y = 0; Y <= 4; Y++) {
        for (let X = 0; X <= 4; X++) {
            if (list[Y][X] == 1) {
                led.plot(X, Y)
            } else {
                led.unplot(X, Y)
            }
        }
    }
    list.unshift(list.pop())
    basic.pause(100)
})
let list: number[][] = []
list = [
[
0,
2,
0,
2,
0
],
[
3,
0,
3,
0,
3
],
[
0,
4,
0,
4,
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
4,
0,
4,
0
]
]
for (let Y = 0; Y <= 4; Y++) {
    for (let X = 0; X <= 4; X++) {
        led.plotBrightness(X, Y, 51 * list[Y][X])
    }
}
basic.forever(function () {
    for (let Y = 0; Y <= 4; Y++) {
        for (let X = 0; X <= 4; X++) {
            led.plotBrightness(X, Y, 51 * list[Y][X])
        }
    }
    list.unshift(list.pop())
    basic.pause(100)
})
