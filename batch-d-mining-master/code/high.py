def on_on_chat():
    for index in range(4):
        for index2 in range(5):
            agent.destroy(FORWARD)
            agent.move(FORWARD, 1)
            agent.destroy(UP)
        agent.move(BACK, 5)
        for index3 in range(5):
            agent.destroy(BACK)
            agent.move(BACK, 1)
            agent.destroy(UP)
        agent.move(FORWARD, 5)
        agent.turn(RIGHT_TURN)
        for index4 in range(3):
            agent.destroy(FORWARD)
            agent.move(FORWARD, 1)
            agent.destroy(UP)
        agent.turn(LEFT_TURN)
player.on_chat("4", on_on_chat)
