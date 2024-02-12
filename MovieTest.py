class Movie:

    def __init__(self, title, genre, score):
        self.title = title
        self.genre = genre
        self.score = score

    def __str__(self):
        return (f"Title: {self.title}; "
                f"Genre: {self.genre}; "
                f"Score: {self.score}")

    def play(self, snack="Popcorn"):  # snack has been given a default value
        print(self.title + " is beginning ....")
        print("take out your {} for munching".format(snack))


if __name__ == "__main__":
    ghost_rider = Movie("Ghost Rider", "Action", 100)
    parasite = Movie("Parasite", "Thriller", 99)
    catching_fire = Movie("Catching Fire", "YA", 84)

    print(parasite)
    print(ghost_rider)
    print(catching_fire)

    ghost_rider.play("Peanut M&Ms")
    parasite.play("Mounds")
    catching_fire.play("Kettle Corn")

'''First Example info
    #print(type(movie1))

    print(movie1)

    #print(movie1.title)
    #print(movie1.genre)
    #print(movie1.score)

    movie1.title = "Good Will Hunting"
    print(movie1)
'''
