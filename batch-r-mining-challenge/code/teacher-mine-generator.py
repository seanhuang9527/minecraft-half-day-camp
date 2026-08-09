index = 0


def on_chat_9():
    global index
    blocks.fill(
        STONE,
        pos(-20, -2, -20),
        pos(20, -1, 20),
        FillOperation.REPLACE
    )

    index = 0
    while index < 1500:
        blocks.place(COAL_ORE, randpos(pos(-20, -2, -20), pos(20, -1, 20)))
        index += 1

    index = 0
    while index < 1000:
        blocks.place(IRON_ORE, randpos(pos(-20, -2, -20), pos(20, -1, 20)))
        index += 1

    index = 0
    while index < 500:
        blocks.place(GOLD_ORE, randpos(pos(-20, -2, -20), pos(20, -1, 20)))
        index += 1

    index = 0
    while index < 200:
        blocks.place(DIAMOND_ORE, randpos(pos(-20, -2, -20), pos(20, -1, 20)))
        index += 1

    player.tell(mobs.target(LOCAL_PLAYER), "礦坑完成")
player.on_chat("9", on_chat_9)
