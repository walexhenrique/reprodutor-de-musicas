from pygame import mixer


class Musica:
    """
    Classe responsável por abstrair os comandos do Pygame e salvar as músicas que serão reproduzidas
    pela classe Playlist.

    Atributos:
    endereco (str): Endereço completo(a partir da raiz do projeto) de onde se localiza a música.
    nome (str): Nome da música.
    """

    def __init__(self, endereco: str, nome: str) -> None:
        self.endereco: str = endereco
        self.nome: str = nome

    def load_music(self) -> None:
        """
        Método responsável por carregar a música no Pygame.
        :return: None
        :rtype: None
        """
        mixer.music.load(self.endereco)
        mixer.music.set_volume(0.5)

    @staticmethod
    def play() -> None:
        """
        Método responsável por tocar a música.
        :return: None
        :rtype: None
        """
        mixer.music.play()

    @staticmethod
    def pausar() -> None:
        """
        Método responsável por pausar a música.
        :return: None
        :rtype: None
        """
        mixer.music.pause()

    @staticmethod
    def despausar() -> None:
        """
        Método responsável por despausar a música.
        :return: None
        :rtype: None
        """
        mixer.music.unpause()
