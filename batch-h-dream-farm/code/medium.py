def on_on_chat():
    agent.move(UP, 1)
    agent.set_slot(1)
    for index in range(5):
        for index2 in range(5):
            agent.move(FORWARD, 1)
            agent.destroy(DOWN)
            agent.place(DOWN)
            agent.collect_all()
        agent.move(BACK, 5)
        agent.move(RIGHT, 1)
player.on_chat("3", on_on_chat)
