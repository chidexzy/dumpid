#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Python 3-safe conversion of the non-sensitive portions of dump.py.

Facebook token/cookie authentication and remote ID harvesting are intentionally
not implemented here. The terminal UI, utility functions, and local file
handling are retained in Python 3 form.
"""

import os
import sys
import time


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def keluar():
    print("\x1b[0;91m•\x1b[0;93m See You Again :)\x1b[0;97m")
    raise SystemExit


def jalan(z):
    """Print text one character at a time, as in the original script."""
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


def hapus():
    """Remove the locally stored login file and return to the menu."""
    try:
        os.remove("login.txt")
    except FileNotFoundError:
        pass
    time.sleep(0.01)
    masuk()


def logo():
    return (
        ' •••\n'
        '  ___  _   _ __  __ ___ \n'
        ' |   \\| | | |  \\/  | _ \\ \n'
        ' | |) | |_| | |\\| |  _/ \n'
        ' |___/ \\___/|_|  |_|_|  \n'
        '\n •••'
    )


def show_logo():
    # Avoid depending on the external `lolcat` command.
    print(logo())


def disabled_feature(name):
    print(f"\x1b[1;93m{name} is disabled in this Python 3 conversion.\x1b[0;97m")
    input("\n\x1b[1;93m[\x1b[1;91mReturn\x1b[1;93m]")
    dump()


def masuk():
    clear_screen()
    show_logo()
    print(50 * "\x1b[1;91m─")
    time.sleep(0.07)
    print("\x1b[1;97m1). Login Via Token Facebook")
    time.sleep(0.07)
    print("\x1b[1;97m2). Login Via Cookie Facebook")
    time.sleep(0.07)
    print("\x1b[1;91m0\x1b[1;97m).\x1b[1;97m Exit")
    time.sleep(0.07)
    print(50 * "\x1b[1;91m─")
    time.sleep(0.07)
    pilih_masuk()


def pilih_masuk():
    msuk = input("* --> ").strip()
    if msuk == "":
        print(" INVALID!!!")
        return pilih_masuk()
    if msuk == "1":
        return login_token()
    if msuk == "2":
        return login_cookie()
    if msuk == "0":
        return keluar()
    print(" INVALID!!!")
    return pilih_masuk()


def login_token():
    """Disabled: original function accepted a Facebook access token."""
    clear_screen()
    show_logo()
    print(50 * "\x1b[1;91m─")
    print("\x1b[1;93mFacebook token login is not implemented in this safe conversion.")
    input("\n\x1b[1;93m[\x1b[1;91mReturn\x1b[1;93m]")
    masuk()


def login_cookie():
    """Disabled: original function accepted a Facebook session cookie."""
    clear_screen()
    show_logo()
    print(50 * "\x1b[1;91m─")
    print("\x1b[1;93mFacebook cookie login is not implemented in this safe conversion.")
    input("\n\x1b[1;93m[\x1b[1;91mReturn\x1b[1;93m]")
    masuk()


def dump():
    clear_screen()
    print(50 * "\x1b[1;91m─")
    print("\x1b[1;97m1). Dump ID Of Friends")
    print("\x1b[1;97m2). Dump ID Of Followers")
    print("\x1b[1;97m3). Dump ID Of Reactors")
    print("\x1b[1;91m0\x1b[1;97m).\x1b[1;97m Back")
    print(50 * "\x1b[1;91m─")
    dump_pilih()


def dump_pilih():
    cuih = input(" *--> ").strip()
    if cuih == "":
        print(" WRONG!")
        return dump_pilih()
    if cuih in {"1", "01"}:
        return id_teman()
    if cuih in {"2", "02"}:
        return idfrom_follow()
    if cuih in {"3", "03"}:
        return idfrom_react()
    if cuih in {"0", "00"}:
        return hapus()
    print(" WRONG!")
    return dump_pilih()


def ensure_out_dir():
    os.makedirs("out", exist_ok=True)


def save_local_ids(items, filename):
    """Generic local-only helper for writing already-provided ID/name pairs."""
    ensure_out_dir()
    path = os.path.join("out", filename)
    with open(path, "w", encoding="utf-8") as fh:
        for item_id, name in items:
            fh.write(f"{item_id}|{name}\n")
    return path


def id_teman():
    disabled_feature("Friend-ID dumping")


def idfrom_follow():
    disabled_feature("Follower-ID dumping")


def idfrom_react():
    disabled_feature("Reaction-ID dumping")


if __name__ == "__main__":
    dump()
