#!/usr/bin/env python
# Copyright (C) 2022 Giuseppe Antonio Motisi, Giulia Nigrelli
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import sphinx
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import InterpolatedUnivariateSpline

class Probability_density_function:
    """
    """
    def __init__(self,x,y):
        """
        """
        super().__init__(self.x, self.y)

if __name__ == '__main__':
    x = np.linspace(0., np.pi, 50)
    y = 1-np.exp(x)
    plt.plot(x,y,'o')
    #plt.plot(x,y)
    f = InterpolatedUnivariateSpline(x,y)
    plt.plot(np.linspace(0., np.pi, 200), f(np.linspace(0., np.pi, 200)), label = 'spline')
    plt.show()