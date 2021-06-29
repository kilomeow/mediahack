charmap = {
    "Белка": "Squirrel",
    "Флоппа": "Floppa",
    "Сорока": "Magpie",
    "Крипто-сова": "Owl",
    "Кролик": "Rabbit"
}


def transform(line):
    line_split = line.split(': ', maxsplit=1)

    outcome = None

    if len(line_split) == 2:
        name, text = line_split
        text = text.rstrip()
        outcome = f'npc.{charmap[name]}.say("{text}"),'
    else:
        outcome = "# " + line

    return outcome


def process(in_fn, out_fn):
    
    with open(in_fn) as source:
        result_lines = map(transform, source.readlines())

    with open(out_fn, 'w') as dest:
        dest.write("\n".join(result_lines))


if __name__ == '__main__':
    import sys

    process(*sys.argv[1:])
