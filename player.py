from mutagen import *
from model import *
from mutagen.mp3 import *
from os import *
from tkinter import filedialog
from pygame.mixer import *

class Player:
    def __init__(self):
        init()
        self.my_model=Model()

    def get_db_status(self):
        return self.my_model.get_db_status()

    def close_player(self):
        music.stop()
        self.my_model.close_db_connection()

    def set_volume(self,volume_level):
        music.set_volume(volume_level)

    def add_song(self):
        song_path=filedialog.askopenfilename(title="Select your song. . .",filetypes=[("mp3 files",".mp3")])
        if song_path=="":
            return
        song_name=path.basename(song_path)
        self.my_model.add_song(song_name,song_path)
        return song_name

    def remove_song(self,song_name):
        self.my_model.remove_song(song_name)

    def get_song_length(self,song_name):
        self.song_path=self.my_model.get_song_path(song_name)
        self.audio_tag= MP3(self.song_path)
        song_legth=self.audio_tag.info.length
        return song_legth

    def play_song(self):
        quit()
        init(frequency=self.audio_tag.info.sample_rate)
        music.load(self.song_path)
        music.play()

    def stop_song(self):
        music.stop()

    def pause_song(self):
        music.pause()

    def umpause_song(self):
        music.unpause()

    def add_song_to_favourites(self,song_name):
        song_path=self.my_model.get_song_path(song_name)
        result=self.my_model.add_song_to_favourites(song_name,song_path)
        return result

    def load_song_from_favourite(self):
        result=self.my_model.load_songs_from_favourites()
        return result,self.my_model.song_dict

    def remove_songs_from_favourites(self,song_name):
        result=self.my_model.remove_song_from_favourites(song_name)
        return result

    def get_song_count(self):
        return self.my_model.get_song_count()

