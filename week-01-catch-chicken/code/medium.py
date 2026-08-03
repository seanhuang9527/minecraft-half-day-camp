time_left = 0
score = 0


def on_chat_start():
    global time_left
    global score
    score = 0
    time_left = 30
    player.tell(mobs.target(LOCAL_PLAYER), "比賽開始！")
    for index in range(30):
        player.tell(mobs.target(LOCAL_PLAYER), "剩餘時間：" + str(time_left))
        loops.pause(1000)
        time_left += -1
    player.tell(mobs.target(LOCAL_PLAYER), "時間到！最後得分：" + str(score))


player.on_chat("2", on_chat_start)


def on_mob_killed_chicken():
    global score
    if time_left > 0:
        score += 1
        player.tell(mobs.target(LOCAL_PLAYER), "分數：" + str(score))


mobs.on_mob_killed(CHICKEN, on_mob_killed_chicken)
