init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_comfortingsor",
            category=['mas_compliment'],
            prompt="You comfort me!",
            random=False,
            pool=True,
            unlocked=True,
        ),
        code="CMP"
    )

label monika_comfortingsor:
    if not renpy.seen_label("monika_comfortingsor01"):
        call monika_comfortingsor01
    else:
        call monika_comfortingsor02

label monika_comfortingsor01:
    $ mas_gainAffection(6, bypass=True)
    m 1hubsb "Aww! You comfort me too, [player]!"
    m 3fubsb "Whenever I'm sad or alone I know I can always count on you."
    show monika 5dubsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5dubsb "We can find comfort in eachother from how cruel the world can get."
    show monika 7eubsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 7eubsb "After all, our love is what saved me!"
    m 1fubfa "I love you, [mas_get_player_nickname()]."
return "love"

label monika_comfortingsor02:
    m 1hublb "[player]! You're such a sweetheart."
    m 1kublb "I'll comfort you anytime."
return


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_everythingsor",
            category=['mas_compliment'],
            prompt="You're my everything!",
            random=False,
            pool=True,
            unlocked=True,
        ),
        code="CMP"
    )

label monika_everythingsor:
    if not renpy.seen_label("monika_everythingsor01"):
        call monika_everythingsor01
    else:
        call monika_everythingsor02

label monika_everythingsor01:
    $ mas_gainAffection(6, bypass=True)
    m 6subfd "[player]!"
    m 1ekbfb "You're so sweet!"
    m 7hubfb "If I could hug you right now, I so would!"
    m 1fublb "You're my everything too."
    m 1lka "You're the only thing I have."
    m 4ekblb "Never forget that, alright?"
return

label monika_everythingsor02:
    show monika 5fublb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5fublb "Always and forever."
    m 5hubla "..."
return