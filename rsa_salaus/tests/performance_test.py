"""performance_test.py testaa algoritmien suorituskykyä"""

import time
import pytest
from src.rsa_salaus.keygen import generate_rsa_keys
from src.rsa_salaus.rsa_crypt import MessageCryption

class TestPerformance:
    """Suorituskykyä testaava luokka"""

    def setup_method(self):
        """Hakee MessageCryption-luokan ja salausavaimen myöhempiä testejä varten."""

        self.public_key, self.private_key = generate_rsa_keys()
        self.crypt = MessageCryption()

    @pytest.mark.performance
    def test_performance_key_generation(self):
        """Testaa suorituskykyä salausavaimen tuottamisessa."""

        time_start = time.time()
        generate_rsa_keys()
        time_end = time.time()

        assert time_end - time_start <= 3

    @pytest.mark.performance
    def test_performance_message_roundtrip(self):
        """Testaa viestin salaamisen ja purkamisen yhdistelmän suorituskykyä."""

        time_start = time.time()

        username = "Testuser"
        plaintext = 'This message is longer and contains special charachters, such as "!#€%&/()=?+_-1234567890'

        encrypted_data = self.crypt.encrypt(username, plaintext, self.public_key)
        assert username == encrypted_data[0]

        decrypted_data = self.crypt.decrypt(username, encrypted_data[1], self.private_key)
        assert username == decrypted_data[0]
        assert plaintext == decrypted_data[1]

        time_end = time.time()

        assert time_end - time_start <= 4

    @pytest.mark.performance
    def test_performance_encrypt(self):
        """Testaa suorituskykyä viestin salaamisessa"""

        time_start = time.time()
        self.crypt.encrypt("Testuser", "message", self.public_key)
        time_end = time.time()

        assert time_end - time_start <= 1

    @pytest.mark.performance
    def test_performance_decrypt(self):
        """Testaa suorituskykyä salatun viestin purkamisessa."""

        username = "Testuser"
        plaintext = "Hello!"

        encrypted_data = self.crypt.encrypt(username, plaintext, self.public_key)

        time_start = time.time()
        decrypted_data = self.crypt.decrypt(username, encrypted_data[1], self.private_key)
        time_end = time.time()

        assert username == decrypted_data[0]
        assert plaintext == decrypted_data[1]
        assert time_end - time_start <= 1

    @pytest.mark.performance
    def test_multiple_roundtrips(self):
        """Testaa perättäisten roundtrip-pyyntöjen suorituskykyä."""

        username = "Testuser"
        plaintext = 'This message is longer and contains special charachters, such as "!#€%&/()=?+_-1234567890'

        time_start = time.time()

        for _ in range(100):
            encrypted_data = self.crypt.encrypt(username, plaintext, self.public_key)
            decrypted_data = self.crypt.decrypt(username, encrypted_data[1], self.private_key)
            assert username == decrypted_data[0]
            assert plaintext == decrypted_data[1]

        time_end = time.time()

        assert time_end - time_start <= 4
