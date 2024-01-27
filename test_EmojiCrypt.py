from EmojiCrypt import encrypt

def test_letters():
    assert encrypt(3, "Pez") == "👂🤞🐆"
    assert encrypt(256, "ElPezEstaRaro") == "❣️😟🥶❣️🧧❣️🕘🫨🖤🏓🖤🏓🌘"

def test_caracteres():
    assert encrypt(5, r" ,.;:-_/*-+()%&!?\"\$") == "💙🩶👱🙍🍍👳💃🍈🍍🍑🍅🥔🥒🥜🥯🍗🍞🍕"
    assert encrypt(480, r" ,.;:-_/*-+()%&!?\"\$") == "☘️🕓🐔🚌👃🍾👹🪁🫣🍾📧🫛🎧💔🌓🏍️🐩🐦‍⬛🧱"