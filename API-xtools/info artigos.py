import requests


def xtools(article):
    url = f'https://xtools.wmflabs.org/api/page/prose/pt.wikipedia.org/{article}'
    data = requests.get(url).json()
    page = data['page']
    characters = data['characters']
    words = data['words']
    references = data['references']
    unique_references = data['unique_references']
    return page, characters, words, references, unique_references


if __name__ == '__main__':
    with open('input.txt') as file:
        file = file.readlines()
    for line in file:
        line = line.replace('\n', '')
        print(xtools(line))

