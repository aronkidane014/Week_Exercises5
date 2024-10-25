# Exercise 3.B lab 1
movie=["dead pool", "Scarface", "The God Father", "The Mask","Aladdin"]

print(f"Thelist'movies' includes my top {len(movie)} favorite movies.")
print(f"This'movies' are my top {len(movie)} favorite movies of all time:{", ".join(movie)}")
print(movie) # this prints in the order they written Question4
print(sorted(movie)) # this sorts them alphabetical order
movie.sort
print(sorted(movie)) #it is the same results
movie.append("Life") #question 5
print(movie)