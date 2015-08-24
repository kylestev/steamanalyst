class QueryBuilder(object):
    def __init__(self, items):
        self.items = items
        self.filters = []

    def _apply(self):
        func = lambda item: True
        for f in self.filters:
            func = f(func)
        return func(self.items)

    def get(self, field=None):
        items = self.items
        for f in self.filters:
            items = filter(f, items)
        self.filters = []

        if not field is None:
            return [getattr(item, field) for item in items]

        return items

    def where(self, func):
        self.filters.append(func)
