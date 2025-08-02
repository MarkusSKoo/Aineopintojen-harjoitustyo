"""performance_test.py testaa avainparien tuottavan funktion suorituskykyä"""

import time
import pytest
from src.rsa_salaus.keygen import generate_rsa_keys

@pytest.mark.performance
def test_performance_generate_rsa_keys():
    time_start = time.time()
    rsa_key = generate_rsa_keys()
    time_end = time.time()

    assert time_end - time_start <= 4
