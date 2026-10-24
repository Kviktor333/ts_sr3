import sys

def main():
    # Бонус: обробка прапорця --help
    if len(sys.argv) > 1 and sys.argv[1] in ("--help", "-h"):
        print("Довідка: Цей скрипт демонструє базовий запуск через sys.argv.")
        print("Використання: python src/sys_tool.py")
        return

    print("командна строка")

if __name__ == "__main__":
    main()