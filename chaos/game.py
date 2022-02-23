"""
A class that represents and runs chaos games.
"""

from decimal import Decimal as D

import chaos.math


class Game:
    """
    A chaos game.
    """

    # The vertexes for the intial polygon.
    vertex_count = 3

    # The points to generate by jumping toward the vertexes.
    point_count = 1000

    # The fraction of the distance to jump toward each vertex.
    factor = D(1) / D(2)
