"""
Ваша команда та ви розробляєте систему входу для веб-додатка,
і вам потрібно реалізувати тести на функцію для логування подій в системі входу.
Дано функцію, напишіть набір тестів для неї.
"""

import logging

def log_event(username: str, status: str):
    """
    Логує подію входу в систему.

    username: Ім'я користувача, яке входить в систему.

    status: Статус події входу:

    * success - успішний, логується на рівні інфо
    * expired - пароль застаріває і його слід замінити, логується на рівні warning
    * failed  - пароль невірний, логується на рівні error
    """
    log_message = f"Login event - Username: {username}, Status: {status}"

    # Створення та налаштування логера
    logging.basicConfig(
        filename='login_system.log',
        level=logging.INFO,
        format='%(asctime)s - %(message)s'
        )
    logger = logging.getLogger("log_event")

    # Логування події
    if status == "success":
        logger.info(log_message)
    elif status == "expired":
        logger.warning(log_message)
    else:
        logger.error(log_message)

log_event(username="admin", status="success")
log_event(username="user", status="expired")
log_event(username="unknown", status="failed")


def test_logger_success():
    with open("login_system.log", "r") as f:
        content = f.read()
        assert "INFO" in content
        assert "Username: admin, Status: success" in content


def test_logger_warning():
    with open("login_system.log", "r") as f:
        content = f.read()
        assert "WARNING" in content
        assert "Username: user, Status: expired" in content

def test_logger_error():
    with open("login_system.log", "r") as f:
        content = f.read()
        assert "ERROR" in content
        assert "Username: unknown, Status: failed" in content

