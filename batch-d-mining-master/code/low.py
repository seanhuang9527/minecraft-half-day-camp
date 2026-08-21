def on_on_chat():
    agent.set_slot(1)
    for index in range(4):
        for index2 in range(4):
            agent.destroy(FORWARD)
            agent.move(FORWARD, 1)
            agent.destroy(UP)
            agent.destroy(DOWN)
            agent.move(DOWN, 1)
            agent.collect_all()
        agent.place(RIGHT)
player.on_chat("3", on_on_chat)
