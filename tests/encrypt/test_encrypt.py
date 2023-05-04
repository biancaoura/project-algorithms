from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message('abc', 'def')

    assert encrypt_message('desserts', 4) == 'stre_ssed'
    assert encrypt_message('stressed', 9) == 'desserts'
