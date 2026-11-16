
class Eleicao:

    def __init__(self):
        self.presidente = {}
        self.governador = {}
        self.senador = {}



    def voto_senador (self, voto):
        voto = str(voto)
        if len (voto) == 2 and voto.isdigit():
            self.senador [voto] = self.senador.get (voto, 0) +1
            print(f"Total de votos {votos} : {self.senador[voto]}")
            return True
        else:
            print("Número inválido")
            return False

    def voto_presidente(self, voto):
        voto = str(voto)
        if len(voto) == 2 and voto.isdigit():
            self.presidente[voto] = self.presidente.get(voto, 0) + 1
            print(f"Total de votos do candidato {voto}: {self.presidente[voto]}")
            return True
        else:
            print("Número inválido")
            return False

    def voto_governador(self, voto):
        voto = str(voto)
        if len(voto) == 2 and voto.isdigit():
            self.governador [voto] = self.governador.get(voto,0) +1
            print(f"Total de votos candidato {voto}: {self.governador[voto]}")
            return True
        else:
            print("Número inválido")
            return False




urna = Eleicao()

urna.voto_presidente(13)
urna.voto_presidente(22)
urna.voto_presidente(13)
urna.voto_governador(13)
urna.voto_governador(22)
urna.voto_senador(123)
urna.voto_senador(123)

print(urna.presidente)
