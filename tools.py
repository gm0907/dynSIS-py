#!/usr/bin/env python
# ! ## File: tools.py
# ! ## Print and read functions.
# ! ## See README.md for more information and use
# !-----------------------------------------------------------------------------
# ! SIS epidemic model algorithm based on the article "Simulation of Markovian epidemic models on large networks"
# ! Copyright (C) 2016 Wesley Cota, Silvio C. Ferreira
# ! 
# ! Please cite the above cited paper as reference to our code.
# ! 
# !    This program is free software: you can redistribute it and/or modify
# !    it under the terms of the GNU General Public License as published by
# !    the Free Software Foundation, either version 3 of the License, or
# !    (at your option) any later version.
# !
# !    This program is distributed in the hope that it will be useful,
# !    but WITHOUT ANY WARRANTY; without even the implied warranty of
# !    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# !    GNU General Public License for more details.
# !
# !    You should have received a copy of the GNU General Public License
# !    along with this program.  If not, see <http://www.gnu.org/licenses/>.
# !-----------------------------------------------------------------------------
# ! Author    : Wesley Cota
# ! Email     : wesley.cota@ufv.br
# ! Date      : October 2016
# !-----------------------------------------------------------------------------
# ! See README.md for more details
# ! This code is available at <https://github.com/wcota/dynSIS-py>

# Print functions
def print_error(st):
    raise ValueError(st)

def print_info(st,nl=False):
    if nl:
        print('')
    print('$!', st, '!$')

def print_progress(st):
    pass
    
def print_header():
    print(  '###############################################################################',
            '#### Simulation of Markovian epidemic models on networks: SIS-II algorithm ####',
            '##============ Copyright(C) 2016 Wesley Cota, Silvio C. Ferreira ============##',
            '##======= This code is available at <https://github.com/wcota/dynSIS> =======##',
            '##======= Please cite the above cited paper as reference to our code. =======##',
            '##=== This code is under GNU General Public License. Please see README.md ===##',
            '###############################################################################',
            '',
            sep='\n')