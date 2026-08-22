def on_on_chat():
    for index in range(15):
        agent.move(FORWARD, 1)
        if agent.inspect(AgentInspection.BLOCK, DOWN) == 152:
            agent.destroy(DOWN)
        agent.collect_all()
player.on_chat("4", on_on_chat)
