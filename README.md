## Get started

```bash
pip install -r requirements.txt
```

### run script

```bash
python sk_generator.py 
```

### Return a 50 character random string usable as a SECRET_KEY setting value.

```bash
python sk_generator.py 50
```

### adapt the path of the icon and the python script and execute the command in the terminal to create an .exe file

```bash
pyinstaller --noconfirm --onefile --icon "E:/develop/python/secretKeyGenerator/assets/icon.ico"  "E:/develop/python/secretKeyGenerator/sk_generator.py"
```
