import time

try:

    while True:

        print('TO JEST KALKULATOR\n\nWybierz jakie działania chcesz wykonać:\n')
        print('Dodawanie, wybierz: {}\nOdejmowanie, wybierz: {}\n'.format('+', '-'))
        print('Mnożenie, wybierz: {}\nDzielenie, wybierz: {}\n'.format('*', '/'))
        print('Dzielenie całkowite, wybierz: {}\nReszta z dzielenia: {}\n'.format('//', '%'))
        print('Potęgowanie, wybierz: {}\n'.format('**'))
        w = input('WYBIERZ: \n')

        if w == '+':
            print('DODAWANIE: \n')
            time.sleep(0.4)
            a = input('Podaj pierwszą liczbę: ')
            b = input('Podaj drugą liczbę: ')
            time.sleep(0.4)
            print(('Wynik to: '), int(a)+int(b))
            time.sleep(0.6)

        if w == '-':
            print('ODEJMOWANIE: \n')
            time.sleep(0.4)
            a = input('Podaj pierwszą liczbę: ')
            b = input('Podaj drugą liczbę: ')
            time.sleep(0.4)
            print(('Wynik to: '), int(a) - int(b))
            time.sleep(0.6)

        if w == '*':
            print('MNOŻENIE: \n')
            time.sleep(0.4)
            a = input('Podaj pierwszą liczbę: ')
            b = input('Podaj drugą liczbę: ')
            time.sleep(0.4)
            print(('Wynik to: '), int(a) * int(b))
            time.sleep(0.6)

        if w == '/':
            print('DZIELENIE: \n')
            time.sleep(0.4)
            a = input('Podaj pierwszą liczbę: ')
            b = input('Podaj drugą liczbę: ')
            time.sleep(0.4)
            print(('Wynik to: '), int(a) / int(b))
            time.sleep(0.6)

        if w == '//':
            print('DZIELENIE CAŁKOWITE: \n')
            time.sleep(0.4)
            a = input('Podaj pierwszą liczbę: ')
            b = input('Podaj drugą liczbę: ')
            time.sleep(0.4)
            print(('Wynik to: '), int(a) // int(b))
            time.sleep(0.6)

        if w == '%':
            print('RESZTA Z DZIELENIA: \n')
            time.sleep(0.4)
            a = input('Podaj pierwszą liczbę: ')
            b = input('Podaj drugą liczbę: ')
            time.sleep(0.4)
            print(('Wynik to: '), int(a) % int(b))
            time.sleep(0.6)

        if w == '**':
            print('POTĘGOWANIE: \n')
            time.sleep(0.4)
            a = input('Podaj pierwszą liczbę: ')
            b = input('Podaj drugą liczbę: ')
            time.sleep(0.4)
            print(('Wynik to: '), int(a) ** int(b))
            time.sleep(0.6)

        while True:
            odp = input('Coś jeszcze? (t/n): \n')
            if odp in ('t', 'n'):
                break
            print('BŁĄD! PODAJ POPRAWNĄ ODPOWIEDŹ!')
        if odp == 't':
            continue
        else:
            print('KONIEC')
            break

except ValueError:
    print('\nBŁĄD! MUSISZ PODAĆ PRAWIDŁOWĄ LICZBĘ!' * 4)
except ZeroDivisionError:
    print('\nBŁĄD! NIE MOŻNA PODZIELIĆ PRZEZ 0!' * 4)