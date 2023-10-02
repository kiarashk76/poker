import rlcard
from agent import RandomAgent
from env import ModifiedEnvironment

env = ModifiedEnvironment(3, [100, 100, 100])
agents = [RandomAgent(num_actions=env.num_actions), 
            RandomAgent(num_actions=env.num_actions),
            RandomAgent(num_actions=env.num_actions)]
env.set_agents(agents)
env.reset()
while not env.is_over():
    curr_player_id = env.get_player_id()
    curr_state = env.get_state(curr_player_id)
    curr_player = agents[curr_player_id]
    action = curr_player.step(curr_state)
    print(f"player: {curr_player_id}, action: {action}, state: {curr_state}")
    env.step(action)
