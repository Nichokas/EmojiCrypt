from EmojiCrypt import encrypt
from EmojiCrypt import decrypt
from EmojiCrypt import main 
import mock


def test_encrypt_decrypt():
    # Prueba que la encriptación y desencriptación son funciones inversas una de la otra
    message = "Mensaje de prueba"
    assert decrypt(encrypt(message)) == message

def test_main_encrypt():
    # Prueba que la opción "1" en la función main llama a la función encrypt
    message = "Mensaje de prueba"
    with mock.patch('builtins.input', side_effect=["1", message]):
        with mock.patch('builtins.print') as mock_print:
            main()
            mock_print.assert_called_with("Message: ", encrypt(message))

def test_main_decrypt():
    # Prueba que la opción "2" en la función main llama a la función decrypt
    encrypted_message = encrypt("Mensaje de prueba")
    with mock.patch('builtins.input', side_effect=["2", encrypted_message]):
        with mock.patch('builtins.print') as mock_print:
            main()
            mock_print.assert_called_with("Message: ", "Mensaje de prueba")
