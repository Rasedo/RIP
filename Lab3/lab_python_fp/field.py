def field(items, *args):
    assert len(args) > 0
    for val in items:
        result = {}
        for arg in args:
            if arg in val:
                result[arg] = val[arg]
        if result:
            yield result


goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'color': 'black'},
    {'asd': 'Диван для отдыха', 'color': 'black'},
    {'title': 'отдыха', 'color': 'black'},
]

field_gen = field(goods, 'title', 'price')
for i in field_gen:
    print(i)
