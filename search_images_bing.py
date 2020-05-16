from requests import exceptions
import argparse
import requests
import cv2
import os

def image_resize(path, image, width = None, height = None, inter = cv2.INTER_AREA):
    # initialize the dimensions of the image to be resized and
    # grab the image size
    dim = None
    (h, w) = image.shape[:2]

    # if both the width and height are None, then return the
    # original image
    if width is None and height is None:
        return image

    # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the
        # dimensions
        r = height / float(h)
        dim = (int(w * r), height)

    # otherwise, the height is None
    else:
        # calculate the ratio of the width and construct the
        # dimensions
        r = width / float(w)
        dim = (width, int(h * r))

    # resize the image
    resized = cv2.resize(image, dim, interpolation = inter)

    # return the resized image
    cv2.imwrite(path, resized)


def search(query, location, number):
    # ap = argparse.ArgumentParser()
    # ap.add_argument("-q","--query", required=True, help="search query to search Bing Image API for")
    # ap.add_argument("-o","--output", required=True,help="path to output directory of images")
    # args = vars(ap.parse_args())


    API_KEY = "45847ab9fe794c45bc5b0790c6b58868"
    GROUP_SIZE = number
    MAX_RESULTS = number*2


    URL = "https://api.cognitive.microsoft.com/bing/v7.0/images/search"

    EXCEPTIONS = set([IOError, FileNotFoundError, exceptions.RequestException,
                    exceptions.HTTPError, exceptions.ConnectionError, exceptions.Timeout])

    term = query
    headers = {"Ocp-Apim-Subscription-Key" : API_KEY}
    params = {"q": term, "offset": 0, "count": GROUP_SIZE}

    print("[INFO] searching Bing API for '{}'".format(term))
    search = requests.get(URL,headers=headers,params=params)
    search.raise_for_status()

    results = search.json()
    estNumResults = min(results["totalEstimatedMatches"], MAX_RESULTS)
    print("[INFO] {} total results for '{}'".format(estNumResults,term))

    total = 0

    for offset in range(0, estNumResults, GROUP_SIZE):
        print("[INFO] making request for group {}-{} of {}...".format(offset, offset + GROUP_SIZE, estNumResults))
        params["offset"] = offset
        search = requests.get(URL, headers=headers,params=params)
        search.raise_for_status()
        results = search.json()
        print("[INFO] making request for group {}-{} of {}...".format(offset, offset + GROUP_SIZE, estNumResults))


    for v in results["value"]:
        try:
            print("[INFO] fetching: {}".format(v["contentUrl"]))
            r = requests.get(v["contentUrl"], timeout=30)
            ext = v["contentUrl"][v["contentUrl"].rfind("."):]
            p = os.path.sep.join([location, "{}{}".format(str(term)+'.'+str(total), ext)])
            f = open(p, "wb")
            f.write(r.content)
            f.close()
        except Exception as e:
            if type(e) in EXCEPTIONS:
                print("[INFO] skipping: {}".format(v["contentUrl"]))
                continue

        image = cv2.imread(p)
        if image is None:
            print("[INFO] deleting: {}".format(p))
            os.remove(p)
            continue
        else:
            print('Resizeing')
            image_resize(p, image, width=100, height=100)


        total += 1

    print('Total images downloaded: '+ str(total))


