from rsa_salaus.keygen import generate_keypair

def main():
    keypair = generate_keypair()
    p = keypair[0]
    q = keypair[1]

    print("Kokeillaan avainparin luomista")
    print()
    print(f"p: {p}")
    

if __name__ == "__main__":
    main()