"""rsa_crypt salaa ja purkaa viestit"""

class MessageCryption:
    """Luokassa on salaus- ja purkufunktiot viesteille"""

    def encrypt(self, username: str, message: str, public_key: tuple):
        """Funktio salaa viestin.
        
        Args:
            username(str): Käyttäjänimi merkkijonona.
            message(str): Salattava viesti merkkijonona.
            public_key[Tuple[int, int]]: Julkinen avain, jossa n ja e kokonaislukuina.
        
        Returns:
            Tuple[str, int]: Palauttaa tuplen, jonka alkioina ovat käyttäjänimi
            merkkijonona ja RSA-salattu viesti kokonaislukuna"""

        if message == "":
            raise ValueError("Message cannot be empty")

        n, e = public_key

        message_bytes = message.encode('utf-8') # Jakaa viestin tavuihin
        message_int = int.from_bytes(message_bytes, byteorder='big')
        # Muuntaa tavut kokonaisluvuiksi (big endian järjestys)

        if message_int >= n:
            raise ValueError("Too long message")

        crypted_message = pow(message_int, e, n)

        return username, crypted_message

    def decrypt(self, username: str, message: int, private_key: tuple):
        """Funktio purkaa salatun viestin luettavaan muotoon.
        
        Args:
            username(str): Käyttäjänimi merkkijonona.
            message(int): Purettava viesti kokonaislukuna.
            private_key[Tuple[int, int]]: Yksityinen avain, jossa n ja d kokonaislukuina.
            
        Returns:
            Tuple[str, int]: Palauttaa tuplen, jonka alkioina ovat käyttäjänimi
            merkkijonona ja purettu viesti merkkijonona"""

        n, d = private_key

        if message >= n:
            raise ValueError("Message too long")

        message_int = pow(message, d, n)
        length = (message_int.bit_length() + 7) // 8 # Lasketaan tallentamiseen tarvittava tavumäärä
        message_bytes = message_int.to_bytes(length, byteorder='big')
        message_str = message_bytes.decode('utf-8')

        return username, message_str
