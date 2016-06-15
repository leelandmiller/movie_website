import media
import fresh_tomatoes

#instance variables
toy_story = media.Movie(
    "Avengers: Age of Ultron",
    "The Avengers battle Ultron",
    "http://vamers.com/wp-content/uploads/2015/03/Vamers-FYI-Movies-Avengers-Age"
    "-of-Ultron-Official-Movie-Poster-01.jpg",
    "https://www.youtube.com/watch?v=JAUoeqvedMo")

avatar = media.Movie(
    "Avatar", "A marine on an alien planet",
    "http://imgs.abduzeedo.com/files/articles/Avatar/4154691413_a695e033a8_o.jpg",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY")

the_dark_knight = media.Movie(
    "The Dark Knight",
    "A vicious battle between Batman and the Joker",
    "https://smilingldsgirl.files.wordpress.com/2013/06/"
    "xemphimso_ky-si-bong-dem-1.jpg",
    "https://www.youtube.com/watch?v=EXeTwQWrcwY")

the_dark_knight_rises = media.Movie(
    "The Dark Knight Rises",
    "A vicious battle between Batman and Bane",
    "http://static.deathandtaxesmag.com/uploads/2012/05/Batman-The-Dark-Knight"
    "-Rises-Movie-Poster.jpg",
    "https://www.youtube.com/watch?v=g8evyE9TuYk")

man_of_steel = media.Movie(
    "Man of Steel",
    "The story of the one and only...Superman",
    "http://www.impawards.com/2013/posters/man_of_steel_ver3.jpg",
    "https://www.youtube.com/watch?v=T6DJcgm3wNY")

the_amazing_spiderman_2 = media.Movie(
    "The Amazing Spider-Man 2",
    "Spider man!!",
    "http://www.movienewz.com/img/gallery/amazing-spiderman-2/posters/"
    "amazing_spider-man_2_movie_poster_5.jpg",
    "https://www.youtube.com/watch?v=DlM2CWNTQ84")

movies_list = [
toy_story,
avatar,
the_dark_knight,
the_dark_knight_rises,
man_of_steel,
the_amazing_spiderman_2
]

fresh_tomatoes.open_movies_page(movies_list)
ratings = media.Movie.VALID_RATINGS

print(ratings)
# print(movies.Movie.__doc__)
# print(movies.Movie.__name__)
# print(movies.Movie.__module__)
