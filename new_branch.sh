# d'abord, add commit & push tes changements de la brnache actuelle
git add .
git commit -m "message"
git push

# création et switch sur une nouvelle branche
git checkout -b nouvelle_branche

# liste des branches:
git branch

# add, commit & push de la nouvelle branche sur github
git add .
git commit -m "1er commit de la nouvelle branche"
git push --set-upstream origin nouvelle_branche