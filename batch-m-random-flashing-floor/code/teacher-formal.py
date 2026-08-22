safe = 0

def build_formal_floor():
    for tile_z in range(4):
        for tile_x in range(4):
            x1 = tile_x * 4 - 8
            z1 = tile_z * 4 + 3
            color_number = (tile_z % 2) * 2 + tile_x % 2
            if color_number == 0:
                blocks.fill(RED_WOOL, pos(x1, -2, z1), pos(x1 + 3, -2, z1 + 3), FillOperation.REPLACE)
            if color_number == 1:
                blocks.fill(YELLOW_WOOL, pos(x1, -2, z1), pos(x1 + 3, -2, z1 + 3), FillOperation.REPLACE)
            if color_number == 2:
                blocks.fill(GREEN_WOOL, pos(x1, -2, z1), pos(x1 + 3, -2, z1 + 3), FillOperation.REPLACE)
            if color_number == 3:
                blocks.fill(BLUE_WOOL, pos(x1, -2, z1), pos(x1 + 3, -2, z1 + 3), FillOperation.REPLACE)

def on_on_chat7():
    blocks.fill(AIR, pos(-9, -13, 2), pos(8, 3, 19), FillOperation.REPLACE)
    blocks.fill(STONE, pos(-1, -1, -2), pos(0, -1, 2), FillOperation.REPLACE)
    blocks.place(GOLD_BLOCK, pos(0, -1, 0))
    blocks.fill(SLIME_BLOCK, pos(-8, -14, 3), pos(7, -14, 18), FillOperation.REPLACE)
    blocks.fill(GLASS, pos(-9, -13, 2), pos(-9, 3, 19), FillOperation.REPLACE)
    blocks.fill(GLASS, pos(8, -13, 2), pos(8, 3, 19), FillOperation.REPLACE)
    blocks.fill(GLASS, pos(-9, -13, 19), pos(8, 3, 19), FillOperation.REPLACE)
    blocks.fill(GLASS, pos(-9, -13, 2), pos(8, -2, 2), FillOperation.REPLACE)
    blocks.fill(GLASS, pos(-9, -1, 2), pos(-2, 3, 2), FillOperation.REPLACE)
    blocks.fill(GLASS, pos(1, -1, 2), pos(8, 3, 2), FillOperation.REPLACE)
    build_formal_floor()
    player.tell(mobs.target(LOCAL_PLAYER), "正式比賽場建立完成！")
player.on_chat("7", on_on_chat7)

def on_on_chat6():
    build_formal_floor()
    player.tell(mobs.target(LOCAL_PLAYER), "正式比賽場已恢復！")
player.on_chat("6", on_on_chat6)

def prepare_formal_floor(shrink):
    build_formal_floor()
    if shrink > 0:
        blocks.fill(AIR, pos(-8, -2, 3), pos(7, -2, 2 + shrink), FillOperation.REPLACE)
        blocks.fill(AIR, pos(-8, -2, 19 - shrink), pos(7, -2, 18), FillOperation.REPLACE)
        blocks.fill(AIR, pos(-8, -2, 3 + shrink), pos(-9 + shrink, -2, 18 - shrink), FillOperation.REPLACE)
        blocks.fill(AIR, pos(8 - shrink, -2, 3 + shrink), pos(7, -2, 18 - shrink), FillOperation.REPLACE)

def on_on_chat5():
    global safe
    shrink = 0
    for round_number in range(10):
        prepare_formal_floor(shrink)
        player.say("第 " + str(round_number + 1) + " 回合！")
        safe = randint(1, 4)
        if safe == 1:
            player.say("安全顏色：紅色！")
        if safe == 2:
            player.say("安全顏色：黃色！")
        if safe == 3:
            player.say("安全顏色：綠色！")
        if safe == 4:
            player.say("安全顏色：藍色！")
        loops.pause(4000)
        min_x = -8 + shrink
        max_x = 7 - shrink
        min_z = 3 + shrink
        max_z = 18 - shrink
        if safe != 1:
            blocks.replace(AIR, RED_WOOL, pos(min_x, -2, min_z), pos(max_x, -2, max_z))
        if safe != 2:
            blocks.replace(AIR, YELLOW_WOOL, pos(min_x, -2, min_z), pos(max_x, -2, max_z))
        if safe != 3:
            blocks.replace(AIR, GREEN_WOOL, pos(min_x, -2, min_z), pos(max_x, -2, max_z))
        if safe != 4:
            blocks.replace(AIR, BLUE_WOOL, pos(min_x, -2, min_z), pos(max_x, -2, max_z))
        player.say("危險地板消失！")
        loops.pause(4000)
        prepare_formal_floor(shrink)
        loops.pause(2000)
        if round_number % 2 == 1:
            shrink += 1
    build_formal_floor()
    player.say("10回合結束！")
player.on_chat("5", on_on_chat5)
