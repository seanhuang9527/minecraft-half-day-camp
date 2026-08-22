def on_on_chat():
    agent.move(UP, 1)
    agent.set_slot(1)
    for index in range(5):
        for index2 in range(5):
            agent.move(FORWARD, 1)
            agent.till(DOWN)
            agent.place(DOWN)
        agent.move(BACK, 5)
        agent.move(RIGHT, 1)
    agent.move(DOWN, 1)
    agent.turn(RIGHT_TURN)
    agent.set_slot(2)
    for index3 in range(4):
        for index4 in range(6):
            agent.move(BACK, 1)
            agent.place(FORWARD)
        agent.turn(RIGHT_TURN)
    agent.move(FORWARD, 1)
player.on_chat("5", on_on_chat)
