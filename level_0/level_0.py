#!/usr/bin/python3
import requests
"""Vote for myself 1024 times"""


for i in range(1024):
    req = requests.post('http://158.69.76.135/level0.php',
                        {'id':144,
                         'holdthedoor':'Submit'})
