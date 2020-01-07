import time
import random


def get_number():
    numbers = [3, 4, 5, 6, 7, 8, 9]
    random_number = random.choice(numbers)
    return random_number


def caunting():
    second_left = get_number()
    print('<Przewidywany czas oczekiwania na połączenie wynosi {} sek.>'.format(second_left))
    while second_left >= 2:
        second_left -= 1
        time.sleep(1)
        print('<Pozostało', second_left, 'sek.>')


def format_name_or_rodo(name_input):
    if name_input == '':
        print('\aDR PYTHON: Aaaaaach rozumiem, RODO...')
    else:
        name_input = name_input.strip()
        name_input = name_input.title()
    return name_input


print('Witaj na TERAPII PAR DR JSON\'A PYTHONA')
time.sleep(3)
print('Proszę czekać, nawiązuje połączenie z Dr J. Pythonem...')
time.sleep(3)
caunting()
time.sleep(1)
print('<nawiązano połączenie>')
time.sleep(4)
print('\aDR PYTHON: Hej, z tej strony Json Python. W terapii par ważne jest abyście byli oboje przed monitorem')
time.sleep(3)
print('\aDR PYTHON: Zawołaj mi tu od razu faceta do klawiatury, pójdzie na pierwszy ogień')
time.sleep(5)
print('\aDR PYTHON: Czy mamy już mężczyznę przy klawiaturze?')
his = input('Ja: ')
his = his.strip()
his = his.lower()

while not (his == 'tak' or his == 'y' or his == 't'):
    time.sleep(1)
    print('\aDR PYTHON: Dawać mi tu chłopa, nie ma czasu, inni pacjenci czekają')
    time.sleep(3)
    print('\aDR PYTHON: Chłopie dotarłeś w reszcie do tej klawiatury? Tak czy nie?')
    his = input('Ja: ')
    his = his.strip()
    his = his.lower()

time.sleep(3)
print('\aDR PYTHON: Witam Szanownego Pana, jak masz na imie?')
he = input('Ja: ')
he = format_name_or_rodo(he)
time.sleep(3)
print('\aDR PYTHON: No to jaki macie problem?')
input('Ja: ')
time.sleep(4)
print('\aDR PYTHON: hmmm... ciekawe, pewnie nie uwierzysz ale spotkałem się już z tym')
time.sleep(3)
print('\aDR PYTHON: Najważniejsze, abyście pamiętali, że nie ma par idealnych, każda ma swoje problemy')
time.sleep(3)
print('\aDR PYTHON: No dobrze ' + he + ', spróbujmy mojej autorskiej terapii intidzerowej, '
                                       'podaj dowolną cyfrę Kochanieńki')
chosen_number = input('Ja: ')

try:
    chosen_number = int(chosen_number)
except ValueError:
    chosen_number = get_number()
    time.sleep(4)
    print('\aDR PYTHON: Miała być cyfra. No trudno, w takim razie wylosowałem za Ciebie cyfrę', chosen_number)

if int(chosen_number) >= 100 or int(chosen_number) <= 0:
    chosen_number = get_number()
    time.sleep(4)
    print('\aDR PYTHON: Ej no miała być cyfra, a ty poleciałeś z gruuuubej rury.'
          'W takim razie wylosuję cyfrę dla Ciebie...')
    time.sleep(4)
    print('\aDR PYTHON: Dziś', chosen_number, 'będzie twoją cyfrą')

time.sleep(4)
print('\aDR PYTHON: Swoją drogą ciekawe, że padło akurat na', chosen_number, 'bo to też moja ulubiona liczba')
time.sleep(3)
print('\aDR PYTHON: Muszę Ci zdradzić, że osoby, którzy wybierają', chosen_number, 'to nie są tak całkiem ten tego...')
time.sleep(3)
print('\aDR PYTHON: No wiesz...')
time.sleep(3)
print('\aDR PYTHON: ok, nieważne, lepiej przejdzmy do terapii...')
time.sleep(3)
print('\aDR PYTHON: Możesz teraz w nagrodę ucałować swoją piękną kobietę', chosen_number, 'razy')
time.sleep(5)
print('\aDR PYTHON: Czy ucałowałeś już?')
his = input('Ja: ')
his = his.strip()
his = his.lower()

missing_kisses = 100 - int(chosen_number)

print('\aDR PYTHON: A jak w ogóle twoja lepsza połówka ma na imię?')
she = input('Ja: ')
she = format_name_or_rodo(she)
time.sleep(3)

if his == 'tak' or his == 'y' or his == 't':
    print('\aDR PYTHON: ' + she + ' kochana moja weź potwierdz czy ucałował Cię', chosen_number, 'razy, ')
    print('\aDR PYTHON: bo jemu to nie można wierzyć, a na kamerce słobo widać. Ucałował?')
else:
    print('\aDR PYTHON: Oj ' + he + ' całuj nie kombinuj. No ucałowałeś', chosen_number, 'razy w reszcie?')
    PD = input('Ja: ')
    time.sleep(4)
    print('\aDR PYTHON: ' + she + ' moja kochana weź potwierdz czy ucałował Cię', chosen_number, 'razy,')
    print('\aDR PYTHON: bo facetom to nie można wierzyć, a ciemno jest i kamerka słabo działa. Ucałował?')

her = input('Ja: ')
her = her.strip()
her = her.lower()
time.sleep(3)

if her == 'tak' or her == 'y' or her == 't':
    print('\aDR PYTHON: No brawo! Cudownie!')
    time.sleep(2)
    print('\aDR PYTHON: A czy wiesz ' + he + ', że do 100 całusów brakuje Ci już '
          'tylko {}?'.format(missing_kisses))
    time.sleep(2)
    print('\aDR PYTHON: Na co czekasz? Do dzieła!')
    time.sleep(3)
    print('\aDR PYTHON: Widzę, że nie jestem Wam już potrzebny. Do następnej sesji. Miłego wieczoru:)')
else:
    print('\aDR PYTHON: Oj to chyba jednak nie ma sensu, inni pacjenci czekają')
    time.sleep(2)
    print('\aDR PYTHON:' + she + ', jako sztuczna inteligencja wszechczasów doradzam Ci wymianę chłopa na lepszy model')
    time.sleep(2)
    print('\aDR PYTHON: Miłego wieczoru Kochana, tego kwiatu jest pół światu;)')

time.sleep(3)
print('<połączenie zakończono>')
time.sleep(4)
print('UWAGA!!! Dr Json P. nie ponosi odpowiedzialności za efekty terapii, w tym rozwody, afty czy nieplanowane ciąże,')
print('aczkolwiek nie ma nic przeciwko aby dzieci narodzone w wyniku terapii były nazywane jego imieniem.')
time.sleep(6)
print('A ha! I jeszcze jedno:')
print(he + ' nie martw się, z osobami, które wybierają liczbę', chosen_number, 'jest wszystko w porządku:)')
input("<Press enter to exit>")
