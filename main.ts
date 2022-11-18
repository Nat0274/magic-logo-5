input.onGesture(Gesture.LogoUp, function on_gesture_logo_up() {
    basic.showLeds(`
    . . # . .
    . # # # .
    # # # # #
    . . # . .
    . . # . .
    `)
})
input.onGesture(Gesture.LogoDown, function on_gesture_logo_down() {
    basic.showLeds(`
    . . # . .
    . . # . .
    # # # # #
    . # # # .
    . . # . .
    `)
})
