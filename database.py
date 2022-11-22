from insured import Insured

list_of_insured = []
new_insured = Insured()
new_insured.init("Lubomír", "Čapatý", 46, "737 458715")
list_of_insured.append(new_insured)


class Database:
    """
    methods for work with registr of insured
    main screen with choices for methods
    method: for creat new insured
            for write the insured
            find an insured
            end the registr
    """

    def main_screen(self):
        """
        Used to select a command by the user.
        """

        print('--------------------')
        print('EVIDENCE POJIŠTĚNÝCH')
        print('--------------------')
        print()

        print('Vyberte si akci')
        print('1 - Přidat nového pojištěnce')
        print('2 - Vypsat všechny pojištěnce')
        print('3 - Vyhledat pojištěnce')
        print('4 - Konec')
        print()

    def create_an_insured(self):
        """
        Creating a new client.
        """

        first_name = input('Jméno pojištěnce: ')
        last_name = input('Přijmení pojištěnce: ')
        age = input('Věk pojištěnce: ')
        phone_number = input('Telefonní číslo: ')

        new_insured = Insured()
        new_insured.init(first_name, last_name, age, phone_number)
        list_of_insured.append(new_insured)
        print(f'Byl přidán pojištěnec: {new_insured}')

    def write_the_insured(self):
        """
        List of clients.
        """

        print('Seznam pojištěnců')
        for search_insured in list_of_insured:
            print(search_insured)

    def find_an_insured(self):
        """
        Searching for a client in the database by first and last name
        """

        search_first_name = input('Jméno pojištěnce: ')
        search_last_name = input('Přijmení pojištěnce: ')
        for search_insured in list_of_insured:
            if (search_first_name == search_insured.first_name and
                    search_last_name == search_insured.last_name):
                print('Nalezen pojištěnec: ', search_insured)

    def end_registr(self):
        """
        Close the program
        """

        print("Děkujeme za použití naší aplikace")
