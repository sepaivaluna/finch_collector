class World_Cup:
    def __init__(self, location, year, champion, runner_up, champion_score,
                 runner_up_score):
        self.location = location
        self.year = year
        self.champion = champion
        self.runner_up = runner_up
        self.champion_score = champion_score
        self.runner_up_score = runner_up_score


world_cups = [
    World_Cup('Russia', 3000, 'France', 'Croatia', 10, 4),
    World_Cup('Brazil', 3020, 'Germany', 'Argentina', 4, 2),
    World_Cup('South Africa', 3012, 'Spain', 'Netherlands', 1, 0)
]