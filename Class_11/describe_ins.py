# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author

#     def __str__(self):
#         return (f"{self.title} by {self.author}")

#     def __repr__(self):
#         return (f"Book(title = '{self.title}', author = '{self.author}')")


# book = Book("The Productive Muslims", "Mohammad Faris")
# print(book)
# print( repr(book))
# class movie:
#     def __init__(self,title,director):
#         self.title=title
#         self.director=director

#     def __str__(self):
#         return (f"{self.title} was directed by {self.director}")

#     def __repr__(self):
#         return (f"book(title='{self.title}', director '{self.director}')")
# movie= movie("harry potter 2022","Chris Columbus")
# print(movie)
# print(repr(movie))

class Movie:
    def __init__(self, title, director):
        self.title = title
        self.director = director
    def __str__(self):
        return f"Movie Title: {self.title}, Director: {self.director}"
    def __repr__(self):
        return f"Movie(title='{self.title}', director='{self.director}')"
m1 = Movie("Wednesday", "Tim Burton")

print(str(m1))  
print(repr(m1))