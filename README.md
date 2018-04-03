gif2txt
=======

Gif image to to Ascii Text.
Convert any GIF, MP4 into ASCII text animation!


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
python gif2txt.py https://i.giphy.com/media/AyawctCEVdEKk/giphy.mp4 -m 80 -o outlink.html
```

Requirements
-----------

* Jinja2
* Pillow
* validators
* moviepy
* imageio

```
pip install -r requirements.txt
```

To-Do
-----
ETA of making GIF

See about making gif 'faster'

Improve sizing of end .GIF

Add support for color > .GIF

Clean files from test after test has completed

Added
-----
URL TO GIF,

HTML/CSS FORMATTING,

MP4 TO GIF AUTO-CONVERT,

Turn into .GIF format alongside of HTML,

Added test
