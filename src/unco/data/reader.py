import pandas as pd
import csv
from colorama import Fore  # prints warnings in red


class Reader:
    """
        Class that reads a file and creates a CSV object.

        Arguments:
            docpath: Path to the input file.
    """

    def __init__(self, docpath: str) -> None:
        self.path = docpath
        self.type : str

        self.initialise_type()

    def initialise_type(self) -> None:
        """
            Extract the file type from the path.
        """

        self.type = self.path[self.path.rfind(".")+1:]

        if len(self.type) > 4:
            print(Fore.RED + "Error: Please enter a complete path with datatype-prefix!" + Fore.RESET)

    def read(self) -> pd.DataFrame:
        """
            Reads the input and returns a CSV object.
        """

        if self.type == "csv":
            try:
                file = open(self.path, 'r', encoding='utf-8')
                return pd.read_csv(file)

            except FileNotFoundError:
                print(Fore.RED + "Error: There is no CSV file on this path." + Fore.RESET)
        
        elif self.type == "pdf":
            print(Fore.RED + "Error: PDF not aviable." + Fore.RESET)
        else:
            print(Fore.RED + "Error: Unknown File-Type!" + Fore.RESET)
