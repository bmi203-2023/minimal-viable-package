class Greeting:
    """A class to represent a welcome greeting.
    """

    # """
    # A class to represent a welcome greeting.

    # Attributes
    # ----------
    # the_world : str
    #     A message to the world.

    # Methods
    # -------
    # bmi_203:
    #     Prints a welcome message for the BMI-203 class.
    
    # _print_message:
    #     An internal method called by bmi_203 to print the welcome message.

    # a_person(name: str):
    #     Prints a welcome message for a person by their name.
    
    # the_zen_of_python(file: str): -> list[str]
    #     Creates a list of strings containing The Zen of Python.
    # """

    def __init__(self):
        """Constructs the attributes for the Greeting object.
        """
        self.the_world = "Hello, World!"

    def bmi_203(self):
        """A welcome message for the students.
        """
        self._print_message()

    def _print_message(self):
        """An internal class method used to print the welcome message for the BMI-203 class.
        """
        print("Welcome to BMI-203!")

    def a_person(self, named=None):
        """A welcome message for a person by their name.

        Args:
            named (str, optional): A person's name. Defaults to None.

        Raises:
            NotImplementedError: If no named person is passed in as a parameter.

        Returns:
            str: A welcome message with a person's name.
        """
        if named is None:
            raise NotImplementedError("That's not there!")

        else:
            msg="Hello, {person}!"
            named_msg = msg.format(person=named)
            return named_msg

    def the_zen_of_python(self, read_file: str) -> list[str]:
        """Reads a text file containing The Zen of Python and returns a list where each element is one line of the 19 aphorisms.

        Args:
            read_file (str): Path to the txt file containing The Zen of Python.      

        Returns:
            list[str]: List of strings, where each element is one line of The Zen of Python.
        """
        with open(read_file) as f:
            zen_list = [line.strip() for line in f.readlines()]
        return zen_list