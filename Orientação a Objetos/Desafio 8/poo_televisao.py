"""
8 - Crie uma classe "Televisao" e uma classe "ControleRemoto" que possa controlar o volume e trocar os canais da
televisão.
    - O contole do volume permite aumentar ou diminuir a potência do volume de som em uma unidade de cada vez;
    - O controle do canal também permite aumentar e diminuir o número do canal em uma unidade, porém, também possibilita
trocar para um canal indicado;
    - Também devem existir métodos para consultar o valor do volume de som e o canal selecionado.
"""


class Televisao:

    def __init__(self):
        self.__canal = 1
        self.__volume = 0

    # Get - "canal".
    @property
    def canal(self):
        return self.__canal

    # Set - "canal".
    @canal.setter
    def canal(self, novo_canal):
        self.__canal = novo_canal

    # Get - "volume".
    @property
    def volume(self):
        return self.__volume

    # Set - "volume".
    @volume.setter
    def volume(self, novo_volume):
        self.__volume = novo_volume

    def mostrar_canal(self):
        print(f' O canal atual é {self.canal}.')

    def mostrar_volume(self):
        print(f' O volume atual é {self.volume}.')


class ControleRemoto:
    televisao1 = Televisao

    def aumentar_volume(self):
        if televisao1.volume < 99:
            televisao1.volume = televisao1.volume + 1

    def diminuir_volume(self):
        if televisao1.volume > 0:
            televisao1.volume = televisao1.volume - 1

    def aumentar_canal(self):
        if televisao1.canal < 999:
            televisao1.canal = televisao1.canal + 1

    def diminuir_canal(self):
        if televisao1.canal > 1:
            televisao1.canal = televisao1.canal - 1

    def escolher_canal(self, novo_canal):
        if 0 < novo_canal < 1000:
            televisao1.canal = novo_canal


# Testando:
televisao1 = Televisao()
controle1 = ControleRemoto()

controle1.aumentar_volume()  # volume 1
controle1.aumentar_volume()  # volume 2
controle1.aumentar_volume()  # volume 3

televisao1.mostrar_volume()  # OUTPUT: 3

controle1.diminuir_volume()  # volume 2

televisao1.mostrar_volume()  # OUTPUT: 2

controle1.aumentar_canal()  # canal 2
controle1.aumentar_canal()  # canal 3

televisao1.mostrar_canal()  # OUTPUT: 3

controle1.diminuir_canal()  # canal 2
controle1.diminuir_canal()  # canal 1
controle1.diminuir_canal()  # canal 1
controle1.diminuir_canal()  # canal 1

televisao1.mostrar_canal()  # OUTPUT: 1

controle1.escolher_canal(595)  # canal 595

televisao1.mostrar_canal()  # OUTPUT: 595
