import os

try:
    os.mkdir('./data')
    print('data Directory created.')
except:
    print('data Directory already created.')

try:
    os.mkdir('./results')
    print('results Directory created.')
except:
    print('results Directory already created.')