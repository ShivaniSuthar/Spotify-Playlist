
def doctests():
    """
    >>> track1 = Song('More Life', 3.11, 'Just Until...', 'Cordae', 1220980)
    >>> print(track1)
    'More Life' by Cordae on 'Just Until...' is 3.11 minutes long with 1220980 streams
    >>> track1.get_artist()
    'Cordae'

    >>> Song.platform
    'Spotify'
    >>> track1.platform
    'Spotify'

    >>> play1 = Playlist('Rap Caviar', 'James')
    >>> print(play1)
    Playlist 'Rap Caviar' by James has 0 songs
    >>> play1.add_song(track1)
    True
    >>> play1.get_total_streams()
    1220980
    >>> print(play1)
    Playlist 'Rap Caviar' by James has 1 songs
    >>> play1.add_song(track1)
    False
    >>> play1.remove_song(track1)
    True
    
    >>> track2 = Song('Good Days', 4.65, 'Good Days', 'SZA', 276568815)
    >>> track3 = Song('Heat Waves', 3.999, 'Dreamland', 'Glass Animals', 5000)
    >>> play1.add_song(track2)
    True
    >>> play1.add_song(track1)
    True
    >>> play1.add_song(track3)
    True
    >>> track2.add_to_playlist(play1)
    False

    >>> play1.sort_songs('length')
    >>> [x.get_name() for x in play1.get_songs()]
    ['More Life', 'Heat Waves', 'Good Days']
    >>> play1.sort_songs('name')
    >>> [x.get_name() for x in play1.get_songs()]
    ['Good Days', 'Heat Waves', 'More Life']
    >>> play1.sort_songs('streams')
    >>> [x.get_name() for x in play1.get_songs()]
    ['Heat Waves', 'More Life', 'Good Days']

    >>> play1.get_most_played_song()
    'Good Days'
    >>> play1.get_total_streams()
    277794795
    >>> play1.get_total_length()
    11.759

    >>> print(play1.play())
    Listening to 'Heat Waves' by Glass Animals
    Listening to 'More Life' by Cordae
    Listening to 'Good Days' by SZA

    >>> print(track1.listen())
    Listening to 'More Life' by Cordae
    >>> play1.get_total_streams()
    277794799

    >>> play2 = Playlist('Anti Pop', 'Spotify')
    >>> play1.combine_playlists(play2)
    True
    >>> play2.combine_playlists(play1)
    True
    >>> print(play2)
    Playlist 'Anti Pop' by Spotify has 3 songs
    >>> play2.combine_playlists(play1)
    3
    >>> play2.remove_song(track2)
    True
    >>> play2.get_most_played_song()
    'More Life'

    >>> track2.add_to_playlist(play2)
    True
    >>> play2.get_most_played_song()
    'Good Days'

    track3 = Song('Im Tired', 3.12, 'So sleepy...', 'Shiv', 1220981)
    track4 = Song('Im Tireds', 3.13, 'So sleepyy...', 'Shivv', 1220982)
    track5 = Song('Im Tiredss', 3.14, 'So sleepyyy...', 'Shivvv', 1220983)
    play3 = Playlist('Hello', 'me')
    play4 = Playlist('Helloo', 'mee')
    play5 = Playlist('Helloo0', 'meee')

    """

class Song:
    """
    Implementation of a song
    """
    # Initializing the class attribute
    platform = "Spotify"

    def __init__(self, name, length, album, artist, streams):
        """
        Song Constructor

        Parameters:
        name (str): name of the song
        length (float): song duration in minutes
        album (str): name of album the song is in
        artist (str): name of artist
        streams (int): number of times the song has been streamed
        """
        self.name = name
        self.length = length
        self.album = album
        self.artist = artist
        self.streams = streams

        assert isinstance(name, str)
        assert len(name) > 0
        assert isinstance(length, float)
        assert length > 0
        assert isinstance(album, str)
        assert len(album) > 0
        assert isinstance(artist, str)
        assert len(artist) > 0
        assert isinstance(streams, int)
        assert streams >= 0


    def get_name(self):
        """ Getter for name attribute """

        return self.name 


    def get_length(self):
        """ Getter for length attribute """

        return self.length 


    def get_album(self):
        """ Getter for album attribute """

        return self.album


    def get_artist(self):
        """ Getter for artist attribute """

        return self.artist


    def get_streams(self):
        """ Getter for streams attribute """

        return self.streams


    def __str__(self):
        """
        String representation of a Song
        """
        return  "'" + self.name + "'" + " by " +\
         self.artist + " on " + "'" + self.album + "'" + " is "\
         + str(self.length) + " minutes long with " +\
          str(self.streams) + " streams"


    def listen(self):
        """
        Listens to the song, increasing the stream counter.
        Returns a string with the song name and artist
        """
        self.streams = self.streams + 1
        return "Listening to " + "'" + self.name + "'" + " by " + self.artist


    def add_to_playlist(self, playlist):
        """
        Takes a Playlist object and adds the current Song instance into it.
        returns True if successful
        returns False if song is already included in playlist
        """
        return playlist.add_song(self)


class Playlist:
    """
    Implementation of a playlist
    """

    def __init__(self, title, user):
        """
        Playlist Constructor

        Parameters:
        title (str): title of the playlist
        user (str): username of user who created playlist

        Attributes:
        songs (list): list used to store songs in playlist
        """
        self.title = title
        self.user = user
        self.songs = []

        assert isinstance(title, str)
        assert len(title) > 0 
        assert isinstance(user, str)
        assert len(user) > 0



    def get_title(self):
        """ Getter for title attribute """

        return self.title


    def get_user(self):
        """ Getter for user attribute """

        return self.user


    def get_songs(self):
        """ Getter for songs attribute """

        return self.songs


    def __str__(self):
        """
        String representation of a Playlist
        """
        return "Playlist " + "'" + self.title + "'" +\
         " by " + self.user + " has " + str(len(self.songs)) + " songs"


    def add_song(self, song):
        """
        Adds song to list
        returns True if successful
        returns False if song is already included in playlist
        """
        cond = song in self.songs
        if cond == False:
            self.songs.append(song)
        return not cond


    def remove_song(self, song):
        """
        Removes a song from the list
        returns True if successful
        returns False if song is not in the playlist
        """
        cond = song in self.songs
        assert cond == True
        if cond == True:
            self.songs.remove(song)
        return cond


    def sort_songs(self, sort_by):
        """
        Sorts the songs by the sort_by attribute in ascending order
        """
        assert isinstance(sort_by, str)

        if sort_by == "length":
            self.songs = sorted(self.songs, key = lambda x: x.length)
        elif sort_by == "name":
            self.songs = sorted(self.songs, key = lambda x: x.name) 
        elif sort_by == "streams":
            self.songs = sorted(self.songs, key = lambda x: x.streams)
        elif sort_by == "artist":
            self.songs = sorted(self.songs, key = lambda x: x.artist) 
        elif sort_by == "album":
            self.songs = sorted(self.songs, key = lambda x: x.album)


    def get_total_streams(self):
        """
        Returns the total amount of streams of the songs in the playlist
        """
        return sum([song.get_streams() for song in self.songs])


    def get_total_length(self):
        """
        Returns the total length of the playlist
        """
        return sum([song.get_length() for song in self.songs])


    def play(self):
        """
        Plays every song in the playlist.
        Returns a string that contains information on all the songs played.
        If the playlist is empty, returns "Empty"
        """
        if len(self.songs) == 0:
            return "Empty"
        final = ""
        for song in self.songs:
            final += song.listen()
            final += "\n" 
        return final [0:-1]


    def combine_playlists(self, other_playlist):
        """
        Adds all songs from other_playlist to current playlist.
        If all songs were added successfully, return True. 
        If not, return the number of songs that weren't added.
        """
        temp = self.songs
        self.songs = list(set([*self.songs, *other_playlist.songs]))
        return  True if len(temp) + len(other_playlist.songs) - \
        len(self.songs) == 0 else len(temp) \
        + len(other_playlist.songs) - len(self.songs)
    

    def get_most_played_song(self):
        """
        Returns the name of the most played song
        """
        if len(self.songs) == 0:
            return ""
        a = 0
        b = 0
        for s in range(len(self.songs)):
            song = self.songs[s]
            if song.get_streams() >= a:
                a = song.get_streams()
                b = s
        return self.songs[b].get_name()
