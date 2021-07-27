import subprocess
from pathlib import Path
import random
from subprocess import PIPE, run
from math import floor

# fun function to print a random quote
def quote():
    quotes = ["Less is more.","Nobody is more inferior than those who insist on being equal.","There are only two tragedies in life: one is not getting what one wants, and the other is getting it.","In the end, everything is a gag.","Questions are never indiscreet, answers sometimes are.","If God did not exist, it would be necessary to invent Him.","The only thing we have to fear is fear itself","The truth is found when men are free to pursue it","It takes a long time to bring the past up to the present.","Cogito, ergo sum.", "Das was mich nicht umbringt, macht mich stärker."]
    print('  \33[3m"' + random.choice(quotes) + '"\033[0m')

# blur image with imagemagick
def blur():
    print("Working in this directory!! ")
    #print(Path.cwd())
    pwd = str(Path.cwd())
    print("\x1b[33m", pwd, "\x1b[0m")
    fullAsk = input("Dropping image in? [Y,n]")
    if(fullAsk == 'N' or fullAsk == 'no'):
        fullAsk = 'n'
    if (fullAsk != 'n'):
        filename = input("Please drag in the image to convert (*.png acceptable for mass conversion): ")
    else:
        filename = input("Please enter filename (in the current directory) of the image to convert (*.png acceptable for mass conversion): ")
    filename = filename.strip()
    width = input("Width: ");
    height = input("Height: ");

    if (filename[0] != "'") and fullAsk != 'n':
        filename = "'" + filename + "'"

    if (fullAsk != 'n'):
        command = "convert " + filename + " \( -clone 0 -blur 0x40 -brightness-contrast -16x1  -resize "
        command = command + str(width) + "x" + str(height) + "\! \) \( -clone 0 -resize " + str(width) + "x" + str(height) + " \) -delete 0 -gravity center -compose over -composite "
    else:
        command = "convert '" + pwd + "/" + filename + "' \( -clone 0 -blur 0x40 -brightness-contrast -16x1  -resize "
        command = command + str(width) + "x" + str(height) + "\! \) \( -clone 0 -resize " + str(width) + "x" + str(height) + " \) -delete 0 -gravity center -compose over -composite "

    result = input("Is 'result.png' an acceptable filename? [Y,n]")
    if (result == 'n'):
        theResult = input("please enter the filename then: ")
        command = command + theResult
    else:
        command = command + "result.png"
    print("\nCommand candidate:")
    print("------------------")
    print(command)
    print("------------------")
    isThatOk = input("Is this command OK to run? [Y,n]")

    if (isThatOk == '' or isThatOk == "y"):
        subprocess.run([command], shell=True)
    else:
        print("Not running then.")
    print("Have a good day, exiting...")


# blur image with imagemagick
def dropShadow():
    print("Working in this directory!! ")
    #print(Path.cwd())
    pwd = str(Path.cwd())
    print("\x1b[33m", pwd, "\x1b[0m")
    fullAsk = input("Dropping image in? [Y,n]")
    if(fullAsk == 'N' or fullAsk == 'no'):
        fullAsk = 'n'
    if (fullAsk != 'n'):
        filename = input("Please drag in the image to convert (*.png acceptable for mass conversion): ")
    else:
        filename = input("Please enter filename (in the current directory) of the image to convert (*.png acceptable for mass conversion): ")
    filename = filename.strip()

    if (filename[0] != "'") and fullAsk != 'n':
        filename = "'" + filename + "'"

    if (fullAsk != 'n'):
        command = "convert " + filename + " \( +clone -background gray14  -blur 0x25 -shadow 100x1+2+2  \) +swap -background none  -layers merge +repage "
    else:
        command = "convert '" + pwd + "/" + filename + "' \( +clone -background gray14  -blur 0x25 -shadow 100x1+2+2  \) +swap -background none  -layers merge +repage "

    result = input("Is 'result.png' an acceptable filename? [Y,n]")
    if (result == 'n'):
        theResult = input("please enter the filename then: ")
        command = command + theResult
    else:
        command = command + "result.png"
    print("\nCommand candidate:")
    print("------------------")
    print(command)
    print("------------------")
    isThatOk = input("Is this command OK to run? [Y,n]")
    if (isThatOk != 'n') or (isThatOk != 'no'):
        subprocess.run([command], shell=True)
    print("If the shadow is too dark, here is the imagemagick color reference. Replace gray14. https://imagemagick.org/script/color.php")
    print("Have a good day, exiting...")
    subprocess.run([command], shell=True)

# password generator
def passwd():
    nums = input("Do you want to include numbers? [Y,n] ")
    specials = input("Do you want to include special characters? [Y,n] ")
    accented  = input("Do you want to include accented letters? [y,N] ")
    passLength = input("Length of password: ")

    regularStr = "abcdefghijklmnopqrstuvwxyz"
    upperStr = regularStr.upper() 
    finalStr = upperStr + regularStr

    if (nums != 'n'):
        finalStr = finalStr + "0123456789"
    if (specials != 'n'):
        finalStr = finalStr + "°+#&@{}^<>~]`[`'\|€¶←↓→}{*&^%$#@!'$/][>"
    if ((accented == 'y') or (accented == 'Y') or (accented == 'yes')):
        finalStr = finalStr + "ěěščřžýáíéůúńǘćś"
    
    output = ''.join(random.choice(finalStr) for i in range(int(passLength)))

    print(output)
    print("Have a good day, exiting...")

# a lot of shell parsing, but it is useful to me. Normally i would just make this a shell script of course, but I want it to be one file only.
def minifetch():
    print('\x1bc')
    subprocess.run(["hostnamectl|grep Operating"], shell=True) # portability is my strong suit! :)
    print("Kernel: ", end="")
    command = ["uname", "-r"]
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True)
    print( result.stdout, result.stderr, end="")
    subprocess.run(["uptime|awk '{print \"Uptime: \" $1}'"], shell=True)    
    subprocess.run(["free -h|grep Mem|awk '{print \"Memory: \" $3 \" / \" $2 \" used\"}'"], shell=True)
    print("-------------------")
    subprocess.run(["cat /proc/cpuinfo|grep MHz|awk '{print \"  CPU\" NR-1 \" \" $4 $5 \" MHz\"}'"], shell=True)
    print(" -------------------")

# an ascii logo of mini
def splash():
    print(" \033[96m__  __   ___   _   _   ___ \n|  \/  | |_ _| | \ | | |_ _|\n| |\/| |  | |  |  \| |  | | \n| |  | |  | |  | |\  |  | | \n|_|  |_| |___| |_| \_| |___| \033[0mversion 1.4")



splash()
quote()
print("\n\33[1mWhat do you want to do today?\033[0m")
print("  1. resize image and blur background using imagemagick")
print("  2. drop shadow (for .png files with transparent backgrounds)")
print("  3. generate a password")
print("  4. mini-fetch")

whatDo = input("\nEnter the number of the operation you want: ")

if whatDo == '':
    print("No such command")
    exit()

if int(whatDo) == 1:
    print("\33[3mOk, blur it is.\033[0m\n")
    blur()
elif int(whatDo) == 2:
    print("\33[3mThis script is shady\033[0m\n")
    dropShadow()
elif int(whatDo) == 3:
    print("\33[3mOk, one password coming up.\033[0m\n")
    passwd()
elif int(whatDo) == 4:
    minifetch()
else:
    print("No such command.\n")
