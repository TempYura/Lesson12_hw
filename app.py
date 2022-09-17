import logging

from flask import Flask, send_from_directory

from config import LOG_FILE_PATH

# Импорт блюпринтов
from main.views import main_blueprint
from loader.views import loader_blueprint


app = Flask(__name__)

# Регистрация блюпринтов
app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)

# Настройка логирования в файл
logging.basicConfig(filename=LOG_FILE_PATH, level=logging.INFO, encoding='utf-8')


@app.route("/uploads/<path:path>")
def static_dir(path):
    """Вьюшка для отображения загруженных картинок"""
    return send_from_directory("uploads", path)


app.run()
