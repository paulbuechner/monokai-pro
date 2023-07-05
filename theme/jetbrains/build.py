from tools import sublate as sub

print("[+] JetBrains")

out_dir = "output/jetbrains"
template_path = out_dir + "/templates"

sub.mkdir(out_dir + "/resources/schemes")
sub.mkdir(out_dir + "/src")

for theme in sub.data["colors"]:
    # schemes
    sub.render(f"{out_dir}/resources/schemes/{theme['id']}.xml", f"{template_path}/scheme.xml", {
        "theme": theme, "italics": True
    })
    sub.render(f"{out_dir}/resources/schemes/{theme['id']}-no-italics.xml", f"{template_path}/scheme.xml", {
        "theme": theme, "italics": False
    })

    # themes
    sub.render(f"{out_dir}/src/{theme['id']}.theme.json", f"{template_path}/theme.json", {
        "theme": theme
    })

sub.rm(template_path)
