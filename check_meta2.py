from check_meta import Resistor

class BoundResistance(Resistor):
    def __init__(self, ohms) -> None:
        super().__init__(ohms)

    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        if ohms <= 0:
            raise ValueError(f'ohms must  be > 0; got {ohms}')
        self._ohms = ohms

r3 = BoundResistance(1e3)
r3.ohms = 0