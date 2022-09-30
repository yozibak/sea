
python3 -m pip install -r requirements.txt

loc="$(dirs)/exec"

echo "
Append PATH in zshrc/bashrc: 
export PATH=\$PATH:$loc
"

echo "
...then you can run:
sea
"