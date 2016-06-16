import webbrowser

class Movie():
    """ This class provides a way to store movie related info """
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    #constructor
    def __init__(self, title, storyline, poster_image_url,
                 trailer_youtube_url, rating):
        '''
        Args:
            title: stores the title of the Movie
            storyline: stores the storyline/simplified plot of the Movie
            poster_image_url: URL for the Movie poster
            trailer_youtube_url: URL for the Movie trailer on YouTube
            rating: the Movie's MPAA rating
        '''
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.rating = rating

    #end __init__ method

    #instance method
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
