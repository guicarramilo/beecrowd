def large_enough():
    string = input()
    if 1 <= len(string) <= 500:
        if len(string) <= 80:
            print('YES')
        else:
            print('NO')

large_enough()
large_enough()