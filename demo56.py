import csv

sampleFile1 = open('data\\data2.csv')
sampleReader1 = csv.reader(sampleFile1)
sampleData1 = list(sampleReader1)
sampleData2 = tuple(sampleReader1)
sampleFile1.close()

print type(sampleData1)
print type(sampleData2)
for l in sampleData1:
    print l
    for c in l:
        print 'col=', c
        for a in c:
            print 'aaaaaaa!!!=', a