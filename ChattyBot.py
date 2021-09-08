#packages needed
import time

# Magnolia introduction
print()
print("Oi! Meu nome é Magnólia.")
time.sleep(1)
print("Eu fui criada em 1997.")
time.sleep(2)
print()

# Magnolia asks questions

# Name
def name():
    print("Qual o seu nome?")
    user_name = input()
    print("Oi, " + user_name + "! Que nome lindo.")
    print()

# Age
def age():
    print("Vou advinhar sua idade.")
    print("Me diga o resto da sua idade quando dividida por 3, 5 e 7:")
    remainder3 = int(input())
    remainder5 = int(input())
    remainder7 = int(input())
    age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
    print()
    print("Hmmm, acho que você tem " + str(age) + " anos. Acertei?")
    input()
    print()
    print("Uhul!")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print()

# Favorite number
def favorite_number():
    print("Qual o seu número favorito?")
    fav_num = int(input())
    print("Eu sei contar até " + str(fav_num) + ", olha só:")
    i = 0
    while i <= fav_num:
        time.sleep(1)
        print(str(i) + "!")
        i += 1
    print("Gostou?!")

def test():
    print("Vamos ver se você me conhece direito.")
    print()
    print("Quem é meu criador?")
    print("1. René Descartes.")
    print("2. Chico Buarque.")
    print("3. Felipe Marcelino.")
    print("4. Elon Musk.")
    answer = int(input())
    if answer == 3:
        print("Parabéns, você acertou!")
    else:
        print("Por favor, tente de novo.")
        test()

def end():
    print()
    print("É isso por hoje. Tchauzinho!")

def back_to_hub():
    print()
    print("Deseja retornar ao menu de rotinas?")
    print("1. Sim.")
    print("2. Não.")
    go_back = int(input())
    if go_back == 1:
        routine_hub()
    else:
        end()

def routine_hub():
    print("Qual rotina você deseja ativar?")
    print("1. Nome.")
    print("2. Idade.")
    print("3. Número favorito.")
    print("4. Quiz.")
    print("5. Sair")
    routine = int(input())
    if routine == 1:
        name()
        back_to_hub()

    if routine == 2:
        age()
        back_to_hub()

    if routine == 3:
        favorite_number()
        back_to_hub()

    if routine == 4:
        test()
        back_to_hub()

    if routine == 5:
        end()

routine_hub()