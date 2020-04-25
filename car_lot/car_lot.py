# import logger
# import definitions
import file_handler
import user
# user elements from pass_dictionary needed to check role and give the current salary to be changed


class CarLot:
    def __init__(self):
        # lot_employee_1 = user.Users('amir bernstein', '12345678')
        lot_user_1 = user.Users()

        self.role = lot_user_1.does_exist()

        self.handler_data = lot_user_1.handler_data

        print(self.handler_data)

        self.data = file_handler.FileHandler()

        self.row = self.update_salary_by_name()

        print(self.row)

        self.data.update_csv("/Users/rommienglard/PycharmProjects/week2/python_mini_project/car_lot/user.csv", self.row['id'], self.row)


# create function that will change the salary if the role of the user is 'admin
    def update_salary_by_name(self):
        try:
            #temp_dictionary = {}
            if self.role == 'admin':
                print('yay')
                employee_name = input("Enter employee name to change salary: ")
                employee_name_list = employee_name.split()
                # split given name into list in order to compare it to handler_data
                for row in self.handler_data:
                    #
                    # for key, value in row.items():
                    #     temp_dictionary[key] = value

                    if employee_name_list[0] == row.get('first_name') and employee_name_list[1] == row.get('last_name'):
                        employee_salary = input("Enter new salary: ")
                        print(f"{employee_name}'s updated salary is {employee_salary}")
                        row['salary'] = employee_salary
                        return row
            else:
                print('no can do bud')

        except Exception as err:
            print(err)


lot = CarLot()

# lot.update_salary_by_name()

# lot.give_raise()

