# Name: Hallie Jenkins

# morsecode.py

# Purpose: Translate plain text to morse code

# Certificate of Authenticity: I certify that this code is entirely
# my own work.

# Input: Plain text message
# Output: Message in morse code

from graphics import *


def main():
    # Store uppercase alphabet in string
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "

    # Store morse code alphabet in list
    morse_code = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.',
                  '....', '..', '.---', '-.-','.-..', '--', '-.',
                  '---', '.--.', '--.-', '.-.', '...', '-', '..-',
                  '...-', '.--', '-..-', '-.--', '--..', '   ']

    # Create window to host UI
    win = GraphWin("Morse Code Translator",400,400)

    # Create Entry box for user input
    in_box = Entry(Point(235,50),30)
    in_box.draw(win)

    # Create label for entry box
    in_box_label = Text(Point(75,50), "Message to code:")
    in_box_label.draw(win)

    # Create a button to prompt the user to click
    r_point_1 = Point(160,92.5)
    r_point_2 = Point(240,127.5)
    button = Rectangle(r_point_1,  r_point_2)
    button.draw(win)

    # Create label for button
    button_label = Text(Point((r_point_1.getX()+r_point_2.getX())/2,
                              (r_point_1.getY() + r_point_2.getY())/2),
                        "Encode")
    button_label.draw(win)
    
    # Wait for user to click
    win.getMouse()

    # Store user input in a string
    message = in_box.getText()

    # Create empty string for translated message
    morse_message = ""

    # For each letter in the message, find the index of that letter
    # in the alphabet string. Add the morse code at the corresponding
    # index to the translated message string.
    for letter in message:
        index = alphabet.find(letter.upper())
        morse_message += morse_code[index]

    # Create output area
    result_label = Text(Point(200,190),"Morse Code Message:")
    result_label.draw(win)

    # Show output
    result = Text(Point(200,200),morse_message)
    result.draw(win)

    # Instruct user to close window
    instructions = Text(Point(200,300), "Click anywhere to close "
                                        "window")
    instructions.draw(win)

    # Wait for mouse click
    win.getMouse()
    win.close()


main()
