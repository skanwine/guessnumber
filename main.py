def on_button_pressed_a():
    global tensDigit, guessNumber
    tensDigit += 1
    tensDigit = tensDigit % 10
    guessNumber = tensDigit * 10 + unitDigit
input.on_button_pressed(Button.A, on_button_pressed_a)

def beginGame():
    global targetNumber
    targetNumber = randint(1, MAX_NUMBER)
    resetVar()
    basic.show_string("?")

def on_button_pressed_ab():
    global state
    if guessNumber > 0:
        state = "Determine"
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global unitDigit, guessNumber
    unitDigit += 1
    unitDigit = unitDigit % 10
    guessNumber = tensDigit * 10 + unitDigit
input.on_button_pressed(Button.B, on_button_pressed_b)

def resetVar():
    global state, unitDigit, tensDigit, guessNumber
    state = "Init"
    unitDigit = 0
    tensDigit = 0
    guessNumber = 0
targetNumber = 0
unitDigit = 0
guessNumber = 0
tensDigit = 0
MAX_NUMBER = 0
state = ""
state = "Init"
MAX_NUMBER = 99
beginGame()

def on_forever():
    if state == "Init":
        if guessNumber > 0:
            basic.show_string(" ")
            basic.show_number(guessNumber)
    else:
        if guessNumber == targetNumber:
            basic.show_icon(IconNames.YES)
            soundExpression.happy.play()
            basic.pause(1000)
            beginGame()
        elif guessNumber > targetNumber:
            basic.show_icon(IconNames.NO)
            basic.show_icon(IconNames.STICK_FIGURE)
            soundExpression.sad.play()
        else:
            basic.show_icon(IconNames.NO)
            basic.show_leds("""
                . . # . .
                . . # . .
                # . # . #
                . . # . .
                . # # . .
                """)
            soundExpression.sad.play()
        resetVar()
basic.forever(on_forever)
