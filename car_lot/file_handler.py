import logger
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
                # print(self.handler_data)
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

    def remove_from_csv(self, file_name, id):
        try:
            self.open_csv_file(file_name)

            for row in self.handler_data:
                if row.get("id") == id:
                    self.handler_data.remove(row)

            with open(file_name, 'w', newline="") as remove_obj:
                changed_file = csv.DictWriter(remove_obj, fieldnames=self.handler_data[0].keys())
                changed_file.writeheader()
                changed_file.writerows(self.handler_data)
            print('True')

        except Exception as err:
            return False, err

    def update_csv(self, file_name, id, data):
        try:
            self.open_csv_file(file_name)
            for row in self.handler_data:
                # print(row)
                if row["id"] == id:
                    #print(row['id'])
                    self.handler_data.remove(row)
                    # index_method to insert new row
                    self.handler_data.insert(int(id)-1, data)
            # print(self.handler_data)

            with open(file_name, 'w', newline="") as remove_obj:
                changed_file = csv.DictWriter(remove_obj, fieldnames=self.handler_data[0].keys())
                changed_file.writeheader()
                changed_file.writerows(self.handler_data)
            print('true')

        except Exception as err:
            return False, err



# new_row = ['4', 'lexus', 'ramon', '4', 'dd', '10']
# my_file = FileHandler()
# #
# # my_file.open_csv_file("/Users/rommienglard/PycharmProjects/week2/python_mini_project/car_lot/vehicle.csv")
#
# #my_file.remove_from_csv("/Users/rommienglard/PycharmProjects/week2/python_mini_project/car_lot/vehicle.csv", '3')
#
# # my_file.update_csv("/Users/rommienglard/PycharmProjects/week2/python_mini_project/car_lot/vehicle.csv", '2', new_row)
#
# # my_file.remove_from_csv("/Users/rommienglard/PycharmProjects/week2/python_mini_project/car_lot/vehicle.csv")
# #
# # my_file.append_to_csv("/Users/rommienglard/PycharmProjects/week2/python_mini_project/car_lot/vehicle.csv", added_input)
#
# updated_row = {'id':1, 'brand': 'hyundai', 'owner':'emily', 'last_test':'5', 'color':'de', 'door_count':'11'}
# #

# my_file.update_csv("/Users/rommienglard/PycharmProjects/week2/python_mini_project/car_lot/vehicle.csv", '2', updated_row)
#
#
#

