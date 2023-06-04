## Classroom Challenge 3 ##
# In this challenge, the main character is about to take a spelling test
# but realizes taht they don't have a pencil. This one goes over their options
# in that scenario

define d = Character("Desk Neighbor")

label ClassroomChallenge3:

    """

    It's morning.

    You're at school, sitting at your desk, ready to start your school day.

    At the front of the class, you hear your teacher say...

    """

    teacher "Ok class. Our spelling test is about to begin. Everyone clear your desks and take out a pencil"

    "All of a sudden..."

    "You realize..."

    "You don't have a pencil!"

    "Time to consider your options"

    menu:

        "Time to consider your options"

        "Your desk neighbor has two pencils on their desk. Surely they won't mind if you grab one...":
            jump .bad1

        "Raise your hand and ask [teacher] for a pencil":
            jump .good1

        "Ask the person next to you for a pencil":
            jump .challengeA2

        "Get up and go get a pencil from your backpack":
            jump .challengeA3

label .bad1:

    "You quickly nab one off the desk of the person who sits next to you."

    "You figure they didn't notice. But whether they saw you or they just happened to recognize their own pencil in your hand..."

    "It doesn't matter. Because they know that the pencil you have is their's."

    #Should probably have the deskmate appear here

    d "HEY! That's my pencil"

    "You quickly try to shush them and say things like \"It's not a big deal\" and \"I'll give it back after the spelling test\""

    "But their hand is up and you're about to get told on."

    "You start to consider your options. But it's too late to do anything. [teacher] is already on her way over to your desks"

    show eileen happy

    teacher "And what is going on over here?"

    d "[mc] took my pencil!"

    mc "I don't see what the big deal is! They've got two and I need one for the spelling test"

    teacher "[mc], taking things without asking is wrong."

    mc "But I need..."

    #should probably change emotion of teacher to angry here

    "You start to push your argument. But you're quickly cut off"

    teacher "no buts. Now give that pencil back to your desk Neighbor"

    "You begrudgingly hand the pencil back to your deskmate"

    # hide the deskmate at this point

    teacher """Now I will loan you one from my desk. But this sort of behavior is unnacceptable!

    As such, you are losing your recess privileges for the day!

    """

    hide eileen happy

    jump badEnd

label .good1:

    "You raise your hand and wait patiently."

    "You're not really sure how this is going to play out..."

label .good2:

    show eileen happy

    teacher "What is it, [mc]? Do you need something?"

    mc "Yes. I seem to have misplaced my pencil. Is there any chance that I can borrow one for this test?"

    teacher "Well, you can't very well take a spelling test without one. Here you go."

    "[teacher] hands you a pencil and now you're ready for the spelling test."

    hide eileen happy

    "It seems like this has played out about as good as it could have"

    jump goodEnd

label .challengeA2:

    "You figure the best course of action is to ask your deskmate if you can borrow one of their pencils"

    "Quietly, you ask..."

    mc "Hey, can I borrow a pencil"

    "... but it might not have been quiet enough. Immediately after asking, almost as if she heard you, you hear [teacher] say"

    teacher "If you need a pencil, please raise your hand and I will come around to give you one"

    "You think of what to do"

    menu:

        "You think of what to do"

        "Yell out \"I don't need your pencil\"":
            jump .bad2

        "Raise your hand and ask the teacher for a pencil":

            "You raise your hand and wait patiently."

            jump .good2

        "Raise your hand and ask if your can use your friend's pencil":
            jump .good3

label .bad2:

    "You stand up and yell..."

    mc "I don't need your pencil teacher!"

    "Already, you know that this isn't going to end well"

    # should definitely have the teacher looking unahappy Here
    show eileen happy

    teacher """ [mc]! That sort of behavior is unnacceptable!

    I will be calling your parents and, instead of taking the spelling test now,

    you're going to take it during afternoon recess.

    and I *will* be calling your parents, [mc]!

    """

    hide eileen happy

    "Just as you suspected, things did not go well."

    "You make your way to the hallway,"

    "and while out there,"

    jump badEnd

label .good3:

    "You raise your hand and wait patiently..."

    show eileen happy

    teacher "Yes, [mc], what is it? Do you need a pencil?"

    mc "Yes, but is it okay that I use my friend's pencil instead?"

    teacher """Well, we don't normally do that.

    But considering I'm running low on spare pencils for the class, I suppose that's fine.
    """

    "With permission from the teacher, you borrow your friend's pencil (after asking, course), and are ready to take your spelling test."

    jump goodEnd

label .challengeA3:

    "Without saying anything to anyone, your abruptly stand up from your desk and make a bee-line for the coat room."

    "You're certain you have a pencil in your backpack."

    "And after all, you will be needing one for the spelling test."

    "All of a sudden..."

    #gotta have unhappy teacher here
    show eileen happy

    teacher """[mc], what are you doing back here?

    Your suddenly leaving has been a major disruption to the class
    """

    "You try to explain yourself..."

    mc "But [teacher], I needed a pencil for my spelling test."

    teacher """Still, this is not how we do things.

    If you need a pencil, you're supposed to raise your hand and let me know.

    """

    """ You think that's kind of ridiculous.

    After all, how disruptive could you *really* have been?

    Still though, maybe she has a point. After all, rules are usually there for a reason.

    You consider what to do next

    """

    menu:

        "You consider what to do next"

        "Continue looking for your pencil in your bag":
            jump .bad3

        "Return to your seat, raise your hand, and ask the teacher for a pencil":
            jump .good4

label .bad3:

    """You decide to continue on with what you were doing.

    After all, you've come this far already.

    Probably best to explain that much to the teacher."""

    mc "It's fine. I'm already back here so I'm just going to grab a pencil from my backpack"

    teacher """No, it is not \"fine\", [mc]. Your behavior today has been unnacceptable!

    In fact, I've had enough. Go sit out in the hall while the rest of the kids take their spelling tests.

    And you can take yours during afternoon recess. Also, I *will* be calling your parents, [mc]"""

    hide eileen happy

    """Well this definitely could have gone better.

    You make your way out to the hall and have a sit.

    And while out there,"""

    jump badEnd

label .good4:

    hide eileen happy

    """You decide it's best to do what [teacher] says and make your way back to your seat.

    You might have mixed emotions about it - after all, how \"disruptive\" were you really - but this is definitely the best option.

    Once back, you raise your hand and ask [teacher] for a pencil.

    At this point, you're ready to take your spelling test and have also avoided getting in trouble!"""

    jump goodEnd
