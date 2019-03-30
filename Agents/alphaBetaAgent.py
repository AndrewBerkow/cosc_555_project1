from abc import ABCMeta, abstractmethod

class AlphaBetaAgent:
    __metaclass__ = ABCMeta

    @classmethod
    def version(self):
        return "1.0"

    @abstractmethod
    def min_max_decision(self, state):
        """
        Use the min max algorithm to get best possible action given utility function.
        :param state: An object that represents a state or an environment
        :return action: A list with the last index storing utility score for action. @todo - actions would be better as a dict with utility and action as seperate indexes.
        """
        raise NotImplementedError

    @abstractmethod
    def max_value(self, state):
        """
        Perform max value step of the min max algorithm
        :param state: An object that represents a state of an environment
        :return utility_value: The utility value of the action with the max utility value according to evaluate_state()
        """
        raise NotImplementedError

    @abstractmethod
    def min_value(self, state):
        """
        Perform min value step of the min max algorithm
        :param state: An object that represents a state of an environment
        :return utility_value: The utility value of the action with the min utility value according to evaluate_state()
        """
        raise NotImplementedError

    @abstractmethod
    def terminal_test(self, state):
        '''
        Test to see if the game is over
        :param state: An object that represents a state of an environment
        :return game_over: True is game over
        '''
        raise NotImplementedError

    @abstractmethod
    def get_possible_actions(self, state):
        '''
        Get possible actions given current state of an environment
        :param state: An object that represents a state of an environment
        :return possible_actions: List of actions that are possible
        '''
        raise NotImplementedError

    @abstractmethod
    def evaluate_state(self, state):
        """
        Function that computes utility given current state of an environment
        :param state: An object that represents a state of an environment
        :return utility: An int score that can be positive or negative to represent utility of current state
        """
        raise NotImplementedError
