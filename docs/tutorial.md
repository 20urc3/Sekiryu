# Tutorial 

## Ghidra

Ghidra is a free, open-source software tool that is used for reverse engineering and analyzing software binaries. It was developed by the National Security Agency (NSA) and was released to the public in 2019. In this tutorial, we will go through the steps required to install Ghidra 

    Download Ghidra:
        Go to the official Ghidra website at https://ghidra-sre.org/
        Click on the "Download Ghidra" button.
        Choose the version of Ghidra that you want to download.

    Extract the Ghidra archive:
        Once the download is complete, extract the Ghidra archive to a location of your choice.
        The archive file will be in .zip format.
        To extract the files, right-click on the archive file and select "Extract All".

    Configure Java:
        Ghidra requires Java to run.
        If you don't already have Java installed on your computer, you can download and install it from the official Java website.
        Once Java is installed, make sure that it is added to your computer's PATH environment variable.

    Run Ghidra:
        Navigate to the location where you extracted the Ghidra files.
        Open the "ghidra" folder and double-click on the "ghidraRun" script.
        Ghidra should now start up and you should see the Ghidra Project Manager.

    Create a Ghidra Project:
        To start using Ghidra, you need to create a new project.
        Click on "File" > "New Project".
        Choose a location for your project and give it a name.
        Click "Finish" to create the project.

Congratulations! You have successfully installed Ghidra on your computer and created a new project. Now you can start analyzing software binaries using Ghidra.

## Ghidrathon

Ghidrathon is a Ghidra extension that adds Python 3 scripting capabilities to Ghidra. Why? Ghidra natively supports scripting in Java and Jython. Unfortunately many 
open-source analysis tools, like capa, Unicorn Engine, angr, etc., are written in Python 3 making it difficult, and in some cases, impossible to use these tools
in Ghidra. More so the security community has released several great plugins for other SRE frameworks like IDA Pro and Binary Ninja, but again, because many of 
these plugins use Python 3 it is difficult to port them to Ghidra. Ghidrathon helps you use existing and develop new Python 3 tooling in Ghidra and script 
Ghidra using modern Python in a way that tightly integrates with Ghidra's UI.

Requirements

### The following tools are needed to build, install, and run Ghidrathon:
  Tool 	Version 	Source
  Ghidra 	>= 10.2 	https://ghidra-sre.org
  Jep 	>= 4.1 	https://github.com/ninia/jep
  Gradle 	>= 7.3 	https://gradle.org/releases
  Python 	>= 3.7 	https://www.python.org/downloads

Note: Ghidra >= 10.2 requires JDK 17 64-bit.
Python Virtual Environments

Ghidrathon supports Python virtual environments. To use a Python virtual environment, simply build Ghidrathon inside your virtual environment and execute Ghidra inside the same virtual environment.
Building Ghidrathon

Note: Review Python Virtual Environments before building if you would like to use a Python virtual environment for Ghidrathon.
Note: Building Ghidrathon requires building Jep. If you are running Windows, this requires installing the Microsoft C++ Build Tools found here. See Jep's documentation here for more information on installing Jep on Windows.

### Use the following steps to build Ghidrathon for your environment:

    Install Ghidra using the documentation here
    Install Gradle from here
    Download the latest Ghidrathon source release from here
    Run the following command from the Ghidrathon source directory:
        Note: Ghidrathon defaults to the Python binary found in your path. You can specify a different Python binary by adding the optional argument -PPYTHON_BIN=<absolute path to Python binary> to the command below
        Note: you may optionally set an environment variable named GHIDRA_INSTALL_DIR instead of specifying -PGHIDRA_INSTALL_DIR

    $ gradle -PGHIDRA_INSTALL_DIR=<absolute path to Ghidra install>

This command installs Jep, configures Ghidrathon with the necessary Jep binaries, and builds Ghidrathon. If successful, you will find a new directory in your Ghidrathon source directory named dist containing your Ghidrathon extension (.zip). Please open a new issue if you experience any issues building Ghidrathon.
Installing Ghidrathon

### Use the following steps to install your Ghidrathon extension in Ghidra:

    Start Ghidra
    Navigate to File > Install Extensions...
    Click the green + button
    Navigate to your Ghidrathon extension built earlier (.zip)
    Click Ok
    Restart Ghidra

### Disabling Jython

Ghidrathon disables the built-in Jython script provider to avoid conflicts when Ghidra decides which provider should handle scripts with the .py file extension. This means existing Jython scripts cannot be executed with Ghidrathon installed. We recommend completely disabling the Jython extension.

### Use the following steps to disable the Jython extension:

    Navigate to File > Configure...
    Click Ghidra Core
    Un-check PythonPlugin

### Use the following steps to enable the Jython extension:

    Uninstall Ghidrathon
    Enable the Jython extension using the steps outlined above
    Restart Ghidra
   
 
# GhidrAI

In order to run the GhidrAI script, you must download the .py files contains in this repository. 
You can simply put those file in your "ghidraScripts" folder or copy them manually:
    
    Open Ghidra
    Open Windows > Script Manager
    Create a new Python3 script
    Copy paste the code
