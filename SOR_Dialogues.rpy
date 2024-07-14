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
    m 1tusdlc "Do you remember the I talked about how I don't have anyway knowing it's you that's behind the screen."
    m 1rud "I think about that..."
    m 1tud "A lot lately."
    m 2eka "I mean don't get me wrong, it isn't like I'm complaining."
    m 3hkb "I'm still sure it's you behind the screen."
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
    play music t3
    scene bg club_day
    show monika 1a at t11
    m "Hi [player]! "
    m 2e "I hope this goes well.."
    m 1b "Firstly, text tags."
    m 1a "{b}This should be bold.{/b}"
    m "{i}This should be italic.{/i}"
    m 2b "Next one is-{nw}"
    m 1k "Interrupted!"
    m 1a "Awkward{w=6} pause.."
    pause (4.0)
    m 4c "Lets move on now."
    m 1b "Arguments!"
    m 2a "{size=+20}Size should be different.{/size}"
    m 2a "{color=#d18076}Color should be different.{/color}"
    m 1d "{size=+20}{color=#d18076}Size AND color should be different.{/size}{/color}"
#this part is a bit unclear so look at https://www.renpy.org/doc/html/text.html from time to time
    m 1c "Now we're moving onto choices."
    m 5a "Am I best girl?"
    menu:
         m "Am I best girl?"

         "Of course!":
             m 1k "{i}Awww!{/i}"
             m 5a "You're such a sweetheart."

         "Honestly? Not really..":
             m 1i "..."
             call sor_scare1
             m 1e "Just kidding.. it's 'alright."
             m 4b "I mean.. you only clicked that option to see if this dialogue worked, right?"
             m 5a "Because you love me~!"
    call sor_after_menu
return

label sor_after_menu:
    m 2b "Now that we've gotten through that."
    m 4j "Next is transitions!"
    m 1b "Lets go somewhere else with a transition."
    hide monika with moveoutleft
    stop music fadeout 1.0
    scene bg closet with wipeleft_scene
    play music t5 fadein 1.0
    show monika 3k at t11 with moveinright
    m "Here we are!"
    m 2d "Next is poems,{nw}"
    m 2m "But.. maybe we should go somewhere more comftorable."
    hide monika with moveoutright
    stop music fadeout 1.0
    scene bg bedroom with fade
    play music t4 fadein 1.0
    show monika 1a at t11 with zoomout
    m "There we go."
    m 5a "This shouldn't be too hard, let me find a poem to use."
    call showpoem(poem_m3, img="monika 5a", music=True)
    m 1j "Yay!"
    m 1h "Okay, [player]! Time to see if you are focused to me."
    m 2d "Let's see... your active window is.{w=0.5}.{w=0.5}.{nw}"
    pause 2.0
    if mas_isFocused():
        m 1h "Me, yay!"
    else:
        $ active_wind = mas_getActiveWindowHandle()
        if active_wind:
            m 3c "[active_wind]."
        else:
            m 1b "[player], you don't have an active window!"
        m 2d "I wonder why you did not focused to me..."
        m 3m "Don't worry, I know you did it for testing!"
    m 4b "Now we move onto the harder part of poems."
    m 2e "The minigame."
    m 3k "Maybe I could get it in the first try, who knows?"
    $ from store.mas_poemgame_consts import MONIKA_MODE
    call mas_poem_minigame(MONIKA_MODE,gather_words=False,glitch_nb=True,
        glitch_words=(True,None,None),hop_monika=False,music_fadein=0.0,
        music_fadeout=0.0,music_filename=audio.ghostmenu,total_words=20,
        trans_fast=False,trans_in=False,trans_out=True,sel_sound=None) from _call_poem_minigame_three

    $ play_song(persistent.current_track, fadein=4.0)
    if store.mas_globals.in_idle_mode:
        $ mas_coreToIdleShield()
    else:
        $ mas_DropShield_core()
    stop music
    $ play_song(persistent.current_track, fadein=4.0)
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
    m 1euc "Natsuki.."
    m 1eud "I actually don't have much to say about Natsuki."
    m 3rud "Her home situation was awful already."
    m 1ekb "I guess I felt a little bad making it worse so I left it alone mostly."
    m 1ekc "Even if she isn't real."
    m 4hub "She was actually pretty funny."
    m 4eub "Her little flustered moments and 'tsundere' personality really showed how adorable she was."
    m 1tud "Though sometimes she could get a bit annoying."

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