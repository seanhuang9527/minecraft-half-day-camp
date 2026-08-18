def on_on_chat():
    for index in range(36):
        agent.set_slot(2)
        agent.place(RIGHT)

        agent.set_slot(1)
        agent.move(FORWARD, 1)
        agent.place(BACK)

player.on_chat("2", on_on_chat)
