import time
from rsa_salaus.keygen import generate_rsa_keys
from rsa_salaus.rsa_crypt import MessageCryption

def main():
    crypt = MessageCryption()
    keypair = generate_rsa_keys()
    public_key = keypair[0]
    private_key = keypair[1]


if __name__ == "__main__":
    main()
