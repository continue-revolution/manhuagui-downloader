# @Author: Xiangxin Kong
# @Date: 2020.5.30
from downloader import MangaDownloader


if __name__ == '__main__':
    # get url from user via command line
    url = input('URL: ')
    path = input('Path: ')
    s = MangaDownloader(url, path)
    print(f"Title: {s.title} | Author: {s.author} | Year: {s.year} | Region: {s.region} | Plot: {s.plot}")
    for i, c in enumerate(s.chapters):
        print(f"Chapter {i}: {c[0]}")
    choice = input('Select chapters to download (separate by comma), default to download all chapters: ')
    if choice:
        for c in choice.split(','):
            s.downloadChapter(s.chapters[int(c)][1])
    else:
        for c in s.chapters:
            s.downloadChapter(c[1])
