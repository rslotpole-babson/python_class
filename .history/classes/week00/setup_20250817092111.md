
step 1: log into your github account  
step 2: In the address bar go to: https://github.com/rslotpole-babson/python_class  
step 3: click on "Use this template" -> "create new repository"  
step 4: Make the repository name: "python-class-YOURNAME"  
step 5: click on "create repository"  

step 6: click on "Code" -> "Codespaces" -> "Create codespace on main"  

step 7:![commit](commit.png)  



run the first 3 git commands only once

git remote add upstream https://github.com/rslotpole-babson/python_class.git         
git config --global pull.rebase false
git config --global core.editor "code --wait"

***************************************************************************************************************
*** each time you get the message from canvas that the template has been updated,                           ***
*** MAKE SURE YOU HAVE COMMITTED AND SYNCED YOUR CHANGES IN CODINGSPACES FIRST, and then run the following: ***
***************************************************************************************************************

git pull --no-edit upstream main 

*** IMPORTANT: NEVER DELETE YOUR REPO OR CODESPACE ***

***************************************************
*** The following commands SHOULD NOT be needed ***
***************************************************

command to merge unrelated histories (should not have to use)
git pull --no-edit upstream main --allow-unrelated-histories

command to rename branch
git branch -m old-name new-name

command to switch to main
git checkout main



