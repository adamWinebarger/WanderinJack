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
            jump .bad2

    label .bad1:

        "You stand up. And at the top of your lungs..."

        mc "[teacher], I don't have my math book"

        "Right away, you have a feeling that things are about to go really bad."

        show eileen happy

        teacher "[mc] sit down!"

        "But you persist."

        mc "But I don't have my book!"

        teacher "Even so, that is not how you communicate that. You're being incredibly disruptive."

        mc "But I don't *have my book* Mrs. E.! What am I going to do???"

        "You say it with some emphasis to really try and get the point across"

        teacher "I'll tell you what you're going to do. You're going to go to the prinicipal's office!"

        "So now here you are, on your way to the principle's office"

        jump badEnd

    label .good1:

        "You put your hand up..."

        "... and patiently wait to be called on."

        "Mrs. E eventually calls on you after what seems like forever."

        teacher "Yes, [mc], what is it?"

        mc "[teacher], I forgot my math book"

        teacher "That's fine, you can use the spare we keep in the class. But you really should remember to bring it next time."

        "While this may have been a bit of a setback, at least it wasn't a disaster."

        "You should really remember your book next time. lol"

        jump goodEnd

    label .challengeA2:

        "You decide the best thing to do here is ask [benny] if you can read off of his textbook."

        "So you try to lean over and quietly go..."

        mc "Hey [benny], I don't have my book. Can I read off of yours?"

        teacher "If you forgot your math book please let me know and you can grab a spare from the front."

        teacher "But you *will* be needing your own book for the assignment"

        "Man, it's almost like she could see what you were trying to do there. But at the same time, it sounds like we're not in trouble yet."

        menu:

            "What should we do here?"

            "Stay the course and ask [benny] to share his book again":
                jump .possiblyBad1

            "Do like [teacher] said and go get a book from the front of the class":
                jump .good2

            "Ask the teacher if you can share books with [benny]":
                jump .possiblyBad2

            ## We might throw a 4th one in there at some point... idk
            # "Just sit there and try to look inconspicuous":
            #     jump .

    label .possiblyBad1:

        "Even though [teacher] told you to get a book from the front, you decide that the best option here is to ask [benny] again to borrow his math book."

        mc "Come on, [benny], what's the issue here?"

        benny "Didn't [teacher] {i}just{/i} say that you should go get a book from the front?"

        mc """Yeah

        but...

        like...

        It's really far...

        and I don't feel like going up there.

        and this is easier anyways"""

        "While this was going on, you didn't even notice [teacher] walk up"

        show eileen happy

        teacher """[mc], [benny],

        Didn't you hear me say that if you needed a math book that you should come get one from the front?"""

        mc "Well, yeah but-"

        teacher "But nothing. You're both being very disruptive to the class."

        teacher "Go wait out in the hall. Both of you"

        """Well, you've really done it now.

        It doubly stings since, not only did you get in trouble, but you also got [benny] in trouble.

        Something tells me he's going to be mad about this for a while."""

        jump badEnd

    label .good2:

        "You decide the best thing to do is go to the front and grab a book."

        show eileen happy

        teacher "Thank you for letting me know that you didn't have your book [mc]. In the future, be sure to remember to bring it to class."

        "Despite the minor setback. You handled the situation well and didn't get in trouble. Good job."

        jump goodEnd

    label .possiblyBad2:

        "Despite what's happened, you decide that the best thing to do here is ask [teacher] if you can share your book with [benny]"

        "... in spite of the fact that [benny] didn't agree to this."

        show eileen unhappy

        mc "[teacher] can I share books with [benny]"

        teacher "No, [mc]. {i}If you need a math book, come up here and get one of the extra ones{/i}"

        "[teacher] seems a little irritated. But it seems like you're not quite in trouble yet."

        menu:

            "What do you want to do?"

            "Keep insisting that you use [benny]'s book":
                jump .bad4

            "Go up and get a spare math book from the front":
                jump .good2 #should we maybe have a slightly different ending for this one? Idk

    label .bad4:

        teacher """[mc] your are being really disruptive right now. 

        Go to the principles office!

        """ ##Maybe we should come back and fix the dialogue on this one a bit but I don't really feel like doing that right now


    label .challengeA4:

        """You don't have your book but you don't want to get in trouble.

        Also, you don't {i}really{/i} want to do the math work today.

        So the best course of action is definitely to sit here and do nothing.

        The trick is going to be not looking too suspicious while you do it.

        So everyone begins working on their stuff, 

        you see [benny] working diligintly away,

        you look out the window and see a few birds. It really is a nice day out. 

        With the peacefulness of outside, you start to doze off...

        You dream of a world that looks a lot nicer than this one...

        Unitl...

        """

        teacher 2x"[mc] what do you think you're doing?"

        "Shoot"

        "We might've been {i}too{/i} inconspicous"

        teacher "[mc], if you're going to sleep in my class, then you can leave"

        teacher "Go to the principle's office!"

        #Should probably do a scene transition right here

        """Well, we really did it now.

        We probably should have just gotten a book when [teacher] said to.

        """

        jump badEnd


