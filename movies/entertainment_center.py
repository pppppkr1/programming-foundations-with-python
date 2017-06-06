import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://en.wikipedia.org/wiki/Toy_Story#/media/File:Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://www.impawards.com/2009/posters/avatar_xlg.jpg",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")

the_handmaiden = media.Movie("The Handmaiden",
                             "A crook-turned-servant falls for the vulnerable heiress she had originally schemed to swindle, in this audacious, visually sumptuous, and highly erotic period piece",
                             "http://www.joblo.com/timthumb.php?src=/posters/images/full/handmaiden-poster.jpg&h=600&q=100",
                             "https://www.youtube.com/watch?v=fvI4yZLGwAk")

#print(toy_story.storyline)
#print(avatar.storyline)

#toy_story.show_trailer()
#the_handmaiden.show_trailer()

movies = [toy_story, avatar, the_handmaiden]
#fresh_tomatoes.open_movies_page(movies)

#print(media.Movie.VALID_RATINGS)

print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)
