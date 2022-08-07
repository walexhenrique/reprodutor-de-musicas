import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.QtWidgets import QWidget, QGridLayout, QLineEdit, QSizePolicy
from playlist import Playlist
from musica import Musica


class Reprodutor(QMainWindow):
    def __init__(self, parent=None):
        self.playlist = Playlist()
        super().__init__(parent)
        self.setWindowTitle('Reprodutor Musical')

        self.setFixedSize(400, 400)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)
        self.cw.setStyleSheet("background-color: #D8BFD8;")

        self.display = QLineEdit()
        self.display.setStyleSheet(
            "color: white; background-color: grey; border:0; font-size: 16px;")
        self.grid.addWidget(self.display, 0, 0, 1, 4)

        self.add_botao(QPushButton('<'), 1, 0, 1, 1, self.voltar_musica,
                       "background-color: #9370DB; color: white; font-size: 50px;")
        self.add_botao(QPushButton('||'), 1, 1, 1, 1, self.pausar_musica,
                       "background-color: #9400D3; color: white; font-size: 50px")
        self.add_botao(QPushButton('|>'), 1, 2, 1, 1, self.despausar_musica,
                       "background-color: #9400D3; color: white; font-size: 50px")
        self.add_botao(QPushButton('>'), 1, 3, 1, 1, self.passar_musica,
                       "background-color: #9370DB; color: white; font-size: 50px;")

        self.display.setDisabled(True)

        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        self.setCentralWidget(self.cw)

    def add_botao(self, botao, linha, coluna, linha_tamanho, coluna_tamanho, funcao=None, style=None):
        self.grid.addWidget(botao, linha, coluna, linha_tamanho, coluna_tamanho)
        botao.clicked.connect(funcao)
        botao.setStyleSheet(style)
        botao.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

    def passar_musica(self):
        self.display.setText(f'Tocando a música {self.playlist.musica_atual()}')
        self.playlist.passar_musica()

    def voltar_musica(self):
        self.display.setText(f'Tocando a música {self.playlist.musica_atual()}')
        self.playlist.voltar_musica()

    def pausar_musica(self):
        if self.display.text():
            self.display.setText(f'A música foi pausada')
        Musica.pause()

    def despausar_musica(self):
        if self.display.text():
            self.display.setText(f'A música foi despausada')
        Musica.despausar()


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    rep = Reprodutor()
    rep.show()
    qt.exec_()
