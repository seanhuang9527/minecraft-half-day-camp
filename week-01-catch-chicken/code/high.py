time_left = 0
score = 0


def on_chat_start():
    global time_left
    global score
    score = 0
    time_left = 30
    player.tell(mobs.target(LOCAL_PLAYER), "進階賽開始！")
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
        player.tell(mobs.target(LOCAL_PLAYER), "抓到雞！分數：" + str(score))


mobs.on_mob_killed(CHICKEN, on_mob_killed_chicken)


def on_mob_killed_cow():
    global score
    if time_left > 0:
        score += -3
        player.tell(mobs.target(LOCAL_PLAYER), "打錯目標，扣 3 分！目前分數：" + str(score))


mobs.on_mob_killed(COW, on_mob_killed_cow)


def on_mob_killed_sheep():
    if time_left > 0:
        player.tell(mobs.target(LOCAL_PLAYER), "獲得 10 秒加速！")
        mobs.apply_effect(SPEED, mobs.target(LOCAL_PLAYER), 10, 1)


mobs.on_mob_killed(SHEEP, on_mob_killed_sheep)


def on_mob_killed_bat():
    if time_left > 0:
        player.tell(mobs.target(LOCAL_PLAYER), "碰到陷阱，失明 5 秒！")
        mobs.apply_effect(BLINDNESS, mobs.target(LOCAL_PLAYER), 5, 1)


mobs.on_mob_killed(BAT, on_mob_killed_bat)
