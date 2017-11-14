# largePickleIO
While dealing with large data set, we might find **error22** using the built-in IO function.
The best way to deal with it is to read or write it by chunks! And following is what I use to IO large pickle. Hope could help someone who is also suffering from these problem.

``` python
def loadPickle(path):
	try:
		with open(file_path, "rb") as file:
			pickle.load(largePickleIO(file))
		print('Load Sucessfully!')
	except Exception as e:
		print(e)
		return None
```

About `loadPickle` function:
- path -Str -Define a path to the pickle file you want to load it.  
And it will seperate into several parts and load it by chunks.

``` python
def savePickle(obj, file_path):
	try:
		with open(file_path, "wb") as file:
			pickle.dump(obj, largePickleIO(file), protocol=pickle.HIGHEST_PROTOCOL)
		print('Save Sucessfully!')
	except Exception as e:
		print(e)
		return None
```

About `savePickle` function:
- path -Str -Define a path to the pickle file you want to load it.
- obj -data you want to save. 
And it will seperate into several parts and save it by chunks.
