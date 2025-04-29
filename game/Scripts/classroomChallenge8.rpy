## Challenge8.rpy

"""

In this challenge, Jack is playing with a toy in secret while the teacher is teaching lessons,
and essentially has the choice to either put the toy away and go back to listening to the lesson,
show it to his friend and get the friend roped into these shennanigans, leading to both of them getting
in trouble, or he can talk to his friend about his toy or continue to play with it in secret.

So basically, the conflict comes from whether he decideds to stop playing with the toy and whether
he decides to do something that might get his friend in trouble

"""

define toldTeacherItWasAnActionFigure = False

label classroomChallenge8:

    $ toldTeacherItWanAnActionFigure = False

    """
    It's morning...

    Things are kind of boring right now.

    [teacher] is at the front of the class, teaching about American history or something like that.

    {i}But none of that is important right now{/i}

    What is important...

    is...

    the awesome new space rangers action figure that you got over the weekend!

    I mean it goes without saying that the obvious thing that you should be doing right now is playing with the cool new action figure that you brought to school today.

    However...

    You get the feeling that Mrs. E. might not feel the same way.

    That being said...

    She definitely hasn't noticed you playing with the Space Rangers figure under your desk yet.

    So if you put it back in your desk it would probably be like this whole thing never happened.

    But at the same time...

    You really want to show it to [benny].

    He was talking about how cool it was the other day and he'd be psyched to see that you got one!

    """

    menu:

        "What are you going to do?"

        "Get [benny]'s attention and show him your action figure":
            jump .bad1

        "Put the figure away and listen to [teacher].\nYou can show [benny] at recess":
            jump .good1

        "Wait to show it to [benny] until recess but keep playing with it under your desk":
            jump .challengeA1

        "Put the toy away but lean over and tell [benny] about it":
            jump .challengeA2

    label .bad1:

        """
        You decide the best thing to do is get [benny]'s attention and show him it right now...

        It might not be the best choice, but [benny] is going to be {i}so{/i} stoked when you show it to him.

        So you lean over and whisper...
        """

        mc "{size=-4}[benny]{/size}"

        mc "{size=-2}hey [benny]{/size}"

        "It looks like he started to turn his head before going back to his work."

        "Let's whisper louder"

        mc "Hey, [benny]!"

        benny "{size=-4}What, [mc]? We shouldn't be talking right now{/size}"

        mc "{size=-4}Hey [benny], check out my new Space Rangers action figure{/size}"

        benny "{size=-4}Cool. You should probably put it away though. [teacher] is teaching{/size}"

        "You feel yourself getting agitated."

        "You thought [benny] would be way more excited about this"

        "You haven't even realized you're starting to talk louder"

        "You also haven't realized that [teacher] has stopped teaching and is looking squarely at you and [benny]"

        benny "[mc], you're going to get us in troub-"

        teacher "{size=+4}[mc], [benny], hallway, {b}NOW{/b}{/size}"

        mc "But-"

        teacher "NOW!!!"

        ##Should probably do a scene change here

        """
        Welp. You really messed up this time.

        You got in trouble with [teacher],

        [benny] is mad at you,

        and you're probably not going to get to play with your new Space Rangers figure at recess
        """

        jump badEnd

    label .good1:

        """
        It is a pretty cool action figure...

        But it's probably best to put it away and listen to [teacher] as she's teaching her class.

        You subtly put your Space Rangers action figure back into your desk.

        You thought you saw [teacher] look in your direction as you were opening your desk.

        But if she noticed what you were up to she hasn't said anything.

        Seems like the best outcome to this situation and you can always show [benny] your Space Rangers figure at recess.

        He's definitely going to be stoked that you got that.
        """

        jump goodEnd

    label .challengeA1:

        """
        You figure it's best to show [benny] your new Space Rangers action figure at recess.

        But you're still going to play with it under your desk right now.

        What's the worst that could happen, right?

        It's not like [teacher] can see you right now.

        ...though it does seem like it's been a little too quite for a while now
        """

        teacher "[mc], what do you think you're doing back there?"

        "Uh oh"

        teacher "[mc], put that away and listen. It's class time right now. You can play with your toy at recess"

        menu .challengeA1Menu:

            "What do you do?"

            "Tell [teacher] \"No\". Put her in her place!":
                jump .bad2

            "Do what [teacher] says and put away the action figure":
                jump .good2

            "Let [teacher] know that it's an action figure, not a toy" if not toldTeacherItWasAnActionFigure:
                jump .challengeB1

    label .bad2:

        """
        You decide the best course of action is to tell [teacher] that you're tired of learning and that it's time to play now.

        This, predictably, does not end well.
        """

        teacher "[mc], I have had it with your attitude today! Go to the principle's office!"

        """
        Well, that definitely could have gone better.

        Perhaps acknowledging your mistake and doing what the teacher said would have been the better choice here.
        """

        jump badEnd

    label .challengeB1:

        "You decide to correct [teacher] on the egregious error she just made"

        mc "Actually, [teacher], it's not a \"toy\", it's an {i}action figure{/i}"

        teacher "Ok [mc]. Then put away the {i}action figure{/i} and pay attention"

        $ toldTeacherItWasAnActionFigure = True

        "Well that was quick"

        "[teacher] seems a little peeved with you right now. But it seems like you're not in trouble yet."

        jump .challengeA1Menu

    label .good2:

        "You decide to do what [teacher] says and put away the Space Rangers action figure."

        "Seems like it would be better to wait until recess to play with it anyways."

        "Mrs. E. looks a little annoyed but it seems like you're not in trouble. So good job with that."

        jump goodEnd

    label .challengeA2:

        "You decide that it would be better to put away your Space Rangers action figure for the time being."

        "But you've {i}gotta{/i} tell [benny] about it."

        "I mean he's {i}right there{/i}."

        "He's just looking forward not really doing anything. Maybe writing something in his notebook occasionally."

        "Wonder what that's about."

        "In any case, he {i}has{/i} to know about your totally awesome Space Rangers action figure that you got this weekend and he has to know right now."

        "So you lean over to whisper"

        mc "{size=-4}[benny]{/size}"

        mc "{size=-2}Hey, [benny]{/size}"

        benny "{size=-4}What is it, [mc]? It's the middle of class{/size}"

        mc "{size=-4}I got a new Space Rangers action figure over the weekend. It's pretty sweet{/size}"

        benny "{size=-4}That's cool, [mc]. Show me at recess{/size}"

        mc "{size=-2}Dude it's so awesome! You won't believe it, but it's arms can--{/size}"

        teacher "[mc], [benny], please be silent. I am trying to teach and you both are being disruptive."

        """Uh-oh

        It looks like [teacher] noticed you and [benny] were talking in the back.

        If you think about it, it's kind of impressive that she caught you guys because you both were being super quiet.

        In any case, she seems a little unhappy with you and [benny]. But you're not quite in trouble yet.
        """

        menu:

            "What do you want to do?"

            "Stop talking":
                jump .good3

            "Apologize, then sit quietly and listen":
                jump .good4

            "Wait until [teacher] starts teaching again and then start talking to [benny] again, more quietly this time":
                jump .bad4

            "Lie and say that you and [benny] weren't talking":
                jump .bad5

        label .good3:

            """
            You decide the best thing to do here is to stop talking.

            It might've been more polite to apologize. But [teacher] doesn't seem too bothered by it.

            [teacher] goes back to teaching and it seems like no further issue is going to arise from this.

            In any case, you're super excited to show [benny] your Space Rangers action figure at recess.
            """

            jump goodEnd

        label .good4:

            """
            You decide that the best course of action here is to apologize and stop talking.
            """

            mc "Sorry, [teacher], that was rude of us."

            teacher "Thank you, [mc]. Now let's get back to it."

            "[teacher] seemed annoyed to have to tell you guys to stop talking. But it seems like she appreciated your apology"

            "In any case, you {i}cannot wait{/i} to show [benny] your Space Rangers action figure at recess."

            jump goodEnd

        label .bad4:

            """
            You decide to quiet down and wait for [teacher] to go back to teaching.

            But this is only a ruse.

            {i}There's no way she's going to catch you talking to [benny] twice!{/i}
            """

            teacher "Now, where was I? So the War of 1812..."

            "Looks like everything is going to plan. Time to start talking to [benny] again."

            mc "[benny], so as I was saying before, my new Space Rangers action figure, his arms can actually-"

            teacher "[mc], [benny], hallway, NOW!!!"

            jump .bad5b

        label .bad5:

            mc "We weren't talking though!"

            """
            That's a lie.

            But there's no way she could have heard you guys talking from the front of the class.

            Since you don't want to get in trouble, the best choice here is to deny everything.
            """

            teacher "{b}[mc] I could see you and [benny] talking{/b}"

            "Uh-oh."

            "I guess we forgot that teachers could {i}see{/i} things."

            "This is likely going to end badly."

            teacher "If you're going to be disruptive, then you and [benny] can both go wait out in the hall."

        label .bad5b:

            benny "But-"

            teacher "No 'buts', you both have already lost your recess privileges for the day. Don't make me send you to the principal's office."

            teacher "{size=+4}Hallway. NOW!!!{/size}"

            """
            Welp. You really messed up this time.

            Somehow, it seems like [benny] got it worse than you did. Not sure how that happened.

            But unsurprisingly, he seems really mad at you. I don't think he's going to want to see your Space Rangers action figure at recess.

            In any case, you guys both lost your recess for the day anyways. So, there's also that.
            """

            jump badEnd
