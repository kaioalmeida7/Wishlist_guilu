from search_movies import Search
from create_user import Registering_user
from Delete_movie import Delete

print('***************************BEM VINDO AO METFLIX!***************************')
print('PARA BUSCAR UM FILME ESCREVA: "buscar"!')
print('PARA SE CADASTRAR ESCREVA: "cadastro"!')
print('PARA DELETAR UM FILME, ESCREVA: "deletar filme" ! ')
choice = input('ESCOLHA UMA DAS OPÇÕES ACIMA:  ')

def menu_metflix(choice):
    if choice == 'buscar':
        call_movie = Search()
        call_movie.search_movies()
    elif choice == 'cadastro':
        call_user = Registering_user()
        call_user.create_user()
    elif choice == 'deletar filme':
        call_delete = Delete()
        call_delete.delete_movie()
    else:
        print('ALTERNATIVA ERRADA! ENCERRANDO PROGRAMA!')
        return menu_metflix
menu_metflix(choice)