import os
import pygame
from src.musica import Musica
from typing import List


class Playlist:
    """
    Classe responsável por gerenciar o funcionamento do reprodutor de música, sendo: passar, voltar e exibir músicas
    e atua na armazenamento nos endereços das músicas que serão tocadas.

    Atributos:
    musicas (list): Lista de objetos Música, no qual está armazena o endereço(caminho/diretorio) da mesma.
    musica_tocando (int): Indice da música que está tocando atualmente pela classe.
    caminho_musicas (str): Pasta que será procurado as músicas para serem adicionadas no reprodutor.
    """

    def __init__(self) -> None:
        # Iniciando variáveis internas necessárias.
        self.musicas: List[Musica] = []
        self.musica_tocando: int = -1
        self.caminho_musicas: str = r'./musicas/'
        pygame.mixer.init()

        # Caso não tenha uma pasta chamada músicas, será criada para o usuário adicionar suas músicas.
        if not os.path.isdir(self.caminho_musicas):
            os.mkdir(self.caminho_musicas)
        self.encontrar_musicas()

    def encontrar_musicas(self) -> None:
        """
        Método responsável por encontrar as músicas da pasta ./músicas/ ela apenas vai usar os arquivos
        com extensão .mp3, outros arquivos serão ignorados.
        :return: None
        :rtype: None
        """
        for raiz, pastas, files in os.walk(self.caminho_musicas):
            for file in files:
                caminho_completo = os.path.join(raiz, file)
                arquivo, exe = os.path.splitext(file)
                if exe != '.mp3':
                    continue

                self._adicionar_musica(caminho_completo, arquivo)

    def _adicionar_musica(self, endereco: str, nome: str) -> None:
        """
        Método interno responsável por adicionar música a lista de músicas da playlist.
        :param endereco: Endereço de pasta a partir da raiz(pasta raiz do projeto).
        :type endereco: str
        :param nome: Nome da música.
        :type nome: str
        :return: None
        :rtype: None
        """
        self.musicas.append(Musica(endereco, nome))

    def musica_atual(self) -> str:
        """
        Método responsável por retornar o nome da música que está em reprodução atualmente.
        :return: Nome da música que está tocando.
        :rtype: str
        """
        return self.musicas[self.musica_tocando].nome

    def passar_musica(self) -> None:
        """
        Método responsável por tocar a próxima música da lista e caso chegue ao final da lista,
        volta para a primeira música da playlist.
        :return: None
        :rtype: None
        """
        self.musica_tocando += 1
        if self.musica_tocando >= len(self.musicas):
            self.musica_tocando = 0
        self.musicas[self.musica_tocando].load_music()
        Musica.play()

    def voltar_musica(self) -> None:
        """
        Método responsável por tocar a música anterior da lista e caso chegue a primeira música da lista,
        vai para a última música da playlist.
        :return: None
        :rtype: None
        """
        self.musica_tocando -= 1
        if self.musica_tocando < 0:
            self.musica_tocando = len(self.musicas) - 1
        self.musicas[self.musica_tocando].load_music()
        Musica.play()

