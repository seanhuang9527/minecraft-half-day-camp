def on_on_chat():
    agent.destroy(FORWARD)
    agent.move(FORWARD, 1)
    for index in range(4):
        agent.destroy(UP)
        agent.move(UP, 1)
        agent.collect_all()
player.on_chat("3", on_on_chat)
