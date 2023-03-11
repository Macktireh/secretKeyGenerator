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

### adapter le chemin de l'icône et du script python et exécuter la commande dans le terminal pour créer un fichier .exe

```bash
pyinstaller --noconfirm --onefile --icon "E:/develop/python/secretKeyGenerator/assets/icon.ico"  "E:/develop/python/secretKeyGenerator/sk_generator.py"
```
