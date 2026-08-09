time = 0
score = 0


def on_block_broken_iron_ore():
    global score
    if time > 0:
        score += 2
blocks.on_block_broken(IRON_ORE, on_block_broken_iron_ore)


def on_chat_2():
    player.execute("title @s actionbar 最後總分:" + str(score))
player.on_chat("2", on_chat_2)


def on_block_broken_coal_ore():
    global score
    if time > 0:
        score += 1
blocks.on_block_broken(COAL_ORE, on_block_broken_coal_ore)


def on_block_broken_gold_ore():
    global score
    if time > 0:
        score += 3
blocks.on_block_broken(GOLD_ORE, on_block_broken_gold_ore)


def on_chat_1():
    global time, score
    time = 60
    score = 0
    gameplay.title(mobs.target(LOCAL_PLAYER), "挖礦挑戰賽", "開始!")

    while time > 0:
        player.execute("title @s actionbar 時間:" + str(time) + " 分數:" + str(score))
        loops.pause(1000)
        time += 0 - 1

    player.execute("title @s actionbar 時間到 分數:" + str(score))
player.on_chat("1", on_chat_1)


def on_block_broken_diamond_ore():
    global score
    if time > 0:
        score += 5
blocks.on_block_broken(DIAMOND_ORE, on_block_broken_diamond_ore)
