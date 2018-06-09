"""This module contains definitions of different classes of vehicles"""


class VehicleBase:
    """Base class for all vehicles"""
    def __init__(self, length, pos, speed, accel):
        self.length = length
        self.position = pos
        self.speed = speed
        self.acceleration = accel

    def update_position(self):
        msg = f'{self.__class__.__name__}: update_position() method not implemented'
        raise NotImplementedError(msg)

    def update_speed(self):
        msg = f'{self.__class__.__name__}: update_speed() method not implemented'
        raise NotImplementedError(msg)

    def update_acceleration(self):
        msg = f'{self.__class__.__name__}: update_acceleration() method not implemented'
        raise NotImplementedError(msg)


class Car(VehicleBase):
    """Class that models a car"""
    def __init__(self, length, pos, speed, accel):
        super().__init__(length, pos, speed, accel)

    def update_position(self):
        pass

    def update_speed(self):
        pass

    def update_acceleration(self):
        pass
