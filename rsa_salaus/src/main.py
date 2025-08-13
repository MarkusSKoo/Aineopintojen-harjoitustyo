"""main.py-tiedostossa on rajapinta käyttäjälle"""

from rsa_salaus.keygen import generate_rsa_keys
from rsa_salaus.rsa_crypt import MessageCryption

class UserInterface:
    """Rajapinta käyttäjälle komentoriviltä."""

    def __init__(self):
        self.rsa_cryptor = MessageCryption()

    def rsa_key(self):
        """Luo käyttäjälle RSA-salausavainparin ja tulostaa sen osat ohjeineen."""

        keypair = generate_rsa_keys()

        public_n = keypair[0][0]
        public_e = keypair[0][1]
        private_n = keypair[1][0]
        private_d = keypair[1][1]

        print(f"Kopioi ja tallenna RSA-avain. Julkisen avaimen 1. osa (N) on:\n{public_n}\n")
        print(f"Julkisen avaimen 2. osa (e) on:\n{public_e}\n")

        print("VAROITUS: Älä jaa yksityistä avainta. Voit kopioida yksityisen avaimen täältä:\n")
        print(f"Yksityisen avaimen 1. osa (N) on:\n{private_n}\n")
        print(f"Yksityisen avaimen 2. osa (d) on: \n{private_d}\n")

    def validate_input_str(self, strinput):
        """Apufunktio merkkijonojen validointiin"""

        string = input(strinput)

        if not isinstance(string, str) or len(string) == 0:
            print("Syöte ei voi olla tyhjä!\n")
            return None
        print()
        return string

    def validate_input_int(self, intinput):
        """Apufunktio kokonaislukujen validointiin"""

        try:
            number = int(input(intinput))
            if isinstance(number, int) and number > 0:
                print()
                return number
            print("Syötteen täytyy olla positiivinen kokonaisluku!\n")
            return None

        except ValueError:
            print("Syötteen töytyy olla positiivinen kokonaisluku!\n")
            return None

    def encrypt_message(self):
        """Salaa käyttäjän syöttämän viestin julkisella avaimella
        ja tulostaa salatun viestin käyttäjälle."""

        print("Olet salaamassa viestiä. Anna käyttäjänimi, viesti ja julkinen avain.\n")

        username = self.validate_input_str("Käyttäjänimi: ")
        if not username:
            return

        message = self.validate_input_str("Salattava viesti: ")
        if not message:
            return

        public_n = self.validate_input_int("Julkisen avaimen 1. osa (N): ")
        if not public_n:
            return

        message_length = int.from_bytes(message.encode('utf-8'), 'big')
        if message_length.bit_length() > public_n.bit_length():
            print("Viesti voi olla korkeintaan avaimen (N) pituinen!\n")
            return

        public_e = self.validate_input_int("Julkisen avaimen 2. osa (e): ")
        if not public_e:
            return

        public_key = public_n, public_e
        encrypted_message = self.rsa_cryptor.encrypt(username, message, public_key)

        print(f"Kiitos {encrypted_message[0]}, kopioi salattu viestisi tästä:\n")
        print(f"{encrypted_message[1]}\n")

    def decrypt_message(self):
        """Purkaa käyttäjän syöttämän salatun viestin yksityisellä avaimella
        ja tulostaa alkuperäisen viestin."""

        print("Olet purkamassa salattua viestiä. Anna käyttäjänimi, viesti ja yksityinen avain:\n")

        username = self.validate_input_str("Käyttäjänimi: ")
        if not username:
            return

        message = self.validate_input_int("Purettava viesti: ")
        if not message:
            return

        private_n = self.validate_input_int("Yksityisen avaimen 1. osa (N): ")
        if not private_n:
            return

        if message.bit_length() > private_n.bit_length():
            print("Viestin koko ylittää avaimen salliman maksimipituuden!\n")
            return

        private_d = self.validate_input_int("Yksityisen avaimen 2. osa (d): ")
        if not private_d:
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
