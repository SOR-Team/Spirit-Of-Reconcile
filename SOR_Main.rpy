init -990 python:
    store.mas_submod_utils.Submod(
        author="SOR Team",
        name="Spirit Of Reconcile",
        description="Monika fixed us, and we fixed her too! Or did we..?",
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
    $ del persistent._seen_ever["sor_monika_are_you_real"]
    $ del persistent._seen_ever["sor_monika_natsuki"]
    $ del persistent._seen_ever["sor_monika_sayori"]
    $ del persistent._seen_ever["sor_monika_yuri"]
    $ del persistent._seen_ever["sor_moni_codes"]
    $ del persistent._seen_ever["sor_scare1"]
    $ del persistent._seen_ever["sor_after_menu"]
return

image scaretest = "/mod_assets/ee_sayori.png"

init python:
    config.overlay_screens.append("reset_sor_button")
    import webbrowser

