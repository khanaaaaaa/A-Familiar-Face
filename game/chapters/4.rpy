label chapter_four:
    call screen chapter_title("04", "What She Knew")

    scene bg black
    with fade

    pause 1.0

    scene bg hallway
    with dissolve

    narrator "The hallway is empty."
    narrator "minju is still holding my wrist."

    mc "You knew what that meant."
    minju "..."
    mc "The stone... you recognized it."

    narrator "He lets go."

    show minjuneutraltalk at center_char
    minju "There was a girl."
    minju "Three years ago."
    minju "She was my friend."
    minju "She disappeared.. in the auditorium... on Halloween."
    minju "I left her alone for five minutes."
    minju "She was gone when I came back."
    hide minjuneutraltalk
    show minjusadquiet at center_char
    mc "Gone?"
    hide minjusadquiet
    show minjuneutraltalk at center_char
    minju "Yeah... gone."
    hide minjuneutraltalk
    show minjuneutralquiet at center_char
    mc "And the promise?"
    hide minjuneutralquiet
    show minjuneutraltalk at center_char
    minju "I told her I wouldn't leave."
    hide minjuneutraltalk
    show minjuneutralquiet at center_char
    narrator "She looks at the floor."
    hide minjuneutralquiet
    show minjuneutraltalk at center_char
    minju "I left."
    hide minjuneutraltalk
    show minjuneutralquiet at center_char
    narrator "A locker rattles somewhere down the hall."
    narrator "Neither of us move."
    mc "What do you want to do?"
    narrator "He looks up."

    menu:
        "We should go back in.":
            scene bg black
            $ minju_affection += 1
            mc "We should go back."
            minju "..."
            minju "Yeah."
            minju "We should."
            jump ending_together

        "Leave it alone":
            scene bg black
            mc "Maybe leave it alone."
            minju "..."
            minju "Maybe."
            narrator "She doesn't sound convinced."
            narrator "Neither am I."
            jump ending_apart

        "Ask if she's okay.":
            scene bg black
            mc "Are you okay?"
            minju "No."
            minju "But I will be."
            narrator "She almost smiles."
            jump ending_peace