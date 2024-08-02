## About
TermiCoeg - Terminal Coeg!<br />
Just be honest, ur brain is small af so this app will help u to connect to ssh that u saved before

## Installation
<b>Make sure you already install <code>virtualenv</code> on your machine<br />
In case you didn't have it yet:

```bash
brew install virtualenv
```

Then:
```bash
virtualenv -p python3.11 venv
source venv/bin/activate
pip install -r requirements.txt
```

## How to use
You might be need to regist it into <code>.bash_profile</code> or <code>.zshrc</code>, then put this alias
```bash
alias termicode="/path/to/project/venv/bin/activate && python /path/to/project/app.py"
```
Finally run the app:
```bash
termicode
```

## Author
Kiritoo9

## Version
0.0.1