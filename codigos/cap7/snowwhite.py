class Personagem:
    def __init__(self, nome):
        self.nome = nome
    
    def falar(self):
        print(f"Oi, Meu nome é {self.nome}")
        input()
    
    def cantar(self):
        print(f"{self.nome} Cantando uma canção na floresta!")
        input()


class Anao(Personagem):
    def __init__(self, nome, altura):
        super().__init__(nome)
        self.altura = altura
    
    def cantar(self):
        print(f"({self.nome}) Eu vou, eu vou, pra casa agora eu vou...")
        input()


if __name__ == "__main__":
    # criando os personagens
    branca_de_neve = Personagem("Branca de Neve")
    bruxa = Personagem("Bruxa Má")
    zangado = Anao("Zangado", 1.3)
    dunga = Anao("Dunga", 1.4)
    mestre = Anao("Mestre", 1.5)
    soneca = Anao("Soneca", 1.3)
    atchim = Anao("Atchim", 1.4)
    dengoso = Anao("Dengoso", 1.5)
    feliz = Anao("Feliz", 1.4)

    personagens = [branca_de_neve, bruxa, zangado, dunga]
    anoes = [mestre, soneca, atchim, dengoso, feliz]

    # usando mecanismo de herança (reutilização de código)
    for p in personagens:
        p.cantar()


    # for a in anoes:
    #     a.cantar()