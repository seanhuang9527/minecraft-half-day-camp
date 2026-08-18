def on_on_chat():
    agent.set_slot(1)

    for index in range(4):
        for index2 in range(8):
            agent.move(FORWARD, 1)
            agent.place(BACK)

        agent.set_slot(2)
        agent.place(RIGHT)

        agent.set_slot(1)
        agent.move(FORWARD, 1)
        agent.place(BACK)

player.on_chat("3", on_on_chat)
