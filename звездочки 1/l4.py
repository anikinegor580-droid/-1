def team_weights(weights):
    return (sum(weights[::2]), sum(weights[1::2]))

if __name__ == "__main__":
    print("Результат работы teams.py:")
    print(team_weights([50, 60, 70, 80]))
