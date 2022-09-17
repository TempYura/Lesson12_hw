import logging

from flask import Blueprint, render_template, request

from utils import load_json, get_posts_by_request

from config import POSTS_FILE_PATH

from json import JSONDecodeError

# Блюпринт для поиска постов
main_blueprint = Blueprint('main_blueprint', __name__, template_folder="templates")


@main_blueprint.route("/")
def main_page():
    """Вьюшка главной страницы"""

    msg = "Запрошена главная страница"
    logging.info(msg)
    return render_template('index.html')


@main_blueprint.route("/search")
def search_page():
    """Вьюшка с результатами поиска"""

    msg = 'Запрос результатов поиска'
    logging.info(msg)
    try:
        all_posts = load_json(POSTS_FILE_PATH)
    except FileNotFoundError:
        msg = "Нет файла с постами"
        logging.error(msg)
        return msg
    except JSONDecodeError:
        msg = "Ошибка распаковки файла с постами"
        logging.error(msg)
        return msg

    user_request = request.args.get('s')

    requested_posts = get_posts_by_request(all_posts, user_request)

    return render_template('post_list.html', user_request=user_request, posts=requested_posts)
