course_origin = world(0, 0, 0)
logo_running = False
logo_step = 0

logo_image = [
    "...................YYYYYYYYYYYY...................",
    "................YYYY..........YYYY................",
    "..............YY......YYYYYYY.....YY..............",
    "............YY....YYYYYYYYYYYYYYY...YY............",
    "..........YY...YYYYYYYYYYYYYYYYYYYY...YY..........",
    ".........YY..YYYYYYYYYYYYYYYYYYYYYYYY..YY.........",
    "........YY..YYYYYYYYYYYYYYYYYYYYYYYYYYY.YY........",
    ".......Y..YYYYYYYYYYYYYYYYYYYYYYYYYYYYYY..Y.......",
    "......Y..YYYYYYBBBYYYYYYYYYYYYYYYYYBYYYYY..Y......",
    ".....YY.YYYYYYYBBBYYYYYYYYBBBBYYYBBBYYYYYY.YY.....",
    "....YY.YYYYYYYYBBBYYYYYYYYBBBBBYYYBBBYYYYYY.YY....",
    "....Y..YYYYYYYYBBBBYYYYYYYYYBBBYYYYBYYYYYYYY.Y....",
    "...Y..YYYYYYYYBBBBBYYYYYYYYBBBYBBBBBBBBYYYYY..Y...",
    "...Y.YYYYYYYYYBBBBBYYYYYYYYBBYYYYBBBBYBYYYYYY.Y...",
    "..Y..YYYYYYYYBBBBBBYYYYYYYYBBYYYYBBBYYYYYYYYY..Y..",
    "..Y.YYYYYYYYYBBBBBBYBYYYYYYBBBBBBBBYBBYYYYYYYY.Y..",
    ".Y..YYYYYYYYBBBBBBBYBBYYYYBBBBBYBBBYBBYYYYYYYY..Y.",
    ".Y..YYYYYYYBBBBBBBBYBBBYYBBBBYYYBBBBBYYYYYYYYYY.Y.",
    ".Y.YYYYYYYBBBBBBBBBYYBYYYYBYBBYYYYBBBBBYYYYYYYY.Y.",
    "YY.YYYYYYBBBYBBBBBBBYYYYYYYBBBYYYYBBBBYYYYYYYYY.YY",
    "Y..YYYYYYYYYYBBBBBBBYYYYYYBBBBYYYBBBBBBYYYYYYYYY.Y",
    "Y..YYYYYYYYYYBBBBBBBYYYYYBBBBYYYBBBBBBBYYYYYYYYY.Y",
    "Y.YYYYYYYYYYBBBBBBYBYYYYYYYBBYYYBBYBYYBYYYYYYYYY.Y",
    "Y.YYYYYYYYYYYYYBYBYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY.Y",
    "Y.YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY.Y",
    "Y.YYYYYYBBBBBBBBBYYYYBYYYYBBBBBBYYBBBBBBYYYYYYYY.Y",
    "Y.YYYYYYBBBBBBBBBBYYBBYYYYBBBBBBYYBBYBBYYYYYYYYY.Y",
    "Y.YYYYYYBBBBBBBYBBBYBBBBYYBBBYBBBBBBYBBYYYYYYYYY.Y",
    "Y..YYYYYYYYBBBBBBBBYBBBBYBBBYYYBBBBBBBBYYYYYYYYY.Y",
    "Y..YYYYYYYYBBBBYBBBYBBBBYYBBBYBBYBBBYBBYYYYYYYYY.Y",
    "YY.YYYYYYYYBBBBYBBBBYBBBBYBBBBBBYBBBBBBYYYYYYYY..Y",
    ".Y.YYYYYYYYBBBBBBBBBBBBBBYBBBBBBBBBBBBBYYYYYYYY.Y.",
    ".Y.YYYYYYYYBBBBBBBBBBBBBBYYYBBYYYBBYYYBYYYYYYYY.Y.",
    ".Y..YYYYYYYBBBBYYBYBYYYBYYYYYYBBBBBBBBBYYYYYYY..Y.",
    "..Y.YYYYYYBBBBBBBBBBBBBBYYYBBBBBBBBBBBBYYYYYYY.Y..",
    "..Y..YYYYBBBBBBBBBBBBBBBYYYBBBBBYBBYBBYYYYYYY..Y..",
    "...Y.YYYYYBYYBBYBBBBBBBBYYYBBYBBYBBYBBYYYYYYY.Y...",
    "...Y..YYYYYYYBBYBBBBBBBBYYYYBBBBYBBYBBYYYYYY..Y...",
    "....Y..YYYYYYBBYYYBBBBYYYYBBBBBBBBBBBBBBYYYY.Y....",
    "....YY.YYYYYYYBYYYBBBBYYYYBBBBBBBBBBBBBBYYY.YY....",
    ".....YY.YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY.YY.....",
    "......Y..YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY..Y......",
    ".......Y..YYYYYYYYYYYYYYYYYYYYYYYYYYYYYY..Y.......",
    "........YY..YYYYYYYYYYYYYYYYYYYYYYYYYYY.YY........",
    ".........YY..YYYYYYYYYYYYYYYYYYYYYYYY..YY.........",
    "..........YY...YYYYYYYYYYYYYYYYYYYY...YY..........",
    "............YY...YYYYYYYYYYYYYYYY...YY............",
    "..............YY.....YYYYYYYYY....YY..............",
    "................YYYY..........YYYY................",
    "...................YYYYYYYYYYYY..................."
]

lamp_x = [
    26, 25, 24, 21, 18, 14, 9, 5,
    0, -6, -10, -15, -19, -22, -25, -26,
    -26, -26, -25, -22, -19, -15, -10, -6,
    -1, 5, 9, 14, 18, 21, 24, 25
]

lamp_y = [
    28, 33, 37, 42, 46, 49, 52, 53,
    54, 53, 52, 49, 46, 42, 37, 33,
    28, 22, 18, 13, 9, 6, 3, 2,
    2, 2, 3, 6, 9, 13, 18, 22
]


def course_pos(x, y, z):
    return positions.add(
        course_origin,
        pos(x, y, z)
    )


def build_border(x1, x2, z1, z2, border_block):
    blocks.fill(
        border_block,
        pos(x1, -1, z1),
        pos(x2, -1, z1),
        FillOperation.REPLACE
    )
    blocks.fill(
        border_block,
        pos(x1, -1, z2),
        pos(x2, -1, z2),
        FillOperation.REPLACE
    )
    blocks.fill(
        border_block,
        pos(x1, -1, z1),
        pos(x1, -1, z2),
        FillOperation.REPLACE
    )
    blocks.fill(
        border_block,
        pos(x2, -1, z1),
        pos(x2, -1, z2),
        FillOperation.REPLACE
    )


def build_station(x1, x2, z1, z2, border_block, teacher_x, teacher_z):
    blocks.fill(
        STONE_BRICKS,
        pos(x1, -1, z1),
        pos(x2, -1, z2),
        FillOperation.REPLACE
    )
    build_border(x1, x2, z1, z2, border_block)
    blocks.place(
        GOLD_BLOCK,
        pos(teacher_x, -1, teacher_z)
    )


def build_execution_station():
    blocks.fill(
        IRON_BLOCK,
        pos(-4, 0, 0),
        pos(-4, 3, 0),
        FillOperation.REPLACE
    )
    blocks.fill(
        IRON_BLOCK,
        pos(4, 0, 0),
        pos(4, 3, 0),
        FillOperation.REPLACE
    )
    blocks.fill(
        IRON_BLOCK,
        pos(-4, 3, 0),
        pos(4, 3, 0),
        FillOperation.REPLACE
    )

    blocks.place(GLOWSTONE, pos(0, 3, 0))
    blocks.place(EMERALD_BLOCK, pos(0, -1, 0))
    blocks.place(GOLD_BLOCK, pos(-1, -1, 0))
    blocks.place(GOLD_BLOCK, pos(1, -1, 0))


def build_station_1():
    build_station(-17, -5, 4, 12, BLUE_WOOL, -4, 8)

    blocks.place(
        blocks.lever(BLOCK_TOP_POINTS_EAST_WHEN_OFF),
        pos(-15, 0, 6)
    )
    blocks.place(STONE_BUTTON, pos(-11, 0, 6))
    blocks.place(STONE_PRESSURE_PLATE, pos(-7, 0, 6))

    for z in range(7, 10):
        blocks.place(REDSTONE_WIRE, pos(-15, 0, z))
        blocks.place(REDSTONE_WIRE, pos(-11, 0, z))
        blocks.place(REDSTONE_WIRE, pos(-7, 0, z))

    blocks.place(REDSTONE_LAMP, pos(-15, 0, 10))
    blocks.place(REDSTONE_LAMP, pos(-11, 0, 10))
    blocks.place(REDSTONE_LAMP, pos(-7, 0, 10))

    blocks.fill(
        GLASS,
        pos(-17, 0, 11),
        pos(-5, 2, 11),
        FillOperation.REPLACE
    )


def build_station_2():
    build_station(5, 25, 14, 22, RED_WOOL, 4, 18)

    blocks.place(
        blocks.lever(BLOCK_TOP_POINTS_EAST_WHEN_OFF),
        pos(7, 0, 17)
    )
    blocks.place(
        blocks.lever(BLOCK_TOP_POINTS_EAST_WHEN_OFF),
        pos(7, 0, 20)
    )

    for x in range(8, 23):
        blocks.place(REDSTONE_WIRE, pos(x, 0, 17))

    for x2 in range(8, 24):
        blocks.place(REDSTONE_WIRE, pos(x2, 0, 20))

    blocks.place(REDSTONE_LAMP, pos(23, 0, 17))
    blocks.place(REDSTONE_LAMP, pos(24, 0, 20))

    blocks.place(GREEN_WOOL, pos(22, -1, 16))
    blocks.place(RED_WOOL, pos(23, -1, 21))

    blocks.fill(
        GLASS,
        pos(6, 0, 16),
        pos(25, 2, 16),
        FillOperation.REPLACE
    )
    blocks.fill(
        GLASS,
        pos(6, 0, 21),
        pos(25, 2, 21),
        FillOperation.REPLACE
    )


def build_station_3():
    build_station(-17, -5, 24, 32, ORANGE_WOOL, -4, 28)

    blocks.place(
        blocks.lever(BLOCK_TOP_POINTS_EAST_WHEN_OFF),
        pos(-15, 0, 26)
    )
    blocks.place(
        blocks.lever(BLOCK_TOP_POINTS_EAST_WHEN_OFF),
        pos(-11, 0, 26)
    )
    blocks.place(
        blocks.lever(BLOCK_TOP_POINTS_EAST_WHEN_OFF),
        pos(-7, 0, 26)
    )

    blocks.place(REDSTONE_WIRE, pos(-15, 0, 27))
    blocks.place(REDSTONE_WIRE, pos(-11, 0, 27))
    blocks.place(REDSTONE_WIRE, pos(-7, 0, 27))

    blocks.place(
        blocks.repeater(SOUTH, 1),
        pos(-15, 0, 28)
    )
    blocks.place(
        blocks.repeater(SOUTH, 2),
        pos(-11, 0, 28)
    )
    blocks.place(
        blocks.repeater(SOUTH, 4),
        pos(-7, 0, 28)
    )

    blocks.place(REDSTONE_WIRE, pos(-15, 0, 29))
    blocks.place(REDSTONE_WIRE, pos(-11, 0, 29))
    blocks.place(REDSTONE_WIRE, pos(-7, 0, 29))

    blocks.place(REDSTONE_LAMP, pos(-15, 0, 30))
    blocks.place(REDSTONE_LAMP, pos(-11, 0, 30))
    blocks.place(REDSTONE_LAMP, pos(-7, 0, 30))


def build_station_4():
    build_station(5, 17, 34, 42, PURPLE_WOOL, 4, 38)

    blocks.place(
        blocks.lever(BLOCK_TOP_POINTS_EAST_WHEN_OFF),
        pos(7, 0, 37)
    )
    blocks.place(REDSTONE_WIRE, pos(8, 0, 37))
    blocks.place(STONE, pos(9, 0, 37))
    blocks.place(REDSTONE_TORCH, pos(9, 1, 37))
    blocks.place(REDSTONE_LAMP, pos(10, 1, 37))

    blocks.place(
        blocks.lever(BLOCK_TOP_POINTS_EAST_WHEN_OFF),
        pos(7, 0, 40)
    )
    blocks.place(REDSTONE_WIRE, pos(8, 0, 40))
    blocks.place(REDSTONE_WIRE, pos(9, 0, 40))
    blocks.place(REDSTONE_WIRE, pos(10, 0, 40))
    blocks.place(REDSTONE_LAMP, pos(11, 0, 40))

    blocks.place(RED_WOOL, pos(13, -1, 37))
    blocks.place(GREEN_WOOL, pos(13, -1, 40))


def build_station_5():
    build_station(-17, -5, 44, 52, GREEN_WOOL, -4, 48)

    blocks.fill(
        STONE,
        pos(-13, 0, 47),
        pos(-13, 0, 49),
        FillOperation.REPLACE
    )
    blocks.fill(
        STONE,
        pos(-6, 0, 47),
        pos(-6, 0, 49),
        FillOperation.REPLACE
    )

    blocks.place(
        blocks.block_with_data(STICKY_PISTON, 5),
        pos(-12, 0, 48)
    )
    blocks.place(
        blocks.block_with_data(STICKY_PISTON, 4),
        pos(-7, 0, 48)
    )

    blocks.place(BLUE_WOOL, pos(-11, 0, 48))
    blocks.place(RED_WOOL, pos(-8, 0, 48))

    blocks.place(
        blocks.lever(BLOCK_TOP_POINTS_EAST_WHEN_OFF),
        pos(-13, 1, 48)
    )
    blocks.place(
        blocks.lever(BLOCK_TOP_POINTS_EAST_WHEN_OFF),
        pos(-6, 1, 48)
    )

    blocks.fill(
        GLASS,
        pos(-14, 2, 47),
        pos(-5, 2, 49),
        FillOperation.REPLACE
    )


def build_station_6():
    build_station(5, 17, 54, 62, CYAN_WOOL, 4, 58)

    blocks.place(STONE_PRESSURE_PLATE, pos(8, 0, 57))
    blocks.place(STONE_PRESSURE_PLATE, pos(11, 0, 57))
    blocks.place(STONE_PRESSURE_PLATE, pos(14, 0, 57))

    blocks.place(REDSTONE_LAMP, pos(8, 0, 58))
    blocks.place(REDSTONE_LAMP, pos(11, 0, 58))
    blocks.place(REDSTONE_LAMP, pos(14, 0, 58))

    blocks.place(STONE_PRESSURE_PLATE, pos(8, 0, 60))
    blocks.place(STONE_PRESSURE_PLATE, pos(11, 0, 60))
    blocks.place(STONE_PRESSURE_PLATE, pos(14, 0, 60))

    blocks.place(REDSTONE_LAMP, pos(8, 0, 61))
    blocks.place(REDSTONE_LAMP, pos(11, 0, 61))
    blocks.place(REDSTONE_LAMP, pos(14, 0, 61))


def build_station_7():
    build_station(-17, -5, 64, 72, YELLOW_WOOL, -4, 68)

    blocks.place(CHEST, pos(-14, 0, 68))
    blocks.place(HOPPER, pos(-14, 1, 68))
    blocks.place(CHEST, pos(-14, 2, 68))

    blocks.place(CHEST, pos(-10, 0, 68))
    blocks.place(HOPPER, pos(-10, 1, 68))
    blocks.place(CHEST, pos(-10, 2, 68))

    blocks.place(CHEST, pos(-6, 0, 68))
    blocks.place(HOPPER, pos(-6, 1, 68))
    blocks.place(CHEST, pos(-6, 2, 68))

    blocks.fill(
        GLASS,
        pos(-16, 0, 71),
        pos(-5, 2, 71),
        FillOperation.REPLACE
    )


def build_station_8():
    build_station(5, 17, 74, 82, MAGENTA_WOOL, 4, 78)

    blocks.place(
        blocks.lever(BLOCK_TOP_POINTS_EAST_WHEN_OFF),
        pos(7, 0, 76)
    )
    blocks.place(REDSTONE_WIRE, pos(7, 0, 77))
    blocks.place(REDSTONE_WIRE, pos(7, 0, 78))
    blocks.place(REDSTONE_WIRE, pos(7, 0, 79))
    blocks.place(REDSTONE_LAMP, pos(7, 0, 80))

    blocks.place(
        blocks.lever(BLOCK_TOP_POINTS_EAST_WHEN_OFF),
        pos(11, 0, 76)
    )
    blocks.place(REDSTONE_WIRE, pos(11, 0, 77))
    blocks.place(
        blocks.repeater(SOUTH, 4),
        pos(11, 0, 78)
    )
    blocks.place(REDSTONE_WIRE, pos(11, 0, 79))
    blocks.place(REDSTONE_LAMP, pos(11, 0, 80))

    blocks.place(
        blocks.lever(BLOCK_TOP_POINTS_EAST_WHEN_OFF),
        pos(15, 0, 76)
    )
    blocks.place(REDSTONE_WIRE, pos(15, 0, 77))
    blocks.place(STONE, pos(15, 0, 78))
    blocks.place(REDSTONE_TORCH, pos(15, 1, 78))
    blocks.place(REDSTONE_LAMP, pos(15, 1, 79))

    blocks.fill(
        GLASS,
        pos(6, 0, 81),
        pos(16, 2, 81),
        FillOperation.REPLACE
    )


def prepare_boards():
    blocks.place(WOOL, course_pos(-6, -1, 1))
    blocks.place(WOOL, course_pos(-5, -1, 4))
    blocks.place(WOOL, course_pos(5, -1, 14))
    blocks.place(WOOL, course_pos(-5, -1, 24))
    blocks.place(WOOL, course_pos(5, -1, 34))
    blocks.place(WOOL, course_pos(-5, -1, 44))
    blocks.place(WOOL, course_pos(5, -1, 54))
    blocks.place(WOOL, course_pos(-5, -1, 64))
    blocks.place(WOOL, course_pos(5, -1, 74))

    mobs.give(
        mobs.target(LOCAL_PLAYER),
        blocks.block_with_data(
            blocks.block_by_name("board"),
            2
        ),
        9
    )

    player.tell(
        mobs.target(LOCAL_PLAYER),
        "已給你9面大型白板，白色羊毛是放置位置"
    )


def clear_course_area():
    blocks.fill(
        AIR,
        pos(-26, 0, 0),
        pos(26, 30, 18),
        FillOperation.REPLACE
    )
    blocks.fill(
        AIR,
        pos(-26, 0, 19),
        pos(26, 30, 37),
        FillOperation.REPLACE
    )
    blocks.fill(
        AIR,
        pos(-26, 0, 38),
        pos(26, 30, 56),
        FillOperation.REPLACE
    )
    blocks.fill(
        AIR,
        pos(-26, 0, 57),
        pos(26, 30, 75),
        FillOperation.REPLACE
    )
    blocks.fill(
        AIR,
        pos(-26, 0, 76),
        pos(26, 30, 88),
        FillOperation.REPLACE
    )

    blocks.fill(
        AIR,
        pos(-32, 0, 89),
        pos(32, 30, 95),
        FillOperation.REPLACE
    )


def clear_logo_area():
    blocks.fill(
        AIR,
        course_pos(-32, 0, 96),
        course_pos(32, 13, 130),
        FillOperation.REPLACE
    )
    blocks.fill(
        AIR,
        course_pos(-32, 14, 96),
        course_pos(32, 27, 130),
        FillOperation.REPLACE
    )
    blocks.fill(
        AIR,
        course_pos(-32, 28, 96),
        course_pos(32, 41, 130),
        FillOperation.REPLACE
    )
    blocks.fill(
        AIR,
        course_pos(-32, 42, 96),
        course_pos(32, 55, 130),
        FillOperation.REPLACE
    )
    blocks.fill(
        AIR,
        course_pos(-32, 56, 96),
        course_pos(32, 60, 130),
        FillOperation.REPLACE
    )


def build_ground():
    blocks.fill(
        blocks.block_by_name("deny"),
        pos(-26, -2, 0),
        pos(26, -2, 88),
        FillOperation.REPLACE
    )
    blocks.fill(
        STONE,
        pos(-26, -1, 0),
        pos(26, -1, 88),
        FillOperation.REPLACE
    )

    blocks.fill(
        blocks.block_by_name("deny"),
        pos(-32, -2, 89),
        pos(32, -2, 130),
        FillOperation.REPLACE
    )
    blocks.fill(
        STONE,
        pos(-32, -1, 89),
        pos(32, -1, 130),
        FillOperation.REPLACE
    )


def build_main_road():
    blocks.fill(
        STONE_BRICKS,
        pos(-2, -1, 0),
        pos(2, -1, 116),
        FillOperation.REPLACE
    )
    blocks.fill(
        YELLOW_WOOL,
        pos(-3, -1, 0),
        pos(-3, -1, 116),
        FillOperation.REPLACE
    )
    blocks.fill(
        YELLOW_WOOL,
        pos(3, -1, 0),
        pos(3, -1, 116),
        FillOperation.REPLACE
    )

    blocks.fill(
        GREEN_WOOL,
        pos(-2, -1, 0),
        pos(2, -1, 2),
        FillOperation.REPLACE
    )
    blocks.fill(
        RED_WOOL,
        pos(-2, -1, 86),
        pos(2, -1, 88),
        FillOperation.REPLACE
    )

    blocks.fill(
        STONE_BRICKS,
        pos(-12, -1, 106),
        pos(12, -1, 116),
        FillOperation.REPLACE
    )
    blocks.fill(
        YELLOW_WOOL,
        pos(-12, -1, 106),
        pos(-12, -1, 116),
        FillOperation.REPLACE
    )
    blocks.fill(
        YELLOW_WOOL,
        pos(12, -1, 106),
        pos(12, -1, 116),
        FillOperation.REPLACE
    )


def build_logo_pixels():
    for row_index in range(50):
        row = logo_image[row_index]
        x = 0

        while x < 50:
            color = row[x]

            if color == ".":
                x += 1
            else:
                start_x = x

                while x < 50 and row[x] == color:
                    x += 1

                if color == "Y":
                    blocks.fill(
                        YELLOW_WOOL,
                        course_pos(25 - x, 52 - row_index, 121),
                        course_pos(24 - start_x, 52 - row_index, 123),
                        FillOperation.REPLACE
                    )
                else:
                    blocks.fill(
                        blocks.block_with_data(WOOL, 15),
                        course_pos(25 - x, 52 - row_index, 121),
                        course_pos(24 - start_x, 52 - row_index, 123),
                        FillOperation.REPLACE
                    )


def build_logo_lamps():
    for index in range(32):
        blocks.place(
            REDSTONE_LAMP,
            course_pos(lamp_x[index], lamp_y[index], 120)
        )
        blocks.place(
            OBSIDIAN,
            course_pos(lamp_x[index], lamp_y[index], 121)
        )


def build_logo():
    blocks.fill(
        IRON_BLOCK,
        course_pos(-29, 0, 118),
        course_pos(28, 0, 125),
        FillOperation.REPLACE
    )

    blocks.fill(
        OBSIDIAN,
        course_pos(-28, 1, 122),
        course_pos(-28, 55, 122),
        FillOperation.REPLACE
    )
    blocks.fill(
        OBSIDIAN,
        course_pos(27, 1, 122),
        course_pos(27, 55, 122),
        FillOperation.REPLACE
    )
    blocks.fill(
        OBSIDIAN,
        course_pos(-28, 55, 122),
        course_pos(27, 55, 122),
        FillOperation.REPLACE
    )

    blocks.fill(
        IRON_BLOCK,
        course_pos(-29, 0, 120),
        course_pos(-25, 2, 124),
        FillOperation.REPLACE
    )
    blocks.fill(
        IRON_BLOCK,
        course_pos(24, 0, 120),
        course_pos(28, 2, 124),
        FillOperation.REPLACE
    )

    build_logo_pixels()
    build_logo_lamps()

    blocks.place(
        GLOWSTONE,
        course_pos(-28, 55, 122)
    )
    blocks.place(
        GLOWSTONE,
        course_pos(27, 55, 122)
    )
    blocks.place(
        GLOWSTONE,
        course_pos(0, 55, 122)
    )


def logo_animation():
    global logo_step

    if logo_running:
        for index2 in range(32):
            if index2 % 4 == logo_step:
                blocks.place(
                    REDSTONE_BLOCK,
                    course_pos(
                        lamp_x[index2],
                        lamp_y[index2],
                        121
                    )
                )
            else:
                blocks.place(
                    OBSIDIAN,
                    course_pos(
                        lamp_x[index2],
                        lamp_y[index2],
                        121
                    )
                )

        logo_step = (logo_step + 1) % 4
        loops.pause(180)
    else:
        loops.pause(100)


def on_build_chat():
    global course_origin
    global logo_running
    global logo_step

    logo_running = False
    loops.pause(300)

    course_origin = player.position()
    logo_step = 0

    clear_course_area()
    clear_logo_area()
    build_ground()
    build_main_road()

    build_execution_station()
    build_station_1()
    build_station_2()
    build_station_3()
    build_station_4()
    build_station_5()
    build_station_6()
    build_station_7()
    build_station_8()
    prepare_boards()
    build_logo()

    logo_running = True

    player.tell(
        mobs.target(LOCAL_PLAYER),
        "紅石大道八關與小孩聯盟Logo完成"
    )


def on_board_chat():
    prepare_boards()


loops.forever(logo_animation)
player.on_chat("7", on_build_chat)
player.on_chat("8", on_board_chat)
