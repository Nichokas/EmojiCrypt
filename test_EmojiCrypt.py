from EmojiCrypt import encrypt

def test_letters():
    assert encrypt(3, "Pez") == "🦿🤌🦁"
