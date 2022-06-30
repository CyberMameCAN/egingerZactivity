# FastAPIを使ってデモを表示してみました

### こちらを参考にしました

- [FastAPI入門](https://zenn.dev/sh0nk/books/537bb028709ab9)

### 公開サイト

- [週末パドラー イカスミエギンガーZ Activity](https://egingerz.to48.org/)

### 注意

初めてローカルにコピーした時は次のコマンドが必要です(下記エラーが出る)。  
docker-compose build の後、docker-compose upの前。

    $ docker-compose run --entrypoint "poetry install" project-egingerz-app

    project-egingerz-app_1  | The virtual environment found in /src/.venv seems to be broken.
    project-egingerz-app_1  | Recreating virtualenv fastapi-app in /src/.venv
    project-egingerz-app_1  | 
    project-egingerz-app_1  |   FileNotFoundError
    project-egingerz-app_1  | 
    project-egingerz-app_1  |   [Errno 2] No such file or directory: b'/bin/uvicorn'
    project-egingerz-app_1  | 
    project-egingerz-app_1  |   at /usr/local/lib/python3.9/os.py:607 in _execvpe
    project-egingerz-app_1  |        603│         path_list = map(fsencode, path_list)
    project-egingerz-app_1  |        604│     for dir in path_list:
    project-egingerz-app_1  |        605│         fullname = path.join(dir, file)
    project-egingerz-app_1  |        606│         try:
    project-egingerz-app_1  |     →  607│             exec_func(fullname, *argrest)
    project-egingerz-app_1  |        608│         except (FileNotFoundError, NotADirectoryError) as e:
    project-egingerz-app_1  |        609│             last_exc = e
    project-egingerz-app_1  |        610│         except OSError as e:
    project-egingerz-app_1  |        611│             last_exc = e
