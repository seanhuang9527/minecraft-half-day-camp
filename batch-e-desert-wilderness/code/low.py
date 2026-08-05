def on_on_chat():
    for index in range(3):
        agent.destroy(DOWN)
        agent.move(DOWN, 1)
    for index2 in range(3):
        agent.destroy(FORWARD)
        agent.destroy(BACK)
        agent.destroy(LEFT)
        agent.destroy(RIGHT)
        agent.collect_all()
player.on_chat("3", on_on_chat)
