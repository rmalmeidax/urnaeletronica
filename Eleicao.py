
class Eleicao:

    def __init__(self):
        self.presidente = {}
        self.governador = {}
        self.senador = {}
        self.dep_federal = {}
        self.dep_estadual = {}

    def voto_dep_estadual(self, voto):
         voto = str(voto)
         if len (voto)== 5 and voto.isdigit():
            self.dep_estadual[voto] = self.dep_estadual(voto,0)+1
            print (f"Total de votos {voto} : {self.dep_estadual[voto]}")
            return True
         else:
            print("Número, inválido")
            return False

    def voto_dep_federal(self,voto):
        voto =str(voto)
        if len(voto) == 4 and voto.isdigit():
            self.dep_federal[voto] = self.dep_federal(voto,0)+1
            print(f"Total de votos {votos}: {self.dep_federal[voto]}")
            return True
        else:
            print("Número invalido")
            return False

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
        lista = ["13", "12", "11", "22"]
        if len(voto) == 2 and voto.isdigit():
            if voto in lista:
                self.presidente[voto] = self.presidente.get(voto, 0) + 1
                print(f"Total de votos do candidato {voto}: {self.presidente[voto]}")
                return True
            else:
                print (f"Candidato não encontrado {voto} ")
        else:
            print(f"Número inválido {voto}")
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
