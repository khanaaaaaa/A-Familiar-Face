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
    show minjuneutraltalk at center_char
    minju "You're late."
    hide minjuneutraltalk
    show minjuneutralquiet at center_char
    mc "Good morning to you too."
    hide minjuneutralquiet
    show minjusmiletalk at center_char
    minju "We have a problem."
    hide minjusmiletalk
    show minjusmilequiet at center_char
    mc "What now?"
    hide minjusmilequiet
    show minjusmiletalk at center_char
    minju "The haunted house."
    hide minjusmiletalk
    show minjusmilequiet at center_char
    mc "What about it?"
    hide minjusmilequiet
    show minjusmiletalk at center_char
    minju "Someone moved the decorations."
    hide minjusmiletalk
    show minjusmilequiet at center_char
    mc "Probably the volunteers."
    hide minjusmilequiet
    show minjusmiletalk at center_char
    minju "No."
    hide minjusmiletalk
    show minjusmilequiet at center_char
    mc "How do you know?"
    hide minjusmilequiet
    show minjusmiletalk at center_char
    minju "Because I locked the room."
    minju "And I still have the key."
    hide minjusmiletalk
    show minjusmilequiet at center_char
    mc "Okay."
    mc "That's weird."
    mc "Maybe someone made a copy."
    hide minjusmilequiet
    show minjusmiletalk at center_char
    minju "Maybe."
    minju "Come on, President."
    hide minjusmiletalk
    show minjusmilequiet at center_char
    mc "Don't call me that."
    hide minjusmilequiet
    show minjusmiletalk at center_char
    minju "Why?"
    hide minjusmiletalk
    show minjusmilequiet at center_char
    mc "It makes me feel old."
    hide minjusmilequiet
    show minjusmiletalk at center_char
    minju "We're seniors."
    hide minjusmiletalk
    show minjusmilequiet at center_char
    mc "Exactly."
    hide minjusmilequiet
    show minjusmiletalk at center_char
    minju "You're dramatic."
    hide minjusmiletalk
    show minjusmilequiet at center_char
    mc "You're annoying."
    hide minjusmilequiet
    show minjusmiletalk at center_char
    minju "And yet.."
    hide minjusmiletalk
    show minjusmilequiet at center_char
    mc "Don't."
    hide minjusmilequiet
    show minjusmiletalk at center_char
    minju "You'd miss me."
    hide minjusmiletalk
    show minjusmilequiet at center_char
    mc "Unfortunately."
    narrator "He laughs."
    narrator "Then he looks toward the old auditorium."
    narrator "His smile disappears."
    hide minjusmilequiet
    show minjuneutraltalk at center_char
    minju "Let's go."
    hide minjuneutraltalk
    show minjuneutralquiet at center_char
    mc "Why?"
    hide minjuneutralquiet
    show minjuneutraltalk at center_char
    minju "I want to check something."
    hide minjuneutraltalk
    show minjuneutralquiet at center_char
    mc "What?"
    hide minjuneutralquiet
    show minjuneutraltalk at center_char
    minju "I'll tell you inside."
    hide minjuneutraltalk
    show minjuneutralquiet at center_char
    narrator "She starts walking."
    narrator "I follow."
    narrator "Neither of us notices the auditorium door slowly closing behind us."

    menu:
        "Follow minju into the audtorium.":
            mc "Fine, let's go."
            hide minjuneutralquiet
            show minjuneutraltalk at center_char
            minju "Good."
            hide minjuneutraltalk
            show minjuneutralquiet at center_char
            narrator "She smiles again."
            narrator "I wish she hadn't."
        
        "Ask minju what's wrong.":
            mc "minju."
            hide minjuneutralquiet
            show minjuneutraltalk at center_char
            minju "Hm?"
            hide minjuneutraltalk
            show minjuneutralquiet at center_char
            mc "What's bothering you?"
            narrator "She stops."
            hide minjuneutralquiet
            show minjuneutraltalk at center_char
            minju "I heard someone calling my name."
            hide minjuneutraltalk
            show minjuneutralquiet at center_char
            mc "From inside?"
            hide minjuneutralquiet
            show minjuneutraltalk at center_char
            minju "No."
            minju "From behind me."
            hide minjuneutraltalk
            show minjuneutalquiet at center_char
            narrator "I look back."
            narrator "The hallway is empty."
            hide minjuneutralquiet
            show minjuneutraltalk at center_char
            minju "Forget it."

        "Suggest we get another student.":
            mc "Shouldn't we get someone else?"
            hide minjuneutralquiet
            show minjuneutraltalk at center_char
            minju "Why?"
            hide minjuneutraltalk
            show minjuneutralquiet at center_char
            mc "Because this is creepy."
            hide minjuneutralquiet
            show minjuneutraltalk at center_char
            minju "You're scared?"
            hide minjuneutraltalk
            show minjuneutralquiet at center_char
            mc "I'm being reasonable."
            hide minjuneutralquiet
            show minjuneutraltalk at center_char
            minju "Then stay here."
            hide minjuneutraltalk
            show minjuneutralquiet at center_char
            narrator "She walks toward the auditorium alone."
            mc "Minju, wait."
            narrator "I follow her."
            
    jump chapter_3