class Personagem:
    def __init__(self, nome):
        self.nome = nome
    
    def falar(self):
        print(f"Meu nome é {self.nome}")

class BrancaDeNeve(Personagem):
    def __init__(self, nome, sobrenome):
        super().__init__(nome)
        self.sobrenome = sobrenome
    
    def cantar(self):
        print(f"Aprenda uma canção com a {self.nome} {self.sobrenome}")


class Anao(Personagem):
    def __init__(self, nome, altura):
        super().__init__(nome)
        self.altura = altura
    
    def cantar(self):
        print("Eu vou, eu vou, pra casa agora eu vou...")
    
    def trabalhar(self):
        print(f"{self.nome} trabalhando...")



class Bruxa(Personagem):
    def __init__(self, nome, sobrenome):
        super().__init__(nome)
        self.sobrenome = sobrenome

    def cantar(self):
        print(f"Quem é mais bela do que {self.nome} {self.sobrenome}")


if __name__ == "__main__":
    # criando os personagens
    branca_de_neve = BrancaDeNeve("Branca", "de Neve")
    bruxa = Bruxa("Bruxa", "Má")
    zangado = Anao("Zangado", 1.3)
    dunga = Anao("Dunga", 1.4)
    mestre = Anao("Mestre", 1.5)
    soneca = Anao("Soneca", 1.3)
    atchim = Anao("Atchim", 1.4)
    dengoso = Anao("Dengoso", 1.5)
    feliz = Anao("Feliz", 1.4)

    personagens = [branca_de_neve, bruxa]
    anoes = [zangado, dunga, mestre, soneca, atchim, dengoso, feliz]

    # usando mecanismo de herança (reutilização de código)
    for p in personagens:
        p.falar()

    # usando herança a partir da classe filha
    for p in personagens:
        p.cantar()

    feliz.cantar()

    for a in anoes:
        a.trabalhar()