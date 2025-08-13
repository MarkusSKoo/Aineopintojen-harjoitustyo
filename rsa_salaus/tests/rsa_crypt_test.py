"""rsa_crypt_test.py testaa rsa_crypt.py:ssä olevien salaus- ja purkufunktioiden toimintaa."""

import pytest
from src.rsa_salaus.keygen import generate_rsa_keys
from src.rsa_salaus.rsa_crypt import MessageCryption

class TestEncryptDecrypt:
    """Testaa viestin salaamista ja purkamista."""

    # pylint: disable=attribute-defined-outside-init
    def setup_method(self):
        """Hakee avainparin tarkistusmetodeja varten."""

        self.keypair = generate_rsa_keys()
        self.public_key = self.keypair[0]
        self.private_key = self.keypair[1]

        self.crypt = MessageCryption()

    def test_roundtrip_simple_message(self):
        """Testaa funktioiden toimintaa salaamalla viestin, purkamalla
        salatun viestin ja vertailemalla näitä keskenään."""

        username = "Testuser"
        plaintext = "Hello!"

        encrypted_data = self.crypt.encrypt(username, plaintext, self.public_key)
        assert username == encrypted_data[0]

        decrypted_data = self.crypt.decrypt(username, encrypted_data[1], self.private_key)

        assert username == decrypted_data[0]
        assert plaintext == decrypted_data[1]

    def test_edge_cases(self):
        """Testaa virheiden käsittelyä."""

        long_message = "This message is too long" * 20
        long_crypted_message = self.private_key[0] + 1

        with pytest.raises(ValueError, match="Message cannot be empty"):
            self.crypt.encrypt("Testuser", "", self.public_key)

        with pytest.raises(ValueError, match="Too long message"):
            self.crypt.encrypt("Testuser", long_message, self.public_key)

        with pytest.raises(ValueError, match="Message too long"):
            self.crypt.decrypt("Testuser", long_crypted_message, self.public_key)

    def test_roundtrip_long_message(self):
        """Testaa funktioiden toimintaa salaamalla viestin, purkamalla
        salatun viestin ja vertailemalla näitä keskenään."""

        username = "Testuser"
        plaintext = 'This message is longer and contains special charachters,' \
        'such as "!#€%&/()=?+_-1234567890'

        encrypted_data = self.crypt.encrypt(username, plaintext, self.public_key)
        assert username == encrypted_data[0]

        decrypted_data = self.crypt.decrypt(username, encrypted_data[1], self.private_key)

        assert username == decrypted_data[0]
        assert plaintext == decrypted_data[1]
