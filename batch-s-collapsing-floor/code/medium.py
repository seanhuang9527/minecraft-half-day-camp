def on_travelled_walk():
    if blocks.test_for_block(WOOL, pos(0, -1, -1)):
        blocks.place(AIR, pos(0, -1, -1))
player.on_travelled(WALK, on_travelled_walk)
