import time
from rsa_salaus.keygen import generate_rsa_keys
from rsa_salaus.rsa_crypt import MessageCryption

class UserInterface:
    """Rajapinta käyttäjälle"""

    def __init__(self):
        self.crypt = MessageCryption()

    def rsa_key(self):
        """Luo käyttäjälle RSA-salausavainparin"""

        keypair = generate_rsa_keys()
        public_n = keypair[0][0]
        public_e = keypair[0][1]
        private_n = keypair[1][0]
        private_d = keypair[1][1]

        print("WARNING: Keep the private key secure at all times! Do not share the private key for security reasons.")
        print("You can share the public key.")
        print()

        print("Your public key first part (N) is:")
        print()
        print(public_n)
        print()

        print("Your public key second part (e) is:")
        print()
        print(public_e)
        print()

        print("Protect your private key! Your private key first part (N) is:")
        print()
        print(private_n)
        print()

        print("Protect your private key! Your private key second part (d) is:")
        print()
        print(private_d)
        print()

    def encrypt_message(self):
        """Salaa käyttäjän syöttämän viestin."""

        print("You are encrypting a message. Please give your username, message and public key.")
        print()

        username = input("Give your username: ")
        message = input("Type your message here: ")
        print()

        public_key_n = int(input("Give the first part of the public key (N): "))
        public_key_e = int(input("Give the second part of the public key (e): "))
        print()

        public_key = public_key_n, public_key_e
        encrypted_message = self.crypt.encrypt(username, message, public_key)

        print(f"Thank you {encrypted_message[0]}, your encrypted message is:")
        print()
        print(encrypted_message[1])
        print()

    def decrypt_message(self):
        """Purkaa käyttäjän syöttämän salatun viestin käyttäjän yksityisellä avaimella."""

        print("You are decrypting a message. Please enter your username, encrypted message and your private key:")
        print()

        username = input("Type your username: ")
        print()

        message = int(input("Give encrypted message: "))
        print()

        private_n = int(input("Give the first part of the private key (N): "))
        private_d = int(input("Give the second part of the private key (d): "))
        private_key = private_n, private_d
        print()

        decrypted_message = self.crypt.decrypt(username, message, private_key)

        print(f"Thank you {decrypted_message[0]}")
        print()
        print(f"Your decrypted message is: {decrypted_message[1]}")
        print()

    def main(self):
        """Pääohjelma"""

        print("Welcome to RSA-cryption! Choose from the following:")
        print()
        print("1. Generate RSA key")
        print("2. Encrypt with a public key")
        print("3. Decrypt with a private key")
        print("4. Exit")
        print()
        while True:
            choice = int(input("Your choice: "))

            if choice == 1:
                self.rsa_key()

            elif choice == 2:
                self.encrypt_message()

            elif choice == 3:
                self.decrypt_message()

            elif choice == 4:
                print("Program closed. Thank you!")
                break

            else:
                print("Invalid command. Restarting.")
                self.main()


if __name__ == "__main__":
    ui = UserInterface()
    ui.main()
