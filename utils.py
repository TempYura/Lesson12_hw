import json

from config import UPLOAD_PIC_PATH

def load_json(file):
    """Загружает список постов из файла json"""
    if not file:
        return "Файл не найден"
    with open(file, 'r', encoding='utf-8') as f:
        return json.load(f)


def get_posts_by_request(all_posts, request):
    """Фильтрует посты по запросу"""
    requested_posts = [post for post in all_posts if request.lower() in post['content'].lower()]
    return requested_posts


def save_picture(picture):
    """Сохраняет картинку на диск"""
    filename = picture.filename
    filetype = filename.split('.')[-1]
    if filetype.lower() not in ['jpg', 'jpeg', 'svg', 'png']:
        return

    picture.save(f'{UPLOAD_PIC_PATH}{filename}')

    # Убираем ./ из начала пути
    url = UPLOAD_PIC_PATH[2:] + filename

    return url


def add_posts_to_file(file, new_post):
    """Добавление нового поста в файл с постами"""
    all_posts = load_json(file)
    all_posts.append(new_post)

    with open(file, "w", encoding='utf-8') as f:
        json.dump(all_posts, f, ensure_ascii=False)
