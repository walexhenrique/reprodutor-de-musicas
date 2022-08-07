from pygame import mixer


class Musica:
    def __init__(self, endereco, nome):
        self.endereco = endereco
        self.nome = nome

    def load_music(self):
        mixer.music.load(self.endereco)

    @staticmethod
    def play():
        mixer.music.play()

    @staticmethod
    def pause():
        mixer.music.pause()

    @staticmethod
    def despausar():
        mixer.music.unpause()
