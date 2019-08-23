name = 'Mary'
password = 'Swordfish'

name = raw_input('What is your name:')
password = raw_input('Enter password:')
if name == 'Mary'and password == 'Swordfish':
    print 'Hello Mary'
else:
    print 'Unknown ID'
    if password == 'Swordfish':
        print 'Access Granted'
    else:
        print 'Access denied'
