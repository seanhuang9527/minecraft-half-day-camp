def on_on_chat():
    agent.move(UP, 2)
    agent.set_slot(2)
    for index in range(4):
        for index2 in range(4):
            agent.place(DOWN)
            agent.move(FORWARD, 1)
        agent.move(BACK, 4)
        agent.move(RIGHT, 1)
player.on_chat("3", on_on_chat)
