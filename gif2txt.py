# -*- coding: utf-8 -*-

import argparse
import validators
import random
import string
import urllib.request
from moviepy.editor import *
from PIL import Image
from jinja2 import Template
import io
import os

def rName():
	len = 5
	rChars = []
	for x in range(0, len):
		rChars.append(random.choice(string.ascii_letters))
		
	joined = ''.join(rChars)
	if os.path.exists(joined) == True:
		rName();
	else:
		return ''.join(rChars);

def gif2txt(filename, maxLen=80, output_file='out.html', with_color=False):
    with_color = False # placeholder, remove
    try:
        maxLen = int(maxLen)
    except:
        maxLen = 80

    chs = "MNHQ$OC?7>!:-;. "
    fileExt = filename.split('.'); # I.E, FileName/./mp4 (/ / = where string is split)
	
    if fileExt[1] == 'mp4':
        print('Converting MP4 to GIF format..');
        clip = (VideoFileClip(filename))
        clip.write_gif(fileExt[0] + '.gif');
        filename = fileExt[0] + '.gif';
		
    try:
        img = Image.open(filename)
    except IOError:
		# Check if type is URL
        if validators.url(filename):
            nameFile = input('Please name this GIF..\n');
            if nameFile == '':
                nameFile = rName();
				
            urllib.request.urlretrieve(filename, nameFile + '.gif');
			# Try again to open it
            try:
                img = Image.open(nameFile + '.gif');
            except IOError:
                print('Error!') # placeholder
                exit();
        else:
            exit("file not found: {}".format(filename))

    width, height = img.size
    rate = float(maxLen) / max(width, height)
    width = int(rate * width)
    height = int(rate * height)

    palette = img.getpalette()
    strings = []

    try:
        while 1:
            img.putpalette(palette)
            im = Image.new('RGB', img.size)
            im.paste(img)
            im = im.resize((width, height))
            string = ''
            for h in range(height):
                for w in range(width):
                    rgb = im.getpixel((w, h))
                    if with_color:
                        string += "<span style=\"color:rgb" + \
                            str(rgb) + ";\">▇</span>"
                    else:
                        string += chs[int(sum(rgb) / 3.0 / 256.0 * 16)]
                string += '\n'
            if isinstance(string, bytes):
                string = string.decode('utf8')
            strings.append(string)
            img.seek(img.tell() + 1)
    except EOFError:
        pass

    with open('template.jinja') as tpl_f:
        template = Template(tpl_f.read())
        html = template.render(strings=strings)
    with io.open(output_file, 'w', encoding="utf-8") as out_f:
        if not isinstance(html, str):
            html = html.encode('utf-8')
        out_f.write(html)


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('filename',
                        help='Gif input file')
    parser.add_argument('-m', '--maxLen', type=int,
                        help='Max width of the output gif')
    parser.add_argument('-o', '--output',
                        help='Name of the output file')
    parser.add_argument('-c', '--color', action='store_true',
                        default=False,
                        help='With color')
    args = parser.parse_args()

    if not args.maxLen:
        args.maxLen = 80
    if not args.output:
        args.output = 'out.html'

    gif2txt(filename=args.filename,
            maxLen=args.maxLen,
            output_file=args.output,
            with_color=args.color)

if __name__ == '__main__':
    main()
