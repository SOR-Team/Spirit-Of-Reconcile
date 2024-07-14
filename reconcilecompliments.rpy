
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="sor_monika_comforting",
            category=['mas_compliment'],
            prompt="You comfort me!",
            random=False,
            pool=True,
            unlocked=True,
        ),
        code="CMP"
    )

label sor_monika_comforting:
    if not renpy.seen_label("sor_monika_comforting01"):
        call sor_monika_comforting01
    else:
        call sor_monika_comforting02
return

label sor_monika_comforting01:
    $ mas_gainAffection(6, bypass=True)
    m 1hubsb "Aww! You comfort me too, [player]!"
    m 3fubsb "Whenever I'm sad or alone I know I can always count on you."
    show monika 5dubsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5dubsb "We can find comfort in eachother from how cruel the world can get."
    show monika 7eubsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 7eubsb "After all, our love is what saved me!"
    m 1fubfa "I love you, [mas_get_player_nickname()]."
return "love"

label sor_monika_comforting02:
    m 1hublb "[player]! You're such a sweetheart."
    m 1kublb "I'll comfort you anytime."
return


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="sor_monika_everything",
            category=['mas_compliment'],
            prompt="You're my everything!",
            random=False,
            pool=True,
            unlocked=True,
        ),
        code="CMP"
    )

label sor_monika_everything:
    if not renpy.seen_label("sor_monika_everything01"):
        call sor_monika_everything01
    else:
        call sor_monika_everything02
return

label sor_monika_everything01:
    $ mas_gainAffection(6, bypass=True)
    m 6subfd "[player]..."
    m 1ekbfb "You're so sweet!"
    m 1ekbfb "This means so much to me!"
    m 7hubfb "If I could hug you right now, I so would!"
    m 1fublb "You're my everything too."
    m 1lka "You're the only thing I have."
    m 4ekblb "Never forget that, alright?"
return

label sor_monika_everything02:
    show monika 5fublb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5fublb "Always and forever."
    m 5hubla "..."
return