p = 857504083339712752489993810777
q = 1029224947942998075080348647219

et = (p-1) * (q - 1)
e=65537
cheia_privata = pow(e, -1, et)
print(cheia_privata)