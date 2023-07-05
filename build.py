#!/usr/bin/env python3
from tools import sublate as sub

sub.data.update({
    "date": sub.date_iso(),
    "colors": list(sub.read("colors/*.yaml").values()),
})

sub.rm("output")
sub.cp("theme", "output")
sub.run("output/*/build.py")
sub.rm("output/*/build.py")
