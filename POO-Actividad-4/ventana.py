class Ventana:
    #Atributos
    __titulo = ''
    __verSupIzqX = 0
    __verSupIzqY  =0
    __verInfDerX = 500
    __verInfDerY =500

    #Metodos
    def __init__(self,titulo='',vsix=0,vsiy=0,vidx=500,vidy=500):
        self.__titulo = titulo
        self.__verSupIzqX = vsix
        self.__verSupIzqY = vsiy
        self.__verInfDerX = vidx
        self.__verInfDerY = vidy
     
    def getTitulo(self):
         return self.__titulo
    

    def mostrar(self):
        print('Valor de las Coordenadas x=',self.__verSupIzqX,' e y=',self.__verSupIzqY,' del vértice superior izquierdo')
        print('Valor de las Coordenadas x=',self.__verInfDerX,' e y=',self.__verInfDerY,' del vértice inferior derecho')

    def alto(self):
        return  (self.__verSupIzqY + self.__verInfDerY)

    def ancho(self):
        return (self.__verSupIzqX + self.__verInfDerX)

    def moverDerecha(self,x=0):
        if(x>0):
            xau=self.__verInfDerX+x
            if xau <= 500 :
                self.__verInfDerX=xau
                xau=self.__verSupIzqX+x
                self.__verSupIzqX=xau
            else:
                print('Imposible Mover a la DERECHA ',x,' Unidades')
                print('=== ++++++++++ ===')
        else:
                print('Imposible Mover a la DERECHA 0 Unidades')
                print('=== ++++++++++ ===')
            
    def moverIzquierda(self,x=0):
        if(x>0):
            xau=self.__verSupIzqX-x
            if xau >= 0 :
                self.__verSupIzqX=xau
                xau=self.__verInfDerX-x
                self.__verInfDerX=xau
            else:
                print('Imposible Mover a la IZQUIERDA ',x,' Unidades')
                print('=== ++++++++++ ===')
        else:
            print('Imposible Mover a la IZQUIERDA 0 Unidades')
            print('=== ++++++++++ ===')
            
    def bajar(self,y=0):
        if(y>0):
            yau=self.__verInfDerY+y
            if (yau <= 500) :
                self.__verInfDerY=yau
                yau=self.__verInfDerY+y
                self.__verInfDerY=yau
            else:
                print('Imposible BAJAR ',y,' Unidades')
                print('=== ++++++++++ ===')
        else:
            print('Imposible BAJAR 0 Unidades')
            print('=== ++++++++++ ===')
            
    def subir(self,y=0):
        if(y>0):
            yau=self.__verSupIzqY-y
            if (yau >= 0) :
                self.__verSupIzqY=yau
                yau=self.__verInfDerY-y
                self.__verInfDerY=yau
            else:
                print('Imposible SUBIR ',y,' Unidades')
                print('=== ++++++++++ ===')
        else:
            print('Imposible SUBIR 0 Unidades')
            print('=== ++++++++++ ===')
        
        

