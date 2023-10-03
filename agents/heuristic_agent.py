import rlcard
from rlcard.agents import RandomAgent
import numpy as np


class HeuristicAgent(object):
    ''' A random agent. Random agents is for running toy examples on the card games
    '''

    def __init__(self, num_actions, name):
        ''' Initilize the random agent

        Args:
            num_actions (int): The size of the ouput action space
        '''
        self.use_raw = False
        self.num_actions = num_actions
        self.name = name
        
    @staticmethod
    def step(state):
        ''' Predict the action given the curent state in gerenerating training data.

        Args:
            state (dict): An dictionary that represents the current state

        Returns:
            action (int): The action predicted (randomly chosen) by the random agent
        '''
        hand = state['raw_obs']['hand']
        ground = state['raw_obs']['public_cards']
        all_money = state['raw_obs']['all_money']
        all_chips = state['raw_obs']['all_chips']
        my_money = state['raw_obs']['my_money']
        my_chips = state['raw_obs']['my_chips']
        print("heuristic:", hand, ground, all_money, all_chips, my_money, my_chips)
        return np.random.choice(list(state['legal_actions'].keys()))


