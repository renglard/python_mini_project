import Logger
import definitions
import csv
from csv import writer


class FileHandler:
    def __init__(self):
        self.handler_data = []

    def open_csv_file(self, file_name):
        try:
            with open(file_name, "r") as csv_file:
                csv_reader = csv.DictReader(csv_file)

                for line in csv_reader:
                    self.handler_data.append(line)
                return self.handler_data

        except Exception as error:
            print("There is an error :" + str(error))

    def append_to_csv(self, file_name, data):

        try:
            self.open_csv_file(file_name)
            for row in self.handler_data:
                if row.get("id") == data[0]:
                    raise Exception("This ID already exists")

            with open(file_name, 'a+', newline='') as write_obj:
                csv_writer = writer(write_obj)
                csv_writer.writerow(data)

        except Exception as error:
            print("There is an error :" + str(error))

        # try:
        # with open(file_name, "r") as csv_file:
        #     csv_reader = csv.DictReader(csv_file)
        #
        #     with open(file_name, "a") as new_file:
        #
        #         field_names = ['id', 'brand', 'owner', 'last_test', 'color', 'door_count']
        #         csv_writer = csv.DictWriter(new_file, fieldnames=field_names)
        #
        #         csv_writer.writeheader()
        #
        #         for line in csv_reader:
        #             csv_writer.writerow(line)

        # except Exception as error:
        #     print("There is an error :" + str(error))


added_input = ['4', 'lexus', 'ramon', '4', 'dd', '10']

my_file = FileHandler()
#
# my_file.open_csv_file("/Users/rommienglard/PycharmProjects/week2/python_mini_project/car_lot/vehicle.csv")
#
my_file.append_to_csv("/Users/rommienglard/PycharmProjects/week2/python_mini_project/car_lot/vehicle.csv", added_input)




