#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
import argparse
import shutil

def run(cmd):
    p = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return p.stdout.strip(), p.stderr.strip()

def exists(cmd):
    return shutil.which(cmd) is not None

# ---------------- APT ----------------
def apt_search(query):
    out, err = run(["apt", "search", query])
    results = []

    for line in out.splitlines():
        if "/" in line and not line.startswith("Sorting"):
            name = line.split("/")[0]
            parts = line.split()
            version = parts[1] if len(parts) > 1 else ""
            results.append((name, version))
    return results[:10]

def apt_info(pkg):
    out, err = run(["apt-cache", "show", pkg])
    info = {"Version": "", "Installed-Size": "", "Depends": ""}

    for line in out.splitlines():
        for key in info:
            if line.startswith(key + ":"):
                info[key] = line.split(":", 1)[1].strip()
    return info

# ---------------- SNAP ----------------
def snap_search(query):
    if not exists("snap"):
        return []
    out, err = run(["snap", "find", query])
    results = []
    for line in out.splitlines()[1:]:
        parts = line.split()
        if parts:
            results.append(parts[0])
    return results[:10]

# ---------------- FLATPAK ----------------
def flatpak_search(query):
    if not exists("flatpak"):
        return []
    out, err = run(["flatpak", "search", query])
    results = []
    for line in out.splitlines()[1:]:
        parts = line.split()
        if parts:
            results.append(parts[0])
    return results[:10]

# ---------------- MAIN ----------------
def main():
    parser = argparse.ArgumentParser(description="OSOP Arama ve Kesif Araci")
    parser.add_argument("paket", help="Aranacak paket adi")
    args = parser.parse_args()

    print("\nAPT Sonuclari:")
    for name, version in apt_search(args.paket):
        info = apt_info(name)
        print(f"- {name} ({version})")
        print(f"  Version: {info['Version']}")
        print(f"  Boyut: {info['Installed-Size']} KB")
        print(f"  Bagimliliklar: {info['Depends']}")

    print("\nSNAP Sonuclari:")
    for name in snap_search(args.paket):
        print(f"- {name}")

    print("\nFLATPAK Sonuclari:")
    for name in flatpak_search(args.paket):
        print(f"- {name}")

if __name__ == "__main__":
    main()
