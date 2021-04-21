input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    tensDigit += 1
    tensDigit = tensDigit % 10
    guessNumber = tensDigit * 10 + unitDigit
})
function beginGame() {
    
    targetNumber = randint(1, MAX_NUMBER)
    resetVar()
    basic.showString("?")
}

input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    
    if (guessNumber > 0) {
        state = "Determine"
    }
    
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    unitDigit += 1
    unitDigit = unitDigit % 10
    guessNumber = tensDigit * 10 + unitDigit
})
function resetVar() {
    
    state = "Init"
    unitDigit = 0
    tensDigit = 0
    guessNumber = 0
}

let targetNumber = 0
let unitDigit = 0
let guessNumber = 0
let tensDigit = 0
let MAX_NUMBER = 0
let state = ""
state = "Init"
MAX_NUMBER = 99
beginGame()
basic.forever(function on_forever() {
    if (state == "Init") {
        if (guessNumber > 0) {
            basic.showString(" ")
            basic.showNumber(guessNumber)
        }
        
    } else {
        if (guessNumber == targetNumber) {
            basic.showIcon(IconNames.Yes)
            soundExpression.happy.play()
            basic.pause(1000)
            beginGame()
        } else if (guessNumber > targetNumber) {
            basic.showIcon(IconNames.No)
            basic.showIcon(IconNames.StickFigure)
            soundExpression.sad.play()
        } else {
            basic.showIcon(IconNames.No)
            basic.showLeds(`
                . . # . .
                . . # . .
                # . # . #
                . . # . .
                . # # . .
                `)
            soundExpression.sad.play()
        }
        
        resetVar()
    }
    
})
