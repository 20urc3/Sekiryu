import os
import platform
import shutil
import subprocess
import sys
import tempfile
import urllib.request
import zipfile
from pathlib import Path

def download_file(url, output_path):
    with urllib.request.urlopen(url) as response:
        with open(output_path, "wb") as out_file:
            shutil.copyfileobj(response, out_file)

def extract_zip(zip_path, extract_dir):
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(extract_dir)

def install_openjdk_linux():
    openjdk_url = "https://objects.githubusercontent.com/github-production-release-asset-2e65be/372925194/eba38ebd-edd2-4004-bb5d-1268cdcbf31a?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIWNJYAX4CSVEH53A%2F20230517%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230517T194640Z&X-Amz-Expires=300&X-Amz-Signature=dd3e3b06fae05df6750784d626740a1339562b53af681db5e50a5c474b045fa2&X-Amz-SignedHeaders=host&actor_id=94982366&key_id=0&repo_id=372925194&response-content-disposition=attachment%3B%20filename%3DOpenJDK17U-jdk_x64_linux_hotspot_17.0.7_7.tar.gz&response-content-type=application%2Foctet-stream"
    download_path = os.path.join(tempfile.gettempdir(), "openjdk.tar.gz")
    download_file(openjdk_url, download_path)

    extract_dir = os.path.join(tempfile.gettempdir(), "openjdk")
    os.makedirs(extract_dir, exist_ok=True)
    subprocess.run(["tar", "-xf", download_path, "-C", extract_dir], check=True)

    os.environ["JAVA_HOME"] = os.path.join(extract_dir, "java-17-openjdk")

def install_openjdk_windows():
    openjdk_url = "https://objects.githubusercontent.com/github-production-release-asset-2e65be/372925194/94b023fd-de41-4b88-b179-c96ad68ff7fd?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIWNJYAX4CSVEH53A%2F20230517%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230517T194706Z&X-Amz-Expires=300&X-Amz-Signature=fa56f67370bdd149e3169befa90c62ebdabd344fd49c685046b91e56f65774ea&X-Amz-SignedHeaders=host&actor_id=94982366&key_id=0&repo_id=372925194&response-content-disposition=attachment%3B%20filename%3DOpenJDK17U-jdk_x64_windows_hotspot_17.0.7_7.zip&response-content-type=application%2Foctet-stream"
    download_path = os.path.join(tempfile.gettempdir(), "openjdk.zip")
    download_file(openjdk_url, download_path)

    extract_dir = os.path.join(tempfile.gettempdir(), "openjdk")
    os.makedirs(extract_dir, exist_ok=True)
    with zipfile.ZipFile(download_path, "r") as zip_ref:
        zip_ref.extractall(extract_dir)

    os.environ["JAVA_HOME"] = os.path.join(extract_dir, "java-17-openjdk")

def install_ghidra():
    ghidra_url = "https://github.com/NationalSecurityAgency/ghidra/releases/download/Ghidra_10.3_build/ghidra_10.3_PUBLIC_20230510.zip"
    download_path = os.path.join(tempfile.gettempdir(), "ghidra.zip")
    download_file(ghidra_url, download_path)

    extract_dir = os.path.join(tempfile.gettempdir(), "ghidra")
    os.makedirs(extract_dir, exist_ok=True)
    extract_zip(download_path, extract_dir)

    os.environ["GHIDRA_HOME_PATH"] = os.path.join(extract_dir, "ghidra_10.3_PUBLIC_20230510")

def download_and_extract_gradle():
    gradle_url = "https://downloads.gradle.org/distributions/gradle-8.1.1-bin.zip"
    download_path = os.path.join(tempfile.gettempdir(), "gradle.zip")
    download_file(gradle_url, download_path)

    extract_dir = os.path.join(tempfile.gettempdir(), "gradle")
    os.makedirs(extract_dir, exist_ok=True)
    extract_zip(download_path, extract_dir)

    os.environ["GRADLE_HOME"] = os.path.join(extract_dir, "gradle-8.1.1")

def install_jep():
    subprocess.run([sys.executable, "-m", "pip", "install", "jep"], check=True)

def main():
    system = platform.system()

    if system == "Linux":
        install_openjdk_linux()
    elif system == "Windows":
        install_openjdk_windows()
    else:
        print("Unsupported operating system: " + system)
        sys.exit(1)

    download_and_extract_gradle()
    install_jep()
    install_ghidra()

    print("Java installed at:", os.environ["JAVA_HOME"])
    print("Gradle extracted to:", os.environ["GRADLE_HOME"])
    print("Ghidra extracted to:", os.environ["GHIDRA_HOME_PATH"])

if __name__ == "__main__":
    main()
