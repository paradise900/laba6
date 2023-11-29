class Gun:
    def __init__(self):
        self.bullets = 30
        self.firerate = 3
        self.fire_range = 50
        self.damage = 20
        self.armor_piercing = 50

    def shoot(self):
        print('tratata')

    def time_to_get_empty(self):
        return int(self.bullets / self.firerate)

    def firerate_per_range(self):
        return int(self.fire_range / self.firerate)

    @classmethod
    def description(cls):
        print("It's {} ".format(cls.__name__))

    def __add__(self, other): # overloading add method for adding two classes
        return (self.damage + other.damage) / 2 


class Rifle(Gun):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.bullets = 30
        self.firerate = 14
        self.fire_range = 130
        self.damage = 32
        self.armor_piercing = 60
    
    def shoot_options(self):
        print('burst, taps, spray')
    
    def selectSO(self, option):
        self.cur_SO = option

class Shotgun(Gun):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.bullets = 5
        self.firerate = 0.5
        self.fire_range = 10
        self.damage = 120
        self.armor_piercing = 90

    def shot_options(self):
        print('tap')

    def handle(self, option: bool):
        self.handle = option
    
class Pistol(Gun):
    
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.bullets = 30
        self.firerate = 7
        self.fire_range = 50
        self.damage = 30
        self.armor_piercing = 20

    def shot_options(self):
        print('taps')

    def muffler_on(self, position: bool):
        self.muffler = position

class SMG(Pistol, Rifle):
    def __init__(self, name):
        self.name = name
        self.bullets = 40
        self.firerate = 10
        self.fire_range = 50
        self.damage = 25
        self.armor_piercing = 10

    def compensator(self, option: bool, type=None):
        if option:
            compensator_type = type

class CreateNewGun(Gun):
    def __init__(self, bullets, firerate, fire_range, damage, armor_piercing):
        self.bullets = bullets
        self.firerate = firerate
        self.fire_range = fire_range
        self.damage = damage
        self.armor_piercing = armor_piercing
    
    def init_name(self, name):
        self.name = name
    
    def init_shot_options(self, option):
        self.shot_options = option
    
    def print_shot_options(self):
        print(self.shot_options)

pistol = Pistol('Glock')
smg = SMG('Usi')
shotgun = Shotgun('xm')
rifle = Rifle('m4a4')
guns = [pistol, smg, shotgun, rifle]
for gun in guns:
    print(gun.name)
    print(f'магазин опустеет за {gun.time_to_get_empty()} секунды')
    print(f'соотношение скорострельности к дальности стрельбы - {gun.firerate_per_range()}\n')

ak47 = CreateNewGun(30, 17, 170, 35, 80)
ak47.init_name('AK47')
ak47.init_shot_options('burst, taps, spray')
ak47.print_shot_options()

print(pistol + smg) # overloading add method for adding two classes