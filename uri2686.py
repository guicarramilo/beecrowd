def horario():
    while True:
        try:
            M = float(input())
            if 0 <= M < 360:
                if M < 90:
                    horas = 6 + M // 15
                    M = (M / 15) - (M // 15)
                    minutos = M * 60
                    print('Bom Dia!!\n{:02.0f}:{:02.0f}:00'.format(horas, minutos))
                elif 180 > M >= 90:
                    horas = 6 + M // 15
                    M = (M / 15) - (M // 15)
                    minutos = M * 60
                    print('Boa Tarde!!\n{:02.0f}:{:02.0f}:00'.format(horas, minutos))
                elif 270 > M >= 180:
                    horas = 6 + M // 15
                    M = (M / 15) - (M // 15)
                    minutos = M * 60
                    print('Boa Noite!!\n{:02.0f}:{:02.0f}:00'.format(horas, minutos))
                elif M >=270:
                    M = M - 270
                    horas = M // 15
                    M = (M / 15) - (M // 15)
                    minutos = M * 60
                    print('De Madrugada!!\n{:02.0f}:{:02.0f}:00'.format(horas, minutos))
        except EOFError:
            break

horario()