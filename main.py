Stappen = 0

def on_gesture_shake():
    global Stappen
    if input.is_gesture(Gesture.SHAKE):
        Stappen += 1
        basic.show_number(Stappen)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
