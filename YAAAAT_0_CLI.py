########################################################################################################################################
#################################################### Author:      s3raph                ################################################
#################################################### Purpose:     To Pass the Butter    ################################################
#################################################### Version:     .07155                ################################################
#################################################### Last Update: 20250311              ################################################
########################################################################################################################################

import sys
import platform
import os
import time
import subprocess
import shutil
import sys
import json
import getopt
import glob
import hashlib
import re
import base64
from subprocess import Popen
from zipfile import ZipFile
from struct import pack, unpack
from xml.sax.saxutils import escape

if sys.version_info >= (2, 7, 0) and sys.version_info < (3, 0, 0):
    import urlparse
if sys.version_info >= (3, 0, 0):
    import urllib.parse
    print("[ERROR]: Python 3 Not Supported At This Time.")
    sys.exit()

def func_fail_whale():
########################################################################################################################################
########################################################### FAIL WHALE FUNCTION ########################################################
########################################################################################################################################
    print(u"\u2584\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2584\u2590\u2588\u2584\u2584\u2584\u2584\u2588\u258c")
    print(u"\u2588\u2588\u2588\u2588\u2588\u2588\u258c\u2584\u258c\u2584\u2590\u2590\u258c\u2588\u2588\u2588\u258c\u2580\u2580\u2588\u2588\u2580\u2580")
    print(u"\u2588\u2588\u2588\u2588\u2584\u2588\u258c\u2584\u258c\u2584\u2590\u2590\u258c\u2580\u2588\u2588\u2588\u2584\u2584\u2588\u258c")
    print(u"\u2584\u2584\u2584\u2584\u2584\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2580")
    time.sleep(.5) 
    print("[ERROR]: Error Occured")
    time.sleep(.3)
    print("[INFO]: Trying Process Again")
    time.sleep(.5)
    return

def func_hello():
########################################################################################################################################
########################################################### MUCH ASCII FUNCTION ########################################################
########################################################################################################################################
    print("")
    print(" @@@ @@@ @@@@@@@@ @@@@@@@       @@@@@@  @@@  @@@  @@@@@@  @@@@@@@ @@@  @@@ @@@@@@@@ @@@@@@@        @@@@@@  @@@  @@@ @@@@@@@  @@@@@@@   @@@@@@  @@@ @@@@@@@ ")
    print(" @@! !@@ @@!        @@!        @@!  @@@ @@!@!@@@ @@!  @@@   @@!   @@!  @@@ @@!      @@!  @@@      @@!  @@@ @@!@!@@@ @@!  @@@ @@!  @@@ @@!  @@@ @@! @@!  @@@")
    print("  !@!@!  @!!!:!     @!!        @!@!@!@! @!@@!!@! @!@  !@!   @!!   @!@!@!@! @!!!:!   @!@!!@!       @!@!@!@! @!@@!!@! @!@  !@! @!@!!@!  @!@  !@! !!@ @!@  !@!")
    print("   !!:   !!:        !!:        !!:  !!! !!:  !!! !!:  !!!   !!:   !!:  !!! !!:      !!: :!!       !!:  !!! !!:  !!! !!:  !!! !!: :!!  !!:  !!! !!: !!:  !!!")
    print("   .:    : :: :::    :          :   : : ::    :   : :. :     :     :   : : : :: ::: !:   : :       :   : : ::    :  :: :  :   :   : :  : :. :  :   :: :  : ")
    print("                                @@@@@@  @@@  @@@  @@@@@@  @@@   @@@ @@@  @@@@@@ @@@  @@@@@@       @@@@@@@  @@@@@@   @@@@@@  @@@    ")
    print("                               @@!  @@@ @@!@!@@@ @@!  @@@ @@!   @@! !@@ !@@     @@! !@@             @@!   @@!  @@@ @@!  @@@ @@!    ")
    print("                               @!@!@!@! @!@@!!@! @!@!@!@! @!!    !@!@!   !@@!!  !!@  !@@!!          @!!   @!@  !@! @!@  !@! @!!    ")
    print("                               !!:  !!! !!:  !!! !!:  !!! !!:     !!:       !:! !!:     !:!         !!:   !!:  !!! !!:  !!! !!:    ")
    print("                                :   : : ::    :   :   : : : ::.::.:    ::.: :  :   ::.: :           :     : :. :   : :. :  : ::.: :")
    print("")
    print("") 
    print("                                                         __..--"".          .""--..__                 ")#Credits For The ASCII Scythe Go To: David Palmer
    print("                                                   _..-``       ][\        /[]       ``-.._           ")
    print("                                               _.-`           __/\ \      / /\__           `-._       ")
    print("                                            .-`     __..---```    \ \    / /    ```---..__     `-.    ")
    print("                                          .`  _.--``               \ \  / /               ``--._  `.    ")
    print("                                         / .-`                      \ \/ /                      `-. \    ")
    print("                                        /.`                          \/ /                          `.\    ")
    print("                                       |`                            / /\                            `|    ")
    print("                                                @@@@@@@  @@@ @@@@@@@  @@@@@@@  @@@@@@@@ @@@@@@@ ")
    print("                                                @@!  @@@ @@! @@!  @@@ @@!  @@@ @@!      @@!  @@@")
    print("                                                @!@!!@!  !!@ @!@@!@!  @!@@!@!  @!!!:!   @!@!!@! ")
    print("                                                !!: :!!  !!: !!:      !!:      !!:      !!: :!! ")
    print("                                                 :   : : :    :        :       : :: :::  :   : :")

def func_goodbye():
########################################################################################################################################
############################################################# SUCH END FUNCTION ########################################################
########################################################################################################################################
    print("")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$NN$$$$$$$NN$$$$N$N$NN$$$$$N$$$$$$$$NNN$$NN$$$$NNNNNNN$$$N$$$NNN$$$$$$N$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$NNV.....:.VN..........M..........F$$$$F:::*VNNV:::VMM*.....*MNMM.....*NNV...*N$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$N.........*M..........M..........MNNNN:....:MN:...*..........VMM......NN*....N$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$N....NN*..NN.....NM:..N....*NM:..NN$$NN*...IM*..**....MNNN:...MN....*$N$$..N$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$N......NMNNM....I..*NNM....I..INN$$$$N$N.......MV....IMNNN*...:M....N$N$...NN$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$NN.......NN........NMN........MN$$$$$N$N.....:NN.....NNN$N....V.....NNNN..MN$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$NNNM*.....MN....MF..NNN....M*..MN$$$$$$$N....VNNN....VNNNNM....N....N$$N...N$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$...NNN....M.....MNN...V....NNM...$$$$$$$N....NNNNV....MMMV....MN....NNNV..M$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$F.........*......................M$$$$$$*.....MNNNN:..........MMN.........:N$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$NVNM:..*MNMVVVVVVVFVVIIVVVVVVVVVIN$$$$$NMVVVVVN$$$$NNMV...*MNN$$$NNI...*MNN$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$$$NNNNNNNNNNNNNN$$$NNNN$$NNNMN$$$$$$$NNNNNNNNNNNNNNNNNNNNN$$$$$NNNNNMNNNNNNNNNNNMMNNNNNNNNNNMNNNNNNNNNNNN$N$$$$$$$$$$$$$$NNNNNNN$$$NNNNNN$NNNNN$$$$$$$$$$$$$$")
    print("$$$N*.........M..........NNM....N$$$$*.........V..........N$$$$NNM.........MMV.........N:.....:......MN..............NNNF.........NM......N*....N$$$$$$$$$$$$$")
    print("$$$M....MM...VNM....M.....MV....NNNM.....MM....N....:MV...N$N$$N:....IMF...M.....MNF....M.....NM....MNN...FM....I....*N.....NNN....M*....NN*...MN$$$$$$$$$$$$$")
    print("$$$I.....MN**NN.....M....:*.....F$M.....NNNN..MI....M*.V.MNN$NM.....NNNN..V....VNNNN.....M....NM....MN...NN....MM:...V....*N$$N*...IN....M...MN$$$$$$$$$$$$$$$")
    print("$$$N.......MNNN..........*.......N.....M$$NNNNN........NNN$NNM:....NN$$NNN*....NN$$N.....M....N*....M...MNM.........VM....N$$$$*...M$V......NN$$$$$$$$$$$$$$$$")
    print("$$$$$M......VN........VM.........N....VN$$$$NNM....V...NNNNNNN....VNN$$NN$.....$NNNM....IM.............NNN....:*....*:...M$$$$N....MNN....*N$$$$$$$$$$$$$$$$$$")
    print("$N..MNNI.....M....M$NNM..........N....INNNNVNM.....MMM..VNNNNN....VNNNNFMN*....N$MM.....NN......M....:NNNM....NNM....M...N$$$$*...*NNI....NNV.:NNI..MMM..IN$$$")
    print("$*....M.....V.....N$$V....MNM.....*.....................MNNNNNF..........MM....VI.....*N$N....:NN..*INNNM*..........INV...MNM:...INN*.....N*....M....M....MN$$")
    print("$..........M......V$$.....NN......MF.......MV...........NN$$$$$M.......*NNNN*.......VN$$$N:...MNN..MN$$NV..........MN$NF:......VN$$N......NM...:M....M....NN$$")
    print("$$NN$$$$$$$NN$$$N$$$$$$N$NNNN$$NNN$$N$N$NNN$$NNNNNNNNNNN$$$$$$$NNNNNNNNN$$NNNNNNNNNNN$$$$NNNNNNN$N$$$$NN$$$$$$$$$NN$$$$$$$$$$$$$$$$$NN$$$N$$$NNNNNNNNN$NN$N$$$")
    print("")

def func_gu_st():
########################################################################################################################################
########################################################### GUCCI MODE FUNCTION ########################################################
########################################################################################################################################
    if arg_verbose_output == 1:
        if arg_gucci_output == 1:
            func_set_console_strobe()
            os.system('color 04')

def func_python_version_check():
########################################################################################################################################
########################################################## PYTHON CHECK FUNCTION #######################################################
########################################################################################################################################
    global var_python_version_info
    global var_python_version2_check
    global var_python_version3_check
    var_current_function = "func_python_version_check"
    
    if sys.version_info >= (2, 7, 0) and sys.version_info < (3, 0, 0):
        var_python_version2_check = "TRUE"
        var_python_version3_check = "FALSE"
        var_python_version_info = "2.7+"
        var_py_complete_flag = 1
    elif sys.version_info >= (3, 0, 0):
        var_python_version2_check = "FALSE"
        var_python_version3_check = "TRUE"
        var_python_version_info = "3.0+"  
        var_py_complete_flag = 1
    else:
        print("[ERROR]: Python Version Does Not Appear to Be Supported")
        print("[WARN]: Python 2.7+ or 3.1+ is a requirement")
        func_fail_whale()

def func_determine_operating_system():
########################################################################################################################################
####################################################### O/S DETERMINATION FUNCTION #####################################################
########################################################################################################################################
    var_current_function = "func_determine_operating_system"
    try:
        global var_OS_ver_A
        global var_OS_ver_B
        global var_OS_ver_C
        global var_OS_ver_D
        global var_OS_ver_E
        global var_OS_main_ver
        global var_PY_ver_A
        global var_PY_ver_B
        global var_PY_ver_C
        global var_sys_complete_flag
        
        var_OS_ver_A = platform.system()
        var_OS_ver_B = os.name
        var_OS_ver_C = sys.platform
        var_OS_ver_D = platform.platform()
        var_OS_ver_E = platform.processor()
        var_OS_main_ver = "O/S: " + platform.platform()
        var_PROC_model = "Processor: " + platform.processor()
        var_PY_ver_A = platform.python_version()
        var_PY_ver_B = sys.version
        var_PY_ver_C = sys.version_info
        var_sys_complete_flag = 1
    except:
        var_manual_error_code = 1
        print("[WARN]: Operating System Determination Failed")
        time.sleep(.5)
        func_fail_whale()

### Console/Error Text Color ###
def func_set_console_color_for_errors():
########################################################################################################################################
######################################################### CONSOLE COLOR FUNCTION #######################################################
########################################################################################################################################
    if var_manual_error_code == (0): ## This Means Normal Operation
        os.system('color 70') 
        return
    if var_manual_error_code == (1): ## This Means Major Error (Hard Fail)
        func_set_console_strobe()
        os.system('color 4F') 
        func_fail_whale()
    if var_manual_error_code == (2): ## This Means Minor Error (Attempting to Recover)
        func_fail_whale()
    else:
        print("Error")

def func_set_console_strobe():
########################################################################################################################################
############################################################ STROBE FUNCTION ###########################################################
########################################################################################################################################
    var_current_function = "func_set_console_strobe"    
    os.system('color 7C')
    time.sleep(.1)
    os.system('color C7')
    time.sleep(.1)
    os.system('color 7C') 
    time.sleep(.1)
    os.system('color C7')
    time.sleep(.1)
    os.system('color 7C')
    time.sleep(.1)

def func_clean_up():
########################################################################################################################################
######################################################### Post-Run Clean Up Function ###################################################
########################################################################################################################################
    if var_forensic_case_bool == 1:
        log_txt_update.close()
    #cert_unproc_txt_update.close()
    os.system('color 07')
    func_goodbye()

def func_initial_logging():
########################################################################################################################################
########################################################## Inital Log File Creation ####################################################
########################################################################################################################################
    if var_forensic_case_bool == 1:
        case_log_file_txt = var_case_delivery_directory + "\\log.txt"
        global log_txt_update
        log_txt_update = open(case_log_file_txt, "a")
        log_txt_update.write("--- YAAAAT CLI Started ---\n")
        log_txt_update.write("[LOG]: CLI Started on: " + timestr_case + " at " + timestr_dir + "\n")  

def randomFunction():
    return "import sys; print(sys.argv[1]); input('Press Enter..')"

def func_command_call():
########################################################################################################################################
############################################################ Command Call Creation #####################################################
########################################################################################################################################
    if script_ext_location_check == 0:
        return
    if script_ext_location_check == 1:
        if platform.system() == "Windows":
            var_core_command = "cmd.exe /c python ./YAAAAT_1_apk_ripper.py "
            if arg_custom_search == 2:
                if arg_string_file_search != "":
                    var_core_command = var_core_command + " " + "-S " + arg_string_file_search + " "
                else:
                    print("error")
            if var_yara_flag == 1:
                var_core_command = var_core_command + " " + "-y "
            if arg_custom_search == 1:
                if arg_string_search != "":
                    var_core_command = var_core_command + " " + "-s " + arg_string_search + " "
            if arg_debug_output == 1:
                var_core_command = var_core_command + " " + "-r "
            if var_forensic_case_bool == 1:
                var_core_command = var_core_command + " " + "-l "
            if arg_gucci_output == 1:
                var_core_command = var_core_command + " " + "-g "
            if arg_verbose_output == 1:
                var_core_command = var_core_command + " " + "-v "
            if arg_autopsy_plugin == 1:
                var_core_command = var_core_command + " " + "-a "
            if var_output_directory_empty != "":
                var_core_command = var_core_command + " " + "-o " + var_case_delivery_directory
            var_core_command = var_core_command + " -i " + inputdirectory_var + " "
            if var_forensic_case_bool == 1:
                log_txt_update.write("[LOG]: CLI passing the following command to APK Ripper: " + var_core_command + "\n")
            if arg_verbose_output == 1:
                print("[LOG]: CLI passing the following command to APK Ripper: " + var_core_command)
            var_command_setup_split = var_core_command.split()
        else:  
            var_command_setup_split = "x-terminal-emulator -e".split()
        echo = [sys.executable, "-c",randomFunction()
                ]
        processes = [Popen(var_command_setup_split)]
        for proc in processes:
            proc.wait()
    if script_ext_location_check == 2:
        if platform.system() == "Windows":
            var_core_command = "cmd.exe /c python ./YAAAAT_1_xapk_ripper.py "
            if arg_custom_search == 2:
                if arg_string_file_search != "":
                    var_core_command = var_core_command + " " + "-S " + arg_string_file_search + " "
                else:
                    print("error")
            if var_yara_flag == 1:
                var_core_command = var_core_command + " " + "-y "
            if arg_custom_search == 1:
                if arg_string_search != "":
                    var_core_command = var_core_command + " " + "-s " + arg_string_search + " "
            if arg_debug_output == 1:
                var_core_command = var_core_command + " " + "-r "
            if var_forensic_case_bool == 1:
                var_core_command = var_core_command + " " + "-l "
            if arg_gucci_output == 1:
                var_core_command = var_core_command + " " + "-g "
            if arg_verbose_output == 1:
                var_core_command = var_core_command + " " + "-v "
            if arg_autopsy_plugin == 1:
                var_core_command = var_core_command + " " + "-a "
            if var_output_directory_empty != "":
                var_core_command = var_core_command + " " + "-o " + var_case_delivery_directory
            var_core_command = var_core_command + " -i " + inputdirectory_var + " "
            if var_forensic_case_bool == 1:
                log_txt_update.write("[LOG]: CLI passing the following command to xAPK Ripper: " + var_core_command + "\n")
            if arg_verbose_output == 1:
                print("[LOG]: CLI passing the following command to xAPK Ripper: " + var_core_command)
            var_command_setup_split = var_core_command.split()
        else:  
            var_command_setup_split = "x-terminal-emulator -e".split()
        echo = [sys.executable, "-c",randomFunction()
                ]
        processes = [Popen(var_command_setup_split)]
        for proc in processes:
            proc.wait()
    if script_ext_location_check == 3:
        if platform.system() == "Windows":
            var_core_command = "cmd.exe /c python ./YAAAAT_1_oat_ripper.py "
            if arg_custom_search == 2:
                if arg_string_file_search != "":
                    var_core_command = var_core_command + " " + "-S " + arg_string_file_search + " "
                else:
                    print("error")
            if var_yara_flag == 1:
                var_core_command = var_core_command + " " + "-y "
            if arg_custom_search == 1:
                if arg_string_search != "":
                    var_core_command = var_core_command + " " + "-s " + arg_string_search + " "
            if arg_debug_output == 1:
                var_core_command = var_core_command + " " + "-r "
            if var_forensic_case_bool == 1:
                var_core_command = var_core_command + " " + "-l "
            if arg_gucci_output == 1:
                var_core_command = var_core_command + " " + "-g "
            if arg_verbose_output == 1:
                var_core_command = var_core_command + " " + "-v "
            if arg_autopsy_plugin == 1:
                var_core_command = var_core_command + " " + "-a "
            if var_output_directory_empty != "":
                var_core_command = var_core_command + " " + "-o " + var_case_delivery_directory
            var_core_command = var_core_command + " -i " + inputdirectory_var + " "
            if var_forensic_case_bool == 1:
                log_txt_update.write("[LOG]: CLI passing the following command to OAT Ripper: " + var_core_command + "\n")
            if arg_verbose_output == 1:
                print("[LOG]: CLI passing the following command to OAT Ripper: " + var_core_command)
            var_command_setup_split = var_core_command.split()
        else:  
            var_command_setup_split = "x-terminal-emulator -e".split()
        echo = [sys.executable, "-c",randomFunction()
                ]
        processes = [Popen(var_command_setup_split)]
        for proc in processes:
            proc.wait()
    if script_ext_location_check == 4:
        if platform.system() == "Windows":
            var_core_command = "cmd.exe /c python ./YAAAAT_1_dex_ripper.py "
            if arg_custom_search == 2:
                if arg_string_file_search != "":
                    var_core_command = var_core_command + " " + "-S " + arg_string_file_search + " "
                else:
                    print("error")
            if var_yara_flag == 1:
                var_core_command = var_core_command + " " + "-y "
            if arg_custom_search == 1:
                if arg_string_search != "":
                    var_core_command = var_core_command + " " + "-s " + arg_string_search + " "
            if arg_debug_output == 1:
                var_core_command = var_core_command + " " + "-r "
            if var_forensic_case_bool == 1:
                var_core_command = var_core_command + " " + "-l "
            if arg_gucci_output == 1:
                var_core_command = var_core_command + " " + "-g "
            if arg_verbose_output == 1:
                var_core_command = var_core_command + " " + "-v "
            if arg_autopsy_plugin == 1:
                var_core_command = var_core_command + " " + "-a "
            if var_output_directory_empty != "":
                var_core_command = var_core_command + " " + "-o " + var_case_delivery_directory
            var_core_command = var_core_command + " -i " + inputdirectory_var + " "
            if var_forensic_case_bool == 1:
                log_txt_update.write("[LOG]: CLI passing the following command to DEX Ripper: " + var_core_command + "\n")
            if arg_verbose_output == 1:
                print("[LOG]: CLI passing the following command to DEX ripper: " + var_core_command)
            var_command_setup_split = var_core_command.split()
        else:  
            var_command_setup_split = "x-terminal-emulator -e".split()
        echo = [sys.executable, "-c",randomFunction()
                ]
        processes = [Popen(var_command_setup_split)]
        for proc in processes:
            proc.wait()
    if script_ext_location_check == 5:
        if platform.system() == "Windows":
            var_core_command = "cmd.exe /c python ./YAAAAT_1_so_ripper.py "
            if arg_custom_search == 2:
                if arg_string_file_search != "":
                    var_core_command = var_core_command + " " + "-S " + arg_string_file_search + " "
                else:
                    print("error")
            if var_yara_flag == 1:
                var_core_command = var_core_command + " " + "-y "
            if arg_custom_search == 1:
                if arg_string_search != "":
                    var_core_command = var_core_command + " " + "-s " + arg_string_search + " "
            if arg_debug_output == 1:
                var_core_command = var_core_command + " " + "-r "
            if var_forensic_case_bool == 1:
                var_core_command = var_core_command + " " + "-l "
            if arg_gucci_output == 1:
                var_core_command = var_core_command + " " + "-g "
            if arg_verbose_output == 1:
                var_core_command = var_core_command + " " + "-v "
            if arg_autopsy_plugin == 1:
                var_core_command = var_core_command + " " + "-a "
            if var_output_directory_empty != "":
                var_core_command = var_core_command + " " + "-o " + var_case_delivery_directory
            var_core_command = var_core_command + " -i " + inputdirectory_var + " "
            if var_forensic_case_bool == 1:
                log_txt_update.write("[LOG]: CLI passing the following command to SO Ripper: " + var_core_command + "\n")
            if arg_verbose_output == 1:
                print("[LOG]: CLI passing the following command to SO Ripper: " + var_core_command)
            var_command_setup_split = var_core_command.split()
        else:  
            var_command_setup_split = "x-terminal-emulator -e".split()
        echo = [sys.executable, "-c",randomFunction()
                ]
        processes = [Popen(var_command_setup_split)]
        for proc in processes:
            proc.wait()
    if script_ext_location_check == 6:
        if platform.system() == "Windows":
            var_core_command = "cmd.exe /c python ./YAAAAT_1_elf_ripper.py "
            if arg_custom_search == 2:
                if arg_string_file_search != "":
                    var_core_command = var_core_command + " " + "-S " + arg_string_file_search + " "
                else:
                    print("error")
            if var_yara_flag == 1:
                var_core_command = var_core_command + " " + "-y "
            if arg_custom_search == 1:
                if arg_string_search != "":
                    var_core_command = var_core_command + " " + "-s " + arg_string_search + " "
            if arg_debug_output == 1:
                var_core_command = var_core_command + " " + "-r "
            if var_forensic_case_bool == 1:
                var_core_command = var_core_command + " " + "-l "
            if arg_gucci_output == 1:
                var_core_command = var_core_command + " " + "-g "
            if arg_verbose_output == 1:
                var_core_command = var_core_command + " " + "-v "
            if arg_autopsy_plugin == 1:
                var_core_command = var_core_command + " " + "-a "
            if var_output_directory_empty != "":
                var_core_command = var_core_command + " " + "-o " + var_case_delivery_directory
            var_core_command = var_core_command + " -i " + inputdirectory_var + " "
            if var_forensic_case_bool == 1:
                log_txt_update.write("[LOG]: CLI passing the following command to ELF Ripper: " + var_core_command + "\n")
            if arg_verbose_output == 1:
                print("[LOG]: CLI passing the following command to ELF Ripper: " + var_core_command)
            var_command_setup_split = var_core_command.split()
        else:  
            var_command_setup_split = "x-terminal-emulator -e".split()
        echo = [sys.executable, "-c",randomFunction()
                ]
        processes = [Popen(var_command_setup_split)]
        for proc in processes:
            proc.wait()
    if script_ext_location_check == 7:
        if platform.system() == "Windows":
            var_core_command = "cmd.exe /c python ./YAAAAT_1_jar_ripper.py "
            if arg_custom_search == 2:
                if arg_string_file_search != "":
                    var_core_command = var_core_command + " " + "-S " + arg_string_file_search + " "
                else:
                    print("error")
            if var_yara_flag == 1:
                var_core_command = var_core_command + " " + "-y "
            if arg_custom_search == 1:
                if arg_string_search != "":
                    var_core_command = var_core_command + " " + "-s " + arg_string_search + " "
            if arg_debug_output == 1:
                var_core_command = var_core_command + " " + "-r "
            if var_forensic_case_bool == 1:
                var_core_command = var_core_command + " " + "-l "
            if arg_gucci_output == 1:
                var_core_command = var_core_command + " " + "-g "
            if arg_verbose_output == 1:
                var_core_command = var_core_command + " " + "-v "
            if arg_autopsy_plugin == 1:
                var_core_command = var_core_command + " " + "-a "
            if var_output_directory_empty != "":
                var_core_command = var_core_command + " " + "-o " + var_case_delivery_directory
            var_core_command = var_core_command + " -i " + inputdirectory_var + " "
            if var_forensic_case_bool == 1:
                log_txt_update.write("[LOG]: CLI passing the following command to JAR Ripper: " + var_core_command + "\n")
            if arg_verbose_output == 1:
                print("[LOG]: CLI passing the following command to JAR Ripper: " + var_core_command)
            var_command_setup_split = var_core_command.split()
        else:  
            var_command_setup_split = "x-terminal-emulator -e".split()
        echo = [sys.executable, "-c",randomFunction()
                ]
        processes = [Popen(var_command_setup_split)]
        for proc in processes:
            proc.wait()

def main(argv):
########################################################################################################################################
######################################################## Global Variable Definitions ###################################################
########################################################################################################################################
    global log_txt_update
    global case_log_file_txt
    global var_manual_error_code
    global inputdirectory
    global var_case_delivery_directory
    global arg_autopsy_plugin
    global arg_verbose_output
    global arg_gucci_output
    global var_forensic_case_bool
    global timestr_dir
    global timestr_case
    global var_output_directory
    global apk
    global arg_debug_output
    global arg_string_search
    global arg_string_file_search
    global arg_custom_search
    global var_sys_complete_flag
    global var_py_complete_flag
    global var_yara_flag
    global var_apk_ripper_flag
    global var_xapk_ripper_flag
    global var_oat_ripper_flag
    global var_dex_ripper_flag
    global var_so_ripper_flag
    global var_elf_ripper_flag
    global var_jar_ripper_flag
    global inputdirectory_var
    global var_output_directory_empty
    
    timestr_dir = time.strftime("%H-%M-%S")
    timestr_case = time.strftime("%Y-%m-%d")
    inputdirectory_var = ''
    var_output_directory = ''
    var_output_directory_empty = ''
    arg_autopsy_plugin = 0
    arg_verbose_output = 0
    arg_gucci_output = 0
    var_forensic_case_bool = 0
    arg_debug_output = 0
    arg_custom_search = 0
    arg_string_search = ""
    arg_string_file_search = ""
    var_sys_complete_flag = 0
    var_py_complete_flag = 0
    var_yara_flag = 0
    var_apk_ripper_flag = 0
    var_xapk_ripper_flag = 0
    var_oat_ripper_flag = 0
    var_dex_ripper_flag = 0
    var_so_ripper_flag = 0
    var_elf_ripper_flag = 0
    var_jar_ripper_flag = 0
    
    global var_current_function
    var_current_function = "func_main"

########################################################################################################################################
############################################################### STAGE SETTING ##########################################################
########################################################################################################################################

    os.system('cls' if os.name == 'nt' else 'clear')
    func_hello()

########################################################################################################################################
############################################################## HELP AND ARGUMENT #######################################################
########################################################################################################################################

    try:
        opts, args = getopt.getopt(argv,"ABXDOEJhacblrfgyvS:s:o:i:",["idir="])
    except getopt.GetoptError:
        var_manual_error_code = (1)
        func_fail_whale()
        print("YAAAAT_apk_ripper.py    -i <Directory_To_Scan_For_APKs>")
        print("At Least One File Type: -A (.apk)")
        print("                        -X (.xapk)")
        print("                        -O (.oat)")
        print("                        -D (.*dex)")
        print("                        -B (.so)")
        print("                        -E (.elf)")
        print("                        -J (.jar)")
        print("Optional Arguments:     -v (For Verbose Output) ")
        print("                        -a (RTFC) ")        
        print("                        -l (Forensic Case)")
        print("                        -f (Fix My Terminal Color x.x)")
        print("                        -r (Show REGEX Debug Output)")
        print("                        -s (Search for String) <From CLI>")
        print("                        -S (Search for Strings) <From File>")
        print("                        -y (Search with Yara)")
        print("YAAAAT_apk_ripper.py    -o <Output_Directory>")
        os.system('color 07')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("YAAAAT_apk_ripper.py    -i <Directory_To_Scan_For_APKs>")
            print("At Least One File Type: -A (.apk)")
            print("                        -X (.xapk)")
            print("                        -O (.oat)")
            print("                        -D (.*dex)")
            print("                        -B (.so)")
            print("                        -E (.elf)")
            print("                        -J (.jar)")
            print("Optional Arguments:     -v (For Verbose Output) ")
            print("                        -a (RTFC) ")        
            print("                        -l (Forensic Case)")
            print("                        -f (Fix My Terminal Color x.x)")
            print("                        -r (Show REGEX Debug Output)")
            print("                        -s (Search for String) <From CLI>")
            print("                        -S (Search for Strings) <From File>")
            print("                        -y (Search with Yara)")
            print("YAAAAT_apk_ripper.py    -o <Output_Directory>")
            os.system('color 07')
            sys.exit()
        if opt == '-f':
            ############################################################
            ###                     [Not Required]                   ###
            ### Name:    Terminal Color Black                        ###
            ### Arg:     -f                                          ###
            ### Info:    This Argument is Used To Fix Terminal Color ###
            ###          After Crashing/Ending This Application      ###
            ###          Ungracefully in Gucci Mode.                 ###
            ### Note:    In Any Color, As Long as You Want It Black  ###
            ### Default: Disabled                                    ###
            ############################################################
            os.system('color 07')
            sys.exit()
        if opt == '-a':
            ############################################################
            ###                     [Not Required]                   ###
            ### Name:    Post-Autopsy File Normalization             ###
            ### Arg:     -a                                          ###
            ### Info:    This Argument is Used To Remove Characters  ###
            ###          Prepended To Filename During The Autopsy    ###
            ###          Extraction Process.                         ###
            ### Default: Disabled                                    ###
            ############################################################
            arg_autopsy_plugin = 1
        if opt == '-v':
            ############################################################
            ###                     [Not Required]                   ###
            ### Name:    Verbosity                                   ###
            ### Arg:     -v                                          ###
            ### Info:    Sets the Verbosity to Debug                 ###
            ### Default: Silent                                      ###
            ############################################################
            arg_verbose_output = 1 
        if opt == '-g':
            ############################################################
            ###              [Absolutely Not Required]               ###
            ### Name:    Gucci Mode                                  ###
            ### Arg:     -g                                          ###
            ### Info:    Original G. <! Epilepsy Warning !>          ###
            ### Note:    Why the F*** Did I Code This?               ###
            ### Default: Disabled                                    ###
            ############################################################
            arg_gucci_output = 1 
        if opt == '-l':
            ############################################################
            ###                     [Not Required]                   ###
            ### Name:    Forensic Case Logging                       ###
            ### Arg:     -l                                          ###
            ### Info:    Outputs Verbose Logging And Forensic System ###
            ###          Information To Log File in Output Directory.### 
            ### Default: Disabled                                    ###
            ############################################################
            var_forensic_case_bool = 1 
        if opt == '-o':
            ############################################################
            ###                     [Not Required]                   ###
            ### Name:    Output Directory                            ###
            ### Arg:     -o                                          ###
            ### Info:    Sets the Output Directory If Defined.       ###
            ### Default: <Input_Directory>                           ###
            ############################################################
            var_output_directory = arg
        if opt == '-r':
            ############################################################
            ###                     [Not Required]                   ###
            ### Name:    REGEX Debug Output                          ###
            ### Arg:     -r                                          ###
            ### Info:    Outputs what was REGEX'd on for development.###
            ### Default: Disabled                                    ###
            ############################################################
            arg_debug_output = 1 
        if opt == '-s':
            ############################################################
            ###                     [Not Required]                   ###
            ### Name:    String Search <CLI>                         ###
            ### Arg:     -s                                          ###
            ### Info:    Search For A Single String in Output of     ###
            ###          decompiled JADX output.                     ###
            ### Default: ""                                          ###
            ############################################################
            arg_custom_search = 1 
            arg_string_search = arg 
        if opt == '-y':
            ############################################################
            ###                     [Not Required]                   ###
            ### Name:    Yara Search                                 ###
            ### Arg:     -y                                          ###
            ### Info:    Uses rules located in ./yara/ to flag on    ###
            ###          specified alerts.                           ###
            ### Default: Disabled                                    ###
            ############################################################
            var_yara_flag = 1 
        if opt == '-S':
            ############################################################
            ###                     [Not Required]                   ###
            ### Name:    String Search <File>                        ###
            ### Arg:     -S                                          ###
            ### Info:    Search For Strings Contained in Specified   ###
            ###          text file against the Output of decompiled  ###
            ###          JADX output.                                ###
            ### Default: ""                                          ###
            ############################################################
            if not os.path.isfile(arg):
                func_fail_whale()
                print("Search String File Not Found: " + arg)
                sys.exit()
            arg_string_file_search = arg 
            arg_custom_search = 2 
        if opt == '-A':
            ############################################################
            ###               [One Filetype Required]                ###
            ### Name:    Specify APK Files                           ###
            ### Arg:     -A                                          ###
            ### Info:    Search For APK files in specified input     ###
            ###          directory to decompile and analyze.         ###
            ###                                                      ###
            ### Default: ""                                          ###
            ############################################################
            var_apk_ripper_flag = 1
        if opt == '-X':
            ############################################################
            ###               [One Filetype Required]                ###
            ### Name:    Specify xAPK Files                          ###
            ### Arg:     -X                                          ###
            ### Info:    Search For xAPK files in specified input    ###
            ###          directory to decompile and analyze.         ###
            ###                                                      ###
            ### Default: ""                                          ###
            ############################################################
            var_xapk_ripper_flag = 1
        if opt == '-O':
            ############################################################
            ###               [One Filetype Required]                ###
            ### Name:    Specify OAT Files                           ###
            ### Arg:     -O                                          ###
            ### Info:    Search For OAT files in specified input     ###
            ###          directory to decompile and analyze.         ###
            ###                                                      ###
            ### Default: ""                                          ###
            ############################################################
            var_oat_ripper_flag = 1
        if opt == '-D':
            ############################################################
            ###               [One Filetype Required]                ###
            ### Name:    Specify *DEX Files                          ###
            ### Arg:     -D                                          ###
            ### Info:    Search For *DEX files in specified input    ###
            ###          directory to decompile and analyze.         ###
            ###          This includes DEX, VDEX, CDEX, DEX gumbo,   ###
            ###          DEX soup, DEX stew, DEX salad...............###
            ### Default: ""                                          ###
            ############################################################
            var_dex_ripper_flag = 1
        if opt == '-B':
            ############################################################
            ###               [One Filetype Required]                ###
            ### Name:    Specify SO Files                            ###
            ### Arg:     -B                                          ###
            ### Info:    Search For SO files in specified input      ###
            ###          directory to decompile and analyze.         ###
            ###                                                      ###
            ### Default: ""                                          ###
            ############################################################
            var_so_ripper_flag = 1
        if opt == '-E':
            ############################################################
            ###               [One Filetype Required]                ###
            ### Name:    Specify ELF Files                           ###
            ### Arg:     -E                                          ###
            ### Info:    Search For ELF files in specified input     ###
            ###          directory to decompile and analyze.         ###
            ###                                                      ###
            ### Default: ""                                          ###
            ############################################################
            var_elf_ripper_flag = 1
        if opt == '-J':
            ############################################################
            ###               [One Filetype Required]                ###
            ### Name:    Specify JAR Files                           ###
            ### Arg:     -J                                          ###
            ### Info:    Search For JAR files in specified input     ###
            ###          directory to decompile and analyze.         ###
            ###                                                      ###
            ### Default: ""                                          ###
            ############################################################
            var_jar_ripper_flag = 1
        elif opt in ("-i", "--idir"):
            ############################################################
            ###                       [Required]                     ###
            ### Name:    Input Directory                             ###
            ### Arg:     -i                                          ###
            ### Info:    Sets the Input Directory.                   ###
            ### Default: <No Value>                                  ###
            ############################################################
            inputdirectory_var = arg

    if not inputdirectory_var:
        print("")
        print("[ERROR]: MUST SPECIFY DIRECTORY")
        print("")
        print("YAAAAT_apk_ripper.py    -i <Directory_To_Scan_For_APKs>")
        print("At Least One File Type: -A (.apk)")
        print("                        -X (.xapk)")
        print("                        -O (.oat)")
        print("                        -D (.*dex)")
        print("                        -B (.so)")
        print("                        -E (.elf)")
        rint("                        -J (.jar)")
        print("Optional Arguments:     -v (For Verbose Output) ")
        print("                        -a (RTFC) ")        
        print("                        -l (Forensic Case)")
        print("                        -f (Fix My Terminal Color x.x)")
        print("                        -r (Show REGEX Debug Output)")
        print("                        -s (Search for String) <From CLI>")
        print("                        -S (Search for Strings) <From File>")
        print("                        -y (Search with Yara)")
        print("YAAAAT_apk_ripper.py    -o <Output_Directory>")
        os.system('color 07')
        sys.exit()

    inputdirectory_var = inputdirectory_var.replace('\"', '') + "\\"	
    var_output_directory = var_output_directory.replace('\"', '') + "\\"	
    func_gu_st()
    func_python_version_check()

########################################################################################################################################
########################################################## CASE DIRECTORY CREATION #####################################################
########################################################################################################################################
    
    print("########################################################################################################################################")
    print("###################################################### CLI STARTED AT: " + timestr_dir + " ######################################################")
    print("########################################################################################################################################")
    print("")

    if var_output_directory == '':
        var_output_directory = inputdirectory
        print("[INFO]: Output Directory is: " + var_output_directory)
    else:
        var_output_directory_empty = var_output_directory
        print("[INFO]: Output Directory is: " + var_output_directory)
    
    outputdirectory = os.path.dirname(var_output_directory)
    if var_forensic_case_bool == 1:
        var_case_delivery_directory = outputdirectory + "\\" + timestr_case + "_case_info"
        if os.path.exists(var_case_delivery_directory):
            print("[INFO]: Case Directory: " + var_case_delivery_directory + " Already Exists")
        else:
            try:
                os.mkdir(var_case_delivery_directory)
            except:
                print("[WARN]: Error Making Main Case Directory: " + var_case_delivery_directory)
        func_initial_logging()
        func_determine_operating_system()

    if var_sys_complete_flag == 1:
        if var_forensic_case_bool == 1:
            log_txt_update.write("[SYS]: O/S Version is: " + var_OS_main_ver + "\n")
            log_txt_update.write("[SYS]: Python Version is: " + var_PY_ver_A + "\n")
            log_txt_update.write("[SYS]: Full Python Info is: " + var_PY_ver_B + "\n")
        if arg_verbose_output == 1:
            print("[SYS]: O/S Version is: " + var_OS_main_ver)
            print("[SYS]: Python Version is: " + var_PY_ver_A)
            print("[SYS]: Full Python Info is: " + var_PY_ver_B)

########################################################################################################################################
####################################################### EXTRACTION DIRECTORY CREATION ##################################################
########################################################################################################################################

    if var_apk_ripper_flag == 1:
        global apk_main_pre_dir
        apk_main_pre_dir = var_case_delivery_directory + "\\apk_post_run\\"
        try:
            os.mkdir(apk_main_pre_dir)
        except:
            if var_forensic_case_bool == 1:
                log_txt_update.write("[WARN]: Error Making APK Results Directory: " + apk_main_pre_dir + ". Directory likely exists.\n")
            if arg_verbose_output == 1:
                print("[WARN]: Error Making APK Results Directory: " + apk_main_pre_dir + ". Directory likely exists.")

    if var_xapk_ripper_flag == 1:
        global xapk_main_pre_dir
        xapk_main_pre_dir = var_case_delivery_directory + "\\xapk_post_run\\"
        try:
            os.mkdir(xapk_main_pre_dir)
        except:
            if var_forensic_case_bool == 1:
                log_txt_update.write("[WARN]: Error Making xAPK Results Directory: " + xapk_main_pre_dir + ". Directory likely exists.\n")
            if arg_verbose_output == 1:
                print("[WARN]: Error Making xAPK Results Directory: " + xapk_main_pre_dir + ". Directory likely exists.")
                
    if var_oat_ripper_flag == 1:
        global oat_main_pre_dir
        oat_main_pre_dir = var_case_delivery_directory + "\\oat_post_run\\"
        try:
            os.mkdir(oat_main_pre_dir)
        except:
            if var_forensic_case_bool == 1:
                log_txt_update.write("[WARN]: Error Making OAT Results Directory: " + oat_main_pre_dir + ". Directory likely exists.\n")
            if arg_verbose_output == 1:
                print("[WARN]: Error Making OAT Results Directory: " + oat_main_pre_dir + ". Directory likely exists.")
    
    if var_dex_ripper_flag == 1:
        global dex_main_pre_dir
        dex_main_pre_dir = var_case_delivery_directory + "\\dex_post_run\\"
        try:
            os.mkdir(dex_main_pre_dir)
        except:
            if var_forensic_case_bool == 1:
                log_txt_update.write("[WARN]: Error Making DEX Results Directory: " + dex_main_pre_dir + ". Directory likely exists.\n")
            if arg_verbose_output == 1:
                print("[WARN]: Error Making DEX Results Directory: " + dex_main_pre_dir + ". Directory likely exists.")

    if var_so_ripper_flag == 1:
        global so_main_pre_dir
        so_main_pre_dir = var_case_delivery_directory + "\\so_post_run\\"
        try:
            os.mkdir(so_main_pre_dir)
        except:
            if var_forensic_case_bool == 1:
                log_txt_update.write("[WARN]: Error Making SO Results Directory: " + so_main_pre_dir + ". Directory likely exists.\n")
            if arg_verbose_output == 1:
                print("[WARN]: Error Making SO Results Directory: " + so_main_pre_dir + ". Directory likely exists.")

    if var_elf_ripper_flag == 1:
        global elf_main_pre_dir
        elf_main_pre_dir = var_case_delivery_directory + "\\elf_post_run\\"
        try:
            os.mkdir(elf_main_pre_dir)
        except:
            if var_forensic_case_bool == 1:
                log_txt_update.write("[WARN]: Error Making ELF Results Directory: " + elf_main_pre_dir + ". Directory likely exists.\n")
            if arg_verbose_output == 1:
                print("[WARN]: Error Making ELF Results Directory: " + elf_main_pre_dir + ". Directory likely exists.")

    if var_jar_ripper_flag == 1:
        global jar_main_pre_dir
        jar_main_pre_dir = var_case_delivery_directory + "\\jar_post_run\\"
        try:
            os.mkdir(jar_main_pre_dir)
        except:
            if var_forensic_case_bool == 1:
                log_txt_update.write("[WARN]: Error Making JAR Results Directory: " + jar_main_pre_dir + ". Directory likely exists.\n")
            if arg_verbose_output == 1:
                print("[WARN]: Error Making JAR Results Directory: " + jar_main_pre_dir + ". Directory likely exists.")

########################################################################################################################################
############################################################# MASTER OF RIPPERS ########################################################
########################################################################################################################################

    global script_ext_location_check
    script_ext_location_check = 0

    if var_apk_ripper_flag == 1:
        script_ext_location_check = 1
        func_command_call()
    if var_xapk_ripper_flag == 1:
        script_ext_location_check = 2
        func_command_call()
    if var_oat_ripper_flag == 1:
        script_ext_location_check = 3
        func_command_call()
    if var_dex_ripper_flag == 1:
        script_ext_location_check = 4
        func_command_call()
    if var_so_ripper_flag == 1:
        script_ext_location_check = 5
        func_command_call()
    if var_elf_ripper_flag == 1:
        script_ext_location_check = 6
        func_command_call()
    if var_jar_ripper_flag == 1:
        script_ext_location_check = 7
        func_command_call()

########################################################################################################################################
############################################################# Per APK Clean-Up #########################################################
########################################################################################################################################     

        if arg_verbose_output == 1:
            print("")
            print("[FIN] ###################################### FIN ######################################")
            print("")

    func_clean_up()

if __name__ == "__main__":
   main(sys.argv[1:])

###########################################################################
################################# ENDING ##################################
###########################################################################

############################### LEGAL NOTES ###############################

###########################################################################
###               Copyright (C)  2025  s3raph                             #
###                                                                       #
### This program is free software: you can redistribute it and/or modify  # 
### it under the terms of the GNU General Public License as published by  #
### the Free Software Foundation, either version 3 of the License, or     #
### (at your option) any later version.                                   #
###                                                                       #
### This program is distributed in the hope that it will be useful,       #
### but WITHOUT ANY WARRANTY; without even the implied warranty of        #
### MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         #
### GNU General Public License for more details.                          #
###                                                                       #
### You should have received a copy of the GNU General Public License     #  
### along with this program.                                              #
### If not, see <https://www.gnu.org/licenses/>.                          #
###########################################################################

################################## FIN ####################################
