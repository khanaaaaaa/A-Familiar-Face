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

    narrator "She lets go."

    minju "There was a girl."
    minju "Three years ago."
    minju "She was my friend."
    minju "She disappeared.. in the auditorium... on Halloween."
    minju "I left her alone for five minutes."
    minju "She was gone when I came back."
    mc "Gone?"
    minju "Yeah... gone."
    narrator "Silence."
    mc "And the promise?"
    minju "I told her I wouldn't leave."
    narrator "She looks at the floor."
    minju "I left."
    narrator "A locker rattles somewhere down the hall."
    narrator "Neither of us move."
    mc "What do you want to do?"
    narrator "She looks up."

    menu:
        "We should go back in.":
            $ minju_affection += 1
            mc "We should go back."
            minju "..."
            minju "Yeah."
            minju "We should."
            jump ending_together

        "Leave it alone":
            mc "Maybe leave it alone."
            minju "..."
            minju "Maybe."
            narrator "She doesn't sound convinced."
            narrator "Neither am I."
            jump ending_apart

        "Ask if she's okay.":
            mc "Are you okay?"
            minju "No."
            minju "But I will be."
            narrator "She almost smiles."
            jump ending_peace