git checkout -b yzpt
git add .
git commit -m "add journal.sh"
git push origin yzpt

git checkout main
git config pull.rebase false
git pull origin main

git branch -d yzpt
git push origin --delete yzpt

git remote show origin

