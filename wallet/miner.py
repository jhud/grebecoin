from wallet import loadKeys

(pubkey, privkey) = loadKeys()

print(pubkey)

while(True):
    print("Looking for grebecoins")