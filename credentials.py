import os


EMAIL = os.getenv("EMAIL")
if EMAIL is None:
    raise AttributeError("Введите email как EMAIL в environment")


PWD = os.getenv("PASSWORD")
if PWD is None:
    raise AttributeError("Введите пароль как PASSWORD в environment")

