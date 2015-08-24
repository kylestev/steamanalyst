import re

SKIN_MATCHER = re.compile(r'^(?:([^a-zA-Z0-9\s]+) )?(?:(StatTrak[^ ]) )?' +
                          '(?:([^|]+) )\| (?:([^\(]+))\(([^\)]+)\)$'.encode('utf8'))


class Wears(object):
    WellWorn = 'Well-Worn'
    FactoryNew = 'Factory New'
    MinimalWear = 'Minimal Wear'
    FieldTested = 'Field-Tested'
    BattleScarred = 'Battle-Scarred'


class Skin(object):
    def __init__(self, raw, gun, name, wear, knife=False, stattrak=False):
        self.raw = raw
        self.gun = gun
        self.name = name
        self.wear = wear
        self.knife = knife
        self.stattrak = stattrak

    def is_knife(self):
        return self.knife

    def is_stattrak(self):
        return self.stattrak

    def is_wear(self, wear):
        return self.wear == wear

    @staticmethod
    def parse(market_name):
        m = SKIN_MATCHER.match(market_name)
        if m is None:
            return None
        (knife, stattrak, gun, name, wear) = m.groups()
        return Skin(market_name, gun, name, wear,
                    knife=(not knife is None),
                    stattrak=(not stattrak is None))
