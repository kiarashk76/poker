import rlcard

from agent import RandomAgent

env = rlcard.make('limit-holdem', 
                  {"game_num_players":2})
agents = [RandomAgent(num_actions=env.num_actions), 
            RandomAgent(num_actions=env.num_actions)]
env.set_agents(agents)

# print(env.num_actions) # 2
# print(env.num_players) # 1
# print(env.state_shape) # [[2]]
# print(env.action_shape) # [None]

info, first_player_id = env.reset()
while not env.is_over():
    curr_player_id = env.get_player_id()
    curr_state = env.get_state(curr_player_id)
    curr_player = agents[curr_player_id]
    action = curr_player.step(curr_state)
    print(curr_player_id)
    env.step(action)