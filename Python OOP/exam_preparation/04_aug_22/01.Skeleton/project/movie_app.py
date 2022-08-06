from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def register_user(self, username, age):
        if self.__user_finder(username) in self.users_collection:
            raise Exception("User already exists!")
        user = User(username, age)
        self.users_collection.append(user)
        return f"{username} registered successfully."

    def upload_movie(self, username, movie):
        user = self.__user_finder(username)
        if user is None:
            raise Exception("This user does not exist!")
        if username != movie.owner.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")
        if movie.owner.username == username:
            self.movies_collection.append(movie)
            user.movies_owned.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def __validate_movie_owner(self, username, movie, must_own: bool):
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        if must_own:
            if movie.owner.username != username:
                raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        else:
            if movie.owner.username == username:
                raise Exception(f"{username} is the owner of the movie {movie.title}!")

    def __user_finder(self, username):
        for u in self.users_collection:
            if u.username == username:
                return u

    def edit_movie(self, username, movie, **kwargs):
        __must_be_owner = True
        self.__validate_movie_owner(username, movie, __must_be_owner)
        for attr, value in kwargs.items():
            setattr(movie, attr, value)
        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username, movie):
        __must_be_owner = True
        movie_title = movie.title
        self.__validate_movie_owner(username, movie, __must_be_owner)
        self.movies_collection.remove(movie)
        user: User = self.__user_finder(username)
        user.movies_owned.remove(movie)
        return f"{username} successfully deleted {movie_title} movie."

    def like_movie(self, username, movie):
        __must_be_owner = False
        self.__validate_movie_owner(username, movie, __must_be_owner)
        user: User = self.__user_finder(username)
        if movie in user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")
        user.movies_liked.append(movie)
        movie.likes += 1
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username, movie):
        __must_be_owner = False
        self.__validate_movie_owner(username, movie, __must_be_owner)
        user: User = self.__user_finder(username)
        if movie not in user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")
        user.movies_liked.remove(movie)
        movie.likes -= 1
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        if not self.movies_collection:
            return "No movies found."

        movies_details = [movie.details() for movie in sorted(
            self.movies_collection, key=lambda movie: (-movie.year, movie.title))]
        return '\n'.join(movies_details)

    def __str__(self):
        if not len(self.users_collection):
            users = "No users."
        else:
            users = ", ".join(user.username for user in self.users_collection)

        if not len(self.movies_collection):
            movies = "No movies."
        else:
            movies = ", ".join(movie.title for movie in self.movies_collection)
        return "All users: " + users + "\n" + "All movies: " + movies

