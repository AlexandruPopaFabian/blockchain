e = 65537
p = 17
q = 23
N = p * q

cyphertext = pow(12, e, N)
print(cyphertext)
