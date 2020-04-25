import logger
import definitions
import file_handler


class Users:

    def __init__(self):

        self.data = file_handler.FileHandler()
        self.handler_data = self.data.open_csv_file("/Users/rommienglard/PycharmProjects/week2/python_mini_project/car_lot/user.csv")
        self.name = input('Enter username: ')
        self.password = input('Enter password: ')
        self.pass_dictionary = {}
        self.dict_names()


    def dict_names(self):
        for users in self.handler_data:
            #add new key/value to empty pass_dictionary
            self.pass_dictionary[users['first_name'] + " " + users['last_name']] = [users['password'], users['role'],
                                                                                    users['salary']]
        #print(self.pass_dictionary)
        return self.pass_dictionary

    def does_exist(self):
        try:
            if self.name in self.pass_dictionary.keys():
                if self.pass_dictionary[self.name][0] == self.password:
                    # return the role
                    return self.pass_dictionary.get(self.name)[1]
            else:
                return False
        except Exception as err:
            print(err)

    def the_salary(self):
        try:
            if self.name in self.pass_dictionary.keys():
                if self.pass_dictionary[self.name][0] == self.password:
                    # return the role
                    return self.pass_dictionary.get(self.name)[2]
            else:
                return False
        except Exception as err:
            print(err)

# data = file_handler.FileHandler()
# handler_data = data.open_csv_file("/Users/rommienglard/PycharmProjects/week2/python_mini_project/car_lot/user.csv")
#
# name = 'hen biton'
# password = '12345678'

# user = Users('hen biton', '12345678')
# print("hen's 1role:", user.does_exist())

# print(user.the_salary())
