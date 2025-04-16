# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.




define teacher = Character("Mrs. E.")
define benny = Character("Benny")

define points = 0

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy

    # These display lines of dialogue.

    #e "You've created a new Ren'Py game."

    #e "Once you add a story, pictures, and music, you can release it to the world!"

    "Welcome to... the game"

    python:
        name = renpy.input("Input your name (optional):")

        name = name.strip() or "Jack"

        currentChallenge = "ClassroomChallenge1"

    define mc = Character("[name]")

    #jump ClassroomChallenge1

    #"Select a scenario:"

    menu mainMenu:

        # "Select a scenario:"
        #
        # "[mc] turns in homework":
        #     $ currentChallenge = "ClassroomChallenge1"
        #
        # "[mc] knows the answer":
        #     $ currentChallenge = "ClassroomChallenge2"
        #
        # "[mc] and the spelling test":
        #     $ currentChallenge = "ClassroomChallenge3"

        "Select a... select an option:"

        "[mc] in the classroom":
            jump classRoomSubMenu
        "[mc] on the playground":
            jump playgroundMenu
        "[mc] at home":
            jump atHomeMenu



    menu classRoomSubMenu:

        "Select a scenario:"

        "[mc] turns in homework":
            $ currentChallenge = "ClassroomChallenge1"

        "[mc] knows the answer":
            $ currentChallenge = "ClassroomChallenge2"

        "[mc] and the spelling test":
            $ currentChallenge = "ClassroomChallenge5"

        "[mc] sees a squirrel":
            $ currentChallenge = "squirrelChallenge"

        "[mc] and the math test":
            $ currentChallenge = "classRoomChallenge3"

        "Go Back":
            jump mainMenu

    jump expression currentChallenge

    # label classRoomSubMenu:
    #
    #     $ options = [
    #         ("[mc] turns in homework", SetVariable("currentChallenge", "ClassroomChallenge1")),
    #         ("[mc] knows the answer", SetVariable("currentChallenge", "ClassroomChallenge2")),
    #         ("[mc] and the spelling test", SetVariable("currentChallenge", "ClassroomChallenge5")),
    #         ("[mc] sees a squirrel", SetVariable("currentChallenge", "squirrelChallenge")),
    #         ("[mc] and the math test", SetVariable("currentChallenge", "classRoomChallenge3")),
    #         ("Go Back", Jump("mainMenu")),
    #     ]
    #
    #     call screen scrollable_menu(options)

    menu playgroundMenu:

        "There is currently nothing here"

        "Go back":
            jump mainMenu

    jump expression currentChallenge

    menu atHomeMenu:

        "There is currently nothing here"

        "Go back":
            jump mainMenu



    #jump expression currentChallenge



label badEnd:

    "You think of how that could have gone differently..."

    jump expression currentChallenge

label goodEnd:

    # Might be worth it to put a little firework effect or something here.

    "Congratulations! You did it!"
    python:
        points = points + 1

    return
