import csv

with open('mycsv.csv', 'w', newline='') as f :
    thewriter = csv.writer(f)

    thewriter.writerow(['col1', 'col2', 'col3'])
    thewriter.writerow(['one', 'two', 'three'])