gif2txt
=======

Gif image to to Ascii Text. (Just a toy)

See also [img2txt](https://github.com/hit9/img2txt).

DEMO
----

![](test.gif)

HTML: 

* http://hit9.github.io/gif2txt/out.html
* http://hit9.github.io/gif2txt/withcolor.html

USAGE
-----

```
python gif2txt.py test.gif -m 80 -o out.html
python gif2txt.py test.gif -m 80 -o withcolor.html -c
```

Requirements
-----------

* Jinja2
* Pillow

```
pip install -r requirements.txt
```

TO-DO
-----
Add moviepy, validators to requirements
ETA of making GIF
Turn into .GIF format alongside of HTML
Check if downloaded GIF is in GIF format, if not convert

ADDED
-----
URL TO GIF,
HTML/CSS FORMATTING,
MP4 TO GIF AUTO-CONVERT