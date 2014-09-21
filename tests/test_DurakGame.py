#==============================================================================#
#                                test_tensor.py                                #
#==============================================================================#

#============#
#  Includes  #
#============#

from test_tools import *
from DurakRules import DurakRules
from DurakGame  import DurakGame


class Test_DurakGame(object):

  def test_durak_game(self):
    DG = DurakGame(players = 2)
    DG.start_game()
   
