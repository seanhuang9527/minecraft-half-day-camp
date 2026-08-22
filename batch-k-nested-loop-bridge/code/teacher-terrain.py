def on_chat_9():
    deny_block = blocks.block_by_name("deny")
    border_block = blocks.block_by_name("border_block")

    red_carpet = blocks.block_by_name("red_carpet")
    orange_carpet = blocks.block_by_name("orange_carpet")
    yellow_carpet = blocks.block_by_name("yellow_carpet")
    lime_carpet = blocks.block_by_name("lime_carpet")
    light_blue_carpet = blocks.block_by_name("light_blue_carpet")
    blue_carpet = blocks.block_by_name("blue_carpet")
    purple_carpet = blocks.block_by_name("purple_carpet")
    pink_carpet = blocks.block_by_name("pink_carpet")

    # A 點：水平橋起點
    blocks.fill(
        deny_block,
        pos(-21, -2, -4),
        pos(20, -2, 4),
        FillOperation.REPLACE
    )
    blocks.fill(
        STONE_BRICKS,
        pos(-21, -1, -4),
        pos(20, -1, 4),
        FillOperation.REPLACE
    )

    # A 點左右護欄
    blocks.fill(
        STONE_BRICKS,
        pos(-21, 0, -4),
        pos(-21, 1, 4),
        FillOperation.REPLACE
    )
    blocks.fill(
        STONE_BRICKS,
        pos(20, 0, -4),
        pos(20, 1, 4),
        FillOperation.REPLACE
    )

    # A 點八條跑道的彩色地毯
    blocks.place(red_carpet, pos(-19, 0, 2))
    blocks.place(orange_carpet, pos(-14, 0, 2))
    blocks.place(yellow_carpet, pos(-9, 0, 2))
    blocks.place(lime_carpet, pos(-4, 0, 2))
    blocks.place(light_blue_carpet, pos(1, 0, 2))
    blocks.place(blue_carpet, pos(6, 0, 2))
    blocks.place(purple_carpet, pos(11, 0, 2))
    blocks.place(pink_carpet, pos(16, 0, 2))

    # B 點：距離 A 點約 50 格
    blocks.fill(
        deny_block,
        pos(-21, -2, 54),
        pos(20, -2, 62),
        FillOperation.REPLACE
    )
    blocks.fill(
        GOLD_BLOCK,
        pos(-21, -1, 54),
        pos(20, -1, 62),
        FillOperation.REPLACE
    )

    # B 點左右護欄
    blocks.fill(
        STONE_BRICKS,
        pos(-21, 0, 54),
        pos(-21, 1, 62),
        FillOperation.REPLACE
    )
    blocks.fill(
        STONE_BRICKS,
        pos(20, 0, 54),
        pos(20, 1, 62),
        FillOperation.REPLACE
    )

    # B 點八條跑道起點
    blocks.place(red_carpet, pos(-19, 0, 60))
    blocks.place(orange_carpet, pos(-14, 0, 60))
    blocks.place(yellow_carpet, pos(-9, 0, 60))
    blocks.place(lime_carpet, pos(-4, 0, 60))
    blocks.place(light_blue_carpet, pos(1, 0, 60))
    blocks.place(blue_carpet, pos(6, 0, 60))
    blocks.place(purple_carpet, pos(11, 0, 60))
    blocks.place(pink_carpet, pos(16, 0, 60))

    # B 點上方邊界方塊
    blocks.fill(
        border_block,
        pos(-21, 0, 62),
        pos(20, 0, 62),
        FillOperation.REPLACE
    )

    # C 點：比 B 點高 50 格
    blocks.fill(
        deny_block,
        pos(-21, 48, 112),
        pos(20, 48, 120),
        FillOperation.REPLACE
    )
    blocks.fill(
        blocks.block_by_name("quartz_block"),
        pos(-21, 49, 112),
        pos(20, 49, 120),
        FillOperation.REPLACE
    )

    # C 點左右護欄
    blocks.fill(
        STONE_BRICKS,
        pos(-21, 50, 112),
        pos(-21, 51, 120),
        FillOperation.REPLACE
    )
    blocks.fill(
        STONE_BRICKS,
        pos(20, 50, 112),
        pos(20, 51, 120),
        FillOperation.REPLACE
    )

    # C 點八條跑道起點
    blocks.place(red_carpet, pos(-19, 50, 118))
    blocks.place(orange_carpet, pos(-14, 50, 118))
    blocks.place(yellow_carpet, pos(-9, 50, 118))
    blocks.place(lime_carpet, pos(-4, 50, 118))
    blocks.place(light_blue_carpet, pos(1, 50, 118))
    blocks.place(blue_carpet, pos(6, 50, 118))
    blocks.place(purple_carpet, pos(11, 50, 118))
    blocks.place(pink_carpet, pos(16, 50, 118))

    # C 點上方邊界方塊
    blocks.fill(
        border_block,
        pos(-21, 50, 120),
        pos(20, 50, 120),
        FillOperation.REPLACE
    )

    # D 點：往下挑戰的終點
    blocks.fill(
        deny_block,
        pos(-21, -1, 170),
        pos(20, -1, 178),
        FillOperation.REPLACE
    )
    blocks.fill(
        blocks.block_by_name("diamond_block"),
        pos(-21, 0, 170),
        pos(20, 0, 178),
        FillOperation.REPLACE
    )

    # D 點左右護欄
    blocks.fill(
        STONE_BRICKS,
        pos(-21, 1, 170),
        pos(-21, 2, 178),
        FillOperation.REPLACE
    )
    blocks.fill(
        STONE_BRICKS,
        pos(20, 1, 170),
        pos(20, 2, 178),
        FillOperation.REPLACE
    )

    player.say("八人造橋關卡完成")

player.on_chat("9", on_chat_9)
