from ventana import Ventana
if __name__=='__main__':
    print('=== Ventana Inicio ===')
    ventanaInicio=Ventana('Inicio')
    ventanaInicio.mostrar()
    print('Ventana: {} Alto: {} Ancho: {}'.format(ventanaInicio.getTitulo(),ventanaInicio.alto(),ventanaInicio.ancho()))
    print('')
    print('=== Ventana Carga ===')
    ventanaCargar=Ventana('Cargar',10,20)
    ventanaCargar.mostrar()
    
    print('=== Mueve a la Derecha en 10 unidades ===')
    ventanaCargar.moverDerecha(10)
    ventanaCargar.mostrar()
    
    print('*** Mueve a la izquierda en 10 unidades ***')
    ventanaCargar.moverIzquierda(10)
    ventanaCargar.mostrar()

    print('*** Bajar en 10 unidades ***')
    ventanaCargar.bajar(10)
    ventanaCargar.mostrar()
    print('')
    print('=== Ventana Borrar ===')
    ventanaBorrar=Ventana('Borrar',10,20,100,200)
    ventanaBorrar.mostrar()
    
    print('=== Subir en 5 unidades ===')
    ventanaBorrar.subir(5)
    ventanaBorrar.mostrar()
    
    print('*** Subir sin unidades ***')

    ventanaBorrar.subir()

    ventanaBorrar.mostrar()

    print('*** Bajar sin unidades  ***')

    ventanaBorrar.bajar()

    ventanaBorrar.mostrar()

    opcion = input("")