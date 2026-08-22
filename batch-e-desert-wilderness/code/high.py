def on_on_chat():
    agent.set_slot(1)
    agent.move(UP, 1)
    for index in range(12):
        for index2 in range(3):
            agent.place(DOWN)
            agent.move(RIGHT, 1)
        agent.move(LEFT, 3)
        agent.move(FORWARD, 1)
player.on_chat("3", on_on_chat)
