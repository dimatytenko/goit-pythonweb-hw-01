import logging

# Налаштування логування
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("app.log"), logging.StreamHandler()],
)

logger = logging.getLogger(__name__)


def main():
    logger.info("Програма запущена")
    try:

        logger.debug("Виконується тестова операція")
        result = 10 / 2
        logger.info(f"Результат обчислення: {result}")

        # Тестуємо обробку помилок
        result = 10 / 0
    except Exception as e:
        logger.error(f"Виникла помилка: {str(e)}")

    logger.info("Програма завершила роботу")


if __name__ == "__main__":
    main()
