def age():
    days = int(input())
    anos = days // 365
    days = days % 365
    meses = days // 30
    days = days % 30
    print(f'{anos} ano(s) \n{meses} mes(es) \n{days} dia(s)')

age()
age()
age()