import os
import pygame
from musica import Musica


class Playlist:
    def __init__(self):
        self.musicas = []
        self.musica_tocando = 0
        self.caminho_musicas = r'./músicas/'
        pygame.mixer.init()
        if not os.path.isdir(self.caminho_musicas):
            os.mkdir(self.caminho_musicas)
        self.encontrar_musicas()

    def encontrar_musicas(self):
        for raiz, pastas, files in os.walk(self.caminho_musicas):
            for file in files:
                caminho_completo = os.path.join(raiz, file)
                arquivo, exe = os.path.splitext(file)
                if exe != '.mp3':
                    continue

                self._adicionar_musica(caminho_completo, arquivo)

    def _adicionar_musica(self, endereco, nome):
        self.musicas.append(Musica(endereco, nome))

    def musica_atual(self):
        return self.musicas[self.musica_tocando].nome

    def passar_musica(self):
        self.musicas[self.musica_tocando].load_music()
        Musica.play()

        self.musica_tocando += 1
        if self.musica_tocando >= len(self.musicas):
            self.musica_tocando = 0

    def voltar_musica(self):
        self.musicas[self.musica_tocando].load_music()
        Musica.play()
        self.musica_tocando -= 1
        if self.musica_tocando <= 0:
            self.musica_tocando = len(self.musicas) - 1
