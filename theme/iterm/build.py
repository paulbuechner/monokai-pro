from tools import sublate as sub

print("[+] iTerm")

out_dir = "output/iterm"
template_path = out_dir + "/templates"

for theme in sub.data["colors"]:
    # convert colors to rgb decimal
    _theme = {"colors": {}}
    for k, v in theme["colors"].items():
        r, g, b = tuple(int(v[1:][i:i+2], 16)/255 for i in (0, 2, 4))
        _theme["colors"][k] = {
            "r":  r,
            "g":  g,
            "b":  b,
        }

    sub.render(f"{out_dir}/{theme['name']}.itermcolors".replace(" ", "_"), f"{template_path}/template.itermcolors", {
        "theme": _theme
    })

sub.rm(template_path)
