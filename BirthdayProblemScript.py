import random as rand
import matplotlib.pyplot as plt

def RunExperiment() -> int:
    people_in_room = []
    # not using a while(true) here because I'm scared of while loops
    for _ in range(0, 365):
        new_guy = rand.randint(1, 365)
        if new_guy in people_in_room:
            people_in_room.append(new_guy)
            return len(people_in_room)
        people_in_room.append(new_guy)
    print("Error, pigeonhole principle violated")

def MeasureDistribution(numTimes):
    experiment_results = []
    for _ in range(0, numTimes):
        experiment_results.append(RunExperiment())
    return experiment_results

def DisplayResults(results):
    x = range(0, 366)
    y = [0] * 366
    for result in results:
        y[result] += 1
    plt.bar(x, y)
    plt.show()

if (__name__ == "__main__"):
    results = MeasureDistribution(1000000)
    DisplayResults(results)
