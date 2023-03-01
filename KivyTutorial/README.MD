Fix for PowerShell Script Not Digitally Signed
https://caiomsouza.medium.com/fix-for-powershell-script-not-digitally-signed-69f0ed518715

Get-ExecutionPolicy

Set-ExecutionPolicy Unrestricted

https://kivy.org/doc/stable/gettingstarted/installation.html#install-pip

Setup terminal

python -m pip install --upgrade pip setuptools virtualenv

python -m virtualenv kivy_venv

kivy_venv\Scripts\activate

python -m pip install "kivy[base]" kivy_examples

Checking the demo
python kivy_venv\share\kivy-examples\demo\showcase\main.py