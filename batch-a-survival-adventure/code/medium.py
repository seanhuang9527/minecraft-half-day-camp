def on_on_chat():
    agent.destroy(FORWARD)
    agent.move(FORWARD, 1)
    for index in range(20):
        agent.destroy(FORWARD)
        agent.destroy(RIGHT)
        agent.move(FORWARD, 1)
        agent.destroy(RIGHT)
        agent.move(BACK, 1)
        agent.destroy(UP)
        agent.move(UP, 1)
        agent.collect_all()
player.on_chat("3", on_on_chat)
