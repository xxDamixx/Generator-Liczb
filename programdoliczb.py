#Autor: Damian Popławski
import random

tolerance = 0.1  # 10% tolerance

while True:
    for i in range(4):
        random_number = random.uniform(500 - (500 * tolerance), 500 + (500 * tolerance))
        print(random_number)
    input("wciśnij dowolny przycisk żeby wygenerować nowe liczby")
