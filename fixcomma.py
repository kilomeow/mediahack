charmap = {
    "Белка": "Squirrel",
    "Флоппа": "Floppa",
    "Сорока": "Magpie",
    "Крипто-сова": "Owl",
    "Кролик": "Rabbit"
}


def transform(line):
    text = line.rstrip()

    if text.endswith(')'):
        text += ','

    return text


def process(in_fn, out_fn):
    with open(in_fn) as source:
        result_lines = map(transform, source.readlines())

    with open(out_fn, 'w') as dest:
        dest.write("\n".join(result_lines))


if __name__ == '__main__':
    import sys

    process(*sys.argv[1:])
