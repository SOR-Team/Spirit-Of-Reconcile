init -990 python:
    store.mas_submod_utils.Submod(
        author="SOR Team",
        name="Spirit Of Reconcile",
        description="Monika fixed us! And we fixed her too! Or is it..?",
        version="1.0.0"
    )

init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="Spirit Of Reconcile",
            user_name="SOR-Team",
            repository_name="Spirit-Of-Reconcile",
            extraction_depth=1
        )

screen reset_sor_button():
    zorder 15
    style_prefix "hkb"
    vbox:
        xpos 0.05
        yanchor 1.0
        ypos 450
        if renpy.get_screen("hkb_overlay"):
            if store.mas_hotkeys.talk_enabled is False:
                textbutton ("RESET SOR"):        
                    xsize 150
            else:
                textbutton ("RESET SOR"):    
                    xsize 150
                    action Jump("sor_reset")

label sor_reset:
    $ del persistent._seen_ever["sor_monika_comforting"]
    $ del persistent._seen_ever["sor_monika_everything"]
    $ del persistent._seen_ever["sor_monika_comforting01"]
    $ del persistent._seen_ever["sor_monika_everything01"]
    $ del persistent._seen_ever["sor_monika_comforting02"]
    $ del persistent._seen_ever["sor_monika_everything02"]
    $ del persistent._seen_ever["sor_monika_natsuki"]
    $ del persistent._seen_ever["sor_monika_sayori"]
    $ del persistent._seen_ever["sor_monika_yuri"]
return

image scaretest = "/mod_assets/ee_sayori.png"

init python:
    config.overlay_screens.append("reset_sor_button")
    import webbrowser

label sor_scare1:
    
    $ mas_RaiseShield_core()

    $ sayor_name = "..."
    define sayor = DynamicCharacter('c_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")

    menu:
        "\"Monika\"":
                 pass

    m "Yes, [mas_get_player_nickname()]?"

    menu:
        "\"I want you to listen to a song\"":
                                            pass

    m 1eub "You want me to listen to a song?"
    m 3hub "Okay, [mas_get_player_nickname()]!"
    ##call mas_poem_minigame_actthree(trans_fast=True,hop_monika=True,gather_words=True) from _call_mpg_sampleone

    menu:
        "Play the song":
                        pause 5
                        play music "Submods/RickrollMonikaSubmod/never-gonna-give-you-up.mp3"
                        m 6cud "..."
  
                        m "Did you just..."
                        m "..."
                        m 6cfo "[player]!{w=1} What the hel-{nw}"
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
                        pause 2
                        show scaretest at thide
                        hide scaretest
                        pause 2
                        $ play_song(persistent.current_track, fadein=4.0)
                        if store.mas_globals.in_idle_mode:
                            $ mas_coreToIdleShield()
                        else:
                            $ mas_DropShield_core()
                        jump ch30_loop

stop music
$ play_song(persistent.current_track, fadein=4.0)
return