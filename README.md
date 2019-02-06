# Intro to Linux
Linux is an essential part of the class, so it's important to get some experience with this before working with the robots. Although you're encouraged to collaborate with others if you are stuck, the lab should be completed individually so you can get practice with skills that will be essential later on in the course when you are in teams. If you have general questions, please post on [Piazza](https://piazza.com/class/jrql7urlkqn189) so other students can benefit from the answer. If you have a question about your individual submission, please make a private post. Make sure you're using an Ubuntu terminal if you're testing the commands. Instructions for setting up the course software is [here](https://github.com/mit-rss/base_installation). Alternatively, you can use your athena terminal to test commands by typing `ssh athena.dialup.mit.edu -l <kerberos>` in your terminal although some commands may not work. 
### Gradescope Submission
In order to get credit for this assignment, you will submit a `.zip` file to [Gradescope](https://gradescope.com/) under lab1a_exercises_linux. The format of the file will be specified in question 4. Your submission will not get graded properly if you don't put it in the right format
### References
If you don't have previous experience with linux, we recommend that you read the following tutorials by the Software Carpentry Foundation before starting on the exercises. Otherwise, you can just use the resources as you need. 
1. [Setup](https://swcarpentry.github.io/shell-novice/setup.html)
2. [Introducing the Shell](https://swcarpentry.github.io/shell-novice/01-intro/)
3. [Navigating files and directories](https://swcarpentry.github.io/shell-novice/02-filedir/)
4. [Working with files and directories](https://swcarpentry.github.io/shell-novice/03-create/)
5. [Pipes and filters](https://swcarpentry.github.io/shell-novice/04-pipefilter/)
6. [Finding things](https://swcarpentry.github.io/shell-novice/07-find/)
### Instructions
1. Clone this repository by typing `git clone https://github.com/mit-rss/intro_to_linux.git` into your terminal
2. Place your answers to 1-3 in `linux_exercise.txt`. Every command should go between the #####<question_number>####### and #####End of Question####### lines
3. During this class, you will need to be familiar with at least one terminal-based text editor like vim, nano, emacs. We recommend getting some practice with a terminal-based text editor when you're editing `linux_exercise.txt`. 
4. Run `sanity_checker.py` to double check that your answers are correctly formatted
5. Provide a single command for each of the following questions. If multiple answers are possible, choose the shortest answer. All of your commands should work regardless of your current working directory. [Hint](https://www.gnu.org/software/bash/manual/html_node/Tilde-Expansion.html)
6. Continue onto question 4 to find out how to submit your answers
### Question 1: Navigating your Home
The first thing you need to learn in the command-line is how to navigate the filesystem and view the contents of directories and files.   

1a. Navigate to your home directory  
1b. Navigate to your root directory  
1c. Navigate to the parent directory of your current directory  
1d. List all the files/directories in your home directory, including hidden ones, in long listing format  
1e. Print your current working directory  
### Question 2: Installing and Controlling Programs
One of the awesome features of UNIX-based operating systems is how simple it is to install programs through the terminal. For this question, use [apt](https://help.ubuntu.com/lts/serverguide/apt.html.en).   

2a. Install a program called `inxi`.  
2b. Open up documentation for `inxi` in the terminal to see what it does. [Hint](https://en.wikipedia.org/wiki/Man_page)  
2c. Use `inxi` to show basic information about your Audio/sound card without extra information  
2d. Uninstall `inxi`  
2e. Open firefox using the terminal  
2f. Update the list of available Ubuntu packages  
2g. Upgrade all existing packages  
### Question 3: ssh
Another cool feature that you will be using often in this class is SSH, which enables you to access the terminals of other Linux-powered remote devices or systems as long as you have access credentials. This is how you will access the racecars. 

3a. Log into a remote shell with the IP address 192.168.0.101 and username "racecar". This probably won't do anything if you try to run it now.    
3b. Exit the ssh session    
3c. Using the scp command from your local terminal, move the file at path `~/Documents/image.png` on your native machine into the folder `~/Pictures` on the machine in part a. This is useful for transferring files between your computer and the racecar.     
3d. Add an [alias](http://www.linfo.org/alias.html) to the end of your `~/.bashrc` file that runs `ls -alF` when you type `ll`. The .bashrc file is executed every time you start a new shell, so this allows you to create shortcuts for longer commands. Try typing `source ~/.bashrc` after and testing out the alias. 

### Question 4: Practice  
Now that you're familiar with the basics of the command line, complete the following exercise in order to get credit for this assignment. In this exercise, you will be reorganizing the `.txt` files found in the `lab1/` directory. In addition to the commands introduced in questions 1-3, you might find `grep`, `|`, `>`, `>>`, `awk`, `sed`, `mkdir`, `rm`, `wc`, `cat`, `cut`, `zip`, `sort`, `for`, etc useful. We encourage you to work incrementally, use the internet as a resource, and write down commands that are helpful as you go. 

Please perform the following modifications to the `lab1/` directory:   
1. Any file with the extension `.txt` that does not contain 10 lines is corrupted and should be deleted from the whole directory. The names of the files that are deleted should be written in a file called `deleted_files.txt` with 1 filename per line in ascending numerical order.   
2. Out of the remaining `.txt` files with 10 lines, the ones that contain the string "IMPORTANT" should be placed in a new directory named `important/`. The rest of the `.txt` files should be placed in another new directory named `unimportant/`.   
3. After reorganizing all the `.txt` files, add the file named `linux_exercise.txt` that contains your answers to questions 1-3 into the `lab1/` directory.   
4. Zip the folder into a file called `lab1.zip`  

As a summary, the final zipped folder should contain the following:     
*linux_exercise.txt  
*deleted_files.txt  
*important/  
*unimportant/  
