import urllib2
from hashlib import md5
import ssl

EXM_PATH = "https://www.duolingo.com/"


def download_file(file_path):
    request = urllib2.Request(file_path)
    res = urllib2.urlopen(request, context=ssl._create_unverified_context())
    code = res.getcode()
    if code != 200:
        raise Exception("bad status code {}".format(code))
    binary = res.read()
    return binary


def calc_hash(binary):
    return md5(binary).hexdigest()


if __name__ == "__main__":
    while True:
        downloaded = download_file(EXM_PATH)
        print("downloaded from: {}, size: {}, md5: {}".format(EXM_PATH, len(downloaded), calc_hash(downloaded)))
