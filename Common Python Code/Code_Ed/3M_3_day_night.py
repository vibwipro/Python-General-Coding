'''
Weather forecasting organization wants to show is it day or night.
So, write a program for such organization to findwhether is it dark outside or not.
Hint: Use time module.
'''

import time
print ('Welcome ! At weather forecasting organization. Do you want to find whether is it dark outside or not ? ')
y = input('Enter Y/N : ')
if (y.upper() == 'Y') :
    tm = time.localtime()
    print ('Current local time is :' + str(tm.tm_hour) + '.' + str(tm.tm_min) + '.' + str(tm.tm_sec) )

    if (tm.tm_hour <= 5 or tm.tm_hour >= 24) :
        print ('Currently it is dark outside, you need to stay back and take rest')
    else :
        print ('Currently it is not dark outside, you can go out and enjoy your day')
else :
    print ('Thank you for visiting weather forecasting organization. Come back soon.')
