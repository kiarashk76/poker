import rlcard
from agent import RandomAgent
from env import ModifiedEnvironment

env = ModifiedEnvironment(3, [3, 3, 3])
agents = [RandomAgent(num_actions=env.num_actions, name="mohsen"), 
            RandomAgent(num_actions=env.num_actions, name="kiarash"),
            RandomAgent(num_actions=env.num_actions, name="hamza")]
env.set_agents(agents)
env.reset()

while not env.is_over():
    curr_player_id = env.get_player_id()
    curr_state = env.get_state(curr_player_id)
    curr_player = agents[curr_player_id]
    action = curr_player.step(curr_state)
    print(f"Money: {env.all_money}")
    print(f"player {curr_player.name} action {action}")
    # print(f"player: {curr_player_id}, action: {action}, state: {curr_state['raw_obs']}")
    env.step(action)
    input("")
print(f"Money:{env.all_money}")

    
