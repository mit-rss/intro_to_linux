
| Deliverable | Due Date              |
|---------------|----------------------------------------------------------------------------|
| Base Installation (nothing to submit)  | Monday, February 13th at 1:00PM EST |
| Intro to Linux [Gradescope Submission (Link to come)](https://www.gradescope.com/)  | Monday, February 13th at 1:00PM EST |
| Intro to Git [Gradescope Submission (Link to come)](https://www.gradescope.com/)  | Monday, February 13th at 1:00PM EST |

# Intro to Linux
Linux is an essential part of the class, so it's important to get some
experience with this before working with the robots. Although you're
encouraged to collaborate with others if you are stuck, the lab should
be completed individually so you can get practice with skills that
will be essential later on in the course when you are in teams. If you
have general questions, please post on
[Piazza](https://tinyurl.com/RSS23-piazza) so other students
can benefit from the answer. If you have a question about your
individual submission, please make a private post. Make sure you're
using a Debian terminal if you're testing the commands. Instructions
for setting up the course software is
[here](https://github.com/mit-rss/base_installation). Alternatively,
you can use your Athena terminal to test commands by typing `ssh
<kerberos>@athena.dialup.mit.edu` in your terminal, substituting
`<kerberos>` for your own kerberos username. Most of the commands below
should work, although a few of them may not.

### Gradescope Submission

In order to get credit for this assignment, you will submit a `.zip`
file to [Gradescope](https://www.gradescope.com/courses/362909) under
**Lab 1A: Intro To Linux**. The format of the file will be specified in
Question 4. Your submission will not get graded properly if you don't
put it in the right format.
          
### References
If you don't have previous experience with Linux, we recommend that
you read the following tutorials by the Software Carpentry Foundation
before starting on the exercises. Otherwise, you can just use the
resources as you need.
1. [Setup](https://swcarpentry.github.io/shell-novice/setup.html)
2. [Introducing the Shell](https://swcarpentry.github.io/shell-novice/01-intro/)
3. [Navigating files and directories](https://swcarpentry.github.io/shell-novice/02-filedir/)
4. [Working with files and directories](https://swcarpentry.github.io/shell-novice/03-create/)
5. [Pipes and filters](https://swcarpentry.github.io/shell-novice/04-pipefilter/)
6. [Finding things](https://swcarpentry.github.io/shell-novice/07-find/)

There are also many Linux cheatsheets online such as the ones [here](https://cheatography.com/davechild/cheat-sheets/linux-command-line/) and [here](https://www.guru99.com/linux-commands-cheat-sheet.html).

Additionally, there is a universally available reference bundled with
almost every Unix system called "man pages" or manual pages. By typing
`man <command>` in the terminal, where `<command>` is the command you
want to learn about, you can see comprehensive documentation about the
command. Many commands also display useful information when called with the help option by running `<command> -h` or `<command> --help`.

### Instructions
1. Clone this repository by typing `git clone
   https://github.com/mit-rss/intro_to_linux.git` into your terminal. 
   **Please make sure you do this in ~/racecar_ws/src if you are using the Docker image.**
2. Place your answers to 1-3 in `linux_exercise.txt`. Every command
   should go between the `#####<question_number>#######` and `#####End
   of Question#######` lines
3. During this class, you will need to be familiar with at least one
   terminal-based text editor like [vim](https://www.vim.org/),
   [nano](https://www.nano-editor.org/),
   [emacs](https://www.gnu.org/software/emacs/). We recommend getting
   some practice with a terminal-based text editor when you're editing
   `linux_exercise.txt`.
4. Run `sanity_checker.py` to double check that your answers are
   correctly formatted
5. Provide a single command for each of the following questions. If
   multiple answers are possible, choose the shortest answer. All of
   your commands should work regardless of your current working
   directory. [Hint](https://www.gnu.org/software/bash/manual/html_node/Tilde-Expansion.html)
6. Continue onto question 4 to find out how to submit your answers. Unlike problems 1-3, this exerise relies on using **multiple commands** to reformat your directory. So, feel free to pipe many commands together or complete file manipulations in consecutive lines as needed. The commands you use to complete this problem will **not** be added to the `linux_exercise.txt` file!  

### Question 1: Navigating your Home
The first thing you need to learn in the command-line is how to
navigate the filesystem and view the contents of directories and
files.

1a. Navigate to your home directory  
1b. Navigate to your root directory  
1c. Navigate to the parent directory of your current directory  
1d. List all the files/directories in your home directory, including hidden ones, in long listing format  
1e. Print your current working directory  
### Question 2: Installing and Controlling Programs
One of the awesome features of UNIX-based operating systems is how simple it is to install programs through the terminal. For this question, use [apt](https://help.ubuntu.com/lts/serverguide/apt.html.en).   

2a. Install a program called `inxi`.  
2b. Open up documentation for `inxi` in the terminal to see what it does. [Hint](https://en.wikipedia.org/wiki/Man_page)  
2c. Use `inxi` to show information about your Audio/sound card  
2d. Uninstall `inxi`  
2e. Update the list of available Debian packages  
2f. Upgrade all existing packages  

### Question 3: ssh
Another cool feature that you will be using often in this class is SSH
(Secure SHell), which enables you to access the terminals of other
Linux-powered remote devices or systems as long as you have access
credentials. This is how you will access the racecars.

3a. Log into a remote shell with the address `athena.dialup.mit.edu` and your kerberos as the username. This will give you secure remote access to a shell running on an Athena machine.  
3b. Logged into your Athena account, download the contents from `https://tinyurl.com/ya67uga4` into a file named `pic.png` in your Athena home directory.  
3c. Exit the ssh session      
3d. Using the scp command from your local terminal, move the photo you just downloaded from your Athena account, `~/pic.png`, onto your native machine into the folder `~/Pictures` on your machine. This is useful for transferring files between your computer and the Racecar.

### Question 4: Practice  
Now that you're familiar with the basics of the command line, complete the following exercise in order to get credit for this assignment. In this exercise, you will be reorganizing the `.txt` files found in the `lab1/` directory. In addition to the commands introduced in questions 1-3, you might find `grep`, `|`, `>`, `>>`, `xargs`, `awk`, `sed`, `mkdir`, `rm`, `wc`, `cat`, `cut`, `zip`, `sort`, `for`, etc useful. We encourage you to work incrementally, use man pages and the internet as a resource, and write down commands that are helpful as you go. 

Please perform the following modifications to the `lab1/` directory:

1. Any file with the extension `.txt` that does not contain **exactly 10 lines** is corrupted and should be deleted from the whole directory. The names of the files that are deleted should be written in a file called `deleted_files.txt` with 1 filename per line in **ascending numerical order** (_not alphabetical order_).   
2. Out of the remaining `.txt` files with 10 lines, the ones that contain the string "IMPORTANT" should be placed in a new directory named `important/`. The rest of the `.txt` files should be placed in another new directory named `unimportant/`.   
3. After reorganizing all the `.txt` files, add the file named `linux_exercise.txt` that contains your answers to questions 1-3 into the `lab1/` directory.
4. Zip the folder into a file called `lab1.zip`

As a summary, the final zipped folder should contain the following:  

* linux\_exercise.txt  
* deleted\_files.txt  
* important/  
* unimportant/  

**Remember:** The shell and filesystem are case sensitive (unlike on Windows!).
Therefore, we expect correct use of upper and lower case in the commands and
files in your submission.

Notes: Make sure you are using the provided VM or an Debian or Ubuntu
machine when doing question 4 or weird things might happen when it's
graded.

### Question 5: `alias` and `.bashrc`
Add an [alias](http://www.linfo.org/alias.html) to the end of your
`~/.bashrc` file that runs `ls -alF` when you type `ll`. The .bashrc
file is executed every time you start a new shell, so this allows you
to create shortcuts for longer commands. You should test your command
by typing `source ~/.bashrc` and typing `ll`. You do not need to
submit anything for this question.
