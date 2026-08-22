def on_on_chat():
    agent.set_slot(1)
    for index in range(15):
        agent.move(FORWARD, 1)
        if agent.inspect(AgentInspection.BLOCK, DOWN) == 152:
            agent.destroy(DOWN)
            agent.collect_all()
        else:
            agent.place(RIGHT)
player.on_chat("4", on_on_chat)
