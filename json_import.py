import json
def counter():
    count = 0
    with open('example.json', 'r') as f:
        for line in f:
            if 'position' in line:
                count += 1
    return count


with open('example.json', 'r') as f:
    f1 = f.read()
    data = json.loads(f1)
    count = counter()
    for i in range(count):
        f2 = [(data['storables'][0]['columns'][i]['header']['name'])]
        print(f2)

f.close()
