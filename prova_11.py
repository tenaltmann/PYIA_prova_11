class Animal:
    def falar(self):
        print("Este animal faz um som genérico !")
        return
    
class Cachorro:
    def falar(self):
        print("O cachorro está latindo !")
        return
    
class Gato:
    def falar(self):
        print("O Gato está Miando !")
        return    
    

animal = Animal()
cachorro = Cachorro()
gato = Gato()


animal.falar()
