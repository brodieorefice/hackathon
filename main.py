import json
import sys
import time
import threading
import random
import os
import subprocess
import platform

# Start visual functions 

def p(interval=1): #easiser way to pause because the whole time thing is too long for muliple times 
    time.sleep(interval)


def scrolling_text(header="", line1="", line2="", line3=""):
    if header:
        print(header)
        p(1)
    print(line1)
    p(0.5)
    print(line2)
    p(0.5)
    print(line3)
    p(0.5)


def printmt(text, space=1): #print things with a space at the top, defaulting to one line. 
    if check_num(space):
        space = int(space)
        for i in range(space):
            print("")
        print(text)
    else:
        print("Error, number must be used for space argument.")


# End visual functions


# Start file interaction functions


def save(file_name="progress.json", data_name= None, data= None): #save thigs to progress.json by default
    if not data_name or not data:
        print("Error: data_name and data must be specified.")
        return
    try:
        with open(file_name, "r") as file:
            current_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        current_data = {}
    current_data[data_name] = data
    with open(file_name, "w") as file:
        json.dump(current_data, file)


def get_value_by_key(filename, key): #grab things from a filename 
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            return data.get(key, "Key not found")
    except FileNotFoundError:
        return "File not found."
    except json.JSONDecodeError:
        return "Error reading JSON."


def check_num(input): #check if an input is a number without crashing the script
    try:
        input = int(input)
        return True
    except ValueError:
        return False


# End file interaction functions


# Classes for player and envorement managment 


class player:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.xp = 0
        self.xp_to_next_level = 100


    def add_xp(self, amount):
        self.xp += amount #add xp to the current ammount
        print(f"You gained {amount} xp!")
        print(f"Total xp: {self.xp}")
        save("progress.json", "xp", self.xp) #save the xp ammount
        self.check_level_up() #call the function (below)


    def check_level_up(self):
        if self.xp >= self.xp_to_next_level: #if the xp ammount is greater to or equal to the amount needed to level up 
            self.level += 1 #add a level to the current one
            print(f"You leveled to level {self.level}")
            save("progress.json", "level", self.level)
            self.xp_to_next_level *= 1.5 #increase the amoount needed to level up 
        else:
            remainder = self.xp_to_next_level - self.xp #caculate how much extra xp is needed to the next level up
            print(f"You have {remainder} xp left to level up.")

def play(name, mission): #start the game by initalizing the class. All of the game flow logic is here.
    Player = player(name)
    #start dev menu

    if Player.name == "dev": 
        while True:
            printmt("Dev menu")
            print("mission one (1)")
            print("mission two (2)")
            menu_choice = input("Choose: ")
            if menu_choice == "1":
                pass
            elif menu_choice == "2":
                pass
            elif menu_choice == "clear":
                os.system('clear') #ill change this if needed but i dont see why i would need to change for windows
            else:
                printmt("Invalid input")

    #end dev menu

    else: #here is the game code for everyone else

        save("progress.json", "played_before", "True")
        save("progress.json", "name", name)
        if mission == "False" or "mission_1": 
            #mission_1 function
            mission_1(name)
        elif mission == "mission_2":
            #mission 2 function
            pass

#Start code for the missions

def jls_extract_def():
    #go into the directory 
    return 


def mission_1(name):
   Player = player(name)
   print(f"Welcome {Player.name}. Let's begin your first task.")
   p()
   print("You have been given remote access to a company's security analyst's computer.")
   p()
   print("We have a strong suspicion he has stored employee passwords in plain text.")
   p()
   print("Get in there and find the file.")
   
   # Randomizing file names
   password_file_name = random.choice(['secret.txt', 'employees.txt', 'audit.txt', 'tasks.txt', 'CHANGE_ASAP.txt', 'ihatemyjob.txt', 'itll_be_fine.txt'])
   xp_file_name = random.choice(['Howsitgoin.txt', 'hackathon.txt', 'readmeplease.txt', 'whowantsfreexp.txt', 'readme.md'])
   extra_file_1_name = random.choice(['ilovehacking.txt', 'howdoideleteafilehelpgoogle.txt', 'how_to_not_get_fired.txt', 'malware.cpp'])
   extra_file_2_name = random.choice(['ilovehacking.txt', 'howdoideleteafilehelpgoogle.txt', 'how_to_not_get_fired.txt', 'malware.cpp'])
   
   # Ensure file names aren't the same
   while extra_file_1_name == extra_file_2_name:
       extra_file_2_name = random.choice(['ilovehacking.txt', 'howdoideleteafilehelpgoogle.txt', 'how_to_not_get_fired.txt', 'malware.cpp'])
   
   # Change directory and clean up
   os.chdir("intro")  # Go into the directory
   current_directory = subprocess.getoutput('basename "$PWD"')
   if current_directory == "intro":
       os.system("rm -rf ./*")  # Clean up previous game files
   
   # Shuffle file creation
   os_statements = [
       lambda: os.system(f"touch {password_file_name} "),
       lambda: os.system(f"touch {xp_file_name}"),
       lambda: os.system(f"touch {extra_file_1_name}"),
       lambda: os.system(f"touch {extra_file_2_name}")
   ]
   random.shuffle(os_statements)
   for statement in os_statements:
       statement()


   # Add content to files
   with open(password_file_name, "a") as file:
       file.write("Important passwords:\n Username: Admin, Password: Icndi4!i2\n")
   with open(xp_file_name, "a") as file:
       file.write("You get some xp! You get some xp! Everyone gets some xp!\n") 
   with open(extra_file_1_name, "a") as file:
       file.write("SGV5IGhvdydkIHlvdSBrbm93IGl0IHdhcyBpbiBiYXNlIDY0PyBuZXJkLg==\n")
   with open(extra_file_2_name, "a") as file:
       file.write("WWVhaCBpIG1heSBoYXZlIGdvdHRlbiBhIGxpdHRsZSBiaXQgbGF6eS4gRW50ZXIgdGhpcyBtZXNzYWdlIGludG8gdGhlIHRlcm1pbmFsIGZvciAyMDAgeHAgZ29vZCBqb2IgZm9yIGJlaW5nIHdlaXJkIGFuZCBkZWNvZGluZyBpdC4=\n")
  
   # Start the interactive part
   while True:
       # Create a kind of realistic UI
       user_command = input(f"{name}@hackathon:~intro$ ")
       allowed_commands = ["clear", "ls", "cat"]  # Allowed commands
       require_arguement = ["cat"]  # Commands that require an argument
       
       # Split the input into command and arguments
       command_parts = user_command.split(' ', 1)
       command = command_parts[0]  # First word is the command
       argument = command_parts[1] if len(command_parts) > 1 else ""  # Remaining part, if any
       
       found_file = False
       if command in allowed_commands:  # Check if it's an allowed command
           if command == "cat" and argument.strip() == password_file_name:  # Check if it's the correct file
               os.system(f"cat {password_file_name}")
               p()
               print("You found the file!")
               os.system("cd ..")
               Player.add_xp(200)
               found_file = True
               break
           elif command in require_arguement:  # If the command needs an argument
               os.system(f"{command} {argument}")
           else:  # If the command doesn't need an argument
               os.system(command)
       else:
           print(f"-bash: {command}: command not found or not allowed")


            

        
        
         
        
            
        


def show_rules(dev_option=False):
    if not dev_option:
        print("'Hackathon' is a game made to simulate a real hacking experience.")
        p()
        print("Tools traditionally included in Kali Linux and other hacking tools are made available to you.")
        print("You will take on the role of a Cyber Security officer working for a government corporation hacking targets.")
        p(6)
        print("The only knowledge required to start is very basic Linux file navigation logic.")
        p(5)
        print("Happy Hacking!")
        input("Click enter to continue...")
    else: #no pauses
        print("'Hackathon' is a game made to simulate a real hacking experience.")
        print("Tools traditionally included in Kali Linux and other hacking tools are made available to you.")
        print("You will take on the role of a Cyber Security officer working for a government corporation hacking targets.")
        print("Happy Hacking!")
        input("Click enter to continue...")


def main_menu(played_before, platform): #get the system so that os command will run the savme on all instances.
    while True:
        printmt("Play (1)")
        print("Progress (2)")
        print("Rules/desc (3)")
        print("Leaderboard (4)")
        menu_choice = input("Enter a choice (1-4): ")
        dev_mode = "-d" in menu_choice #check for dev option
        choice = menu_choice.replace(" -d", "") #remove it so that it can check for what option is wanting to be called

        if choice == "1":
            if dev_mode:
                play("dev","N/A") #mission is N/A becasue we will not use this arguement
            else:
                if played_before == "True": 
                    name = get_value_by_key("progress.json", "name") #get the name if they have played before
                    mission = get_value_by_key("progress.json", "mission")
                    play(name, mission)
                else:
                    print("No previous game detected.")
                    name = input("Welcome hacker. Enter an alias: ")
                    mission = "False" #this is because the user hasn't played before. Most readable format to use.
                    os.system("mkdir intro") #create the directory
                    play(name, mission)


        elif choice == "2":
            pass


        elif choice == "3":
            show_rules(dev_mode)


        elif choice == "4":
            pass


        elif choice == "clear":
            if platform == "Windows":
                os.system('cls')
            else:
                os.system('clear')
        else:
            printmt("Please enter a valid option")
            p(0.5)


print('''
██╗  ██╗ █████╗  ██████╗██╗  ██╗ █████╗ ████████╗██╗  ██╗ ██████╗ ███╗   ██╗
██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔══██╗╚══██╔══╝██║  ██║██╔═══██╗████╗  ██║
███████║███████║██║     █████╔╝ ███████║   ██║   ███████║██║   ██║██╔██╗ ██║
██╔══██║██╔══██║██║     ██╔═██╗ ██╔══██║   ██║   ██╔══██║██║   ██║██║╚██╗██║
██║  ██║██║  ██║╚██████╗██║  ██╗██║  ██║   ██║   ██║  ██║╚██████╔╝██║ ╚████║
╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
                                                                            
''')


if __name__ == "__main__":
    played_before = get_value_by_key("progress.json", "played_before") #check if they have played before
    if played_before == "File not found.": #meaning they havent played before
        played_before = "False" #set the value to false for easier readability
    platform = platform.system() #check the system being ran on 
