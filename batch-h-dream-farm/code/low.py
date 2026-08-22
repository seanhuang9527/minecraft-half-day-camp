def on_on_chat():
    agent.move(UP, 1)
    agent.set_slot(1)
    for index in range(5):
        agent.till(DOWN)
        agent.place(DOWN)
        agent.move(FORWARD, 1)
player.on_chat("4", on_on_chat)
