# voice2process

## Goal
Create a VM from a public cloud over a voice command

## Required Software
- Python 2.7
- Pip for python
- Mac (for speech)

## How to install ?
- First install the requirements using pip.
```
$pip install -r requirements.txt
```
In case pyaudio is not getting installed, install it using brew 
```
brew install pyaudio
```
- If you are using Linux install festival (Not yet tested from my end.)
For Ubuntu:
```
$sudo apt-get install festival
```
For Centos:
```
$yum install festival
```
## How to run ?
```
$python order_vm_voice.py
```
