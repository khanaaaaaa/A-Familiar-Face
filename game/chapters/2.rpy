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
    narrator "A giant paper moon hangs over the entrance."
    narrator "Mina is already there."

    mina "You're late."

    mc "Good morning to you too."

    mina "We have a problem."

    mc "What now?"

    mina "The haunted house."

    mc "What about it?"

    mina "Someone moved the decorations."

    mc "Probably the volunteers."

    mina "No."

    mc "How do you know?"

    mina "Because I locked the room."

    mc "..."

    mina "And I still have the key."

    mc "Okay."
    mc "That's weird."

    mina "A little."

    mc "Maybe someone made a copy."

    mina "Maybe."

    narrator "She smiles."

    mina "Come on, President."

    mc "Don't call me that."

    mina "Why?"

    mc "It makes me feel old."

    mina "We're seniors."

    mc "Exactly."

    mina "You're dramatic."

    mc "You're annoying."

    mina "And yet.."

    mc "Don't."

    mina "You'd miss me."

    mc "Unfortunately."

    narrator "She laughs."
    narrator "Then she looks toward the old auditorium."
    narrator "Her smile disappears."

    mina "Let's go."

    mc "Why?"

    mina "I want to check something."

    mc "What?"

    mina "I'll tell you inside."

    narrator "She starts walking."
    narrator "I follow."
    narrator "Neither of us notices the auditorium door slowly closing behind us."

    return