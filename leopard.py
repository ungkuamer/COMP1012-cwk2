
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
            self.header = next(csv_reader)  # populating the header array

            for row in csv_reader:  # populating the data array
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

            # checks if the data is a numerical data
            if data.isnumeric():
                for j in range(len(self.data)):
                    # checks if the data is to be included
                    if self.data[j][count].isnumeric():
                        current_data = int(self.data[j][count])
                        data_add[0] = data_add[0] + 1
                        total += current_data

                        # comparing current data for min and max
                        if current_data < int(self.data[0][count]):
                            data_add[2] = current_data
                        if current_data > data_add[3]:
                            data_add[3] = current_data

                    data_add[1] = round((total/data_add[0]), 2)

                    # combine two list
                    new_dict[current_header] = dict(zip(header_dict, data_add))

            count += 1

        return new_dict

    def html_stats(self, stats: dict, filepath: str) -> None:
        fp = open(filepath, "w")

        table = "<style>\n"  # defining the sytle of the tags
        table += "  table, tr, th, td {\n"
        table += "      border: 1px solid black;\n"
        table += "      font-family: verdana;\n"
        table += "  }\n"
        table += "  table.center {\n"
        table += "      margin-left: auto;\n"
        table += "      margin-right: auto;\n"
        table += "      width: 100%;\n"
        table += "  }\n"
        table += "  h1 {\n"
        table += "      text-align: center;\n"
        table += "      font-family: verdana;\n"
        table += "  }\n"
        table += "</style>\n"

        table += '<style type="text/css">\n'
        table += "  table    {border:solid 1px #000;}\n"
        table += "  table td {border:solid 5px red;\n"
        table += "            border-top-color:#FEB9B9;\n"
        table += "            border-right-color:#B22222;\n"
        table += "            border-bottom-color:#B22222;\n"
        table += "            border-left-color:#FEB9B9;}\n"
        table += "</style>\n"
        table += '<style type="text/css">\n'
        table += "  table    {border:solid 1px #000;}\n"
        table += "  table td {border:solid 5px red;\n"
        table += "            border-top-color:#B22222;\n"
        table += "            border-right-color:#FEB9B9;\n"
        table += "            border-bottom-color:#FEB9B9;\n"
        table += "            border-left-color:#B22222;}\n"
        table += "</style>\n"

        table += "<h1>"  # displays the filename
        table += filepath[:-5]
        table += " dataset"
        table += "</h1>\n"

        table += '<table class="center">\n'  # creating table
        table += " <tr>\n"

        data_list = []
        header_list = []
        header = stats.keys()  # table column lable
        table += '     <th style="text-align: center">'
        table += '{0}</th>\n'.format("")
        table += '     <th style="text-align: center">'
        table += '{0}</th>\n'.format("COUNT")
        table += '     <th style="text-align: center">'
        table += '{0}</th>\n'.format("MEAN")
        table += '     <th style="text-align: center">{0}</th>\n'.format("MIN")
        table += '     <th style="text-align: center">{0}</th>\n'.format("MAX")

        # reading the data of the dictionary using the appropriate key
        for column in header:
            data_list.append(stats[column]["count"])
            data_list.append(stats[column]["mean"])
            data_list.append(stats[column]["min"])
            data_list.append(stats[column]["max"])
            header_list.append(column)

        table += " </tr>\n"

        # data part of the table and the row lable
        for i in range(int(len(data_list)/4)):
            table += " <tr>\n"
            table += '     <td style="text-align: center">'
            table += '<strong>'
            table += '{0}</strong></td>\n'.format(header_list[i].upper())
            calc_pos = i*4
            table += '     <td style="text-align: center">'
            table += '{0}</td>\n'.format(data_list[calc_pos])
            table += '     <td style="text-align: center">'
            table += '{0}</td>\n'.format(data_list[calc_pos+1])
            table += '     <td style="text-align: center">'
            table += '{0}</td>\n'.format(data_list[calc_pos+2])
            table += '     <td style="text-align: center">'
            table += '{0}</td>\n'.format(data_list[calc_pos+3])

            table += " </tr>\n"

        table += "</table>\n"

        # writing the 'table' string into the html file
        fp.write(table)
        fp.close()

    def count_instances(self, **kwargs) -> int:
        """
        Counts the number of instances where condition(s) are met

        The function will access the data from the file
        and compare it to the given criteria, if the condition(s)
        are met, it will increment the counter by 1.

        The function could take n-numbers of condition(s),
        where n > 0.

        Parameter
        ---------
        ( **kwargs )
        The function will accept conditions given by
        the user by using a dictionary style format,
        user are required to enter 1 or more conditions
        using ' key=value '.

        'key' represents the header of which
        the data is associated with.

        'value' represents the value or data
        that the condition must met.

        Returns
        -------
        The function will return an integer where
        the integer represents the number of
        instances where the condition(s) are met.

        Error Handling
        --------------
        An appropriate warning will be printed and the
        program will be terminated if the following occurs :-
            1. There is no argument or condition(s) given.
            2. The given argument or condition(s) does
               not exists in the .csv file.

        """
        count = 0
        location = []
        total_array = []
        row_num = []

        if len(kwargs) == 0:
            print("No condition is given.")
            exit()

        headers = self.header
        datas = self.data
        values = list(kwargs.values())

        # finding the row which data is located
        for keys in kwargs.keys():
            for i in range(len(headers)):
                if keys == headers[i]:
                    location.append(i)

        if len(location) != len(kwargs.keys()):
            print("The following header does not exists")
            exit()

        # repeat based on num of condition
        for i in range(len(location)):
            row_num = []
            current_check = location[i]
            for j in range(len(datas)):  # repeat until end of data
                if datas[j][current_check] == values[i]:
                    row_num.append(j)
            total_array.append(row_num)

        count = len(set(total_array[0]).intersection(*total_array[1:]))
        return count


if __name__ == "__main__":
    # DO NOT COMMENT ALL WHEN SUBMIT YOUR FILE, cannot have an if statement
    # with nothing afterwards.

    # test diabetes_data.csv
    test = Leopard("diabetes_data.csv")
    '''
    print(test.get_header())
    print(test.get_data())
    stats = test.stats()
    print(stats)
    test.html_stats(stats, "diabetes.html")
    '''
    print(test.count_instances(Gender="Male", weakness="Yes"))

    # test fide2021.csv
    test2 = Leopard("fide2021.csv")
    stats2 = test2.stats()
    test2.html_stats(stats2, "fide2021.html")

    '''
    print(test2.get_header())
    print(test.get_data())
    print(stats2)
    print(test2.count_instances(Country="NOR", Title="g"))
    '''

    # test student.csv
    test3 = Leopard("student.csv")
    '''
    print(test3.get_header())
    #print(test.get_data())
    #stats3 = test3.stats()
    #print(stats3)
    #test3.html_stats(stats3, "student.html")
    '''
