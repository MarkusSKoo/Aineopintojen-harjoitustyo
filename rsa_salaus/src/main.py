"""main.py-tiedostossa on rajapinta käyttäjälle"""

from rsa_salaus.keygen import generate_rsa_keys
from rsa_salaus.rsa_crypt import MessageCryption

class UserInterface:
    """Rajapinta käyttäjälle komentoriviltä."""

    def __init__(self):
        self.rsa_cryptor = MessageCryption()
        self.n_min_size = 2048

    def rsa_key(self):
        """Luo käyttäjälle RSA-salausavainparin ja tulostaa sen osat ohjeineen."""

        keypair = generate_rsa_keys()

        public_n = keypair[0][0]
        public_e = keypair[0][1]
        private_n = keypair[1][0]
        private_d = keypair[1][1]

        print("VAROITUS: Älä jaa yksityistä avainta turvallisuussyistä!")
        print("Voit jakaa julkisen avaimen.\n")

        print(f"Kopioi ja tallenna RSA-avain. Julkisen avaimen 1. osa (N) on:\n{public_n}\n")
        print(f"Julkisen avaimen 2. osa (e) on:\n{public_e}\n")

        print("Suojaa yksityinen avaimesi huolellisesti. Voit kopioida sen täältä:\n")
        print(f"Yksityisen avaimen 1. osa (N) on: \n{private_n}\n")
        print(f"Yksityisen avaimen 2. osa (d) on: \n{private_d}\n")

    def encrypt_message(self):
        """Salaa käyttäjän syöttämän viestin julkisella avaimella
        ja tulostaa salatun viestin käyttäjälle."""

        print("Olet salaamassa viestiä. Anna käyttäjänimi, viesti ja julkinen avain.\n")

        username = input("Käyttäjänimi: ")
        message = input("Salattava viesti: ")

        try:
            public_n = int(input("Julkisen avaimen 1. osa (N): "))
            print()

            if public_n.bit_length() < self.n_min_size:
                print("Liian lyhyt julkinen avain (N)!\n")
                return

            public_e = int(input("Julkisen avaimen 2. osa (e): "))
            print()

            if public_e <= 0 or public_n <= 0:
                print("Virhe syötteessä! Avaimen (N ja e) tulee olla positiivisia lukuja.\n")
                return

        except ValueError:
            print("Virhe syötteessä! avaimen (N ja e) täytyy olla positiivisia kokonaislukuja.\n")
            return

        public_key = public_n, public_e
        encrypted_message = self.rsa_cryptor.encrypt(username, message, public_key)

        print(f"Kiitos {encrypted_message[0]}, kopioi salattu viestisi tästä:\n")
        print(f"{encrypted_message[1]}\n")

    def decrypt_message(self):
        """Purkaa käyttäjän syöttämän salatun viestin yksityisellä avaimella
        ja tulostaa alkuperäisen viestin."""

        print("Olet purkamassa salattua viestiä. Anna käyttäjänimi, viesti ja yksityinen avain:\n")

        username = input("Käyttäjänimi: ")

        try:
            message = int(input("Purettava viesti: "))
            print()
            private_n = int(input("Yksityisen avaimen 1. osa (N): "))
            print()

            if private_n.bit_length() < self.n_min_size:
                print("Virhe syötteessä: N on liian lyhyt.\n")
                return

            private_d = int(input("Yksityisen avaimen 2. osa (d): "))
            print()

        except ValueError:
            print("Virhe syötteissä! Avaimen (N ja d) ja salatun viestin tulee olla lukuja.\n")
            return

        private_key = private_n, private_d

        try:
            decrypted_message = self.rsa_cryptor.decrypt(username, message, private_key)

        except UnicodeDecodeError:
            print("Purkaminen epäonnistui! Tarkista että viesti ja avain ovat oikein.\n")
            return

        print(f"Kiitos {decrypted_message[0]}\n")
        print(f"Purettu viestisi on: {decrypted_message[1]}\n")

    def show_options(self):
        """Tulostaa ohjelmassa suoritettavat valinnat."""

        print("Valitse seuraavista vaihtoehdoista:\n")

        print("1. Luo RSA-avain")
        print("2. Salaa julkisella avaimella")
        print("3. Pura yksityisellä avaimella")
        print("4. Lopeta\n")

    def main(self):
        """Pääohjelma"""

        print("Tervetuloa RSA-salausohjelmaan!\n")

        while True:
            self.show_options()

            try:
                choice = int(input("Valintasi: "))
            except ValueError:
                print("Virheellinen valinta!\n")
                continue

            if choice == 1:
                self.rsa_key()

            elif choice == 2:
                self.encrypt_message()

            elif choice == 3:
                self.decrypt_message()

            elif choice == 4:
                print("Ohjelma suljettu. Kiitos!")
                break

            else:
                print("Virheellinen valinta!\n")

if __name__ == "__main__":
    ui = UserInterface()
    ui.main()
