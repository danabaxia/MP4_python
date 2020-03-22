#!/usr/bin/env python
import sys
import math

wordsToCounts = []

for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)
    count = int(count)
    wordsToCounts.append((word, count))

total = 0
for (word, count) in wordsToCounts:
    total += count
average = int(math.floor(total / len(wordsToCounts)))
variance = 0
for (word, count) in wordsToCounts:
    variance += (average - count) ** 2
variance /= len(wordsToCounts)
variance = int(math.floor(variance))
minimum = min(wordsToCounts, key=lambda x: x[1])
maximum = max(wordsToCounts, key=lambda x: x[1])

print 'Mean\t%d' % average
print 'Sum\t%d' % total
print 'Min\t%d' % minimum[1]
print 'Max\t%d' % maximum[1]
print 'Var\t%d' % variance
