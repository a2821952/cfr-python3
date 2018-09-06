# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 17:55:28 2018

@author: Yao
"""
from card import *
from pokertrees import *
from pokergames import *
players = 2
deck = [Card(14,1),Card(13,2),Card(13,1),Card(12,1)]
rounds = [RoundInfo(holecards=1,boardcards=0,betsize=2,maxbets=[2,2]),RoundInfo(holecards=0,boardcards=1,betsize=4,maxbets=[2,2])]
ante = 1
blinds = [1,2]
gamerules = GameRules(players, deck, rounds, ante, blinds, handeval=leduc_eval)
gametree = GameTree(gamerules)
gametree.build()



from pokertrees import *
from pokergames import *
from pokerstrategy import *
rules = leduc_rules()

# load first player strategy
s0 = Strategy(0)
s0.load_from_file('strategies/leduc/0.strat')

# load second player strategy
s1 = Strategy(1)
s1.load_from_file('strategies/leduc/1.strat')

# Create a strategy profile for this game
profile = StrategyProfile(rules, [s0,s1])

ev = profile.expected_value()
