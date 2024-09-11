# def secret_replace(text, **secrets):
#     new_text = ''
#     print(text)
#     print(secrets)

def secret_replace(text, **replays):
    textn = ''
    dict1 = { key: [replays[key], 0] for key in replays}
    for i in text:
        if i in replays:
            textn += replays[i][dict1[i][1]]
            dict1[i][1] += 1
            if len(dict1[i][0]) == dict1[i][1]:
                dict1[i][1] = 0
        else:
            textn += i
        print(textn)

# result = secret_replace("Hello, world!", l=("hi", "y"), o=("123", "z"))
result = secret_replace(
    "ABRA-KADABRA",
    A=("Z", "1", "!"),
    B=("3",),
    R=("X", "7"),
    K=("G", "H"),
    D=("0", "2"),
)
