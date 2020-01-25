import mysql.connector
import pandas as pd

#********************************************* Connection string ***************************************************#
connection = mysql.connector.connect(host="127.0.0.1",  user="root",  password="Sudeep!96",   database="careallDB")

#********************************************* Young champ class ***************************************************#

class YoungChamp:
    def __init__(self, name, password, income_earned, contact, address, id_proof, no_of_oldies, rating, adult_obj):
        self.name = name
        self.__password = password
        self.__income_earned = income_earned
        self.contact = contact
        self.address = address
        self.id_proof = id_proof
        self.no_of_oldies = no_of_oldies
        self.rating = rating
        self.adult_obj = adult_obj
        print("*************************************************************************************")

     # A method for champs to accept oldie after the adult has approved the champ
    def accept_oldie(self):
        print("Accepting oldies by champ : ")
        print("Hi Champ! You have been assigned an oldie.")
        print("Oldie  name  :", self.adult_obj.oldies_name)
        selection = input("Please type y for accepting oldie ")
        if selection.lower() == 'y':
            champ_id = input("Please Enter your(Champ) id  ")
            #print(champ_id)
            print("Approval from adults : ")
            self.adult_obj.approve_young(champ_id)
        else:
            champ_id = 0
            self.adult_obj.approve_young(champ_id)

    def show_oldies(self):
        print("Showing all the oldies assigned to a particular champ")
        champ_id = input("Please enter your champ_id: ")
        cursor = connection.cursor()
        args = [champ_id]
        cursor.callproc('SelectAllOldies',args)

        # print out the result
        for result in cursor.stored_results():
            x = result.fetchall()
        df = pd.DataFrame(x, columns=['Oldie Name', 'Oldie ID','Assigned Champ','Champ Name'])
        print(df)
        cursor.close()
        print("********************************* END OF SHOWING OLDIES ****************************************************")

    def update_income(self):
        print("Request from champ for payment : ")
        champ_id = input("Please Enter your(Champ) id  ")
        self.adult_obj.make_payment(champ_id)
        print("Your income has been updated!!!")
        print("********************************* END OF PAYMENT ********************************************************")

    def reset_password(self):
        new_password = input("Please Enter your new password  ")
        self.__password = new_password
        print("Your password has been updated successfully!!!")
        print("*************************************************************************************")

#********************************************* Adult class ***************************************************#


class Adult:
    def __init__(self, name, password, contact, address, id_proof, oldies_name):
        self.name = name
        self.__password = password
        self.contact = contact
        self.address = address
        self.id_proof = id_proof
        self.oldies_name = oldies_name
        print("*************************************************************************************")

    def show_young(self):
        print("Showing champ who is taking care of a particular oldie : ")
        oldie_id = input("Please Enter your oldie id  ")
        cursor = connection.cursor()
        args = [oldie_id]
        cursor.callproc('SelectAllchamps',args)
        result_list = []
        for result in cursor.stored_results():
            x = result.fetchall()
        df = pd.DataFrame(x, columns=['Oldie Name', 'Oldie ID', 'Assigned Champ', 'Champ Name','Champ contact'])
        print(df)
        cursor.close()
        print("*********************************END OF SHOWING CHAMPS ****************************************************")

    def approve_young(self, champ_id):
        if int(champ_id) == 0:
            print("The champ is not willing to take care of your oldie : ")
            print("*************************************************************************************")
        else:
            sql_select_Query = "select * from young_champs where no_of_oldies < 4"
            cursor = connection.cursor(buffered=True)
            cursor.execute(sql_select_Query)
            if cursor.rowcount > 0:
                records = cursor.fetchall()
            champs_list = []
            for row in records:
                champs_dict = {"username": row[0], "pass": row[1], "income_earned": row[2], "contact": row[3],
                       "address": row[4], "id_proof": row[5], "no_of_oldies": row[6], "rating": row[7], "id": row[8]}
                champs_list.append(champs_dict)
            for champ in champs_list:
                #print(champ)
                if int(champ["id"]) == int(champ_id):
                    # print(champ_id)
                    # print(champ["no_of_oldies"])
                    no_of_oldies_current = champ["no_of_oldies"]
                    print("Currently the champ is taking care of " + str(no_of_oldies_current) + "  oldie(s)")
            no_of_oldies = input("Please enter number of oldies based on champ's vacancy ")
            no_of_oldies = int(no_of_oldies_current) + int(no_of_oldies)
            sql_update_query = "update young_champs set no_of_oldies = %s where id = %s"
            data = (no_of_oldies, champ_id)
            cursor = connection.cursor()
            cursor.execute(sql_update_query, data)
            connection.commit()
            cursor.close()
            print(" The oldie has been assigned to champ_id: ", champ_id)
            print("*******************************END OF OLDIE ASSIGNMENT ******************************************************")

    def make_payment(self, champ_id):
        print("Payment from adult : ")
        print("Please make the payment for the champ ", champ_id)
        sql_select_Query = "select * from young_champs where no_of_oldies < 4"
        cursor = connection.cursor(buffered=True)
        cursor.execute(sql_select_Query)
        if cursor.rowcount > 0:
            records = cursor.fetchall()
        champs_list = []
        for row in records:
            champs_dict = {"username": row[0], "pass": row[1], "income_earned": row[2], "contact": row[3],
                           "address": row[4], "id_proof": row[5], "no_of_oldies": row[6], "rating": row[7],
                           "id": row[8]}
            champs_list.append(champs_dict)
        for champ in champs_list:
            if int(champ["id"]) == int(champ_id):
                #print(champ_id)
                current_income = champ["income_earned"]
        payment = input("Please enter the amount you want to pay  ")
        total_income = int(current_income) + int(payment)
        sql_update_query = "update young_champs set income_earned = %s where id = %s"
        data = (total_income, champ_id)
        cursor = connection.cursor()
        cursor.execute(sql_update_query, data)
        connection.commit()
        cursor.close()

    def reset_password(self, new_password):
        new_password = input("Please Enter your new password  ")
        self.__password = new_password
        print("Your password has been updated successfully!!!")
        print("*************************************************************************************")

#******************************************** Testing *********************************************#

def test():
    adult1 = Adult("adult2","5698",2308561230,"pune","aadhar","oldie3,oldie4")
    champ1 = YoungChamp("name4","147",1000,56710561230,"pune","aadhar",1,4,adult1)
    champ1.accept_oldie()
    champ1.update_income()
    champ1.show_oldies()
    adult1.show_young()

test()





