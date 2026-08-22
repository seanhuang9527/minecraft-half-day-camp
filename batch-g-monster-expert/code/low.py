def on_on_chat():
    agent.set_slot(1)
    for index in range(4):
        agent.place(FORWARD)
        agent.move(RIGHT, 1)
        agent.place(FORWARD)
        agent.move(RIGHT, 1)
        agent.place(FORWARD)
        agent.turn(RIGHT_TURN)
player.on_chat("3", on_on_chat)
