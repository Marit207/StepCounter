let Stappen = 0
input.onGesture(Gesture.Shake, function () {
    if (input.isGesture(Gesture.Shake)) {
        Stappen += 1
        basic.showNumber(Stappen)
    }
})
