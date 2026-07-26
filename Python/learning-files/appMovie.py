from MovieClass import Movie

#creating a list of hollywood movies
list_of_hollywood_movies = [
    Movie("Inception", "Christopher Nolan", 2010, ["Action", "Sci-Fi"]),
    Movie("The Shawshank Redemption", "Frank Darabont", 1994, ["Drama"]),
    Movie("The Godfather", "Francis Ford Coppola", 1972, ["Crime", "Drama"]),
    Movie("The Dark Knight", "Christopher Nolan", 2008, ["Action", "Crime", "Drama"]),
    Movie("Pulp Fiction", "Quentin Tarantino", 1994, ["Crime", "Drama"]),
    Movie("The Lord of the Rings: The Return of the King", "Peter Jackson", 2003, ["Adventure", "Drama", "Fantasy"]),
    Movie("Forrest Gump", "Robert Zemeckis", 1994, ["Drama", "Romance"]),
    Movie("The Matrix", "Lana Wachowski, Lilly Wachowski", 1999, ["Action", "Sci-Fi"]),
    Movie("Fight Club", "David Fincher", 1999, ["Drama"]),
    Movie("The Silence of the Lambs", "Jonathan Demme", 1991, ["Crime", "Drama", "Thriller"]),
]

#creating a list of bollywood movies
list_of_bollywood_movies = [
    Movie("3 Idiots", "Rajkumar Hirani", 2009, ["Comedy", "Drama"]),
    Movie("Dangal", "Nitesh Tiwari", 2016, ["Biography", "Drama", "Sport"]),
    Movie("Bajrangi Bhaijaan", "Kabir Khan", 2015, ["Adventure", "Comedy", "Drama"]),
    Movie("PK", "Rajkumar Hirani", 2014, ["Comedy", "Drama", "Sci-Fi"]),
    Movie("Baahubali: The Beginning", "S. S. Rajamouli", 2015, ["Action", "Drama", "Fantasy"]),
    Movie("Bajrangi Bhaijaan", "Kabir Khan", 2015, ["Adventure", "Comedy", "Drama"]),
    Movie("Kabir Singh", "Sandeep Reddy Vanga", 2019, ["Drama", "Romance"]),
    Movie("Andhadhun", "Sriram Raghavan", 2018, ["Crime", "Drama", "Thriller"]),
    Movie("Tanhaji: The Unsung Warrior", "Om Raut", 2020, ["Action", "Biography", "Drama"]),
    Movie("Chhichhore", "Nitesh Tiwari", 2019, ["Comedy", "Drama"]),
]

#function to print the suggestions based on the genre
def print_suggestions(suggestions):
    if not suggestions:
        print(f"No movies found for the genre '{genre}'.")
    else:
        for movie in suggestions:
            print(f"{movie.title} ({movie.year}) directed by {movie.director}. Genres: {', '.join(movie.genres)}")

#function to get movie suggestions based on the genre
def get_suggestions():
    genre = input("Enter a genre to get movie suggestions: ")
    suggestions = []
    
    print("Hollywood Movies:")
    
    #appending the movies of the given genre from hollywood movies
    for movie in list_of_hollywood_movies:
        if genre in movie.genres:
            suggestions.append(movie)
    print_suggestions(suggestions)
            
    print("\nBollywood Movies:")
    
    #appending the movies of the given genre from bollywood movies
    for movie in list_of_bollywood_movies:
        if genre in movie.genres:
            suggestions.append(movie)
    print_suggestions(suggestions)
    

#running the function to get movie suggestions based on the genre
get_suggestions()