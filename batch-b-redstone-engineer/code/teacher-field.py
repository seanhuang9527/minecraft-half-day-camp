def build_lane(lane_x, start_wool):
    blocks.fill(
        blocks.block_by_name("allow"),
        pos(lane_x - 1, -2, 0),
        pos(lane_x + 1, -2, 40),
        FillOperation.REPLACE
    )

    blocks.place(start_wool, pos(lane_x, -1, 2))
    blocks.place(RED_WOOL, pos(lane_x, -1, 37))
    blocks.place(GLASS, pos(lane_x, 0, 1))
    blocks.place(GLASS, pos(lane_x, 0, 39))

    blocks.fill(
        YELLOW_WOOL,
        pos(lane_x + 2, -1, 0),
        pos(lane_x + 2, -1, 40),
        FillOperation.REPLACE
    )


def on_on_chat():
    blocks.fill(
        AIR,
        pos(-20, 0, 0),
        pos(20, 5, 40),
        FillOperation.REPLACE
    )

    blocks.fill(
        blocks.block_by_name("deny"),
        pos(-20, -2, 0),
        pos(20, -2, 40),
        FillOperation.REPLACE
    )

    blocks.fill(
        STONE,
        pos(-20, -1, 0),
        pos(20, -1, 40),
        FillOperation.REPLACE
    )

    build_lane(-18, blocks.block_by_name("white_wool"))
    build_lane(-14, blocks.block_by_name("orange_wool"))
    build_lane(-10, blocks.block_by_name("yellow_wool"))
    build_lane(-6, blocks.block_by_name("lime_wool"))
    build_lane(-2, blocks.block_by_name("green_wool"))
    build_lane(2, blocks.block_by_name("cyan_wool"))
    build_lane(6, blocks.block_by_name("light_blue_wool"))
    build_lane(10, blocks.block_by_name("blue_wool"))
    build_lane(14, blocks.block_by_name("purple_wool"))
    build_lane(18, blocks.block_by_name("magenta_wool"))

    player.tell(
        mobs.target(LOCAL_PLAYER),
        "10線紅石鐵路測試場完成"
    )


player.on_chat("9", on_on_chat)
