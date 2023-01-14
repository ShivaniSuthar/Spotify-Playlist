"""
DSC 20 Homework 07
Name: Shivani Suthar
PID:  A16138767
"""

def doctests_go_here():
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


    # Add your doctests below here #

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
    # TODO: Initialize class attribute
    platform = "Spotify"

    def __init__(self, name, length, album, artist, streams):
        """
        Constructor of Song

        Parameters:
        name (str): name of the song
        length (float): song duration in minutes
        album (str): name of album the song is in
        artist (str): name of artist
        streams (int): number of times the song has been streamed
        """
        # YOUR CODE STARTS HERE #

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
        # YOUR CODE STARTS HERE #

        return self.name 


    def get_length(self):
        """ Getter for length attribute """
        # YOUR CODE STARTS HERE #

        return self.length 


    def get_album(self):
        """ Getter for album attribute """
        # YOUR CODE STARTS HERE #

        return self.album


    def get_artist(self):
        """ Getter for artist attribute """
        # YOUR CODE STARTS HERE #

        return self.artist


    def get_streams(self):
        """ Getter for streams attribute """
        # YOUR CODE STARTS HERE #

        return self.streams


    def __str__(self):
        """
        String representation of Song
        """
        # YOUR CODE STARTS HERE #

        return  "'" + self.name + "'" + " by " +\
         self.artist + " on " + "'" + self.album + "'" + " is "\
         + str(self.length) + " minutes long with " +\
          str(self.streams) + " streams"


    def listen(self):
        """
        Listens to the song, increasing the stream counter.
        Returns a string with the song name and artist
        """
        # YOUR CODE STARTS HERE #

        self.streams = self.streams + 1
        return "Listening to " + "'" + self.name + "'" + " by " + self.artist


    def add_to_playlist(self, playlist):
        """
        Takes a Playlist object and adds the current Song instance into it.
        return True if successful
        return False if song is already included in playlist
        """
        # YOUR CODE STARTS HERE #

        return playlist.add_song(self)


class Playlist:
    """
    Implementation of a playlist
    """

    def __init__(self, title, user):
        """
        Constructor of Playlist

        Parameters:
        title (str): title of the playlist
        user (str): username of user who created playlist

        Attributes:
        songs (list): list used to store songs in playlist
        """
        # YOUR CODE STARTS HERE #

        self.title = title
        self.user = user
        self.songs = []

        assert isinstance(title, str)
        assert len(title) > 0 
        assert isinstance(user, str)
        assert len(user) > 0



    def get_title(self):
        """ Getter for title attribute """
        # YOUR CODE STARTS HERE #

        return self.title


    def get_user(self):
        """ Getter for user attribute """
        # YOUR CODE STARTS HERE #

        return self.user


    def get_songs(self):
        """ Getter for songs attribute """
        # YOUR CODE STARTS HERE #

        return self.songs


    def __str__(self):
        """
        String representation of Playlist
        """
        # YOUR CODE STARTS HERE #

        return "Playlist " + "'" + self.title + "'" +\
         " by " + self.user + " has " + str(len(self.songs)) + " songs"


    def add_song(self, song):
        """
        Adds song to list
        return True if successful
        return False if song is already included in playlist
        """
        # YOUR CODE STARTS HERE #

        cond = song in self.songs
        if cond == False:
            self.songs.append(song)
        return not cond


    def remove_song(self, song):
        """
        Removes a song from the list
        return True if successful
        return False if song is not in the playlist
        """
        # YOUR CODE STARTS HERE #

        cond = song in self.songs
        assert cond == True
        if cond == True:
            self.songs.remove(song)
        return cond


    def sort_songs(self, sort_by):
        """
        Sorts the songs by the sort_by attribute in ascending order
        """
        # YOUR CODE STARTS HERE #

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
        # YOUR CODE STARTS HERE #

        return sum([song.get_streams() for song in self.songs])


    def get_total_length(self):
        """
        Returns the total length of the playlist
        """
        # YOUR CODE STARTS HERE #

        return sum([song.get_length() for song in self.songs])


    def play(self):
        """
        Plays every song in the playlist.
        Returns a string that contains information on all the songs played.
        Format is specified in the writeup
        If the playlist is empty, return "Empty"
        """
        # YOUR CODE STARTS HERE #

        if len(self.songs) == 0:
            return "Empty"
        final = ""
        for song in self.songs:
            final += song.listen()
            final += "\n" 
        return final [0:-1]


    def combine_playlists(self, other_playlist):
        """
        Add all songs from other_playlist to current playlist.
        If all songs were added successfully, return True. 
        If not, return the number of songs that weren't added.
        """
        # YOUR CODE STARTS HERE #

        """

        second_playlist = other_playlist.songs
        my_songs = self.songs
        temp = list(set(my_songs + second_playlist))
        self.songs = temp
        if len(my_songs) + len(second_playlist) == len(temp):
            return True
        else:
            return (len(my_songs) + len(second_playlist)) - len(temp)

        """

        temp = self.songs
        self.songs = list(set([*self.songs, *other_playlist.songs]))
        return  True if len(temp) + len(other_playlist.songs) - \
        len(self.songs) == 0 else len(temp) \
        + len(other_playlist.songs) - len(self.songs)
    

    def get_most_played_song(self):
        """
        Return the name of the most played song
        """
        # YOUR CODE STARTS HERE #

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


################ RECURSION PART ##################

# Question 2.5

def type_with_number(message):
    """
    This function takes in a string as
    an input and returns a string with a series
    of integers from 1-9 where each integer 
    corresponds to each character in the input
    string according to a given cell phone
    key pad
    map_values finds the corresponding values
    for the key pad characters 

    >>> type_with_number('Welcome to Beijing!')
    '9352663086023454641'
    >>> type_with_number('I miss my laptop.')
    '40647706905278671'
    >>> type_with_number('!!??..  ,,')
    '1111110011'

    # Add your doctests below here #
    >>> type_with_number('   ')
    '000'
    >>> type_with_number('R r')
    '707'
    >>> type_with_number('P. Q,! rS')
    '710711077'

    """
    # your code is here

    def map_values(c):
        c = c.lower()
        k = [ " ",
          ",.?!",
          "abc",
          "def",
          "ghi",
          "jkl",
          "mno",
          "pqrs",
          "tuv",
          "wxyz"]
        for i in range(len(k)):
            if k[i].find(c) != -1:
                return str(i)
            
    if len(message)==0:
        return ""
    return map_values(message[0]) + type_with_number(message[1:])



# Question 3.1

def create_palindrome_v1(start, end):
    """
    Creates a palindrome of integers starting from start, ending at end
    (in the middle) All inputs are positive integers. No input validation
    required.
    Parameters: start, end (int), positive integers
    Returns: palindrome sequence (str)
    Restrictions. You should use recursion in this question.
    >>> create_palindrome_v1(1, 1)
    '1'
    >>> create_palindrome_v1(3, 5)
    '34543'
    >>> create_palindrome_v1(5, 2)
    '5432345'
    
    # Add your doctests below here #
    >>> create_palindrome_v1(1, 2)
    '121'
    >>> create_palindrome_v1(2, 1)
    '212'
    >>> create_palindrome_v1(1, 9)
    '12345678987654321'
    >>> create_palindrome_v1(9, 1)
    '98765432123456789'

    """
    # your code is here

    if start == end:
        return str(start)
    
    result = str(start)

    if start < end:
        return result + create_palindrome_v1(start+1,end) + result
      
    elif start > end:
        return result + create_palindrome_v1(start-1,end) + result 



def create_palindrome_v2(start1, end1, start2, end2):
    """
    Creates a two level palindrome of integers. The first level (outer level)
    starts from start1 and ends at end1. The second level (inner level) starts
    from start2 and end2. No input validation is required.
    Parameters: start1, end1, start2, end2 (int), positive integers
    Returns: palindrome sequence (str)
    Restrictions. You should use recursion in this question.
    >>> create_palindrome_v2(1, 1, 1, 1)
    '1_1_1'
    >>> create_palindrome_v2(2, 5, 5, 4)
    '2345_545_5432'
    >>> create_palindrome_v2(3, 1, 5, 9)
    '321_567898765_123'
    
    # Add your doctests below here #
    >>> create_palindrome_v2(1, 2, 3, 4)
    '12_343_21'
    >>> create_palindrome_v2(2, 5, 5, 2)
    '2345_5432345_5432'
    >>> create_palindrome_v2(3, 1, 5, 3)
    '321_54345_123'
    >>> create_palindrome_v2(1, 1, 5, 3)
    '1_54345_1'
    >>> create_palindrome_v2(1, 2, 5, 5)
    '12_5_21'

    """
    # your code is here

    result1 = str(start1)
    result2 = str(end1)

    if start1 == end1:
        return result1 + "_" + create_palindrome_v1(start2, end2) + "_" + result1
    
    if start1 < end1:
        return result1 + create_palindrome_v2(start1+1,end1, start2,end2) + result1
    elif start1 > end1:
        return result1 + create_palindrome_v2(start1-1,end1, start2, end2) + result1


    return result

# Question 4

def lutee_reproduction(n):
    """
    # Given a number of months,
    this function returns the 
    amount of lutee creatures at
    that month according to their
    reproductive patterns #

    >>> lutee_reproduction(1)
    2
    >>> lutee_reproduction(2)
    2
    >>> lutee_reproduction(3)
    4
    >>> lutee_reproduction(4)
    6
    >>> lutee_reproduction(6)
    16

    # Add your doctests below here #
    >>> lutee_reproduction(5)
    10
    >>> lutee_reproduction(7)
    26
    >>> lutee_reproduction(10)
    110
    """


    # your code is here

    two = 2

    if n <= two:
      return two
    return lutee_reproduction(n-1) + lutee_reproduction(n-two)
