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
    nvl_narrator "minju started a conversation."
    minju_nvl "Good morning, corpse."
    mc_nvl "It's too early."
    minju_nvl "It's 7:31."
    mc_nvl "Exactly."
    minju_nvl "You're coming, right?"
    mc_nvl "Coming where?"
    minju_nvl "School."
    mc_nvl "Obviously."
    minju_nvl "Good."
    mc_nvl "Why wouldn't I?"
    minju_nvl "You forgot yesterday."
    mc_ncl "I did not."
    minju_nvl "You did."
    mc_nvl "What did I forget?"
    minju_nvl "Halloween."
    mc_nvl "Oh."
    minju_nvl "Exactly."
    mc_nvl "It's just Halloween."
    minju_nvl "We're student council presidents."
    mc_nvl "Unfortunately."
    minju_nvl "Which means..."
    mc_nvl "We have to organize everything."
    minju_nvl "Yup."
    mc_nvl "I hate this."
    minju_nvl "See you soon ♡"

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
    narrator "minju is already there."

    minju "You're late."

    mc "Good morning to you too."

    minju "We have a problem."

    mc "What now?"

    minju "The haunted house."

    mc "What about it?"

    minju "Someone moved the decorations."

    mc "Probably the volunteers."

    minju "No."

    mc "How do you know?"

    minju "Because I locked the room."

    mc "..."

    minju "And I still have the key."

    mc "Okay."
    mc "That's weird."

    minju "A little."

    mc "Maybe someone made a copy."

    minju "Maybe."

    narrator "She smiles."

    minju "Come on, President."

    mc "Don't call me that."

    minju "Why?"

    mc "It makes me feel old."

    minju "We're seniors."

    mc "Exactly."

    minju "You're dramatic."

    mc "You're annoying."

    minju "And yet.."

    mc "Don't."

    minju "You'd miss me."

    mc "Unfortunately."

    narrator "She laughs."
    narrator "Then she looks toward the old auditorium."
    narrator "Her smile disappears."

    minju "Let's go."

    mc "Why?"

    minju "I want to check something."

    mc "What?"

    minju "I'll tell you inside."

    narrator "She starts walking."
    narrator "I follow."
    narrator "Neither of us notices the auditorium door slowly closing behind us."

    menu:
        "Follow minju into the audtorium.":
            mc "Fine, let's go."
            minju "Good."
            narrator "She smiles again."
            narrator "I wish she hadn't."
        
        "Ask minju what's wrong.":
            mc "minju."
            minju "Hm?"
            mc "What's bothering you?"
            narrator "She stops."
            minju "I heard someone calling my name."
            mc "From inside?"
            minju "No."
            minju "From behind me."
            narrator "I look back."
            narrator "The hallway is empty."
            minju "Forget it."
            jump chapter_3

        "Suggest we get another student.":
            mc "Shouldn't we get someone else?"
            minju "Why?"
            mc "Because this is creepy."
            minju "You're scared?"
            mc "I'm being reasonable."
            minju "Then stay here."
            narrator "She walks toward the auditorium alone."
            mc "minju, wait."
            narrator "I follow her."
            
    jump chapter_3