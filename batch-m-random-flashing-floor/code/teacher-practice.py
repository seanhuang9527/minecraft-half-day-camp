def build_practice_floor(cx, cz):
    blocks.fill(RED_WOOL, pos(cx - 4, -2, cz + 3), pos(cx - 3, -2, cz + 4), FillOperation.REPLACE)
    blocks.fill(YELLOW_WOOL, pos(cx - 2, -2, cz + 3), pos(cx - 1, -2, cz + 4), FillOperation.REPLACE)
    blocks.fill(GREEN_WOOL, pos(cx, -2, cz + 3), pos(cx + 1, -2, cz + 4), FillOperation.REPLACE)
    blocks.fill(BLUE_WOOL, pos(cx + 2, -2, cz + 3), pos(cx + 3, -2, cz + 4), FillOperation.REPLACE)
    blocks.fill(BLUE_WOOL, pos(cx - 4, -2, cz + 5), pos(cx - 3, -2, cz + 6), FillOperation.REPLACE)
    blocks.fill(RED_WOOL, pos(cx - 2, -2, cz + 5), pos(cx - 1, -2, cz + 6), FillOperation.REPLACE)
    blocks.fill(YELLOW_WOOL, pos(cx, -2, cz + 5), pos(cx + 1, -2, cz + 6), FillOperation.REPLACE)
    blocks.fill(GREEN_WOOL, pos(cx + 2, -2, cz + 5), pos(cx + 3, -2, cz + 6), FillOperation.REPLACE)
    blocks.fill(GREEN_WOOL, pos(cx - 4, -2, cz + 7), pos(cx - 3, -2, cz + 8), FillOperation.REPLACE)
    blocks.fill(BLUE_WOOL, pos(cx - 2, -2, cz + 7), pos(cx - 1, -2, cz + 8), FillOperation.REPLACE)
    blocks.fill(RED_WOOL, pos(cx, -2, cz + 7), pos(cx + 1, -2, cz + 8), FillOperation.REPLACE)
    blocks.fill(YELLOW_WOOL, pos(cx + 2, -2, cz + 7), pos(cx + 3, -2, cz + 8), FillOperation.REPLACE)
    blocks.fill(YELLOW_WOOL, pos(cx - 4, -2, cz + 9), pos(cx - 3, -2, cz + 10), FillOperation.REPLACE)
    blocks.fill(GREEN_WOOL, pos(cx - 2, -2, cz + 9), pos(cx - 1, -2, cz + 10), FillOperation.REPLACE)
    blocks.fill(BLUE_WOOL, pos(cx, -2, cz + 9), pos(cx + 1, -2, cz + 10), FillOperation.REPLACE)
    blocks.fill(RED_WOOL, pos(cx + 2, -2, cz + 9), pos(cx + 3, -2, cz + 10), FillOperation.REPLACE)

def build_practice_arena(cx, cz):
    blocks.fill(AIR, pos(cx - 5, -6, cz + 2), pos(cx + 4, 2, cz + 11), FillOperation.REPLACE)
    blocks.fill(STONE, pos(cx - 1, -1, cz - 1), pos(cx, -1, cz + 2), FillOperation.REPLACE)
    blocks.place(GOLD_BLOCK, pos(cx, -1, cz))
    blocks.fill(SLIME_BLOCK, pos(cx - 4, -7, cz + 3), pos(cx + 3, -7, cz + 10), FillOperation.REPLACE)
    blocks.fill(GLASS, pos(cx - 5, -6, cz + 2), pos(cx - 5, 2, cz + 11), FillOperation.REPLACE)
    blocks.fill(GLASS, pos(cx + 4, -6, cz + 2), pos(cx + 4, 2, cz + 11), FillOperation.REPLACE)
    blocks.fill(GLASS, pos(cx - 5, -6, cz + 11), pos(cx + 4, 2, cz + 11), FillOperation.REPLACE)
    blocks.fill(GLASS, pos(cx - 5, -6, cz + 2), pos(cx + 4, -2, cz + 2), FillOperation.REPLACE)
    blocks.fill(GLASS, pos(cx - 5, -1, cz + 2), pos(cx - 2, 2, cz + 2), FillOperation.REPLACE)
    blocks.fill(GLASS, pos(cx + 1, -1, cz + 2), pos(cx + 4, 2, cz + 2), FillOperation.REPLACE)
    build_practice_floor(cx, cz)

def on_on_chat8():
    for index in range(5):
        build_practice_arena(index * 20 - 40, 0)
        build_practice_arena(index * 20 - 40, 20)
    player.tell(mobs.target(LOCAL_PLAYER), "10座練習場建立完成！")
player.on_chat("8", on_on_chat8)

def on_on_chat9():
    build_practice_floor(0, 0)
    player.tell(mobs.target(LOCAL_PLAYER), "這一座練習場已恢復！")
player.on_chat("9", on_on_chat9)
