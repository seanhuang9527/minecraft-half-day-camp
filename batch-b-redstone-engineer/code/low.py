def on_on_chat():
    agent.set_slot(1)

    for index in range(36):
        agent.move(FORWARD, 1)
        agent.place(BACK)

player.on_chat("1", on_on_chat)
