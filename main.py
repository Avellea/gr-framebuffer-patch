import os

source_str = '5ff434701a905ff4cc70'
replace_str = '5ff470701a905ff40870'

def is_elf_patched():
    with open('eboot.bin.elf', 'rb') as f:
        data = f.read().hex()
        return replace_str in data

def is_eboot_patched():
    with open('eboot.bin', 'rb') as f:
        data = f.read().hex()
        return replace_str in data

def eboot_exists():
    return os.path.exists('eboot.bin')

def elf_exists():
    return os.path.exists('eboot.bin.elf')

def begin():
    if not eboot_exists():
        print("eboot.bin not found! Exiting...")
        os._exit(1)
    else:
        print("eboot.bin found! Beginning unmake.")
        print('> vita-unmake-fself.exe eboot.bin')
        os.system('vita-unmake-fself.exe eboot.bin')
        if not elf_exists():
            print("eboot.bin.elf not found! Exiting...")
            os._exit(1)
        else:
            print("Beginning patch...")
            patch()

def patch():
    with open('eboot.bin.elf', 'rb') as elf:
        data = elf.read().hex()
        print(source_str + " in `eboot.bin.elf`: ", source_str in data)
        data = data.replace(source_str, replace_str)
        
    with open('eboot.bin.elf', 'wb') as elf:
        elf.write(bytes.fromhex(data))

    if is_elf_patched():
        build()

def build():
    print("Patched! Building...")
    print('> vita-elf-inject.exe eboot.bin eboot.bin.elf')
    os.system('vita-elf-inject.exe eboot.bin eboot.bin.elf')
    print("Done!")

begin()