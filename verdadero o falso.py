from pygame import *
import sys

init()

al_v = 500
an_v = 800

ventana = display.set_mode((an_v , al_v))
display.set_caption('QUIZ V/F')

fondo = (58, 232, 128)
letras = (0 , 0 , 0)
respuesta_in = (245, 73, 39)
respuesta_co = (13, 161, 87)

fuente = font.SysFont('Candara', 32 )

list = [
    ('pvz 1 se publico en 1999 ','V'),
    ('los perros cimarron cruza policia son muy inteligentes','V'),
    ('excisten diferentes razas de gatos','F'),
    ('los gatos tienen la misma temperatura corporal que los humanos normales','F'),
    ('los volcanes pueden entrar en erupcion mas de una vez ','F'),

]
indice = 0
puntuacion = 0
mostrar_f= False
f_texto = ''
tiempof = 0
fcolor = letras

clock = time.Clock()


def dibujar_txt(txt, color, x , y):
    render = fuente.render(txt , True , color)
    ventana.blit(render,(x, y))
    
jugando = True
while jugando:
    ventana.fill(fondo)

    for e in event.get():
        if e.type == QUIT:
            jugando = False
            sys.exit()

        if e.type == KEYDOWN and not mostrar_f:
            if e.key == K_v:
                respuesta = 'V'

            elif e.key == K_f:
                respuesta = 'F'

            else :
                respuesta = None

            if respuesta :
                correcta = list[indice][1]
                if respuesta == correcta :
                    fcolor = respuesta_co
                    f_texto = 'correcto'
                    puntuacion += 1


                else:
                    fcolor = respuesta_in 
                    f_texto = 'mal'
                    puntuacion -= 1
                    
                mostrar_f = True
                tiempof = time.get_ticks()

    if indice < len(list):

        if not mostrar_f :
            dibujar_txt(f'pregunta{indice +1 }/{len(list)}', letras ,50 , 80)
            dibujar_txt(list[indice][0],letras ,50 , 150)
            dibujar_txt('presiona V(verdadero) o F(falso)',letras , 50 , 350)

        else:
            dibujar_txt(f_texto , fcolor ,50 , 200 )


            if time.get_ticks() - tiempof > 1500:
                mostrar_f = False
                indice +=1
    else:
        dibujar_txt('haz finalizado con este encuentro , continua con tu viaje', letras , 50 , 150)
        dibujar_txt(f'puntaje total:{puntuacion} / {len(list)}', letras ,50 , 230)
        dibujar_txt(' presiona la tecla ESC para salir', letras , 50 , 300)
         
        if key.get_pressed()[K_ESCAPE]:
            jugando = False
    display.update() 

    clock.tick(60)

quit()