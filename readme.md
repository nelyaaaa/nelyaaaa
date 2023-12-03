git init
git add readme.md
git commit -m "Initial commit"
git push --set-upstream origin main
git checkout -b develop
git clone https://github.com/bard/git-flow-example.git
git checkout develop
# Игнорируем файлы, созданные PyCharm
/venv/
.idea/

git add .gitignore
git commit -m ".gitignore"
git push
git checkout -b feature/Task2
