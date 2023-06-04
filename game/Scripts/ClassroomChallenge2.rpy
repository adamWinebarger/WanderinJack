##Classroom Challenge 2
# In this one, the player character is in class and the teacher asks a question
# mc knows the answer and is so excited that they know the answer that they can
# barely contain themself. So they're presented with options that baiscally amount to
# yelling out the answer, raising their hand, bouncing up and down in their seat,
# or shouting "pick me". That's basically what's going on here

init python:
    answers = ["7", "Henry Ford", "The War of 1812", "William Howard Taft", "144", "Napoleon",
        "Waterloo", "Normandy", "81", "42", "Orange", "Lincoln", "Washington D.C"]

label ClassroomChallenge2:

    "It's the middle of the day and you're in class."

    "The teacher is teaching and the subject she's teaching is surprisingly easy."

    "The teacher asks a question..."

    #Make this part bold if you can
    "And holy wow you know the answer!"

    "Like, this isn't even a hard question"

    "The answer is so obvious. WHY HAS NO ONE SAID IT YET?"

    "Your practicallay bursting at the seems ready to yell it out."

    show eileen happy

    teacher "Does anyone know the answer?"

    "WHAT ARE WE GOING TO DO???"

    menu:

        "WHAT ARE WE GOING TO DO???"

        "Yell out the answer. Just yell it out!":

            $ randomValue = renpy.random.randint(0, len(answers) - 1)
            $ answer = answers[randomValue]

            mc "The answer is [answer]!"

            jump .bad1

        "Raise your hand and wait to be called on":
            jump .callPossible

        "Raise you hand. But be sure to wave it around and maybe move around in your seat. Gotta make sure [teacher] can see you.":
            jump .challengeA2

        "Raise your hand and yell out \"Pick Me!\" so that you know that she knows that you know the answer":
            jump .challengeA3

label .callPossible:
    $ randomValue = renpy.random.randint(1,100)

    if randomValue > 50:
        jump .calledOn
    else:
        jump .notCalledOn

label .bad1:

    teacher "[mc] that is unnacceptable. Raise your hand and wait to be called on!"

    mc "But [teacher], that's the right answer, right?"

    teacher "[mc], you're being disruptive and disrespectful!"

    mc "But I'm right!"

    "At this point, [teacher] is visibly upset."

    teacher "If you're going to be disruptive, then go sit out in the hall!"

    hide eileen happy

    "Despite being right, the fact that you blurted out the answer rather than waiting to be called on - disrupting the class in the process - led to you getting in trouble"

    "While out in the hall, you have plenty of time to think of how that played out."

    jump badEnd

label .calledOn:

    teacher "Yes, [mc]"

    $ randomValue = renpy.random.randint(0, len(answers) - 1)
    $ answer = answers[randomValue]

    mc "The answer is [answer]!"

    teacher "Very good! That's correct."

    "[teacher] continues teaching the subject and you feel proud that you knew the answer."

    jump goodEnd

label .notCalledOn:

    "Despite raising your hand and doing everything the right way, the teacher called on someone else."

    "That other person said the answer, which was the same answer that you had."

    "And that's kind of a bummer... but it could be worse. At least you didn't get in trouble, right?"

    jump goodEnd

label .challengeA2:

    "You raise your hand. But you can barely contain yourself."

    "You're bouncing up and down in your seat and hoping to God that [teacher] calls on you."

    #If we have a teacher sprite up, we should probably change the expression to unhappy right here

    "[teacher] is looking right at you but she doesn't look happy. But you're not going to let that slow you down."

    teacher "Now class, I need you all to settle down and *calmly* raise your hands if you know the answer"

    """
    She said \"class\" but you have a sneaking suspicion that she was referring to you specifically

    It might be time to re-evaluate your strategy...
    """

    menu:

        "It might be time to re-evaluate your strategy..."

        "Settle down and calmly raise your hand":
            jump .callPossible

        "Blurt out the answer. Just send it!":
            jump .bad1

label .challengeA3:

    "You raise your hand. But you're also sure to shout \"Pick me!\" repeatedly so that [teacher] knows you have the answer."

    #change the teacher sprite to unhappy here

    teacher "Now class, let's remember that raising your hand is something you do *quietly* and that we wait until we're called on to speak"

    """
    Well, she definitely heard you.

    And even though she said \"class\" but you have a sneaking suspicion that she was referring to you specifically

    It might be time to re-evaluate your strategy...
    """

    menu:

        "It might be time to re-evaluate your strategy..."

        "Settle down and calmly raise your hand":
            jump .callPossible

        "Just yell it out. Go for it!":
            jump .bad1

        "Realize you don't know the answer and put your hand down":

            hide eileen happy

            "You realize you don't know the answer and decide to put your hand down"

            "[teacher] calls on someone else who then answers the question"

            "You realize that the way you approached the situation could have been better but you were still able to turn things around and get a good outcome after realizing your first mistake."

            "And you didn't get in trouble. So that's always nice."

            jump goodEnd
