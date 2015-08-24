from steamanalyst import entities
from steamanalyst import queries


def find_knives(skins):
    builder = QueryBuilder(skins)

    builder.where(lambda skin: skin.is_knife())

    return builder.get()

def find_stattrak_awps(skins):
    builder = QueryBuilder(skins)

    builder.where(lambda skin: skin.name == 'AWP')
    builder.where(lambda skin: skin.is_stattrak())

    return builder.get()

def find_factory_new_stattrak_awps(skins):
    builder = QueryBuilder(skins)

    builder.where(lambda skin: skin.name == 'AWP')
    builder.where(lambda skin: skin.is_stattrak())
    builder.where(lambda skin: skin.is_wear(entities.Wears.FactoryNew))

    return builder.get()

