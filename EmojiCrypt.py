from colorama import Fore

emojis={'a': '😀', 'b': '🤓', 'c': '👀', 'd': '😁', 'e': '😆', 'f': '😅', 'g': '🤣', 'h': '😂', 'i': '🙂', 'j': '🙃', 'k': '🫠', 'l': '😉', 'm': '😊', 'n': '😇', 'o': '🥰', 'p': '😍', 'q': '🤩', 'r': '😘', 's': '😗', 't': '😚', 'u': '😙', 'v': '🥲', 'w': '😋', 'x': '😛', 'y': '😜', 'z': '🤪', ' ': '😝', ',': '🤑', '.': '🤗', ';': '🤭', ':': '🫢', '-': '🤐', '_': '🤫', '/': '🤔', '*': '🫡', '+': '🤨', '(': '😐', ')': '😑', '%': '😶', '&': '🫥', '"': '🥵', '!': '😏', '?': '😒', '$': '🙄', "'": '😬'}




def encrypt(ms):
    finals = []
    ms = ms.lower()
    for letra in ms:
        x = emojis.get(letra)
        finals.append(x)
    return "".join(finals)



def main():
    verde = Fore.GREEN

    logo = (
        verde
        + f"""
                                              mm   mm                                                   
    *@@@***@@@                                @@   @@    mm@***@m@                                 @@   
      @@    *@                                         m@@*     *@                                 @@   
      @@   @   *@@@@@@@@m@@@@@m    m@@*@@m  *@@@ *@@@  @@*       **@@@m@@@ *@@*   *@@**@@@@@@@@m @@@@@@ 
      @@@@@@     @@    @@    @@   @@*   *@@   @@   @@  @@           @@* **   @@   m@    @@   *@@   @@   
      @@   @  m  !@    @@    @@   @@     @@   @@   !@  @!m          @!        @@ m!     !@    @@   @@   
      @!     m@  !@    !@    @@   @@     !@   @@   !@  *!@m     m*  @!         @@!      !@    !@   @!   
      !!   !  !  !!    !!    !!   !@     !!   !!   !!  !!!          !!         @!!      !@!   !!   !!   
      !!     !!  :!    :!    !!   !!!   !!!   !!   !!  :!!:     !*  !:         !!:      !@   !!!   !!   
    : :::!: : :: :!:  :::   ::!:   : : : :    :  : : :   : : : :! : :::        !!       :!: : :    ::: :
                                           :: ::                             ::!        ::              
                                           ::::                            :::        : : ::            
               
    """
    )

    print(logo)

    print()
    print()

    print("1. Encrypt")
    print("2. Descrypt")
    print()

    option = input("Select an option:")

    ms = input("Mensaje: ")
    print()

    finals = []  # Crear una lista vacía para almacenar todos los "final"

    if option == '1':
        print("Mensaje cifrado: ", encrypt(ms))
    else:
        print("Opción no válida")


if __name__ == "__main__":
    main()
