import datetime, sys
def get_datetime():
    return datetime.datetime.now()
def cmd_not_found(cmd):
    print("\033[31m", f"Command {cmd} not found", "\033[0m")

filesystem = {
        "files": [],
        "programs": [
            "calculator",
            "python compiler",
            "python interpreter"
            ],
        "system": [],
        }

print("Welcome to LXPonOS v.1.0.0")
print("Enter 'help' to see available commands")
while True:
    term = input("~$ ")
    if term == "help":
        print("ls       - list of files and directories")
        print("lshw     - hardware parameters")
        print("kversion - OS kernel version/params")
        print("kernel   - OS kernel config (needs reboot)")
        print("iversion - OS interpreter version")
    elif term == "ls":
        print("Filesystem 1")
        for key in filesystem:
            print(key, filesystem[key])
    elif term == "lshw":
        print("Parameters:")
        print("CPU:", "Emulated")
        print("GPU:", "Emulated")
        print("RAM:", "4096kB")
        print("ROM:", "11500GB")
    elif term == "kversion":
        print("LXPonOS v.1.0.0.153 tinykrnl")
        print("System:")
        print("    Packaging & updating:")
        print("        Enabled: True")
        print("        Managers:")
        print("            ximan [0]")
        print("    Kernel:")
        print("        Noroot reconfiguring: False")
        print("        Version: 8.5.43")
        print("        Full name & root: CPonOS")
        print("Date & time:")
        print("    Datetime:", get_datetime())
    elif term == "kernel":
        print("No superuser binary detected. Are you rooted?")
        print("[   0.000132] - Noroot kernel reconfiguring disabled.")
    elif term == "iversion":
        print("OS interpreter:")
        print(f"    {sys.version} {sys.version_info.major}.{sys.version_info.minor}")
    elif term == "exit":
        exit()
    else:
        cmd_not_found(term)
