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

import string
import sys
import timeit
import numpy as np
import matplotlib.pyplot as plt

start = timeit.timeit()

def search_letters(strg, alphabet, number_letters):
    alphabet=list(string.ascii_uppercase)
    ustrg=strg.upper()
    counter=0
    letters_counter=np.array([])
    while counter<number_letters:
        letters_counter=np.insert(letters_counter,counter,int(ustrg.count(alphabet[counter])))
        counter+=1
    return letters_counter

with open(sys.argv[1], 'r') as f: #argparse
    txt=f.read()

alphabet=list(string.ascii_uppercase)
number_letters=len(alphabet)
counter=0
counter_letters=search_letters(txt, alphabet, number_letters)
while counter<number_letters:
    print(alphabet[counter],counter_letters[counter])
    counter+=1

fig, ax = plt.subplots()

ax.bar(alphabet, counter_letters)
ax.set_ylabel('Counter Letters')
ax.set_title('Statistics of a Book')

plt.show()

end = timeit.timeit()

print('Elapsed time:',end-start)