label chapter_four:
    call screen chapter_title("04", "What She Knew")

    scene bg black
    with fade

    pause 1.0

    scene bg hallway
    with dissolve

    narrator "The hallway is empty."
    narrator "Mina is still holding my wrist."

    mc "You knew what that meant."

    mina "..."

    mc "The stone... you recognized it."

    narrator "She lets go."

    mina "There was a girl."
    mina "Three years ago."
    mina "She was my friend."
    mina "She disappeared.. in the auditorium... on Halloween."
    mina "I left her alone for five minutes."
    mina "She was gone when I came back."
    mc "Gone?"
    mina "Yeah... gone."
    narrator "Silence."
    mc "And the promise?"
    mina "I told her I wouldn't leave."
    narrator "She looks at the floor."
    mina "I left."
    narrator "A locker rattles somewhere down the hall."
    narrator "Neither of us move."
    mc "What do you want to do?"
    narrator "She looks up."

    menu:
        "We should go back in.":
            $ mina_affection += 1
            mc "We should go back."
            mina "..."
            mina "Yeah."
            mina "We should."
            jump ending_together

        "Leave it alone":
            mc "Maybe leave it alone."
            mina "..."
            mina "Maybe."
            narrator "She doesn't sound convinced."
            narrator "Neither am I."
            jump ending_apart

        "Ask if she's okay.":
            mc "Are you okay?"
            mina "No."
            mina "But I will be."
            narrator "She almost smiles."
            jump ending_peace