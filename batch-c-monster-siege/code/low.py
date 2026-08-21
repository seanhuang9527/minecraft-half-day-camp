def on_on_chat():
    agent.move(UP, 1)
    agent.set_slot(1)
    for index in range(4):
        agent.place(DOWN)
        agent.move(FORWARD, 1)
player.on_chat("1", on_on_chat)
