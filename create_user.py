import json


class Registering_user:

    def __init__(self):
        self.user_name = input('Digite seu nome: ')
        self.user_email = input('Digite seu email: ')
        self.user_cpf = input('Digite seu CPF: ')


    def create_user(self):
        

        users = []
        user = {
           'nome':self.user_name,
           'email':self.user_email,
           'cpf':self.user_cpf
        }

    

        flag = False

        try:
            with open('users.json') as file:
                users = json.load(file)
                for i in users:
                    if i['cpf'] == self.user_cpf:
                        print('**********USUÁRIO JÁ CADASTRADO! CADASTRE OUTRO!**********')
                        flag = True
                        break
                    else: 
                        flag = False
                        pass
                if flag == True:
                    pass
                else:
                    users.append(user)
                    with open ('users.json', 'w') as file:
                        json.dump(users, file, indent=2)
            

        except:
            users.append(user)
            with open('users.json', 'w') as file:
                json.dump(users, file, indent=2) 


    