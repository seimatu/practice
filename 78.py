class Planet:
    shape='squea'

    def __init__(self,water,moon):
        self.water=water
        self.moon=moon

    def orbit(self):
        return f'{self.water} and satellite is {self.moon}'
#@classmethodはクラスとつなげることができる。
    @classmethod
    def commons(cls):
        return f'all the planets are {cls.shape}'

naboo=Planet('yes','moon is not present')
print(Planet.shape)
print(Planet.commons())

print('--------------------------')

print(naboo.orbit())