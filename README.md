# PhotoMaker

![PyPI - Downloads](https://img.shields.io/pypi/dm/photomaker)
![PyPI - Downloads](https://img.shields.io/pypi/dw/photomaker)
![PyPI - Downloads](https://img.shields.io/pypi/dd/photomaker)

**PhotoMaker** is a library to create funny pictures with your friends' photos.

## Installation 

```
pip install photomaker
```

## Examples



```python
from photomaker import *

MainKronos = None
someone = None

with open("documentation/input/me.jpeg", 'wb') as f:
	MainKronos = f.read()

with open("documentation/input/someone.jpeg", 'wb') as f:
	someone = f.read()
```

<img src="documentation/input/me.jpg" align="left" width="150">
<img src="documentation/input/someone.jpg" width="150">

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`MainKronos` &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`someone`

### Burn

<img src="documentation/output/burn.gif" align="right" width="150">

> `MainKronos` is on fire.

```python
with open("output.gif", 'wb') as f:
	f.write(burn(MainKronos))
```

### Salt

<img src="documentation/output/salt.gif" align="right" width="150">

> `MainKronos` needs to be salty.

```python
with open("output.gif", 'wb') as f:
	f.write(salt(MainKronos))
```

### Trash

<img src="documentation/output/trash.png" align="right" width="150">

> `MainKronos` is actually trash.

```python
with open("output.png", 'wb') as f:
	f.write(trash(MainKronos))
```

### Delete

> It is better to delete `MainKronos`.

<img src="documentation/output/delete.png" align="right" width="150">

```python
with open("output.png", 'wb') as f:
	f.write(delete(MainKronos))
```

### Hitler

<img src="documentation/output/hitler.png" align="right" width="150">

> `MainKronos` is worst than Hitler.

```python
with open("output.png", 'wb') as f:
	f.write(hitler(MainKronos))
```

### RIP

> `MainKronos` is dead.

<img src="documentation/output/rip.png" align="right" width="150">

```python
with open("output.png", 'wb') as f:
	f.write(rip(MainKronos))
```

### Facepalm

> `MainKronos` is facepalming.

<img src="documentation/output/facepalm.png" align="right" width="150">

```python
with open("output.png", 'wb') as f:
	f.write(facepalm(MainKronos))
```

### Leader

<img src="documentation/output/leader.png" align="right" width="150">

> `MainKronos` is a good leader.

```python
with open("output.png", 'wb') as f:
	f.write(leader(MainKronos))
```

### Beautiful

<img src="documentation/output/beautiful.png" align="right" width="150">

> `MainKronos` is really beautiful.

```python
with open("output.png", 'wb') as f:
	f.write(beautiful(MainKronos))
```

### Affect

<img src="documentation/output/affect.png" align="right" width="150" height="170">

> `MainKronos` is the worst.

```python
with open("output.png", 'wb') as f:
	f.write(affect(MainKronos))
```

### Kiss

> `MainKronos` kisses `someone`.

<img src="documentation/output/kiss.png" align="right" width="150">

```python
with open("output.png", 'wb') as f:
	f.write(kiss(MainKronos, someone))
```

### Spank

<img src="documentation/output/spank.png" align="right" width="150">

> `MainKronos` spanks `someone`.

```python
with open("output.png", 'wb') as f:
	f.write(spank(MainKronos, someone))
```

### Bed

<img src="documentation/output/bed.png" align="right" width="150">

> `MainKronos` says that `someone` is worse than a monster.

```python
with open("output.png", 'wb') as f:
	f.write(bed(MainKronos, someone))
```
