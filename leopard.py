"""
Please write your name
@author: Ungku Amer Iskandar

"""

# Reminder: You are only allowed to import the csv module (done it for you).
# OTHER MODULES ARE NOT ALLOWED (NO OTHER IMPORT!!!).

import csv


class Leopard:
    def __init__(self, filepath: str) -> None:
        # delete pass and this comment to write your code
        pass

    def get_header(self) -> list:
        # delete pass and this commentto write your code
        pass

    def get_data(self) -> list:
        # delete pass and this commentto write your code
        pass

    def stats(self) -> dict:
        # delete pass and this comment to write your code
        pass

    def html_stats(self, stats: dict, filepath: str) -> None:
        # delete pass and this comment to write your code
        pass

    def count_instances(self, criteria) -> int:
        """
        Write your docstring to explain how to use this method.
        You are to decide what data type format is criteria or how many
        arguments to this method.
        Delete above and this comment to write your docstring.
        """
        # delete pass and this comment to write your code
        pass


if __name__ == "__main__":
    # DO NOT COMMENT ALL WHEN SUBMIT YOUR FILE, cannot have an if statement
    # with nothing afterwards.

    # test diabetes_data.csv
    test = Leopard("diabetes_data.csv")
    print(test.get_header())
    print(test.get_data())
    stats = test.stats()
    print(stats)
    test.html_stats(stats, "diabetes.html")
    print()

    # test fide2021.csv
    test2 = Leopard("fide2021.csv")
    print(test2.get_header())
    print(test.get_data())
    stats2 = test2.stats()
    print(stats2)
    test2.html_stats(stats2, "fide2021.html")
    print()

    # test student.csv
    test3 = Leopard("student.csv")
    print(test3.get_header())
    print(test.get_data())
    stats3 = test3.stats()
    print(stats3)
    test3.html_stats(stats3, "student.html")
