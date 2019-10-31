'''
Business challenge/requirement

one Bank runs marketing campaign to offer loans to clients.
Loan is offered to only clients withparticular professions. List of successful campaigns(withclientdata) is given in attached dataset.
You have to come up with program which reads the file and builds a set of unique profession list and given input profession of client
–system tells whether client iseligible to be approached for marketing campaign.
'''

import os
job_ip = input('Enter list of comma seperated profesion which are eligible for loan : ')
job_ip_elg = job_ip.split(",")

ip = input ('Do you want eligible customers list ? Enter Y/N : ')

if (ip.upper() == 'Y'):
    print('Loan eligible customers list : ')
    newfile=open("Data/3M2_banking_data","r")
    job_lst = []
    for i in newfile :
        a = i.split(",")
        b = (a[1])
        if (b not in job_lst and b != 'job') :
            job_lst.append(b)

        for j in job_ip_elg :
            if (b == j) :
                print (i)
else :
    print ('Thank you for visting! Try again later')

#print (job_lst)

