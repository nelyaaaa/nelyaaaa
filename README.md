# Создаем директорию
mkdir git_project

# Инициализируем репозиторий
cd git_project
git init

# Копируем .gitignore
wget https://raw.githubusercontent.com/bard/git-example/main/.gitignore

# Делаем коммит
git add .gitignore
git commit -m "Добавили .gitignore"

# Создаем директорию src/
mkdir src

# Создаем файл main.py в src/
touch src/main.py

# Создаем директорию tests/
mkdir tests

# Создаем файл test_basic.py в tests/
touch tests/test_basic.py

# Делаем коммит с добавлением main.py
git add src/main.py
git commit -m "Добавили main.py"

# Делаем коммит с добавлением test_basic.py
git add tests/test_basic.py
git commit -m "Добавили test_basic.py"

# Создаем ssh-ключ
ssh-keygen -t rsa -b 4096

# Копируем ssh-ключ на GitHub
cat ~/.ssh/id_rsa.pub | pbcopy

# Создаем репозиторий на GitHub
git clone git@github.com:bard/git-example.git

# Привязываем репозиторий
git remote add origin git@github.com:bard/git-example.git

# Запушиваем изменения
git push origin master
# Создаем файл README.md на GitHub
echo "Это README.md" > README.md
git add README.md
git commit -m "Добавили README.md"
git push origin master

# Обновляем локальный репозиторий
git pull origin master
# Добавляем код в main.py
echo "print('Hello World')" >> src/main.py

# Делаем коммит
git add src/main.py
git commit -m "Добавили Hello World"

# Отменяем последний коммит
git reset --hard HEAD~1

# Изменяем Hello World на Hello Linux
echo "print('Hello Linux')" >> src/main.py

# Делаем коммит
git add src/main.py
git commit -m "Изменили Hello World на Hello Linux"

# Отменяем коммит с добавлением Hello World
git revert HEAD~1

# Запушиваем изменения
git push origin master
# Создаем новый проект
File > New Project > Python Project

# Создаем файл .gitignore
File > Settings > Version Control > Git > Ignored Files

# Добавляем в .gitignore
/venv/
.idea/

# Создаем файл funcs.py
File > New > File

# Пишем код в funcs.py
def add(a, b):
    return a + b

# Подключаем Git
Tools > Version Control > Git

# Делаем коммит
Commit

# Добавляем вторую функцию
def sub(a, b):
    return a - b

# Добавляем в funcs.py
def sub(a, b):
    return a - b

# Делаем коммит
Commit

# Создаем файл main.py
File > New > File

# Добавляем в main.py
import funcs

print(funcs.add(1, 2))

# Добавляем main.py в отслеживаемые файлы
File > Settings > Version Control > Git > Untracked Files

# Делаем коммит
Commit

# Добавляем вызов функции sub в main.py
print(funcs.sub(3, 2))

# Делаем коммит
Commit

# Просматриваем историю изменений
Git > History
# Добавляем SSH-ключ в GitHub
File > Settings > Version Control > GitHub
