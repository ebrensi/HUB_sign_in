#!/usr/bin/env python

# -*- coding: utf-8 -*-
"""
Created on Mon May 18 13:16:20 2015

@author: Efrem
"""

import pandas as pd

df = pd.read_csv('Export_2015-04-16.csv')

col_name_map = {'Submitted Date': 'tstamp',
                'First Name': 'first',
                'Last Name': 'last',
                'Is this your first visit?': 'first?',
                'How did you hear about us?': 'how',
                'Which Hub are you a Member of?': 'alt_hub',
                'Who are you visiting?': 'visiting',
                'Type of Visit': 'type',
                'Completion Time': 'form_time'}

df = df.rename(columns=col_name_map)

df = df[['tstamp', 'first', 'last', 'first?',
         'type', 'visiting', 'how', 'alt_hub', 'form_time']]

df = df.set_index('tstamp')
