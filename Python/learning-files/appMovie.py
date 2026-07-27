from MovieClass import Movie
import json

JSON_FILE = "moviesList.json"

#function to load movies from JSON
def load_movies_from_json():
    database = {"Hollywood": [], "Bollywood": []}
    
    #load JSON file
    with open(JSON_FILE, "r") as file:
        raw_data = json.load(file)
    
        #append Hollywood and Bollywood movies individually into database
        for industry in database.keys():
            if industry in raw_data:
                for movie_dict in raw_data[industry]:
                    database[industry].append(movie_dict)
                    
    return database
        
        
#function to print the suggestions based on the genre
def print_suggestions(suggestions, genre, industry_name):
    print(f"\n--- {industry_name} Movies---")
    if not suggestions:
        print(f"No movies found for the genre '{genre}'.")
    else:
        for movie in suggestions:
            print(f"{movie["title"]} ({movie["year"]}) directed by {movie["director"]} | Genre: " + (", ".join(movie["genre"])))

#function to search for movies based on user genre
def search_for_movies(movies_db):
    try:
        user_genre = input("\nEnter a genre to search (or press Enter to cancel): ")
        
        if not user_genre:
            print("\n-----Action cancelled-----")
            return
        
        #.title() changes "sci-fi" to "Sci-Fi" autoamtically
        formatted_genre = user_genre.title()
        
        #search with Hollywood and Bollywood movies separately and append to print suggestions
        for industry, movies_list in movies_db.items():
            suggestions = [] 
            for movie in movies_list:
                if formatted_genre in movie['genre']:
                    suggestions.append(movie)
            print_suggestions(suggestions, formatted_genre, industry)
            
    except KeyboardInterrupt:
        print("\nSearch interrupted by user")
    except Exception as e:
        print(f"An error occured during search: {e}")
                    

#function to get movie suggestions based on the genre
def main_menu():
   
    movies_db = load_movies_from_json()
    
    while True:
        print("\n==================================\n")
        print("     MOVIE RECOMMENDATIONS    ")
        print("\n==================================")
        print("1. Search movies by genre")
        print("2. Exit Application")

        #strip removes spaces from the input (before & after)
        choice = input("\nSelect an option (1-2): ").strip()
        
        if choice == "1":
            search_for_movies(movies_db)
        elif choice == "2":
            print("\nThankyou for using the Movie app. Bye!\n")
            break
        else:
            print("INVALID CHOICE. Please enter a valid number (1 or 2)")
    

#running the function to get movie suggestions based on the genre
if __name__ == "__main__":
    main_menu()