score = 0

def on_block_broken_iron_ore():
    global score
    score += 2
    player.tell(mobs.target(LOCAL_PLAYER), score)
blocks.on_block_broken(IRON_ORE, on_block_broken_iron_ore)

def on_chat_2():
    player.tell(mobs.target(LOCAL_PLAYER), score)
player.on_chat("2", on_chat_2)

def on_block_broken_coal_ore():
    global score
    score += 1
    player.tell(mobs.target(LOCAL_PLAYER), score)
blocks.on_block_broken(COAL_ORE, on_block_broken_coal_ore)

def on_block_broken_gold_ore():
    global score
    score += 3
    player.tell(mobs.target(LOCAL_PLAYER), score)
blocks.on_block_broken(GOLD_ORE, on_block_broken_gold_ore)

def on_chat_1():
    global score
    score = 0
    gameplay.title(mobs.target(LOCAL_PLAYER), "挖礦挑戰賽", "開始!")
player.on_chat("1", on_chat_1)

def on_block_broken_diamond_ore():
    global score
    score += 5
    player.tell(mobs.target(LOCAL_PLAYER), score)
blocks.on_block_broken(DIAMOND_ORE, on_block_broken_diamond_ore)
