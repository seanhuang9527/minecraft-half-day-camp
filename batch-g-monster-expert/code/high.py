def on_on_chat():
    agent.move(UP, 1)
    for index in range(4):
        for index2 in range(4):
            agent.move(FORWARD, 1)
            agent.set_slot(1)
            agent.place(DOWN)
        agent.turn(RIGHT_TURN)
    agent.move(RIGHT, 2)
    agent.destroy(DOWN)
    agent.move(FORWARD, 2)
    agent.set_slot(2)
    agent.place(DOWN)
player.on_chat("1", on_on_chat)
