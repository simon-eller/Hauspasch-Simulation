import random, csv
import matplotlib.pyplot as plt
import numpy as np

class Dice():
    def __init__(self):
        self.combinations = np.empty([6, 6, 6], dtype=int)
        with open("dice_combinations_weightings.csv", encoding='utf-8-sig', newline='') as csvfile:
            for row in csv.DictReader(csvfile, delimiter=';'):
                self.combinations[int(row["dice1"])-1,int(row["dice2"])-1,int(row["dice3"])-1] = int(row["weighting"])

    def roll(self):
        return int(self.combinations[random.randrange(0,6), random.randrange(0,6), random.randrange(0,6)])

def convert_results_coordinates(playing_results:dict):
    x_coordinates:list = []
    y_coordinates:list = []

    for i in playing_results:
        x_coordinates.append(playing_results[i]["name"])
        y_coordinates.append(playing_results[i]["count"])

    for i in range(len(y_coordinates)):
        y_coordinates[i] = y_coordinates[i]/sample

    return x_coordinates, y_coordinates

def simulate_rolls(sample:int, GamingDice:Dice):
    dice_weightings_names:dict = {}

    with open("dice_weightings_names.csv", encoding='utf-8-sig', newline='') as csvfile:
        for row in csv.DictReader(csvfile, delimiter=';'): dice_weightings_names = row

    for i in dice_weightings_names:
        playing_results[int(i)] = {"count" : 0, "name": dice_weightings_names[str(i)]}

    for i in range(sample):
        current_roll:int = GamingDice.roll()
        playing_results[current_roll]["count"] += 1

    x_coordinates, y_coordinates = convert_results_coordinates(playing_results)

    plt.bar(height=y_coordinates, x=x_coordinates)
    plt.xticks(rotation=90)
    plt.show()


if __name__ == "__main__":
    GamingDice:Dice = Dice()
    playing_results:dict = {}
    sample:int = 1000000

    simulate_rolls(sample, GamingDice)