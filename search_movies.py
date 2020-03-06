import requests
import json



class Search:
   
    def __init__(self):
        self.name_movie = input("Digite o nome do filme antisocial lazarento: ")

    def search_movies(self):
        
        movies = []

        params = {
            't':self.name_movie    
        }

        url = 'http://www.omdbapi.com/?apikey=29f3c461&'

        request_movie = requests.get(url, params)
        request = request_movie.json()
        ##print(request)

        movie = {
            'nome':request['Title'],
            'ano':request['Year'],
            'genero':request['Genre'],
            'diretor':request['Director']
        }

        flag = False

        try:
        
            with open ('movies.json') as file:
                movies = json.load(file)
                for i in movies:
                    print ('entrou no for?')
                    if i['nome'] == self.name_movie:

                        print('FILME JÁ INCLUSO NO SISTEMA!')
                        flag = True
                        break
                    else:
                        flag = False
                        pass
                
                if flag == True:
                    pass
                    
                    
                else:
                    movies.append(movie)
                    with open ('movies.json', 'w') as file:
                        json.dump(movies, file, indent=2)
        
        except:
            movies.append(movie)
            with open ('movies.json', 'w') as file:
                json.dump(movies, file, indent=2)

        
           