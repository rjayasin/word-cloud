import collections
import re
import stoplist
from PIL import Image, ImageFont, ImageDraw
from random import randrange

CANVAS_X = 1000
CANVAS_Y = 1000

def main():
	cnt = collections.Counter()
	words = re.findall(r'\w+', open('hamlet.txt', encoding='utf8').read().lower())
	words = [x for x in words if x not in stoplist.stoplist]
	words = collections.Counter(words).most_common(100)

	txt = Image.new('RGBA', (CANVAS_X, CANVAS_Y), color=rand_back())

	# get drawing context
	d = ImageDraw.Draw(txt)
	# find the width multiplier
	mult = find_multiplier(words)
	y_pos = 0
	x_pos = 0
	for word, count in words:
		fnt = ImageFont.truetype('helvetica.otf', int(count * mult))
		d.text((x_pos, y_pos), word, font=fnt, fill=rand_word())
		y_pos += fnt.getsize(word)[1] #increase y_pos based on height of last word
		if y_pos >= CANVAS_Y:
			y_pos = 0
			x_pos += 300

	txt.show()
	txt.save('wip.bmp')


def find_multiplier(most_common):
	word, count = most_common[0]
	print("Word:", word)
	multiplier = 100
	while(True):
		fnt = ImageFont.truetype('helvetica.otf', int(count * (multiplier / 100)))
		if fnt.getsize(word)[0] > CANVAS_X:
			multiplier -= 1
		else:
			return multiplier / 100


def rand_back():
	return (randrange(120, 255), randrange(120, 255), randrange(120, 255))

def rand_word():
	return (randrange(255), randrange(255), randrange(255))

def rand_loc():
	return randrange(1), randrange(1000)

if __name__ == '__main__':
	main()