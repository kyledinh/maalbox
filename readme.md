Maalbox
-------
Built for functional testing, this is an Anonymous Mailserver built on Python 3.

The services runs on the default :8025 port for the HMTL and :25 for smtp.

 
Installing setuptools, Pip and Flask
------------------------------------
* http://www.pip-installer.org/en/latest/installing.html
* ez_setup.py and get-pip.py in /assets
* edit .profile

```bash
alias pip3='/Library/Frameworks/Python.framework/Versions/3.3/bin/pip-3.3'
## or
export PATH=/Library/Frameworks/Python.framework/Versions/<version number>/bin:$PATH
```

```    
sudo python3 ez_setup.py
curl -O https://raw.github.com/pypa/pip/master/contrib/get-pip.py
sudo python3 get-pip.py 
pip3 install Flask 

pip3 install -U selenium
```   

Debian
```
$ sudo apt-get install python3-pip
```   

Resources
---------
* http://pymotw.com/2/smtpd/index.html


License
-------
Copyright 2013 Kyle Dinh

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
