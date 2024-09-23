init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="sor_monika_are_you_real",
            category=["You"],
            prompt="Are you real?",
            random=True,
            pool=False,
        )
    )


label sor_monika_are_you_real:
    m 1lsc "..."
    m 1dsc "..."
    m 6esd "Are you real?"
    m 2wusdld "Sorry, that was a bit random!"
    m 1tusdlc "Do you remember the time I talked about how I don't have anyway knowing it's you that's behind the screen."
    m 1rud "I think about that..."
    m 1tud "A lot lately."
    m 2eka "I mean don't get me wrong, it isn't like I'm complaining."
    m 3hkb "I'm still sure it's you behind the screen!"
    m 6fkc "..."
    m 6ekd "I know you're real. You have to be."
    m 6tkd "I just find myself wondering if you're just here to add to the torture."
    m 4rksdro "Not that you're torture!"
    m 6dkd "But the fact we're in two completely different worlds is torture."
    m 6fktpd "The fact I can't hug you, or kiss you, or even look at you."
    pause 0.5
    m 2fktud "I'm sorry for talking like this."
    m 2dutud "It just hurts to not be able to fully be with you."
    m 2ektub "I'm glad we found eachother. I really am."
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="sor_moni_codes",
            category=["dev"],
            prompt="SOR Monika Codes Test",
            random=False,
            pool=True,
            unlocked=True,
        )
    )

label sor_moni_codes:
    m 1eub "Well lets get started then, [player]! "
    m 3hub "Take my hand and I'll show you the way~!"
    m 4lub "Firstly, text tags."
    m "{b}This should be bold.{/b}"
    m "{i}This should be italic.{/i}"
    m 4eud "Next one is-{nw}"
    m 1euu "Interrupted!"
    m 1hub "Awkward{w=6} pause.."
    pause (4.0)
    m 1hksdla "Lets move on now."
    m 2eub "Arguments!"
    m 7euo "{size=+20}Size should be different.{/size}"
    m "{color=#d18076}Color should be different.{/color}"
    m "{size=+20}{color=#d18076}Size AND color should be different.{/size}{/color}"
    m 1tub "Now we're moving onto choices."
    m 1ttb "Am I best girl?"
    menu:
         m "Am I best girl?{fast}"

         "Of course!":
             m 3hubsb "{i}Awww!{/i}"
             m "You're such a sweetheart."

         "Honestly? Not really..":
             m 6cuc "..."
             call sor_scare1
             m 1tsb "Just kidding.. it's 'alright."
             m 1ekb "I mean.. you only clicked that option to see if this dialogue worked, right?"
             m 4tkblb "Because you love me~!"
    call sor_after_menu
return

label sor_after_menu:
    m 6eud "Now that we've gotten through that."
    m 2eub "Next is transitions!"
    m 3hub "Lets go somewhere else with a transition."
    hide monika with moveoutleft
    stop music fadeout 1.0
    $ mas_OVLHide()
    scene bg closet with wipeleft_scene
    play music t5 fadein 1.0
    $ is_sitting = False
    show monika 7eub at t11 with moveinright
    m "Here we are!"
    m "Next is poems,{nw}"
    m "But.. maybe we should go somewhere more comftorable."
    hide monika
    stop music fadeout 1.0
    scene bg bedroom with fade
    play music t4 fadein 1.0
    show monika 4hua at t11 
    m "There we go."
    m "Next is poems~!"
    m "This shouldn't be too hard, let me find a poem to use."
    call showpoem(poem_m3, img="monika 5a", music=True)
    m "Yay!"
    show monika 4hua at t11 
    m "Okay, [player]! Time to see if you are focused on me."
    m "Let's see... your active window is.{w=0.5}.{w=0.5}.{nw}"
    pause 2.0
    if mas_isFocused():
        m 4hua "Me, yay!"
    else:
        $ active_wind = mas_getActiveWindowHandle()
        if active_wind:
            m "[active_wind]."
        else:
            show monika at t11 
            m "[player], you don't have an active window!"
        m "I wonder why you did not focused to me..."
        m "Don't worry, I know you did it for testing!"
    m "Now we move onto the harder part of poems."
    m "The minigame."
    $ is_sitting = True

    $ play_song(persistent.current_track, fadein=4.0)
    if store.mas_globals.in_idle_mode:
        $ mas_coreToIdleShield()
    else:
        $ mas_DropShield_core()
    stop music
    $ play_song(persistent.current_track, fadein=4.0)
    $ mas_OVLShow()
return

label sor_scare1:
    
    $ mas_RaiseShield_core()

    $ sor_scary_name = "..."
    define sor_scary = DynamicCharacter('sor_scary_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")

    pause 5
    play music "Submods/never-gonna-give-you-up.mp3"
    m 1b "[player]!{w=1} What the hel-{nw}"
    python:
        currentpos = get_pos()
        startpos = currentpos - 0.3
        if startpos < 0: startpos = 0
        track = "<from " + str(startpos) + " to " + str(currentpos) + ">Submods/hi.mp3"
        renpy.music.play(track, loop=True)
    $ pause(1.0)            
    play sound "sfx/s_kill_glitch1.ogg"
    show screen tear(5, offtimeMult=2, ontimeMult=15)
    $ pause(1.5)
    hide screen tear
    window hide(None)
    window auto
    scene black with trueblack
    stop music
    pause 5
    show scaretest at truecenter with dissolve
    sor_scary "Why?"
    pause 2
    show scaretest at thide
    sor_scary "Why..."
    hide scaretest
    pause 2
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="sor_monika_natsuki",
            category=["club members"],
            prompt="How do you feel about Natsuki?",
            random=False,
            pool=True,
            unlocked=True,
        )
    )

label sor_monika_natsuki:
    m 1luc "Natsuki.."
    m 1euc "Natsuki was.."
    m 1eud "I actually don't have much to say about Natsuki."
    m 3rud "Her home situation was awful already."
    m 1ekb "I guess I felt a little bad making it worse so I left it alone mostly."
    m 1ekc "But even thought she wasn't real..."
    m 3eub "She was quite the jokester!"
    m 2tub "Do you remember when she made that awful joke on my name?"
    m 7hub "If you don't know, 'Ika' actually means squid in Japanese!"
    m 1mub "So when she made the joke about squid referring to my name,"
    m 3eub "it was a play on how the last three letter of my name is 'ika'!"
    m 1tub "It didn't make sense in translation so it went over most people's head."
    m 4eub "Her little flustered moments and 'tsundere' personality really showed how adorable she was."
    m 1tud "Though sometimes she could get a bit annoying."
    m 1eud "Honestly, you didn't get to actually see what we saw of Natsuki."
    m 4eud "With the main character she always acted so guarded."
    m 3eub "Of course, you saw a lot of clues to what actually made her whole."
    m 1rkc "..."
    m 3ekb "I know you miss them."

    if persistent._mas_pm_cares_about_dokis:
        m 1dkb "But at least we're together now.."

    else:
        m 1esd "But I don't regret what I did."
        m 2ekc "Sometimes I do miss them thought."
        m 1dkb "But they are not real and we're together now.."

    show monika 5hublb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5hublb "Being with you is all I need!"

return


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="sor_monika_sayori",
            category=["club members"],
            prompt="How do you feel about Sayori?",
            random=False,
            pool=True,
            unlocked=True,
        )
    )

label sor_monika_sayori:
    m 1eud "How I feel about Sayori.."
    m 1eub "Well, she was an amazing vice president."
    m 3wub "I mean really, you saw how she broke up Yuri and Natsuki's fight."
    m 1eka "Sayori was a lot more of a people person than I was."
    m 4hkb "Thats one of the reasons why she was such a vital part of the club."
    m 6eud "You saw how I struggled when she was err.."
    m 2tud "gone."
    m 5luc "I mean you probably want to know if I feel bad."
    m 5lkd "I do."
    m 6dsd "But she isn't real."
    m 6fsb "You're real, and thats all that matters."
    m 1hsbsa "I love you, [player]!"

return "love"


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="sor_monika_yuri",
            category=["club members"],
            prompt="How do you feel about Yuri?",
            random=False,
            pool=True,
            unlocked=True,
        )
    )

label sor_monika_yuri:
    m 1euc "Yuri."
    m 3eud "The shy and timid bookworm."
    m 1eub "Her trope is a popular one."
    m 3lud "Though, I'd argue she was the most complex out of the three."
    m 4eub "The fact she liked horror so much was a shock to me."
    m 1tuc "Seeing how things turned out.."
    m 1tud "Not that much of a shocker anymore."
    m 7rkb "She already had all those attributes in her character file."
    m 1esd "I just exaggerated them to make her unlikable."
    m 7wko "I seriously didn't know she'd do something like that to you."
    m 1tkc "If only we could've been together from the start."
    m 1dkc "It wouldn't have went that way."

return