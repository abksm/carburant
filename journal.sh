# git new branch cmd
git checkout -b yz
git add .
git commit -m "add journal.sh"
git push origin yz

git checkout main
git config pull.rebase false
git pull origin main

# git delete branch
git branch -d yz
git push origin --delete yz

# display origin url
git remote show origin

#test