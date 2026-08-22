def on_chat_1():
    for index in range(5):
        blocks.fill(
            WOOL,
            pos(-12, -1 - index * 5, -12),
            pos(12, -1 - index * 5, 12),
            FillOperation.REPLACE
        )

        blocks.place(
            YELLOW_WOOL,
            pos(0, -1 - index * 5, 0)
        )
        blocks.place(
            YELLOW_WOOL,
            pos(-8, -1 - index * 5, 0)
        )
        blocks.place(
            YELLOW_WOOL,
            pos(8, -1 - index * 5, 0)
        )
        blocks.place(
            YELLOW_WOOL,
            pos(0, -1 - index * 5, -8)
        )
        blocks.place(
            YELLOW_WOOL,
            pos(0, -1 - index * 5, 8)
        )

    blocks.fill(
        HAY_BLOCK,
        pos(-12, -29, -12),
        pos(12, -29, 12),
        FillOperation.REPLACE
    )

    blocks.fill(
        GLASS,
        pos(-13, -28, -13),
        pos(-13, 3, 13),
        FillOperation.REPLACE
    )
    blocks.fill(
        GLASS,
        pos(13, -28, -13),
        pos(13, 3, 13),
        FillOperation.REPLACE
    )
    blocks.fill(
        GLASS,
        pos(-13, -28, -13),
        pos(13, 3, -13),
        FillOperation.REPLACE
    )
    blocks.fill(
        GLASS,
        pos(-13, -28, 13),
        pos(13, 3, 13),
        FillOperation.REPLACE
    )

    blocks.fill(
        blocks.block_by_name("deny"),
        pos(-13, -30, -13),
        pos(-13, -30, 13),
        FillOperation.REPLACE
    )
    blocks.fill(
        blocks.block_by_name("deny"),
        pos(13, -30, -13),
        pos(13, -30, 13),
        FillOperation.REPLACE
    )
    blocks.fill(
        blocks.block_by_name("deny"),
        pos(-13, -30, -13),
        pos(13, -30, -13),
        FillOperation.REPLACE
    )
    blocks.fill(
        blocks.block_by_name("deny"),
        pos(-13, -30, 13),
        pos(13, -30, 13),
        FillOperation.REPLACE
    )

    blocks.fill(
        AIR,
        pos(13, -28, -1),
        pos(13, -27, 1),
        FillOperation.REPLACE
    )

    blocks.fill(
        STONE,
        pos(13, -29, -1),
        pos(16, -29, 1),
        FillOperation.REPLACE
    )

    blocks.fill(
        GLASS,
        pos(13, -28, -2),
        pos(17, -2, -2),
        FillOperation.REPLACE
    )
    blocks.fill(
        GLASS,
        pos(13, -28, 2),
        pos(17, -2, 2),
        FillOperation.REPLACE
    )
    blocks.fill(
        GLASS,
        pos(17, -28, -2),
        pos(17, -2, 2),
        FillOperation.REPLACE
    )

    blocks.fill(
        blocks.block_by_name("deny"),
        pos(14, -1, -13),
        pos(25, -1, 13),
        FillOperation.REPLACE
    )
    blocks.fill(
        STONE,
        pos(14, 0, -12),
        pos(25, 0, 12),
        FillOperation.REPLACE
    )

    blocks.fill(
        GLASS,
        pos(14, 1, -13),
        pos(25, 3, -13),
        FillOperation.REPLACE
    )
    blocks.fill(
        GLASS,
        pos(14, 1, 13),
        pos(25, 3, 13),
        FillOperation.REPLACE
    )
    blocks.fill(
        GLASS,
        pos(25, 1, -13),
        pos(25, 3, 13),
        FillOperation.REPLACE
    )

    blocks.fill(
        SCAFFOLDING,
        pos(16, -28, 0),
        pos(16, 0, 0),
        FillOperation.REPLACE
    )

player.on_chat("1", on_chat_1)


def on_chat_2():
    blocks.fill(
        HAY_BLOCK,
        pos(-20, -9, -15),
        pos(25, -9, 15),
        FillOperation.REPLACE
    )

    blocks.fill(
        WOOL,
        pos(-17, -1, -12),
        pos(17, -1, 12),
        FillOperation.REPLACE
    )

    blocks.fill(
        YELLOW_WOOL,
        pos(-10, -1, -1),
        pos(-8, -1, 1),
        FillOperation.REPLACE
    )
    blocks.fill(
        YELLOW_WOOL,
        pos(-1, -1, -1),
        pos(1, -1, 1),
        FillOperation.REPLACE
    )
    blocks.fill(
        YELLOW_WOOL,
        pos(8, -1, -1),
        pos(10, -1, 1),
        FillOperation.REPLACE
    )

    blocks.fill(
        STONE,
        pos(25, -8, -1),
        pos(25, -8, 1),
        FillOperation.REPLACE
    )
    blocks.fill(
        STONE,
        pos(24, -7, -1),
        pos(24, -7, 1),
        FillOperation.REPLACE
    )
    blocks.fill(
        STONE,
        pos(23, -6, -1),
        pos(23, -6, 1),
        FillOperation.REPLACE
    )
    blocks.fill(
        STONE,
        pos(22, -5, -1),
        pos(22, -5, 1),
        FillOperation.REPLACE
    )
    blocks.fill(
        STONE,
        pos(21, -4, -1),
        pos(21, -4, 1),
        FillOperation.REPLACE
    )
    blocks.fill(
        STONE,
        pos(20, -3, -1),
        pos(20, -3, 1),
        FillOperation.REPLACE
    )
    blocks.fill(
        STONE,
        pos(19, -2, -1),
        pos(19, -2, 1),
        FillOperation.REPLACE
    )
    blocks.fill(
        STONE,
        pos(18, -1, -1),
        pos(18, -1, 1),
        FillOperation.REPLACE
    )

player.on_chat("2", on_chat_2)
