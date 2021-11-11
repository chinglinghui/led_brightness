let list = [
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
for (let index = 0; index <= 24; index++) {
    if (list[1][index % 5 + 1] == 0) {
        led.toggle(Math.floor(index / 5), index % 5)
    }
}
basic.forever(function () {
	
})
