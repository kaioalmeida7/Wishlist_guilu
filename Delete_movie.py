import json

class Delete:

    def __init__(self):
        self.name_movie = input('Digite o nome do Filme: ')

    def delete_movie(self):
        
        movies = []
        flag = False

        try:
        
            with open ('movies.json') as file:
                movies = json.load(file)
                for i in movies:
                    print ('entrou no for?')
                    if i['nome'] == self.name_movie:
                        movies.remove(i)
                        flag = True
                        break
                    else:
                        flag = False
                        pass
                
                if flag == True:
                    with open ('movies.json', 'w') as file:
                        json.dump(movies, file, indent=2)
                    
                else:
                  pass  
        
        except:
            pass
