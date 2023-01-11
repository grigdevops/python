from fabric import Connection, Config

config = Config(overrides={"sudo": {"password": "Akmli6964"}})

c = Connection(host='95.111.230.51', user='root', connect_kwargs={'password': 'Akmli6964'}, config=config)

c.put('/home/grigor/python/ino/dashboard.py', '/root/dashboard.py')


run_script = c.run('python3 dashboard.py Yeghizaryan 8FXb9iyzxQu9N6g')


print(run_script.stdout)

c.close()