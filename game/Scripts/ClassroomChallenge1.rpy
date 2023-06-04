
##Classroom challenge 1##
# In this challenge, the main character has to get their homework out for the
# teacher, but gets distracted talking to their friends. In the process, mc
# forgets to grab their homework until the teacher comes around and has to ask
# mc to get their homework out and hand it in.
#
# This chanllenge examines the options that mc can/should go through in this
#scenario

init python:
    show = "Space Rangers"

label ClassroomChallenge1:

    "It's afternoon in the class."

    "You've just finished up with lunch and are now back in the classroom, ready to learn."

    "You hear the teacher's voice from elsewhere in the class"

    teacher "Now class I'll be coming around to collect your homework shortly. So have it ready!"

    "You start to get it out. But then your friend [benny] starts talking to you..."

    benny "Hey [mc] did you see the new episode of [show] last night?"

    mc "Yeah! It was awesome"

    "You and [benny] start talking about last night's TV show and you totally lose track of what you were doing."

    "Before you know it, the teacher is at your desk."

    show eileen happy

    teacher "[mc], do you have your homework?"

    "You think of what to say..."

    menu:

        "You think of what to say..."

        "I'm busy":
            jump .badOutcome

        "(Grab Binder and hand homework to teacher) Here you go.":
            jump .goodOutcome

        "Can I hand it in later?":
            jump .challengeA2

        "(Ignore the teacher)":
            jump .challengeA3

label .badOutcome:

    teacher "[mc], that is unnacceptable behavior!"

    teacher "Your parents will be hearing about this."

    teacher "Now go to the principals office."

    #Should probably change scene here

    hide eileen happy

    "You head to the principals office."

    "And on your way"

    jump badEnd

label .goodOutcome:

    teacher "Thank you [mc]. I'm sure you worked very hard on this and it will show."

    #Teacher disappears here

    hide eileen happy

    "Once the teacher has left, you and [benny] go back to talking about [show] until it's time to do the next thing"

    jump goodEnd

label .goodOutcomeB:

    "You quickly grab your homework from your bag"

    "After all, that is what you were in the process of doing before you got distracted talking to [benny]"

    teacher "In the future, I would appreciate it if you could have your homework ready *before* I get to you"

    teacher "But I'm glad you had it done on time"

    jump .goodOutcome

label .challengeA2:

    teacher "No you may not, [mc]."

    teacher "I need you to hand me your homework right now. You're holding up the class."

    menu:

        "Well, can you keep going around the classroom and come back to me in a bit?":

            teacher "No, [mc]. In fact, given how disrespectful you've been, I'm giving you a zero on this assignment."

            teacher "And I will be calling your parents."

            hide eileen happy

            jump badEnd

        "Ok! Here you go.":
            jump .goodOutcomeB

        "Sorry. Let me get it out":
            jump .goodOutcomeB

label .challengeA3:

    "[teacher] clears her throat."

    teacher "[mc], do you have your homework?"

    "You recognize the tone in her voice."

    "You're not quite *in* trouble yet but you will be if you make the wrong move here."

    "You think of what to do..."

    menu:

        "You think of what to do..."

        "(Continue ignoring [teacher])":
            jump .badOutcome

        "Sorry, I didn't hear you. Let me get that right now!":
            jump .goodOutcomeB

        "Ok [teacher]. Here you go!":
            jump .goodOutcomeB
