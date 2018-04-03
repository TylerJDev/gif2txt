import unittest
import argparse
import validators
import random
import string
import urllib.request
from moviepy.editor import *
from PIL import Image, ImageDraw
from jinja2 import Template
import io
import os
import time
import imageio

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

def toMP4(f, fExt):
	print(fExt);
	print('Converting MP4 to GIF format..');
	clip = (VideoFileClip(f))
	clip.write_gif(fExt[0] + '.gif');
	f = fExt[0] + '.gif';

def gif2txt(filename, maxLen=80, output_file='out.html', with_color=False):
	# # with_color = False # placeholder, remove
	try:
		maxLen = int(maxLen)
	except:
		maxLen = 80

	chs = "MNHQ$OC?7>!:-;. "
	fileExt = filename.split('.'); # I.E, FileName/./mp4 (/ / = where string is split)

	if fileExt[1] == 'mp4':
		toMP4(filename, fileExt);

	try:
		img = Image.open(filename)
	except IOError:
		# Check if type is URL
		if validators.url(filename):
			nameFile =  ''; # input('Please name this GIF..\n');
			if nameFile == '':
				nameFile = rName();
			
			# Check ext
			x = filename.split('.');
			y = x[len(x) - 1]
			
			ext = 'gif';
			
			if (y == 'mp4'):
				ext = 'mp4'
			
			urllib.request.urlretrieve(filename, nameFile + '.' + ext);
			
			if ext == 'mp4':
				toMP4(nameFile + '.' + ext, [nameFile]);
				
			# Try again to open it
			try:
				img = Image.open(nameFile + '.gif');
			except IOError:
				print('An error has occurred!')
				exit();
		else:
			exit("file not found: {}".format(filename))

	width, height = img.size
	rate = float(maxLen) / max(width, height)
	width = int(rate * width)
	height = int(rate * height)

	palette = img.getpalette()
	strings = []
	c = 0;
	if os.path.exists('2__gif/') != True:
		# Create the folder
		os.makedirs('2__gif/')
									

	def toImage(s, count): #8
		img = Image.new('RGB', (width * 8, height * 17), color='white')
		d = ImageDraw.Draw(img)
		d.text((width, height), s.encode('utf-8'), fill=(0, 0, 0))
		img.save('2__gif/pil_text_' + str(count) + '.png')

	def toGIF(count):
		print('Converting to .GIF format...');
		g_images = []

		for x in range(1, count):
			g_images.append(imageio.imread('2__gif/pil_text_' + str(x) + '.png'))
			imageio.mimsave(output_file.split('.')[0] + '.gif', g_images)
			
		for clean in range(1, (count + 1)):
			os.remove('2__gif/pil_text_' + str(clean) + '.png');

	try:
		while 1:
			img.putpalette(palette)
			im = Image.new('RGB', img.size)
			im.paste(img)
			im = im.resize((width, height))
			string = ''
			print ('Creating GIF...', end="\r") # + str(c * 3 + 13) + '%', end="\r") # If lasting point is 29
			c += 1;
			for h in range(height):
				for w in range(width):
					rgb = im.getpixel((w, h))
					if with_color:
						string += "<span style=\"color:rgb" + \
							str(rgb) + ";\">▇</span>"
					else:
						string += chs[int(sum(rgb) / 3.0 / 256.0 * 16)]
				if with_color == False:
					toImage(string, c)
				string += '\n'
			if isinstance(string, bytes):
				string = string.decode('utf8')

			strings.append(string)
			img.seek(img.tell() + 1)
	except EOFError:
		pass
	if with_color == False:
		toGIF(c)
	with open('template.jinja') as tpl_f:
		template = Template(tpl_f.read())
		html = template.render(strings=strings)
	with io.open(output_file, 'w', encoding="utf-8") as out_f:
		if not isinstance(html, str):
			html = html.encode('utf-8')
		out_f.write(html)
		
	return True

class TestGIF(unittest.TestCase):
	def testMakingGIFs(self):
		self.assertEqual(gif2txt('test.gif', 50, 'testOut.html', False), os.path.exists('testOut.html')); # Test GIF-Making
		self.assertEqual(gif2txt('https://i.giphy.com/media/AyawctCEVdEKk/giphy.mp4', 50, 'testOut1.html', False), os.path.exists('testOut1.html')); # Test making GIF from .MP4
		self.assertEqual(gif2txt('test.gif', 50, 'testOut2.html', True), os.path.exists('testOut2.html')); # Test GIF-Making with color
		
if __name__ == '__main__':
    unittest.main()
