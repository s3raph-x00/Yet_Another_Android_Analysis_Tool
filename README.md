# This Project Is Still In Early Alpha #

## Yet Another Android Analysis Tool (YAAAAT) ###

##### Because it is still in pre-alpha, there are alot of bugs. Please let me know if you run into any issues and I'll try my best to knock them out. #####

##### At this time, Python 2.7 is the primary supported implementation. This is primarily because Autopsy is still using Python 2. #####

### Background: 

    ######################################################################
    ### The name and the methodology stems from a need to be able to   ###
    ### conduct larger scale Android forensics. This does not replace  ###
    ### industry tools such as Cellebrite, etc but rather augments     ###
    ### the analysis and data already collected.                       ###
    ######################################################################

### DESCRIPTION:

    ######################################################################
    ### SYNOPSIS:    Collection Starts Either Automated (In Autopsy)   ###
    ###              or manually (via CLI). Each script has it's own   ###
    ###              -h switch depending on what you want to do.       ###
    ######################################################################

The core functionality of the tool requires the associated binaries to be in the ./ directory. Plan accordingly prior to running. 
- Test software and script prior to using in a live enviorment

Each script is intended on being ran individually if required (i.e. APK Ripper can be ran as a stand alone script). 
However, the current intent is to run one of the following:
<blockquote>
# YAAAAT_0_AUT.py // Autopsy Plugin (Currently in Active Development and Testing)<br/>
# YAAAAT_0_CLI.py // Command Line Version (Currently in Active Development and Testing)<br/>
# YAAAAT_0_WEB.py // Local webpage (Currently Being Developed)<br/>
# YAAAAT_0_GUI.py // Graphical User Interface (Planned)<br/>
</blockquote>
    
### REQUIREMENTS: <br />
Note: Store Binaries (And Their Associated DLLs/Files) In The Following Folder Structure:<br/>
<blockquote>
#   ./YAAAAT*.py<br/>
#      ./win/<br/>
#         ./win/strings.exe<br/>
#         ./win/ssdeep.exe<br/>
#         ./win/openssl.exe (and associated dlls)<br/>
#         ./win/lib/(jadx classes)<br/>
#         ./win/bin/jadx.bat<br/>
#         ./win/bin/jadx.exe<br/>
#         ./win/bin/yarac64.exe<br/>
#         ./win/bin/yara64.exe<br/>
</blockquote>
    
### Current Development Status 
  1. Autopsy Plugin
     - [X] Core Functionality <br />
       &#9746; Switches and Parametization<br/>
       &#9746; Testing<br/>
     - [ ] GUI   
  2. Python Ripper
     - [ ] Decompile and Analysis Functionaliy
       - &#9746; APK decompilation and analysis<br/>   
       - &#9746; JAR decompilation and analysis<br/>
       - &#9746; DEX decompilation and analysis<br/>
       - &#9746; CLASS decompilation and analysis<br/>
       - &#9746; XAPK decompilation and analysis<br/>
       - &#9746; SO decompilation and analysis<br/>
       - [ ] OAT decompilation and analysis<br/>
       - [ ] ELF decompilation and analysis<br/>
       - [ ] vDEX/cDEX decompilation and analysis<br/>
       - [ ] Testing 
     - [ ] GUI   

##### Legend:
- - [X] - Completed <br />
&#9746; - Partially Completed
- - [ ] - Not Started

##### Known Issues:
  1. Everything

### Updating The Core Binaries

When updating various binaries, ensure the name matches what is currently in the directory and copy over any associated files. 

### Where To Get The Core Binaries: <br />
strings: https://docs.microsoft.com/en-us/sysinternals/downloads/strings <br />
openssl: https://www.openssl.org/source/ <br />
jadx:    https://github.com/skylot/jadx/releases <br />
yara:    https://github.com/VirusTotal/yara/releases <br />
ssdeep:  https://github.com/ssdeep-project/ssdeep <br />
