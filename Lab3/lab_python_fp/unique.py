import types


class Unique(object):
    def __init__(self, items, **kwargs):
        self.used_elements = set()
        self.items = items
        self.index = 0
        if 'ignore_case' in kwargs:
            self.ignore_case = kwargs['ignore_case']
        else:
            self.ignore_case = False

    def __next__(self):
        if isinstance(self.items, types.GeneratorType):
            while True:
                current = self.items.__next__()
                if isinstance(current, dict):
                    current = current['job-name']
                if self.ignore_case and isinstance(current, str):
                    current = current.lower()
                self.index = self.index + 1
                if current not in self.used_elements:
                    self.used_elements.add(current)
                    return current
        else:
            while True:
                if self.index >= len(self.items):
                    raise StopIteration
                else:
                    if self.ignore_case:
                        current = self.items[self.index].lower()
                    else:
                        current = self.items[self.index]
                    self.index = self.index + 1
                    if current not in self.used_elements:
                        self.used_elements.add(current)
                        return current

    def __iter__(self):
        return self


lst1 = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
lst2 = [1, 3, 2, 3, 2, 1, 4, 3, 3, 3]
result = ''
for i in Unique((i for i in lst1), ignore_case=False):
    result += str(i) + ' '
print(f'Generator: {result}')
result = ''
for i in Unique(lst2):
    result += str(i) + ' '
print(f'List: {result}')
