input.onButtonPressed(Button.A, function () {
    for (let Y = 0; Y <= 4; Y++) {
        for (let X = 0; X <= 4; X++) {
            led.plotBrightness(X, Y, 51 * list[Y][X])
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
while (!(input.buttonIsPressed(Button.A) || input.buttonIsPressed(Button.B) || input.buttonIsPressed(Button.AB))) {
    for (let Y = 0; Y <= 4; Y++) {
        for (let X = 0; X <= 4; X++) {
            led.plotBrightness(X, Y, 51 * list[Y][X])
        }
    }
    list.unshift(list.pop())
    basic.pause(100)
}
basic.clearScreen()
basic.forever(function () {
	
})
