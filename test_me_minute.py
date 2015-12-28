#! /usr/bin/env python
'''
  Name:        test_me_minute.py
  Description: This file ties in with CRON to make requests at a minute interval
  Author:      Bob Strecansky <bob@mailchimp.com>
  Version:     0.1
'''


from colinExample import print_for_colin


def print_for_colin_test():
    assert print_for_colin() == 'print_for_colin completed'
