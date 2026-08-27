define nvl_mode = "phone"
define MC_Name = "Me"

init -1 python:
    phone_position_x = 0.3
    phone_position_y = 0.5

    def Phone_RecieveSound(event, interact=True, **kwargs):
        if event == "show_done":
            renpy.sound.play("audio/RecieveText.ogg")
    def Phone_SendSound(event, interact=True, **kwargs):
        if event == "show_done":
            renpy.sound.play("audio/SendText.ogg")
    def print_bonjour():
        print("bonjour")

transform phone_transform(pXalign=0.5, pYalign=0.5):
    xcenter pXalign
    yalign pYalign

transform phone_appear(pXalign=0.5, pYalign=0.5):
    xcenter pXalign
    yalign pYalign

    on show:
        yoffset 1000
        easein_back 1.0 yoffset 0

transform message_appear (pDirection):
    alpha 0.0
    xoffset 50 * pDirection
    parallel:
        ease 0.5 alpha 1.0
    parallel:
        easein_back 0.5 offset 0 

transform message_appear_icon():
    zoom 0.0 
    easein_back 0.5 zoom 1.0

transform message_narrator:
    alpha 0.0
    yoffset -50

    parallel:
        ease 0.5 alpha 1.0
    parallel:
        easein_back 0.5 yoffset 0
    