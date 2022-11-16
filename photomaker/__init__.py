from PIL import ImageFilter, ImageDraw, Image, ImageSequence
from io import BytesIO

def burn(pic: bytes) -> bytes:
	"""
	`pic` is on fire.
	```
	return GIF
	```
	"""

	base = "photomaker/res/burn.gif"

	img = Image.open(BytesIO(pic)).convert("RGBA")
	base = Image.open(base)

	img = img.resize((500, 500))

	frames = []

	for frame in ImageSequence.Iterator(base):
		frame = frame.convert("RGBA").resize((500, 500))
		burninate = Image.blend(img.copy(), frame, alpha=0.7)
		frames.append(burninate)


	final_buffer = BytesIO()
	frames[0].save(final_buffer, format="GIF", save_all=True, append_images=frames[1:], optimize=False, loop=0)
	final_buffer.seek(0)
	return final_buffer.read()

def salt(pic: bytes) -> bytes:
	"""
	`pic` needs to be salty.
	```
	return GIF
	```
	"""

	base = "photomaker/res/salt.gif"

	img = Image.open(BytesIO(pic)).convert("RGBA").resize((500, 500))
	base = Image.open(base)

	frames = []

	for frame in ImageSequence.Iterator(base):
		frame = frame.convert("RGBA").resize((500, 500))

		new_frame = img.copy()
		
		new_frame.paste(frame, mask=frame) 
		frames.append(new_frame)


	final_buffer = BytesIO()
	frames[0].save(final_buffer, format="GIF", save_all=True, append_images=frames[1:], optimize=False, loop=0)
	final_buffer.seek(0)

	return final_buffer.read()

def trash(pic: bytes) -> bytes:
	"""
	`pic` is actually trash.
	```
	return PNG
	```
	"""

	base = "photomaker/res/trash.png"

	img = Image.open(BytesIO(pic)).convert("RGBA")
	base = Image.open(base).convert("RGBA").copy()

	img = img.resize((309, 309))
	img = img.filter(ImageFilter.BLUR)

	base.paste(img, (309, 0))

	final_buffer = BytesIO()
	base.save(final_buffer, "png")
	final_buffer.seek(0)

	return final_buffer.read()

def delete(pic: bytes) -> bytes:
	"""
	It is better to delete `pic`.
	```
	return PNG
	```
	"""

	base = "photomaker/res/delete.png"

	img = Image.open(BytesIO(pic)).convert("RGBA")
	base = Image.open(base).convert("RGBA").copy()

	img = img.resize((195, 195))

	base.paste(img, (120, 135))

	final_buffer = BytesIO()
	base.save(final_buffer, "png")
	final_buffer.seek(0)

	return final_buffer.read()

def hitler(pic: bytes) -> bytes:
	"""
	`pic` is worst than Hitler.
	```
	return PNG
	```
	"""

	base = "photomaker/res/hitler.png"

	img = Image.open(BytesIO(pic)).convert("RGBA")
	base = Image.open(base).convert("RGBA").copy()

	img = img.resize((140, 140))

	base.paste(img, (46, 43))

	final_buffer = BytesIO()
	base.save(final_buffer, "png")
	final_buffer.seek(0)

	return final_buffer.read()

def rip(pic: bytes) -> bytes:
	"""
	`pic` is dead.
	```
	return PNG
	```
	"""

	base = "photomaker/res/rip.png"

	img = Image.open(BytesIO(pic)).convert("RGBA")
	base = Image.open(base).convert("RGBA").copy()

	mask = Image.new("RGBA", (720, 405), 0)

	img = img.resize((85, 85))
	mask.paste(img, (110, 47))

	base = Image.alpha_composite(mask, base)

	final_buffer = BytesIO()
	base.save(final_buffer, "png")
	final_buffer.seek(0)

	return final_buffer.read()

def facepalm(pic: bytes) -> bytes:
	"""
	`pic` is facepalming.
	```
	return PNG
	```
	"""

	base = "photomaker/res/facepalm.png"

	img = Image.open(BytesIO(pic)).convert("RGBA")
	base = Image.open(base).convert("RGBA").copy()

	mask = Image.new("RGBA", (632, 357), 0)

	img = img.resize((255, 255)).crop((10, 10, 245, 245))
	mask.paste(img, (199, 112))

	base = Image.alpha_composite(mask, base)

	final_buffer = BytesIO()
	base.save(final_buffer, "png")
	final_buffer.seek(0)

	return final_buffer.read()

def leader(pic: bytes) -> bytes:
	"""
	`Pic` is a good leader.
	```
	return PNG
	```
	"""

	base = "photomaker/res/leader.png"

	img = Image.open(BytesIO(pic)).convert("RGBA")
	base = Image.open(base).convert("RGBA").copy()

	mask = Image.new("RGBA", (600, 539), 0)

	img = img.resize((135, 135))
	mask.paste(img, (350, 20))

	base = Image.alpha_composite(mask, base)

	final_buffer = BytesIO()
	base.save(final_buffer, "png")
	final_buffer.seek(0)

	return final_buffer.read()

def affect(pic: bytes) -> bytes:
	"""
	`pic` is the worst.
	```
	return PNG
	```
	"""

	base = "photomaker/res/affect.png"

	img = Image.open(BytesIO(pic)).convert("RGBA")
	base = Image.open(base).convert("RGBA").copy()

	img = img.resize((200, 200)).crop((0, 21.5, 200, 178.5))

	base.paste(img, (180, 383))

	final_buffer = BytesIO()
	base.save(final_buffer, "png")
	final_buffer.seek(0)

	return final_buffer.read()

def beautiful(pic: bytes) -> bytes:
	"""
	`pic` is really beautiful.
	```
	return PNG
	```
	"""

	base = "photomaker/res/beautiful.png"

	img = Image.open(BytesIO(pic)).convert("RGBA")
	base = Image.open(base).convert("RGBA").copy()

	mask = Image.new("RGBA", (376, 400), 0)

	img = img.resize((95, 95))
	mask.paste(img, (258, 28))
	mask.paste(img, (258, 229))

	base = Image.alpha_composite(mask, base)

	final_buffer = BytesIO()
	base.save(final_buffer, "png")
	final_buffer.seek(0)

	return final_buffer.read()

def kiss(pic1: bytes, pic2: bytes) -> bytes:
	"""
	`pic1` kisses `pic2`.
	```
	return PNG
	```
	"""

	base = "photomaker/res/kiss.png"

	img1 = Image.open(BytesIO(pic1)).convert("RGBA")
	img2 = Image.open(BytesIO(pic2)).convert("RGBA")
	base = Image.open(base).convert("RGBA").copy()

	mask = Image.new("L", (200, 200), 0)

	draw = ImageDraw.Draw(mask)
	draw.ellipse((0, 0, 200, 200), fill=255)

	img1 = img1.resize((200, 200))
	img2 = img2.resize((200, 200))

	base.paste(img1, (150, 25), mask)
	base.paste(img2, (350, 25), mask)

	final_buffer = BytesIO()
	base.save(final_buffer, "png")
	final_buffer.seek(0)

	return final_buffer.read()

def bed(pic1: bytes, pic2: bytes) -> bytes:
	"""
	`pic1` says that `pic2` is worse than a monster.
	```
	return PNG
	```
	"""

	base = "photomaker/res/bed.png"

	img1 = Image.open(BytesIO(pic1)).convert("RGBA")
	img2 = Image.open(BytesIO(pic2)).convert("RGBA")
	base = Image.open(base).convert("RGBA").copy()

	mask1 = Image.new("L", (100, 100), 0)
	mask2 = Image.new("L", (70, 70), 0)

	draw = ImageDraw.Draw(mask1)
	draw.ellipse((0, 0, 100, 100), fill=255)
	draw = ImageDraw.Draw(mask2)
	draw.ellipse((0, 0, 70, 70), fill=255)

	img1 = img1.resize((100, 100))
	img1_2 = img1.resize((70, 70))
	img2 = img2.resize((70, 70))

	base.paste(img1, (25, 100), mask1)
	base.paste(img1, (25, 300), mask1)
	base.paste(img1_2, (53, 450), mask2)
	base.paste(img2, (53, 575), mask2)

	final_buffer = BytesIO()
	base.save(final_buffer, "png")
	final_buffer.seek(0)

	return final_buffer.read()

def spank(pic1: bytes, pic2: bytes) -> bytes:
	"""
	`pic1` spanks `pic2`.
	```
	return PNG
	```
	"""

	base = "photomaker/res/spank.png"

	img1 = Image.open(BytesIO(pic1)).convert("RGBA")
	img2 = Image.open(BytesIO(pic2)).convert("RGBA")
	base = Image.open(base).convert("RGBA").copy()

	mask = Image.new("L", (140, 140), 0)

	draw = ImageDraw.Draw(mask)
	draw.ellipse((0, 0, 140, 140), fill=255)

	img1 = img1.resize((140, 140))
	img2 = img2.resize((140, 140))

	base.paste(img1, (225, 5), mask)
	base.paste(img2, (350, 220), mask)

	final_buffer = BytesIO()
	base.save(final_buffer, "png")
	final_buffer.seek(0)

	return final_buffer.read()