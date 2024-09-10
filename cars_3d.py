from math import cos, sin
from sys import argv
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

global esqdir
global cimabaixo
global aux1
global aux2

esqdir = 0
cimabaixo = 0
aux1 = 0
aux2 = 0

def desenha_carro():    
    # Corpo do carro
    glColor3f(1.0, 0.0, 0.0)  # Cor vermelha para o carro
    glPushMatrix()
    glTranslatef(0, 0, 0)

    glScalef(0.7, 0.7, 0.7)  # escala para diminuir o carro

    glPushMatrix()

    glTranslatef(0.0, 0.0, 0.0)
    glScalef(1.5, 0.3, 0.5)
    glutSolidCube(1.0)
    glPopMatrix()

    # Teto do carro (também vermelho)
    glPushMatrix()
    glTranslatef(0.0, 0.25, 0.0)
    glScalef(1.0, 0.3, 0.5) 
    glutSolidCube(1.0)
    glPopMatrix()

    # Janelas laterais
    glColor3f(0.53, 0.81, 0.92)  # Cor azul para as janelas

    # Janela do lado esquerdo
    glPushMatrix()
    glTranslatef(0.2, 0.15, 0.25)  
    glScalef(0.4, 0.2, 0.01) 
    glutSolidCube(0.5)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-0.2, 0.15, 0.25) 
    glScalef(0.4, 0.2, 0.01)  
    glutSolidCube(0.5)
    glPopMatrix()

    # Janela do lado direito
    glPushMatrix()
    glTranslatef(0.2, 0.15, -0.25) 
    glScalef(0.4, 0.2, 0.01)  
    glutSolidCube(0.5)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-0.2, 0.15, -0.25)  
    glScalef(0.4, 0.2, 0.01)
    glutSolidCube(0.5)
    glPopMatrix()

    # Adicionando o para-brisa na frente
    glColor3f(0.53, 0.81, 0.92)  # Azul para o para-brisa
    glPushMatrix()
    glTranslatef(0.5, 0.2, 0.0)  # Posição exata na frente do carro
    glScalef(0.05, 0.3, 0.5)  # Faz o para-brisa fino (X reduzido) e largo
    glutSolidCube(0.8)  # Pode usar um cubo ou mudar para quadrados
    glPopMatrix()

    # Rodas do carro
    glColor3f(0.0, 0.0, 0.0)  # Cor preta para as rodas

    # Rodas traseiras
    for z in [-0.3, 0.3]:
        glPushMatrix()
        glTranslatef(-0.5, -0.2, z)  # Posições das rodas traseiras
        glutSolidCylinder(0.15, 0.05, 10, 10)
        glPopMatrix()

    # Rodas da frente
    for z in [-0.3, 0.3]:
        glPushMatrix()
        glTranslatef(0.5, -0.2, z)  # Posições das rodas da frente
        glutSolidCylinder(0.15, 0.05, 10, 10)
        glPopMatrix()

    # Faróis amarelos
    glColor3f(1.0, 1.0, 0.0)  # Cor amarela para os faróis
    
    farol_tamanho = 0.2  
    farol_raio = 0.2 

    # Faróis da frente
    glPushMatrix()
    glTranslatef(0.75, 0.0, 0.2)  # Posição do farol direito
    glScalef(farol_tamanho, farol_tamanho, farol_tamanho)  # Ajusta o tamanho dos faróis
    glutSolidSphere(farol_raio, 10, 10)  # Desenha uma esfera para o farol
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.75, 0.0, -0.2)  # Posição do farol esquerdo
    glScalef(farol_tamanho, farol_tamanho, farol_tamanho)  # Ajusta o tamanho dos faróis
    glutSolidSphere(farol_raio, 10, 10)  # Desenha uma esfera para o farol
    glPopMatrix()

    # Parte traseira
    glColor3f(0.0, 0.0, 0.0)
    glPushMatrix()
    glTranslatef(-0.8, -0.02, -0.1)  
    glScalef(0.5, 0.15, 0.2)
    glutSolidCube(0.5) 
    glPopMatrix()

    glPopMatrix()

def desenha_varios_carros():
    espacamento = 1.3 
    numero_de_carros = 2  
    
    # Posiciona o carro extra antes do carro central
    posicao_do_carro_extra = -espacamento 
    
    # Desenha o carro extra
    glPushMatrix()
    glTranslatef(posicao_do_carro_extra, 0.0, 0.0)  
    glScalef(0.7, 0.7, 0.7)  
    desenha_carro() 
    glPopMatrix()
    
    # Desenha o restante dos carros
    for i in range(numero_de_carros):
        glPushMatrix()
        glTranslatef(i * espacamento, 0.0, 0.0) 
        glScalef(0.7, 0.7, 0.7)  
        desenha_carro() 
        glPopMatrix()

def tela():
    glClearColor(0.5, 0.5, 0.5, 0.5)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(distancia, 1, 0.1, 500)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(sin(esqdir) * 10, 0 + cimabaixo, cos(esqdir) * 10, 0, 0, 0, 0, 1, 0)
    glEnable(GL_DEPTH_TEST)

    desenha_varios_carros()

    glFlush()
    glutSwapBuffers()

def Teclado(tecla, x, y):
    global aux1
    global aux2
    print("*** Tratamento de teclas comuns")
    print(">>> Tecla: ", tecla)

    if tecla == chr(27):  # ESC ?
        sys.exit(0)

    if tecla == b'a':  # A
        aux1 = aux1 - 0.1
        print("aux1 = ", aux1)

    if tecla == b's':  # S
        aux1 = aux1 + 0.1
        print("aux1 = ", aux1)

    if tecla == b'w':  # W
        aux2 = aux2 + 0.1
        print("aux2 = ", aux2)

    if tecla == b'z':  # Z
        aux2 = aux2 - 0.1
        print("aux2 = ", aux2)
    tela()
    glutPostRedisplay()

def TeclasEspeciais(tecla, x, y):
    global esqdir
    global cimabaixo
    print("*** Tratamento de teclas especiais")
    print("tecla: ", tecla)
    if tecla == GLUT_KEY_F1:
        print(">>> Tecla F1 pressionada")
    elif tecla == GLUT_KEY_F2:
        print(">>> Tecla F2 pressionada")
    elif tecla == GLUT_KEY_F3:
        print(">>> Tecla F3 pressionada")
    elif tecla == GLUT_KEY_LEFT:
        esqdir = esqdir - 0.1
    elif tecla == GLUT_KEY_RIGHT:
        esqdir = esqdir + 0.1
    elif tecla == GLUT_KEY_UP:
        cimabaixo = cimabaixo + 0.05
    elif tecla == GLUT_KEY_DOWN:
        cimabaixo = cimabaixo - 0.05
    else:
        print("Apertou... ", tecla)
    tela()
    glutPostRedisplay()

def ControleMouse(button, state, x, y):
    global distancia
    if (button == GLUT_LEFT_BUTTON):
        if (state == GLUT_DOWN):
            if (distancia >= 10):
                distancia -= 2

    if (button == GLUT_RIGHT_BUTTON):
        if (state == GLUT_DOWN):  # Zoom-out
            if (distancia <= 130):
                distancia += 2
    tela()
    glutPostRedisplay()

global distancia
glutInit(argv)
glutInitDisplayMode(GLUT_RGBA | GLUT_DEPTH)
glutInitWindowSize(600, 600)
glutCreateWindow(b"Carros vermelho")
distancia = 20
glutDisplayFunc(tela)
glutMouseFunc(ControleMouse)
glutKeyboardFunc(Teclado)
glutSpecialFunc(TeclasEspeciais)

glutMainLoop()