"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType

"""

x = 1j
print(x)
print(type(x))

x = ["apple", "jam", "kola"]
print(x)
print(type(x))

x = ("apple", "jam", "kola")
print(x)
print(type(x))

x = range(6)
print(x)
print(type(x))

x = {"name": "Kishor", "aim": "good software engineer"}
print(x)
print(type(x))

x = {"apple", "kola", "kola", "jam", 10}
print(x)
print(type(x))

x = frozenset({"apple", "kola", "kola", "jam", 10})
print(x)
print(type(x))

x = True
print(x)
print(type(x))

x = b"Hello"
print(x)
print(type(x))

x = "Hello"
print(x)
print(type(x))

x = bytearray(5)
print(x)
print(type(x))

x = memoryview(bytes(5))
print(x)
print(type(x))

x = None
print(x)
print(type(x))
