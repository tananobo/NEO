
from helpers import cd_to_datetime, datetime_to_str


class NearEarthObject:
    def __init__(self, **info):

        self.designation = info['pdes']
        self.name = info['name'] if info['name'] != "" else None
        self.diameter = float(
            info['diameter']) if info['diameter'] != "" else float('nan')
        self.hazardous = True if info['pha'] == 'Y' else False
        self.approaches = []

    @property
    def fullname(self):
        if self.name is None:
            tmp = self.designation
        else:
            tmp = self.designation + '(' + self.name + ')'
        return tmp

    def __str__(self):
        tmp = 'is' if self.hazardous else 'is not'
        return f"{self.fullname} has a diameter of {self.diameter} km and {tmp} hazardrous."

    def __repr__(self):
        return (f"NearEarthObject(designation={self.designation!r}, name={self.name!r}, "
                f"diameter={self.diameter:.3f}, hazardous={self.hazardous!r})")


class CloseApproach:
    def __init__(self, **info):
        self._designation = info['des']
        self.time = cd_to_datetime(info['cd'])
        self.distance = float(
            info['dist']) if info['dist'] != "" else float('nan')
        self.velocity = float(
            info['v_rel']) if info['v_rel'] != "" else float('nan')

        # Create an attribute for the referenced NEO, originally None.
        self.neo = None

    @property
    def time_str(self):
        return datetime_to_str(self.time)

    def __str__(self):
        return f"On {self.time_str}, '{self._designation}' approaches Earth at a distance of {self.distance:.2f} au and a velocity of {self.velocity:.2f} km/s."

    def __repr__(self):
        return (f"CloseApproach(time={self.time_str!r}, distance={self.distance:.2f}, "
                f"velocity={self.velocity:.2f}, neo={self.neo!r})")
