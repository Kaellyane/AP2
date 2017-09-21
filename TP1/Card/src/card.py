#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`card` module 

:author: ` YOUR NAME
         Univ. Lille <http://portail.fil.univ-lille1.fr>`_

:date: 2017, september. Last revision: 2017, september


"""



import random



class Card(object):
    """
    Cards are defined by a value and a color.
    Possible values and colors are listed in ``Card.VALUES`` and ``Card.COLORS``.

    >>> c1 = Card("Ace", "heart")
    >>> c1.get_color()
    'heart'
    >>> c1.get_value()
    'Ace'
    >>> c1
    Card("Ace", "heart")
    >>> c2 = Card.random()
    >>> c2.get_value() in Card.VALUES
    True
    >>> c2.get_color() in Card.COLORS
    True
    >>> c1 == c1
    True
    >>> c1 != c1
    False
    >>> c1 < c1
    False
    >>> c1 <= c1
    True
    """

    ## tuple of possible values and colors in ascending order
    VALUES = ("Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Knight", "Queen", "King")
    """
    possible values for card's construction
    """
    
    COLORS = ("spade", "heart", "diamond", "club")
    """
    possible colors for card's construction
    """
    
    def __init__(self, value, color):
        """
        creates a card with value and color

        :param value: value of the card
        :type value: element of `Card.VALUES`
        :param color: color of the card
        :type color: element of `Card.COLORS`
        """
        self.__value = VALUES
        self.__color = COLORS
    
    def random():
        """
        create a card whose value and color are randomly chosen
        
        :returns: *(card)* -- a randomly chosen card
        
        >>> c = Card.random()
        >>> c.get_value() in Card.VALUES
        True
        >>> c.get_color() in Card.COLORS
        True
        """
        Val = random.choice(VALUES)
        Col = random.choice(COLORS)
        return Card(Val,Col)

    def get_color(self):
        """
        returns the color of the card

        :return: the color of the card
        :rtype: str
        :UC: none
        :Example:

        >>> c = Card('Ace', 'heart')
        >>> c.get_color()
        'heart'
        """
        return self.color

    def get_value(self):
        """
        returns the value of the card
    
        :param card: the card
        :type card: card
        :returns:  the value of the card
        :rtype: str
        :UC: none
        :Example:
        
        >>> c = Card('Ace', 'heart')
        >>> c.get_value()
        'Ace'
        """
        return self.value

    
    def compare_value(self, card):
         """
         compares cards values

         :param card: the second card
         :type card: card
         :return: (int)

            * a positive number if self's value is greater than card's
            * a negative number if self's value is lower than card's
            * 0 if self's value is the same greater than card's
         :UC: none
         :Example: 

         >>> c1 = Card('Ace', 'heart')
         >>> c2 = Card('King', 'heart')
         >>> c3 = Card('Ace', 'spade')
         >>> c1.compare_value(c2) < 0
         True
         >>> c2.compare_value(c1) > 0
         True
         >>> c3.compare_value(c1) == 0
         True
         """
         val1 = self.get_value()
         val2 = C2.get_value()
         comp = card.values.index(val1) - card.values.index(val2)
         return comp
        
    def compare_color(self, card):
        """
        compares cars colors, returns : 
        
        :param card: the second card
        :type card: card
        :returns: *(int)* --      
          
           * a positive number if self's color is greater than card's
           * a negative number if self's color is lower than card's
           * 0 if self's color is the same greater than card's
        :UC: none
        :Example: 

        >>> c1 = Card('Ace', 'heart')
        >>> c2 = Card('King', 'heart')
        >>> c3 = Card('Ace', 'spade')
        >>> c1.compare_color(c3) > 0
        True
        >>> c3.compare_color(c1) < 0
        True
        >>> c1.compare_color(c2) == 0
        True
        """
        col1 = self.get_color()
        col2 = C2.get_color()
        comp = card.COLORS.index(col1) - card.COLORS.index(col2)
        return comp

    def compare(self, card):
        """
        compares cards.

        Order on cards is defined  first by order on values, and in case of equal values 
        by order on colors. Order on values is defined by `VALUES` attribute. Same for colors.

        :param card: the second card
        :type card: card

        :return: *(int)* --     
          
           * a positive number if self is greater than card
           * a negative number if self is lower than card
           * 0 if self is the same than card

        :UC: none
        :Example: 

        >>> c1 = Card('Ace', 'heart')
        >>> c2 = Card('King', 'heart')
        >>> c3 = Card('Ace','spade')
        >>> c1bis = Card('Ace','heart')
        >>> c1.compare(c2) < 0
        True
        >>> c2.compare(c1) > 0
        True
        >>> c1.compare(c3) > 0
        True
        >>> c1bis.compare(c1bis) == 0
        True
        """
        pass
    

if __name__ == '__main__':
    import doctest
    doctest.testmod()
