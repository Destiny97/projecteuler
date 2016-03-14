from modules.matlib import primeFactors

factors = []

for x in range(2, 21, 1):
    facts = primeFactors(x)
    for f in facts:
        for i in range(facts.count(f)-factors.count(f)): factors.append(f)

nsn = 1
for x in factors: nsn *= x

print(nsn)
