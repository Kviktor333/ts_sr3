import fire
import utils

if __name__ == '__main__':
    # Передаємо модуль utils у fire, щоб автоматично експортувати всі його функції
    fire.Fire(utils)