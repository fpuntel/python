import sys 
import serial

# Programa que manda sinais par ao arduino com um controle joystick

pipe = open('/dev/input/js0', 'r') #Porta em que o controle está conectado
porta = '/dev/ttyACM0'             #Porta em que o Arduino está conectado
baud_rate = 9600
action = []
spacing = 0

def escrever_porta(valor):

    try:
        #valor = (raw_input("Digite o valor a ser enviado:"));
        Obj_porta = serial.Serial(porta, baud_rate)
        Obj_porta.write(valor)
        Obj_porta.close()
    except serial.SerialException:
        print 'ERRO: Verifique se ha algum dispositivo conectado'
    return valor

while 1:
    for character in pipe.read(1):
        action += ['%02X' % ord(character)]
        if len(action) == 8:
            num = int (action[5], 16) #traduz para inteiro
            percent254 = str(((float(num)-128.0)/126.0)-100)[4:6] 
            percent128 = str((float(num)/127.0))[2:4]

            if percent254 == '.0':
                percent254 = '100'
            if percent128 == '0':
                percent128 = '100'
            if action[6] == '01': #Botao (1, 2, 3, 4)    
                if action[4] == '01':
                    print 'Voce pressionou o botao: ' + action[7]
                    escrever_porta(action[7])
            elif action[7] == '00': #Direita ou esquerda
                if action[4] == 'FF':
                    print 'Voce pressionou: PARA DIREITA'
                    escrever_porta('D')
                elif action[4] == '01':
                    print 'Voce pressionou: PARA ESQUERDA'
                    escrever_porta('E')
            elif action[7] == '01':
                if action[4] == 'FF':
                    print 'Voce pressionou: PARA BAIXO'
                    escrever_porta('B')
                elif action[4] == '01':
                    print 'Voce pressionou: PARA CIMA'
                    escrever_porta('C')

            action = [] 
