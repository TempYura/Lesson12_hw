ДЗ https://skyengpublic.notion.site/12-fbb835bd92c448439b74f36afbd0f4fe

Проект Flask с использованием
- блюпринтов (blueprint), 
- отображения страниц по шаблонам (render_template)
- сохранением картинок на диск (picture.save в path = "./uploads/images/filename"), 
- отображением загруженных картинок (url = "uploads/images/filename"), 
- обновлением json файла с постами (json.dump), 
- базовым логированием в файл (logging.basicConfig). 

Список страниц:
- `/` – главная страница (поиск постов)
- `/search/?s=поиск` – страничка ленты по тегу
- `GET /post` – страничка добавления поста
- `POST /post` – страничка после добавления поста
