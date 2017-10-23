
# Uses the pure Python implementation of RSA. You can look in its source package
# and see how it uses 2 large prime numbers to generate a public and private
# key.
import rsa

# We need to be able to sign our grebecoin transfers, to validate that they came
# from this wallet. Otherwise anybody could initiate a transfer!

def loadKeys():
    # Load keys, or create them if they don't exist
    try:
        with open('private.pem', mode='rb') as keyfile:
            keydata = keyfile.read().decode('utf-8')
            privkey = rsa.PrivateKey.load_pkcs1(keydata)
        
        with open('public.pem', mode='rb') as keyfile:
            keydata = keyfile.read().decode('utf-8')
            pubkey = rsa.PublicKey.load_pkcs1(keydata)
    except(FileNotFoundError):
        print("Could not load your wallet: creating a new one.")
        (pubkey, privkey) = rsa.newkeys(256)
        priv_save_data = rsa.PrivateKey.save_pkcs1(privkey)
        with open("private.pem", 'w') as outfile:
            outfile.write(priv_save_data.decode('utf-8'))
        
        pub_save_data = rsa.PublicKey.save_pkcs1(pubkey)
        with open("public.pem", 'w') as outfile:
            outfile.write(pub_save_data.decode('utf-8'))
    return (pubkey, privkey)


(pubkey, privkey) = loadKeys()
        
print("a) send grebecoins")
print("b) get balance")
choice = input("Choose an option: ")
    