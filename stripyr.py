#!/usr/bin/env python3
"""
	stripyr is a program that strips extra data from a text file
	Copyright 2016 Kevin R. Kowalczyk

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from sys import argv

script, target, dest = argv

in_file = open(target)
out_file = open(dest, 'w')

print ("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

for line in in_file:
	text = line.split(' ')
	text[0] += '\n'
	out_file.write(text[0])

in_file.close()
out_file.close()