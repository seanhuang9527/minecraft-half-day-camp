score = 0


def on_chat_reset():
    global score
    score = 0
    player.tell(mobs.target(LOCAL_PLAYER), "分數歸零")


player.on_chat("1", on_chat_reset)


def on_mob_killed_chicken():
    global score
    score += 1
    player.tell(mobs.target(LOCAL_PLAYER), "分數：" + str(score))


mobs.on_mob_killed(CHICKEN, on_mob_killed_chicken)
