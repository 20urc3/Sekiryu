import os
import platform
import shutil
import subprocess
import sys
import tempfile
import requests
import zipfile
from pathlib import Path

def download_file(url, output_path):
    response = requests.get(url)
    response.raise_for_status()
    with open(output_path, "wb") as out_file:
        out_file.write(response.content)

def extract_zip(zip_path, extract_dir):
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(extract_dir)

def install_ghidra():
    ghidra_url = "https://github.com/NationalSecurityAgency/ghidra/releases/download/Ghidra_10.3_build/ghidra_10.3_PUBLIC_20230510.zip"
    download_path = os.path.join(tempfile.gettempdir(), "ghidra.zip")
    download_file(ghidra_url, download_path)

    extract_dir = os.path.join("/home/", "ghidra")
    os.makedirs(extract_dir, exist_ok=True)
    extract_zip(download_path, extract_dir)

    os.environ["GHIDRA_HOME_PATH"] = os.path.join(extract_dir, "ghidra_10.3_PUBLIC_20230510")

def download_and_extract_gradle():
    gradle_url = "https://downloads.gradle.org/distributions/gradle-8.1.1-bin.zip"
    download_path = os.path.join(tempfile.gettempdir(), "gradle.zip")
    download_file(gradle_url, download_path)

    extract_dir = os.path.join("/home/", "gradle")
    os.makedirs(extract_dir, exist_ok=True)
    extract_zip(download_path, extract_dir)

    os.environ["GRADLE_HOME"] = os.path.join(extract_dir, "gradle-8.1.1")

def main():

    download_and_extract_gradle()
    install_ghidra()

    print("Gradle extracted to:", os.environ["GRADLE_HOME"])
    print("Ghidra extracted to:", os.environ["GHIDRA_HOME_PATH"])

if __name__ == "__main__":
    main()
