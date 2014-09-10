#==============================================================================#
#                                DurakRules.py                                 #
#==============================================================================#

#============#
#  Includes  #
#============#

import types

#==============================================================================#
#                                 DomainError                                  #
#==============================================================================#

class DomainError(Exception):
  """
  DomainError exception is raised if the user specified a wrong domain, e.g.
  ranges of args and metrics, wrong tensor multiplication/addition etc.
  """
  def __init__(self, value):
    self.value = value
  def __str__(self):
    return repr(self.value)

#==============================================================================#
#                                  DurakRules                                  #
#==============================================================================#

class DurakRules(object):

  """Docstring for DurakRules. """
  family_names = ["Herz", "Kreuz", "Karo", "Pik"]

  def __init__(self, decksize = 32, families = 4, **kwargs):
    """@todo: to be defined1.

    :decksize: @todo
    :families: @todo

    """
    print "decksize%families:", decksize%families
    print "decksize:", decksize
    print "families:", families
    if not isinstance(decksize, types.IntType):
      raise DomainError('Decksize must be an integer' )
    if decksize%families != 0:
      raise DomainError('Number of cards not divisable by ' +
                        str(families) + ' familiies' )
    self.family_size   = decksize/families
    self.decksize = decksize
    self.families = families

    self.family_dict  = {DurakRules.family_names[i]: i for i in range(families)}

    # Given a family value, family_members returns all members of that family
    self.family_members = {}
    # Given a card, values_family returns to which family the card belongs
    self.card_family    = {}
    # Given a card, card_value returns the cards value
    self.card_value     = {}
    # Given a card value ( domain = range( family_size))
    self.value_family   = {}

    for family_id, offset in enumerate(range(0, decksize, self.family_size)):
      family_members = range(offset, offset + self.family_size)
      self.family_members[family_id] = family_members
      self.card_family.update({val: family_id for val in family_members})

    for card_value in range(self.family_size):
      self.value_family[card_value] = [ self.family_members[family_id]
                                        [card_value] for family_id in
                                        self.family_members ]
      for family_id in self.family_members:
        card_id = self.family_members[family_id][card_value]
        self.card_value[card_id] = card_value

  def declare_trumpf(self, trumpf):
    """@todo: Docstring for declare_trumpf.

    :trumpf: @todo
    :returns: @todo

    """
    if isinstance(trumpf, types.StringType):
      if trumpf in self.family_dict:
        self.trumpf = self.family_dict[trumpf]
      else:
        raise DomainError('Invalid trumpf' )
    elif isinstance(trumpf, types.IntType):
      if trumpf < self.families:
        self.trumpf = trumpf
      else:
        raise DomainError('Invalid trumpf' )

  def valid_hit(self, value_bottom, value_on_top):
    f1 = self.card_family[value_on_top]
    f2 = self.card_family[value_bottom]
    # card in the same family
    if (f1 == f2):
      if value_on_top > value_bottom:
        return True
      else:
        return False
    # cards differ in family
    else:
      if self.card_family[value_on_top] == self.trumpf:
        return True
      else:
        return False
