def encode_string():
    #line
    #this code is to encode a string to jpeg file
    with open('photo.jpg','ab') as f:
        f.write(b"Hello world")
def decode_string():
    #line
    #this code is to decode string from jpeg file
    with open('photo.jpg','rb') as f:
        content=f.read()
        offset=content.index(bytes.fromhex('FFD9'))
        values=f.seek(offset + 2)
        print(f.read())
decode_string()
#encode_string()

# my final finding how stegnography tools are made
