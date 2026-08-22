def on_travelled_walk():
    blocks.replace(
        AIR,
        WOOL,
        pos(0, -1, -1),
        pos(0, -1, -1)
    )
player.on_travelled(WALK, on_travelled_walk)
