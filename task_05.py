#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A program that gives you the status of your blood pressure."""

USR_BP = int(raw_input('What is your blood pressure? '))

BP_STATUS = 'Low.'

if USR_BP <= 89:
    BP_STATUS = 'Low.'
elif USR_BP > 89 and USR_BP < 120:
    BP_STATUS = 'Ideal.'
elif USR_BP > 119 and USR_BP < 140:
    BP_STATUS = 'Warning!'
elif USR_BP > 139 and USR_BP < 160:
    BP_STATUS = 'High.'
else:
    BP_STATUS = 'Emergency!'

BP_RESULT = 'Your status is currently: {}'.format(BP_STATUS)
print BP_RESULT
