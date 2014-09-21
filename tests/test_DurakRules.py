#==============================================================================#
#                                test_tensor.py                                #
#==============================================================================#

#============#
#  Includes  #
#============#

from test_tools import *
from DurakRules import DurakRules
from DurakGame  import DurakGame


class Test_UserDatabase(object):

  def test_family_member(self):
    DR = DurakRules()
    eq_(DR.family_members[3], range(24, 32))

  def test_declare_trumpf(self):
    DR1 = DurakRules(32)
    DR1.declare_trumpf(0)

    DR2 = DurakRules(32)
    family_name = DurakRules.family_names[0]
    DR2.declare_trumpf(family_name)

    eq_(DR1.trumpf, DR2.trumpf)

  def test_value_family(self):
    DR = DurakRules(32)
    first_family  = [0, 8, 16, 24]
    fourth_family = [ u + 3 for u in first_family]
    eq_(DR.value_family[0], first_family)
    eq_(DR.value_family[3], fourth_family)

  def test_value_family(self):

    DR = DurakRules(32)
    family_name = DurakRules.family_names[0]
    DR.declare_trumpf(family_name)

    eq_(DR.valid_hit(6,7), True)
    eq_(DR.valid_hit(7,6), False)
    eq_(DR.valid_hit(7,8), False)
    eq_(DR.valid_hit(8,7), True)
    eq_(DR.valid_hit(2,15), False)
    
    family_name = DurakRules.family_names[1]
    DR.declare_trumpf(family_name)
    eq_(DR.valid_hit(7,8), True)
    print DR.family_members[1]
    





