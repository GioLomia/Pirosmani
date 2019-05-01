# import the necessary packages
from imutils import paths
import requests
import os

image_urls="C:/Users/lomiag/PycharmProjects/Pirosmani/im_urls.txt"
output_url="C:/Users/lomiag/PycharmProjects/Pirosmani/Painting_Database"

# grab the list of URLs from the input file, then initialize the
# total number of images downloaded thus far
rows = open(image_urls).read().strip().split("\n")
total = 0

# loop the URLs
for url in rows:
    try:
        # try to download the image
        r = requests.get(url, timeout=60)

        # save the image to disk
        p = os.path.sep.join([output_url, "{}.jpg".format(
            str(total).zfill(8))])
        f = open(p, "wb")
        f.write(r.content)
        f.close()

        # update the counter
        print("[INFO] downloaded: {}".format(p))
        total += 1

    # handle if any exceptions are thrown during the download process
    except:
        print("[INFO] error downloading {}...skipping".format(p))