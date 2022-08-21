from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Dict
from src.playlist import Playlist
from src.musica import Musica


class IComando(ABC):
    """ Interface de comandos para a interface do reprodutor"""

    def __init__(self, playlist: Playlist) -> None:
        self.playlist: Playlist = playlist

    @abstractmethod
    def executar(self) -> None: pass


class PassarMusica(IComando):
    """
    Classe responsável pelo comando de passar música.

    Atributos:
    playlist (Playlist): Objeto responsável pela playlist.
    """

    def executar(self) -> None:
        self.playlist.passar_musica()


class VoltarMusica(IComando):
    """
    Classe responsável pelo comando de voltar música.

    Atributos:
    playlist (Playlist): Objeto responsável pela playlist.
    """

    def executar(self) -> None:
        self.playlist.voltar_musica()


class PausarMusica(IComando):
    """
    Classe responsável pelo comando de pausar música.

    Atributos:
    playlist (Playlist): Objeto responsável pela playlist.
    """

    def executar(self) -> None:
        Musica.pausar()


class ExibirMusicaAtual(IComando):
    """
    Classe responsável por exibir música(praticamente abstrata, pois tem apenas a função de ter o
    objeto Playlist armazenado).

    Atributos:
    playlist (Playlist): Objeto responsável pela playlist.
    """

    def executar(self) -> None:
        pass


class DespausarMusica(IComando):
    """
    Classe responsável pelo comando de despausar música.

    Atributos:
    playlist (Playlist): Objeto responsável pela playlist.
    """

    def executar(self) -> None:
        Musica.despausar()


class InterfaceReprodutor:
    """
    Classe que atua como 'Invoker'(padrão Command) sendo responsável por chamar os comandos quando requisitados
    pelo reprodutor.

    Atributos:
    comandos (Dict): Dicionário de comandos que ela vai chamar quando for necessitado pelo reprodutor. (dicionário
    de objetos de Comandos).
    """

    def __init__(self) -> None:
        self.comandos: Dict[str, IComando] = {}

    def adicionar_comando(self, nome: str, comando: IComando) -> None:
        """
        Método responsável por adicionar comando a interface do reprodutor.

        :param nome: Nome do comando que vai ser usado para chamar o comando respectivo cadastrado.
        :rtype: str
        :param comando: Comando que será executado ao chamar o mesmo.
        :rtype: IComando
        :return: None
        :rtype: None
        """
        self.comandos[nome] = comando

    def executar_comando(self, nome: str) -> None:
        """
        Método responsável por executar o comando que foi chamado, caso não exista, não será executado nada.

        :param nome: Nome do comando que vai ser utilizado (o mesmo precisa ter sido cadastrado anteriormente).
        :rtype nome: str
        :return: None
        :rtype: None
        """
        if nome not in self.comandos:
            return

        self.comandos[nome].executar()

    def musica_atual(self) -> str:
        """
        Método responsável apenas por retornar o nome dá música que está tocando no momento exato.

        :return: Retorna o nome da música em execução.
        :rtype: str
        """
        return self.comandos['musica_atual'].playlist.musica_atual()
