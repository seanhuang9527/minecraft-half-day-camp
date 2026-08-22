time = 0

def on_chat_1():
    global time
    time = 60
    gameplay.title(mobs.target(LOCAL_PLAYER), "挖礦挑戰賽", "開始!")
    while time > 0:
        player.execute("title @s actionbar 時間:" + str(time))
        loops.pause(1000)
        time += 0 - 1
    player.execute("title @s actionbar 時間到")
player.on_chat("1", on_chat_1)
