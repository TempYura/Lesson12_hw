import logging

from flask import Blueprint, render_template, request

from utils import load_json, add_posts_to_file, save_picture

from config import POSTS_FILE_PATH

# Блюпринт для добавления поста с фото и текстом
loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder="templates")


@loader_blueprint.route("/post", methods=["GET"])
def post_page():
    """Вьюшка с формой для добавления новых постов"""
    return render_template('post_form.html')


@loader_blueprint.route("/post", methods=["POST"])
def add_post_page():
    """Вьюшка с добавленным постом"""

    msg = "Запрос на добавление нового поста"
    logging.info(msg)

    picture = request.files.get("picture")
    content = request.form.get("content")

    if not picture or not content:
        msg = "Нет картинки или текста"
        logging.info(msg)
        return msg

    # Сохранение файла на диск
    picture_url = save_picture(picture)

    if not picture_url:
        msg = "Загруженный файл не картинка"
        logging.info(msg)
        return msg

    new_post = {"pic": picture_url, "content": content}

    # Запись обновленного списка с постами в файл
    add_posts_to_file(POSTS_FILE_PATH, new_post)

    return render_template('post_uploaded.html', picture_url=picture_url, content=content)
