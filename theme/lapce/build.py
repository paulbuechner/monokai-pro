from tools import sublate as sub

print("[+] Lapce")

out_dir = "output/lapce"
template_path = out_dir + "/templates"

sub.mkdir(out_dir + "/src")

for theme in sub.data["colors"]:
    sub.render(f"{out_dir}/src/{theme['id']}.toml", f"{template_path}/theme.toml", {
        "theme": theme
    })

sub.rm(template_path)
