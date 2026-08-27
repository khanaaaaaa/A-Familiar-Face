label chapter_2:

    call screen chapter_title("02", "Trick Or Treat")

    scene bg black
    with fade

    pause 1.0

    scene bg bedroom
    with dissolve

    narrator "The first thing I notice when I wake up is the rain."
    narrator "It taps softly against my window."
    narrator "Not hard enough to be a storm."
    narrator "Just enough to make the whole morning feel sleepy."
    narrator "My alarm rings."
    narrator "I ignore it."
    narrator "It rings again."
    narrator "I ignore it again."
    narrator "Then my phone vibrates across the bedsides table."
    narrator "I reach for it without opening my eyes."

    # starting the phone texts here

    $ nvl_mode = "phone"
    nvl_narrator "Mina started a conversation."
    mina_nvl "Good morning, corpse."
    mc_nvl "It's too early."
    mina_nvl "It's 7:31."
    mc_nvl "Exactly."
    mina_nvl "You're coming, right?"
    mc_nvl "Coming where?"
    mina_nvl "School."
    mc_nvl "Obviously."
    mina_nvl "Good."
    mc_nvl "Why wouldn't I?"
    mina_nvl "You forgot yesterday."
    mc_ncl "I did not."
    mina_nvl "You did."
    mc_nvl "What did I forget?"
    mina_nvl "Halloween."
    mc_nvl "Oh."
    mina_nvl "Exactly."
    mc_nvl "It's just Halloween."
    mina_nvl "We're student council presidents."
    mc_nvl "Unfortunately."
    mina_nvl "Which means..."
    mc_nvl "We have to organize everything."
    mina_nvl "Yup."
    mc_nvl "I hate this."
    mina_nvl "See you soon ♡"

    narrator "I stare at the last message."
    narrator "She's right."
    narrator "Being student council president sounded impressive when we were elected."
    narrator "Now it mostly means paperwork."
    narrator "And cleaning."
    narrator "Especially on Halloween."

    nvl clear

    scene bg School
    with dissolve

    narrator "By the time I reach school, the rain has stopped."
    narrator "The courtyard is covered in puddles."
    narrator "Orange leaves cling to the pavement."
    narrator "Halloween decorations hand from every tree."

    return