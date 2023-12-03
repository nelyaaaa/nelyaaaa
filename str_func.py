def to_upper(text: str) -> str:
    return text.upper()
git add str_func.py
git commit -m "Added str_func.py"
git push
git checkout develop
git pull origin feature/Task2
git merge origin/feature/Task2
git branch -d feature/Task2
git checkout develop
git pull
def to_upper(text: str) -> str:
    """
    Возвращает строку со всеми заглавными буквами.

    Args:
        text: Строка.

    Returns:
        Строка со всеми заглавными буквами.
    """

    return text.upper()
  def to_title(text: str) -> str:
    """
    Возвращает строку, в которой первые буквы каждого слова сделаны заглавными.

    Args:
        text: Строка.

    Returns:
        Строка, в которой первые буквы каждого слова сделаны заглавными.
    """

    return " ".join(word[
