import modules
import modules.init


def stringifyAction(a):
    if hasattr(a, 'text') and hasattr(a, 'npc'):
        suffix = ""
        a_class = a.__class__.__name__.lower()

        if a_class != "say":
            suffix += f" #{a_class}"

        if a_class == "ask":
            suffix += f" [ {' | '.join([o[0]+' -> '+o[1] for o in a.options])} ]"
            suffix += f" {a.var}"

        return f"{a.npc.name}: {a.text}" + suffix
    else:
        return "//" + repr(a)
    

def stringifyModule(name):
    story = getattr(modules, name).content
    out_glides = list()
    for glide, actions in story.glides.items():
        out_actions = '\n'.join(map(stringifyAction, actions))
        out_glides.append("@" + glide + "\n" + out_actions)

    return "\n\n".join(out_glides)


import os.path

def exportModules(dest=""):
    for name in modules.init.modules_deps.keys():
        out = stringifyModule(name)
        fp = os.path.join(dest, f"{name}.txt")
        with open(fp, 'w') as out_f:
            out_f.write(out)
        print(f"`{fp}` write succesfully")