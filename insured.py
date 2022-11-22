class Insured:
    """
    Creat an insured.
    Insured has first name, last name, age and telephone number

    """

    def init(self, first_name, last_name, age, telephone_number):
        """
        Initialize the object's the insured

        Args:
            first_name (_str_): first name of the insured
            last_name (_str_): last name of the insured
            age (_int_): age of the insured
            telephone_number (_str_): telephone number of the insured
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.telephone_number = telephone_number

    def __str__(self):

        return f"{self.first_name} \t {self.last_name} \t {self.age} \t {self.telephone_number}"
