import urllib2
from bs4 import BeautifulSoup


def video_name(id):
    html_doc = urllib2.urlopen("http://www.youtube.com/watch?v=" + str(id))
    soup = BeautifulSoup(html_doc)
    vid_name = soup.find(id="eow-title").string
    print(vid_name.strip())


video_name("oCokVr-OHHg")