def on_on_chat():
    agent.set_slot(1)
    for index in range(4):
        agent.place(FORWARD)
        agent.move(RIGHT, 1)
    for index2 in range(4):
        agent.place(FORWARD)
        agent.move(UP, 1)
    for index3 in range(5):
        agent.place(FORWARD)
        agent.move(LEFT, 1)
    for index4 in range(5):
        agent.place(FORWARD)
        agent.move(DOWN, 1)
    agent.set_slot(2)
    agent.move(RIGHT, 1)
    agent.move(UP, 1)
    agent.place(FORWARD)
player.on_chat("3", on_on_chat)
