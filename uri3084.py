def pointers():
    while True:
        try:
            h, m = map(int, input().split())
            if 0 <= h < 360 and 0 <= m < 360:
                horas = h / 30
                minutos = m / 6
                print('{:02.0f}:{:02.0f}'.format(horas, minutos))
        except EOFError:
            break

pointers()
    