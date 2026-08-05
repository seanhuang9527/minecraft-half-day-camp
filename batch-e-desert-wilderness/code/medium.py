def on_on_chat():
    for index in range(2):
        for index2 in range(3):
            agent.destroy(DOWN)
            agent.move(DOWN, 1)
        for index3 in range(3):
            agent.destroy(FORWARD)
            agent.destroy(BACK)
            agent.destroy(LEFT)
            agent.destroy(RIGHT)
            agent.collect_all()
        agent.move(UP, 3)
        agent.move(FORWARD, 3)
player.on_chat("3", on_on_chat)
