def on_button_pressed_a():
    global tensDigit, guessNumber
    tensDigit += 1
    tensDigit = tensDigit % 10
    guessNumber = tensDigit * 10 + unitDigit
input.on_button_pressed(Button.A, on_button_pressed_a)

def beginGame():
    global state, targetNumber, unitDigit, tensDigit, guessNumber
    state = "Init"
    targetNumber = randint(1, MAX_NUMBER)
    unitDigit = 0
    tensDigit = 0
    guessNumber = 0
    basic.show_string("?")

def on_button_pressed_ab():
    global tempGuestNumber, unitDigit, tensDigit, guessNumber
    if guessNumber > 0:
        tempGuestNumber = guessNumber
        unitDigit = 0
        tensDigit = 0
        guessNumber = 0
        if tempGuestNumber == targetNumber:
            basic.show_icon(IconNames.YES)
            soundExpression.happy.play_until_done()
            basic.pause(2000)
            beginGame()
        elif tempGuestNumber > targetNumber:
            basic.show_icon(IconNames.NO)
            basic.show_string("Smaller")
        else:
            basic.show_icon(IconNames.NO)
            basic.show_string("Larger")
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global unitDigit, guessNumber
    unitDigit += 1
    unitDigit = unitDigit % 10
    guessNumber = tensDigit * 10 + unitDigit
input.on_button_pressed(Button.B, on_button_pressed_b)

tempGuestNumber = 0
targetNumber = 0
state = ""
unitDigit = 0
guessNumber = 0
tensDigit = 0
MAX_NUMBER = 0
MAX_NUMBER = 99
beginGame()

def on_forever():
    if guessNumber > 0:
        basic.show_number(guessNumber)
basic.forever(on_forever)
