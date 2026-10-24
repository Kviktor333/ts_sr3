# Python CLI Tools Demo

Цей проект демонструє три підходи до створення CLI в Python.

## Встановлення залежностей
\`\`\`bash
pip install click fire
\`\`\`

## Тестування інструментів

### 1. sys_tool.py
Прямий запуск:
\`\`\`bash
python src/sys_tool.py
# Вивід: командна строка
\`\`\`
Перевірка імпорту (нічого не виведе):
\`\`\`bash
python -c "import src.sys_tool"
\`\`\`

### 2. click_tool.py
\`\`\`bash
python src/click_tool.py say --name Alice
# Вивід: Alice

python src/click_tool.py say --name peter
# Вивід: Ім’я не підходить
\`\`\`

### 3. fire_expose.py
\`\`\`bash
python src/fire_expose.py greet Alice
# Вивід: Привіт, Alice!

python src/fire_expose.py goodbye Bob
# Вивід: Бувай, Bob!
\`\`\`