import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.QtWidgets import QWidget, QGridLayout, QLineEdit, QSizePolicy
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
from src.playlist import Playlist
from src.comandos import InterfaceReprodutor, PassarMusica, VoltarMusica, PausarMusica, DespausarMusica, \
    ExibirMusicaAtual
from typing import Callable


class Reprodutor(QMainWindow):
    """
    Classe responsável pelo funcionamento do reprodutor(GUI) e será essa que o Usuário vai instanciar para utilizar

    Atributos:
    interface_reprodutor (InterfaceReprodutor): Objeto responsável pela funcionalidade dos botões. Ela faz a ligação ao
    'back-end', porém abstrai os comandos para o Reprodutor.
    cw, grid, display: Atributos necessários para o funcionamento do PyQt5.
    """

    def __init__(self, playlist: Playlist, parent=None) -> None:
        super().__init__(parent)

        # Configurando os comandos respectivos a cada botão
        self.interface_reprodutor: InterfaceReprodutor = InterfaceReprodutor()
        passar_musica = PassarMusica(playlist)
        voltar_musica = VoltarMusica(playlist)
        pausar_musica = PausarMusica(playlist)
        despausar_musica = DespausarMusica(playlist)
        musica_atual = ExibirMusicaAtual(playlist)
        self.interface_reprodutor.adicionar_comando('passar_musica', passar_musica)
        self.interface_reprodutor.adicionar_comando('voltar_musica', voltar_musica)
        self.interface_reprodutor.adicionar_comando('pausar_musica', pausar_musica)
        self.interface_reprodutor.adicionar_comando('despausar_musica', despausar_musica)
        self.interface_reprodutor.adicionar_comando('musica_atual', musica_atual)

        # Realizando as configurações do PyQt5
        self.setWindowTitle('Repr. Musical')
        self.setWindowIcon(QIcon('imgs/icon.png'))
        self.setFixedSize(400, 400)
        self.cw: QWidget = QWidget()
        self.grid: QGridLayout = QGridLayout(self.cw)
        self.cw.setStyleSheet("background-color: black;")

        self.display: QLineEdit = QLineEdit()

        # Adicionando os botões do reprodutor de música e terminando de realizar as últimas configurações
        self.display.setStyleSheet(
            "color: white; background-color: black; padding-left: 10px; font-size: 13px; border-color: #00f;"
            " font-family: sans-serif; ")
        self.grid.addWidget(self.display, 0, 0, 1, 4)

        self.add_botao(QPushButton(), 1, 0, 1, 1, self.voltar_musica,
                       "background-color: white; color: white;", 'imgs/voltar.png')
        self.add_botao(QPushButton(), 1, 1, 1, 1, self.pausar_musica,
                       "background-color: white; color: white;", 'imgs/pausar.png')
        self.add_botao(QPushButton(), 1, 2, 1, 1, self.despausar_musica,
                       "background-color: white; color: white;", 'imgs/play.png')
        self.add_botao(QPushButton(), 1, 3, 1, 1, self.passar_musica,
                       "background-color: white; color: white;", 'imgs/passar.png')

        self.display.setDisabled(True)

        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        self.setCentralWidget(self.cw)

    def add_botao(self, botao: QPushButton, linha: int, coluna: int, linha_tamanho: int, coluna_tamanho: int,
                  funcao: Callable = None, style: str = None, endereco_icon: str = None) -> None:
        """
        Método interno responsável por adicionar um botão no reprodutor.

        :param botao: Objeto botão a ser adicionado.
        :type botao: QPushButton
        :param linha: Indice da linha a ser colocado.
        :type linha: int
        :param coluna: Indice da coluna a ser colocado.
        :type coluna: int
        :param linha_tamanho: Quantas linhas o botão ocupará no reprodutor.
        :type linha_tamanho: int
        :param coluna_tamanho: Quantas colunas o botão ocupará no reprodutor.
        :type coluna_tamanho: int
        :param funcao: Função específica que será utilizada ao pressionar o botão.
        :type funcao: Callable
        :param style: Estilização css do botão.
        :type style: str
        :param endereco_icon: Endereço do icon para adicionar no botão.
        :type endereco_icon: str
        :return: None
        :rtype: None
        """
        self.grid.addWidget(botao, linha, coluna, linha_tamanho, coluna_tamanho)
        botao.clicked.connect(funcao)
        botao.setStyleSheet(style)
        botao.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        botao.setIcon(QIcon(endereco_icon))
        botao.setIconSize(QSize(50, 50))

    def passar_musica(self) -> None:
        """
        Método responsável por passar a música ao pressionar o botão respectivo e apresentar a música atual.
        :return: None
        :rtype: None
        """

        self.interface_reprodutor.executar_comando('passar_musica')
        self.display.setText(f'{self.interface_reprodutor.musica_atual()}, status = TOCANDO')

    def voltar_musica(self) -> None:
        """
        Método responsável por voltar a música ao pressionar o botão respectivo e apresentar a música atual.
        :return: None
        :rtype: None
        """
        self.interface_reprodutor.executar_comando('voltar_musica')
        self.display.setText(f'{self.interface_reprodutor.musica_atual()}, status = TOCANDO')

    def pausar_musica(self) -> None:
        """
        Método responsável por pausar a música ao pressionar o botão respectivo e apresentar a música atual.
        :return: None
        :rtype: None
        """
        self.interface_reprodutor.executar_comando('pausar_musica')
        if self.display.text():
            self.display.setText(f'{self.display.text()[:-7]}PAUSADO')

    def despausar_musica(self) -> None:
        """
        Método responsável por despausar a música ao pressionar o botão respectivo e apresentar a música atual.
        caso seja a primeira música ao abrir o reprodutor, ela tocará a primeira música da playlist.
        :return: None
        :rtype: None
        """
        if not self.display.text():
            self.passar_musica()
            return

        self.interface_reprodutor.executar_comando('despausar_musica')
        self.display.setText(f'{self.display.text()[:-7]}TOCANDO')


if __name__ == '__main__':
    # Código a ser executado para o funcionamento do programa.
    qt = QApplication(sys.argv)
    playlist = Playlist()
    rep = Reprodutor(playlist)
    rep.show()
    qt.exec_()
