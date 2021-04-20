input.onButtonPressed(Button.A, function () {
    tensDigit += 1
    tensDigit = tensDigit % 10
    guessNumber = tensDigit * 10 + unitDigit
})
function beginGame () {
    targetNumber = randint(1, MAX_NUMBER)
    unitDigit = 0
    tensDigit = 0
    guessNumber = 0
    basic.showString("?")
}
input.onButtonPressed(Button.AB, function () {
    if (guessNumber > 0) {
        tempGuestNumber = guessNumber
        unitDigit = 0
        tensDigit = 0
        guessNumber = 0
        if (tempGuestNumber == targetNumber) {
            basic.showIcon(IconNames.Yes)
            soundExpression.happy.playUntilDone()
            basic.pause(2000)
            beginGame()
        } else if (tempGuestNumber > targetNumber) {
            basic.showIcon(IconNames.No)
            basic.showIcon(IconNames.StickFigure)
        } else {
            basic.showIcon(IconNames.No)
            basic.showLeds(`
                . . # . .
                . . # . .
                # . # . #
                . . # . .
                . # # . .
                `)
        }
    }
})
input.onButtonPressed(Button.B, function () {
    unitDigit += 1
    unitDigit = unitDigit % 10
    guessNumber = tensDigit * 10 + unitDigit
})
let tempGuestNumber = 0
let targetNumber = 0
let unitDigit = 0
let guessNumber = 0
let tensDigit = 0
let MAX_NUMBER = 0
MAX_NUMBER = 99
beginGame()
basic.forever(function () {
    if (guessNumber > 0) {
        basic.showString(" ")
        basic.showNumber(guessNumber)
    }
})
