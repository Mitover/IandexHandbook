with open("numbers.num", "rb") as file:
    values = []
    while True:
        bytes_chunk = file.read(2)
        if not bytes_chunk:
            break
        values.append(int.from_bytes(bytes_chunk, "big"))
print(values)
print(sum(values) % 2**16)