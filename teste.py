
d = [ ['1', '2'],
      ['3', '4'] ]

#q = [ for c in [line for line in d] ]
q = [ int(number) for number in line for line in d ]
print(q)