##Classroom challenge 5
# In this one, the main character doesn't have their math book... and then
# there are some option for them on how to proceed


label ClassroomChallenge5:

    """It's afternoon.

    You've just gotten back from recess...

    and that means it's time for math.

    At the front of you the class, you hear the teacher..."""

    show eileen happy

    teacher "Ok class, it's time to learn some math, and you know what that means..."

    teacher "It's time to get out your math books."

    """You go to get your math book out.

    But there's just one problem...

    It seems that you don't have your math book.

    This could be problematic. But maybe you could salvage the situation.

    You consider your options..."""

    menu:

        "You consider your options..."

        "Stand up and yell out \"I don't have my book\"":
            jump .bad1

        "Raise your hand and let the teacher know":
            jump .good1

        "Quietly ask the person next to you if you can read off of their book":
            jump .challengeA2

        "Ignore the teacher. Just act like you didn't hear her. But try not to be too conspicuous.":
            jump .challengeA3

    label .bad1:

        "You stand up. And at the top of your lungs..."

        mc "[teacher], I don't have my math book"

        "Right away, you have a feeling that things are about to go really bad."

        teacher "[mc] sit down!"

        "But you persist."

        mc "But I don't have my book!"

        teacher "Even so, that is not how you communicate that. You're being incredibly disruptive."

        teacher ""
