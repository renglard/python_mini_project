import logger
import definitions
import file_handler


class Users:

    def __init__(self, name, user_list, password):
        self.name = name
        self.user_list = user_list
        self.password = password

    def dict_names(self):
        pass_dictionary = {}
        for users in self.user_list:
            #add new key/value to empty pass_dectionary
            pass_dictionary[users['first_name'] + " " + users['last_name']] = [users['password'], users['role']]
        print(pass_dictionary)
        return pass_dictionary

    def does_exist(self, pass_dict):
        try:
            if self.name in pass_dict.keys():
                if pass_dict[self.name][0] == self.password:
                    return pass_dict.get(self.name)[1]
            else:
                return False
        except Exception as err:
            print(err)


data = file_handler.FileHandler()
user_list = data.open_csv_file("/Users/rommienglard/PycharmProjects/week2/python_mini_project/car_lot/user.csv")

print(user_list)

name = input("Enter your first and last name: ").lower()
password = input("enter your password: ").lower()
user = Users(name, user_list, password)
pass_dictionary = user.dict_names()
print(pass_dictionary)
print(user.does_exist(pass_dictionary))
