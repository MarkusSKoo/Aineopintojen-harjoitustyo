import time
from rsa_salaus.keygen import generate_keypair

def main():
    start_time = time.time()
    keypair = generate_keypair()
    end_time = time.time()
    p = keypair[0]
    q = keypair[1]

    print("Kokeillaan avainparin luomista")
    print()
    print(f"p: {p}")
    print()
    print(f"q: {q}")
    print()
    print(f"Aikaa avainparin luomiseen kului {end_time - start_time} sekuntia")


if __name__ == "__main__":
    main()
