import concurrent.futures
import urllib.request
import sys


def download(url):
    try:
        with urllib.request.urlopen(url) as conn:
            image_data = conn.read()
            return image_data
    except Exception as e:
        print(f"Ошибка при загрузке изображения по адресу {url}: {e}")


def main():
    urls = input().split()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        future_to_url = {executor.submit(download, url): url for url in urls}
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                image = future.result()
                if image:
                    with open(url.split("/")[-1], "wb") as file:
                        file.write(image)
                        print(f"Изображение по адресу {url} успешно загружено и сохранено.")
            except Exception as e:
                print(f"Ошибка при загрузке изображения по адресу {url}: {e}")


if __name__ == "__main__":
    main()