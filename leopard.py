"""
Please write your name
@author: Ungku Amer Iskandar

"""

# Reminder: You are only allowed to import the csv module (done it for you).
# OTHER MODULES ARE NOT ALLOWED (NO OTHER IMPORT!!!).

import csv


class Leopard:
    def __init__(self, filepath: str) -> None:

        self.header = []
        self.data = []

        try:
            csv_file = open(filepath)

        except FileNotFoundError:
            print("File not found.")
            exit()

        else:
            csv_reader = csv.reader(csv_file)

            if csv_file.readline()[0] is None:
                csv_file.seek(0)  # reset file pointer to start
                print("Empty file.")
                csv_file.close()
                exit()

            csv_file.seek(0)
            self.header = next(csv_reader)

            for row in csv_reader:
                self.data.append(row)

            csv_file.seek(0)
            csv_file.close()


    def get_header(self) -> list:
        return self.header

    def get_data(self) -> list:
        return self.data

    def stats(self) -> dict:
        new_dict = {}
        current_row = self.data[0]

        count = 0
        header_dict = ["count", "mean", "min", "max"]

        for data in current_row:
            current_header = self.header[count]
            data_add = [0, 0, 0, 0]  # count, mean, min, max
            total = 0

            if data.isnumeric():
                for j in range(len(self.data)):
                    if self.data[j][count].isnumeric():
                        current_data = int(self.data[j][count])
                        data_add[0] = data_add[0] + 1
                        total += current_data

                        if current_data < int(self.data[0][count]):
                            data_add[2] = current_data
                        if current_data > data_add[3]:
                            data_add[3] = current_data

                    data_add[1] = round((total/data_add[0]), 2)

                    new_dict[current_header] = dict(zip(header_dict, data_add))  # combine two list

            count += 1

        return new_dict

    def html_stats(self, stats: dict, filepath: str) -> None:
        fp = open(filepath, "w")

        table = "<table>\n"
        table += " <tr>\n"
  
        data_list = []
        header = stats.keys()
        table += "     <th>{0}</th>\n".format("count")
        table += "     <th>{0}</th>\n".format("mean")
        table += "     <th>{0}</th>\n".format("min")
        table += "     <th>{0}</th>\n".format("max")
        
        for column in header:
            #table += "     <th>{0}</th>\n".format(column.strip())
            data_list.append(stats[column]["count"])
            data_list.append(stats[column]["mean"])
            data_list.append(stats[column]["min"])
            data_list.append(stats[column]["max"])

        table += " </tr>\n"
        table += " <tr>\n"

        count = 0
        for i in range(int(len(data_list)/4)):
            line = data_list[count]
            if count < 4:
                table += "    <td>{0}</td>\n".format(line)
            else:
                count = 0
            count += 1
        table += "</tr>\n"

        table += "</table>"
        print(table)
        fp.write(table)
        fp.close()

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
    #test = Leopard("diabetes_data.csv")
    #print(test.get_header())
    #print(test.get_data())
    #stats = test.stats()
    #print(stats)
    #test.html_stats(stats, "diabetes.html")
    #print()

    # test fide2021.csv
    test2 = Leopard("fide2021.csv")
    print(test2.get_header())
    #print(test.get_data())
    stats2 = test2.stats()
    print(stats2)
    test2.html_stats(stats2, "fide2021.html")
    #print()

    # test student.csv
    #test3 = Leopard("student.csv")
    #print(test3.get_header())
    #print(test.get_data())
    #stats3 = test3.stats()
    #print(stats3)
    #test3.html_stats(stats3, "student.html")
