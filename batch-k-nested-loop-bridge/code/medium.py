def on_on_chat():
    agent.move(UP, 1)
    for index in range(50):
        for index2 in range(4):
            agent.place(DOWN)
            agent.move(RIGHT, 1)
        agent.move(LEFT, 4)
        agent.move(FORWARD, 1)
        agent.move(UP, 1)
player.on_chat("3", on_on_chat)
