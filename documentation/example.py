import photomaker
import requests
import random

me = requests.get("https://avatars.githubusercontent.com/u/21228689").content
someone = requests.get(f"https://avatars.githubusercontent.com/u/{random.randint(0,100000000)}").content

with open("output/burn.gif", 'wb') as f:
	f.write(photomaker.burn(me))

with open("output/salt.gif", 'wb') as f:
	f.write(photomaker.salt(me))

with open("output/trash.png", 'wb') as f:
	f.write(photomaker.trash(me))

with open("output/delete.png", 'wb') as f:
	f.write(photomaker.delete(me))

with open("output/hitler.png", 'wb') as f:
	f.write(photomaker.hitler(me))

with open("output/rip.png", 'wb') as f:
	f.write(photomaker.rip(me))

with open("output/facepalm.png", 'wb') as f:
	f.write(photomaker.facepalm(me))

with open("output/leader.png", 'wb') as f:
	f.write(photomaker.leader(me))

with open("output/affect.png", 'wb') as f:
	f.write(photomaker.affect(me))

with open("output/beautiful.png", 'wb') as f:
	f.write(photomaker.beautiful(me))

with open("output/kiss.png", 'wb') as f:
	f.write(photomaker.kiss(me, someone))

with open("output/bed.png", 'wb') as f:
	f.write(photomaker.bed(me, someone))

with open("output/spank.png", 'wb') as f:
	f.write(photomaker.spank(me, someone))