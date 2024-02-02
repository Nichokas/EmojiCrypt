from EmojiCrypt import encrypt


def test_letters():
    assert encrypt("Pez") == "🥵😌🤓"
    assert encrypt("ElPezEstaRaro") == "😔🤢🥶😔🧐😔😵‍💫🤯😮‍💨😵😮‍💨😵🥵"


def test_caracteres():
    assert encrypt(r" ,.;:-_/*-+()%&!?\"\$") == "😕🫤😟🙁☹️🥺😯😲😳🥺🥹😦😧😨😰😢😭😬😥😬😱"
