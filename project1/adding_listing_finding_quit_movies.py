avaliable_menu = "enter 'a' to add a movie, enter 'l' to list a movie, enter 'f' to find the movie:- "
movies = []

def add_movies():
    title = input("enter a movie name:- ")
    rating = int(input("enter a movie rating:- "))
    ticket_price = int(input("enter the ticket price:- "))
    movie_hero = input("enter a movie hero name:- ")
   
   
    
    movies.append({
        "title":title,
        "rating":rating,
        "ticket_price":ticket_price,
        "movie_hero":movie_hero
    })
    
def listing_movies():
    for movie in movies:
        print(movie)
        
def finding_movies():
    find_movie = input("enter a movie name to find:- ")
    if movie in movies:
        if movie["title"] ==  find_movie:
            print(movie)
            
            
menu_prompt = input(avaliable_menu)
while menu_prompt != 'q':
    if menu_prompt == 'a':
        add_movies()
    elif menu_prompt == 'l':
        listing_movies()
    elif menu_prompt == 'f':
        finding_movies()
        
    else:
        print("sorry for inconvinence, kindly recheck the values that are entered:) ")
