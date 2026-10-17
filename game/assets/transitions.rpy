default minju_affection = 0
default ren_affection = 0
default replied_to_minju = False

screen chapter_title(number, title):
    modal True

    add Solid("#0d0b10")

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 12

        text "CHAPTER [number]":
            xalign 0.5
            size 28
            color "#c9a9b8"
            font "DejaVuSans.ttf"

        text "[title]":
            xalign 0.5
            size 64
            color "#f4e8ed"
            font "DejaVuSans.ttf"

        text "✦  ─────────  ✦":
            xalign 0.5
            size 20
            color "#9d7185"

    timer 3.5 action Return

define nvl_mode = "phone"
define MC_Name = "Me"

define minju_nvl = Character(
    "minju",
    kind=nvl
)

define mc_nvl = Character(
    "Me",
    kind=nvl
)

transform bg_fit:
    size (1920, 1080)
    xalign 0.5
    yalign 0.5

transform center_char:
    xalign 0.5
    yalign 1.0
    zoom 1.5

image bg bedroom = "images/bedroom.jpg"
image bg auditorium = "images/auditorium.avif"
image bg classroom = "images/classroom.avif"
image bg hallway = "images/hallway.jpeg"
image bg school = "images/school.jpg"