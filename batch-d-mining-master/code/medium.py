def on_on_chat():
    for index in range(10):
        agent.destroy(DOWN)
        agent.move(DOWN, 1)
    for index2 in range(10):
        agent.destroy(FORWARD)
        agent.move(FORWARD, 1)
        agent.destroy(UP)
    agent.move(BACK, 10)
    for index3 in range(10):
        agent.destroy(BACK)
        agent.move(BACK, 1)
        agent.destroy(UP)
    agent.move(FORWARD, 10)
    for index4 in range(10):
        agent.destroy(LEFT)
        agent.move(LEFT, 1)
        agent.destroy(UP)
    agent.move(RIGHT, 10)
    for index5 in range(10):
        agent.destroy(RIGHT)
        agent.move(RIGHT, 1)
        agent.destroy(UP)
    agent.move(LEFT, 10)
player.on_chat("4", on_on_chat)
