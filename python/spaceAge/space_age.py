class SpaceAge:

    one_earth_year = 31557600

    def __init__(self, seconds):
        if seconds < 0:
            raise Exception("Not a valid entry")
        self.seconds = seconds

    def on_earth(self):
        answer = self.seconds / SpaceAge.one_earth_year
        return round(answer, 2)

    def on_mercury(self):
        planet_change = 0.2408467
        temp_answer = self.seconds / SpaceAge.one_earth_year
        answer = temp_answer/planet_change
        return round(answer, 2)

    def on_venus(self):
        planet_change = 0.61519726
        temp_answer = self.seconds / SpaceAge.one_earth_year
        answer = temp_answer / planet_change
        return round(answer, 2)

    def on_mars(self):
        planet_change = 1.8808158
        temp_answer = self.seconds / SpaceAge.one_earth_year
        answer = temp_answer / planet_change
        return round(answer, 2)

    def on_jupiter(self):
        planet_change = 11.862615
        temp_answer = self.seconds / SpaceAge.one_earth_year
        answer = temp_answer / planet_change
        return round(answer, 2)

    def on_saturn(self):
        planet_change = 29.447498
        temp_answer = self.seconds / SpaceAge.one_earth_year
        answer = temp_answer / planet_change
        return round(answer, 2)

    def on_uranus(self):
        planet_change = 84.016846
        temp_answer = self.seconds / SpaceAge.one_earth_year
        answer = temp_answer / planet_change
        return round(answer, 2)

    def on_neptune(self):
        planet_change = 164.79132
        temp_answer = self.seconds / SpaceAge.one_earth_year
        answer = temp_answer / planet_change
        return round(answer, 2)
