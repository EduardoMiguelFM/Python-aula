class Carro(): 

    def __init__(self):
        self.ligado = False
        self.marca = "Generica"
        self.modelo = "X"
        self.velocidade = 0

    

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

    def situacao(self):
        texto = "Ligado" if self.ligado else "Desligado"
        print(f"O carro{self.modelo} da {self.marca} esta {texto} viajando a {self.velocidade} por hora" ,texto)

    def acelerar(self):
        if self.ligado:
            self.velocidade = self.velocidade + 5
            print(f"Acelerando para {self.velocidade} km/hora")
        else: 
            print("O carro precisa estar ligado para acelerar!")


def main():
    c1= Carro()
    c2= Carro()
    c3= Carro()

    c1.marca = "Fiat"
    c1.modelo = " Mobly"
    
    c2.marca = "Honda"
    c2.modelo = " City"

    c3.marca = "Renault"
    c3.modelo = " Kwid"

    c2.ligar()
    c2.acelerar()
    c2.acelerar()

    # c1.situacao()
    # c2.situacao()
    # c3.situacao()

if __name__ == "__main__":
    main()