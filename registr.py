from database import Database


class Registr:
    """
    Connect main screen with methods.
    """

    registr = Database()

    while True:
        registr.main_screen()
        choice = input('Jaká je tvá volba: ')
        print()

        if choice == '1':
            registr.create_an_insured()

        elif choice == '2':
            registr.write_the_insured()

        elif choice == '3':
            registr.find_an_insured()

        elif choice == '4':
            registr.end_registr()
