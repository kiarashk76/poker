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
        self.env = rlcard.make('limit-holdem', 
                                {"game_num_players": self.num_in_game_players})
        self.env.reset()

    @property 
    def num_in_game_players(self):
        counter = 0
        for i in range(len(self.all_money)):
            if self.all_money[i] > 0:
                counter += 1
        return counter

    def update_money(self, payoffs):
        counter = 0
        for i in range(len(self.all_money)):
            if self.all_money[i] > 0:
                self.all_money[i] += payoffs[counter] * self.big_blind
                counter += 1
            
    
    def step(self, action):
        self.env.step(action)
        if self.env.is_over():
            payoffs = self.env.get_payoffs()
            self.update_money(payoffs)
            self.reset()
    
    def get_state(self, player_id):
        counter = -1
        for i in range(len(self.all_money)):
            if self.all_money[i] > 0:
                counter += 1
            if i == player_id:
                env_id = counter

        state = self.env.get_state(env_id)
        state['raw_obs']['all_money'] = self.all_money
        state['raw_obs']['my_money'] = self.all_money[env_id]
        if state['raw_obs']['my_money'] <= 0:
            state['legal_actions'] = OrderedDict()
            state['legal_actions'][2] = None
            state['raw_obs']['legal_actions'] = ['fold']
            state['raw_legal_actions'] = ['fold']
        return state
    
    def get_player_id(self):
        env_id = self.env.get_player_id() 
        counter = -1         
        for i in range(len(self.all_money)):
            if self.all_money[i] > 0:
                counter += 1
            if counter == env_id:
                return i
            
    def is_over(self):
        if self.num_in_game_players == 1:
            return True
        return False
    
    def get_payoffs(self):
        return self.env.get_payoffs()
