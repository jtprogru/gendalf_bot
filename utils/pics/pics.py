import os
import random
from utils.misc.logging import logging
import requests
from data.config import IMG_DIR, UNSPLASH_API_KEY
from pyunsplash import PyUnsplash

pyunsplsh = PyUnsplash(api_key=UNSPLASH_API_KEY)


# Пока локально лежачие фотки
def local_image():
    """
    :return: img: путь до файла с картинкой на файловой системе
    """
    # Список локальных директорий из который достаются картинки
    path_list = [
        "/bot/pics/pics0/",
        "/bot/pics/pics1/",
        "/bot/pics/pics2/",
        "/bot/pics/pics3/",
        "/bot/pics/pics4/",
        "/bot/pics/pics5/",
        "/bot/pics/Girl0/",
    ]
    img_list = []
    # Проходим по каждой директории из списка
    for path in path_list:
        # Получаем список файлов из каждой директории
        img_names = next(os.walk(path))[2]

        for img_name in img_names:
            # Проходим по списку файлов и добавив к нему
            # имя директории добавляем в глобальный список картинок
            img_list.append(path + img_name)
    # Рандомно выбираем картинку из общей кучи
    img = random.choice(img_list)
    logging.debug("Send image: " + img)
    return img


# С сайтом Unsplash я уже работал
# Недостаток - время
# Делается запрос на одну рандомную картинку по определенному запросу
def unsplashed_img() -> str:
    # Get one random image
    collections_page = pyunsplsh.photos(
        type_="random", count=1, featured=True, query="programming,computer,technology"
    )
    for photo in collections_page.entries:
        # Full file name for save resized image
        done_file_name = IMG_DIR + photo.id + ".jpg"
        with open(done_file_name, "wb") as handle:
            response = requests.get(photo.link_download, stream=True)
            if not response.ok:
                print(response)
            for block in response.iter_content(1024):
                if not block:
                    break
                handle.write(block)
        if os.path.exists(done_file_name):
            return done_file_name



