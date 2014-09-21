#==============================================================================#
#                                 DurakGame.py                                 #
#==============================================================================#

#============#
#  Includes  #
#============#

import sys
import random
from DurakRules import DurakRules, DomainError

def pop_slice(cards, n):
  ret = cards[-n:]
  del cards[-n:]
  return ret

class ArgError(Exception):
  """
  ArgError exception is raised if the user has not specified mandatory arguments
  """
  def __init__(self, value):
    self.value = value
  def __str__(self):
    return repr(self.value)

class DurakGame(DurakRules):

  """Docstring for DurakGame. """
  mandatory_arguments = ['players']
  optional_arguments  = ['decksize', 'families', 'handcards']

  def __init__(self, *args, **kwargs):
    """@todo: to be defined1.

    :decksize: @todo
    :families: @todo

    """
    for arg in DurakGame.mandatory_arguments:
      if not arg in kwargs:
        raise ArgError("Argument '" + arg + "' missing" )
      if arg == 'players':
        players = kwargs['players']
        if players < 2:
          raise DomainError("Invalid playernumber" )
        self.players = players

    super(DurakGame, self).__init__(*args, **kwargs)

    if 'handcards' in kwargs:
      hc = kwargs['handcards']
      if not ( (hc > 0) and (hc < self.decksize/players)):
        raise DomainError("Invalid handcards" )
    else:
      hc = 5
      if not ( (hc > 0) and (hc < self.decksize/players)):
        raise DomainError("Handcards are by default 5, conflict with" +
                          "playernumbers and decksize" )
      self.handcards = hc

  def distribute_cards(self, deck):
    self.player_cards = {}
    for player in range(self.players):
      self.player_cards[player] = pop_slice(deck, self.handcards)

  def determine_trumpf(self, deck):
    trumpf_card = pop_slice(deck, 1)[0]
    self.declare_trumpf(self.card_family[trumpf_card])
    deck = [trumpf_card] + deck
    return trumpf_card
  
  def HumanPlayer(self, number):
    mycards = self.player_cards[number]
    print mycards
    print "which one?"
    player_answer = sys.stdin.readline()
    player_answer = [int(u) for u in player_answer.split()]
    return player_answer
  
  def start_game(self):
    deck = range(self.decksize)
    random.shuffle(deck)
    self.distribute_cards(deck)
    trumpf_card = self.determine_trumpf(deck)

    removed_cards         = []
    cards_played          = []
    open_cards_on_table   = []
    closed_cards_on_table = []
    self.HumanPlayer(0)
    #for player in range(self.players):
      #player_cards = pop_slice(deck, self.handcards)
      #print "player, player_cards:", player, player_cards
      #data = sys.stdin.readline()
      #if not data:
        #return


