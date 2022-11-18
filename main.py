def on_gesture_logo_up():
    basic.show_leds("""
    . . # . .
    . # # # .
    # # # # #
    . . # . .
    . . # . .
    """)
input.on_gesture(Gesture.LOGO_UP, on_gesture_logo_up)
def on_gesture_logo_down():
    basic.show_leds("""
    . . # . .
    . . # . .
    # # # # #
    . # # # .
    . . # . .
    """)
input.on_gesture(Gesture.LOGO_DOWN, on_gesture_logo_down)
