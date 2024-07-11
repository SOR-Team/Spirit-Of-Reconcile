init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_natsukisor",
            category=["Reconcile"],
            prompt="How do you feel about Natsuki?",
            random=False,
            pool=True,
            unlocked=True,
        )
    )

label monika_natsukisor:
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
            eventlabel="monika_sayorisor",
            category=["Reconcile"],
            prompt="How do you feel about Sayori?",
            random=False,
            pool=True,
            unlocked=True,
        )
    )

label monika_sayorisor:
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
            eventlabel="monika_yurisor",
            category=["Reconcile"],
            prompt="How do you feel about Yuri?",
            random=False,
            pool=True,
            unlocked=True,
        )
    )

label monika_yurisor:
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