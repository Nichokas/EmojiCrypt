from EmojiCrypt import encrypt
from EmojiCrypt import decrypt


def test_letters():
    assert encrypt("a") == "😀"
    assert encrypt("b") == "🤓"
    assert encrypt("c") == "👀"
    assert encrypt("d") == "😁"
    assert encrypt("e") == "😆"
    assert encrypt("f") == "😅"
    assert encrypt("g") == "🤣"
    assert encrypt("h") == "😂"
    assert encrypt("i") == "🙂"
    assert encrypt("j") == "🙃"
    assert encrypt("k") == "🫠"
    assert encrypt("l") == "😉"
    assert encrypt("m") == "😊"
    assert encrypt("n") == "😇"
    assert encrypt("ñ") == "🌟"
    assert encrypt("o") == "🥰"
    assert encrypt("p") == "😍"
    assert encrypt("q") == "🤩"
    assert encrypt("r") == "😘"
    assert encrypt("s") == "😗"
    assert encrypt("t") == "😚"
    assert encrypt("u") == "😙"
    assert encrypt("v") == "🥲"
    assert encrypt("w") == "😋"
    assert encrypt("x") == "😛"
    assert encrypt("y") == "😜"
    assert encrypt("z") == "🤪"

    assert decrypt("😀") == "a"
    assert decrypt("🤓") == "b"
    assert decrypt("👀") == "c"
    assert decrypt("😁") == "d"
    assert decrypt("😆") == "e"
    assert decrypt("😅") == "f"
    assert decrypt("🤣") == "g"
    assert decrypt("😂") == "h"
    assert decrypt("🙂") == "i"
    assert decrypt("🙃") == "j"
    assert decrypt("🫠") == "k"
    assert decrypt("😉") == "l"
    assert decrypt("😊") == "m"
    assert decrypt("😇") == "n"
    assert decrypt("🌟") == "ñ"
    assert decrypt("🥰") == "o"
    assert decrypt("😍") == "p"
    assert decrypt("🤩") == "q"
    assert decrypt("😘") == "r"
    assert decrypt("😗") == "s"
    assert decrypt("😚") == "t"
    assert decrypt("😙") == "u"
    assert decrypt("🥲") == "v"
    assert decrypt("😋") == "w"
    assert decrypt("😛") == "x"
    assert decrypt("😜") == "y"
    assert decrypt("🤪") == "z"

def test_mayusc() :
    assert encrypt("A") == "🏰"
    assert encrypt("B") == "🗽"
    assert encrypt("C") == "🎡"
    assert encrypt("D") == "🚀"
    assert encrypt("E") == "💎"
    assert encrypt("F") == "📱"
    assert encrypt("G") == "💻"
    assert encrypt("H") == "🎨"
    assert encrypt("I") == "🎲"
    assert encrypt("J") == "🧩"
    assert encrypt("K") == "🎸"
    assert encrypt("L") == "🎺"
    assert encrypt("M") == "🏀"
    assert encrypt("N") == "⚽"
    assert encrypt("O") == "🏓"
    assert encrypt("P") == "🎳"
    assert encrypt("Q") == "🛹"
    assert encrypt("R") == "🎿"
    assert encrypt("S") == "🪂"
    assert encrypt("T") == "🏹"
    assert encrypt("U") == "🎭"
    assert encrypt("V") == "💙"
    assert encrypt("W") == "🧵"
    assert encrypt("X") == "🧶"
    assert encrypt("Y") == "📚"
    assert encrypt("Z") == "📌"

    assert decrypt("🏰") == "A"
    assert decrypt("🗽") == "B"
    assert decrypt("🎡") == "C"
    assert decrypt("🚀") == "D"
    assert decrypt("💎") == "E"
    assert decrypt("📱") == "F"
    assert decrypt("💻") == "G"
    assert decrypt("🎨") == "H"
    assert decrypt("🎲") == "I"
    assert decrypt("🧩") == "J"
    assert decrypt("🎸") == "K"
    assert decrypt("🎺") == "L"
    assert decrypt("🏀") == "M"
    assert decrypt("⚽") == "N"
    assert decrypt("🏓") == "O"
    assert decrypt("🎳") == "P"
    assert decrypt("🛹") == "Q"
    assert decrypt("🎿") == "R"
    assert decrypt("🪂") == "S"
    assert decrypt("🏹") == "T"
    assert decrypt("🎭") == "U"
    assert decrypt("💙") == "V"
    assert decrypt("🧵") == "W"
    assert decrypt("🧶") == "X"
    assert decrypt("📚") == "Y"
    assert decrypt("📌") == "Z"

def test_symbols():
    assert encrypt(" ") == "😝"
    assert encrypt(",") == "🤑"
    assert encrypt(".") == "🤗"
    assert encrypt(";") == "🤭"
    assert encrypt(":") == "🫢"
    assert encrypt("-") == "🤐"
    assert encrypt("_") == "🤫"
    assert encrypt("/") == "🤔"
    assert encrypt("*") == "🫡"
    assert encrypt("+") == "🤨"
    assert encrypt("(") == "😐"
    assert encrypt(")") == "😑"
    assert encrypt("%") == "😶"
    assert encrypt("&") == "🫥"
    assert encrypt('"') == "🥵"
    assert encrypt("!") == "😏"
    assert encrypt("?") == "😒"
    assert encrypt("$") == "🙄"
    assert encrypt("'") == "😬"

    assert decrypt("😝") == " "
    assert decrypt("🤑") == ","
    assert decrypt("🤗") == "."
    assert decrypt("🤭") == ";"
    assert decrypt("🫢") == ":"
    assert decrypt("🤐") == "-"
    assert decrypt("🤫") == "_"
    assert decrypt("🤔") == "/"
    assert decrypt("🫡") == "*"
    assert decrypt("🤨") == "+"
    assert decrypt("😐") == "("
    assert decrypt("😑") == ")"
    assert decrypt("😶") == "%"
    assert decrypt("🫥") == "&"
    assert decrypt("🥵") == '"'
    assert decrypt("😏") == "!"
    assert decrypt("😒") == "?"
    assert decrypt("🙄") == "$"
    assert decrypt("😬") == "'"