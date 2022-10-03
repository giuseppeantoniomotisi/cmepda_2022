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
import argparse
import timeit
import numpy as np
import matplotlib.pyplot as plt

start = timeit.timeit()

def search_letters(strg, alphabet):
 alphabet = list(string.ascii_uppercase)
 number_letters = len(list(string.ascii_uppercase))
 counter = 0
 letters_counter = np.array([], dtype=int)
 while counter<number_letters:
  letters_counter = np.insert(letters_counter,counter,int(strg.count(alphabet[counter])))
  counter += 1
 return letters_counter

def histo(alphabet, counter_letters):
 fig, ax = plt.subplots()
 ax.bar(alphabet, counter_letters)
 ax.set_ylabel('Counter Letters')
 ax.set_title('Statistics of a Book')
 plt.show()

def process(file_path, bool_histo):
 """
 """
 print(f'Opening input file {file_path}...')
 
 with open(file_path, 'r') as input_file:
  text = input_file.read().upper()
  if bool_histo == 'Y':
    histo(list(string.ascii_uppercase), search_letters(text,string.ascii_uppercase))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='This module print a Statistics of a Book. You have to use the command $python3 assigment1.py inputfilepath/inputfilename.txt$ to use the programm.')
    parser.add_argument('infile', type=str, help='Path to the Input File')
    parser.add_argument('-histo', choices=['Y', 'N'],type=str, default='N', help="Show Histogram of the Frequences", action="store")
    args = parser.parse_args()
    process(args.infile, args.histo)

print('Elapsed time:',timeit.timeit()-start)