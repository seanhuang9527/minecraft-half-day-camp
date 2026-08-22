def on_travelled_walk():
    mobs.apply_effect(
        JUMP_BOOST,
        mobs.target(LOCAL_PLAYER),
        3,
        2
    )

    if blocks.test_for_block(WOOL, pos(0, -1, -1)):
        blocks.place(AIR, pos(0, -1, -1))

    if blocks.test_for_block(YELLOW_WOOL, pos(0, -1, -1)):
        mobs.apply_effect(
            SPEED,
            mobs.target(LOCAL_PLAYER),
            3,
            1
        )
        blocks.place(AIR, pos(0, -1, -1))

player.on_travelled(WALK, on_travelled_walk)
