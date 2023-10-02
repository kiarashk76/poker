import rlcard
from agent import RandomAgent
from collections import OrderedDict

class ModifiedEnvironment():
    def __init__(self, num_agents, init_money_lst):
        self.num_agents = num_agents
        self.all_money = init_money_lst
        self.env = rlcard.make('limit-holdem', 
                                {"game_num_players": num_agents})
        self.num_actions = self.env.num_actions
        self.big_blind = 2
    
    def set_agents(self, agents_lst):
        self.env.set_agents(agents_lst)
    
    def reset(self):
        self.env.reset()

    def step(self, action):
        self.env.step(action)
        if self.env.is_over():
            payoffs = self.env.get_payoffs()
            for i in range(len(self.all_money)):
                self.all_money[i] += payoffs[i] * self.big_blind
            
            self.env.reset()
    
    def get_state(self, player_id):
        state = self.env.get_state(player_id)
        state['raw_obs']['all_money'] = self.all_money
        state['raw_obs']['my_money'] = self.all_money[player_id]
        if state['raw_obs']['my_money'] <= 0:
            state['legal_actions'] = OrderedDict()
            state['legal_actions'][2] = None
            state['raw_obs']['legal_actions'] = ['fold']
            state['raw_legal_actions'] = ['fold']
        return state
    
    def get_player_id(self):
        return self.env.get_player_id()            
    
    def is_over(self):
        num_lost_players = 0
        for i in range(len(self.all_money)):
            if self.all_money[i] <= 0:
                num_lost_players +=1
        if num_lost_players >= self.num_agents - 1:
            return True
        return False
    
    def get_payoffs(self):
        return self.env.get_payoffs()
