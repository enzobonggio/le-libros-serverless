# import binascii
# from io import BytesIO

# import numpy as np
import requests
# import scipy.cluster
# from PIL import Image
from bs4 import BeautifulSoup

# NUM_CLUSTERS = 5


def get(book: str):
    url = "https://lelibros.online/libro/descargar-libro-" + str(book) + '-en-pdf-epub-mobi-o-leer-online/'
    page = requests.get(url)
    return BeautifulSoup(page.content, 'html.parser')


# def colors_from_image(image):
#     print('reading image')
#     response = requests.get(image)
#     im = Image.open(BytesIO(response.content))
#     ar = np.asarray(im)
#     shape = ar.shape
#     ar = ar.reshape(np.product(shape[:2]), shape[2]).astype(float)
#
#     print('finding clusters')
#     codes, dist = scipy.cluster.vq.kmeans(ar, NUM_CLUSTERS)
#     print('cluster centres:\n', codes)
#
#     vecs, dist = scipy.cluster.vq.vq(ar, codes)  # assign codes
#     counts, bins = np.histogram(vecs, len(codes))  # count occurrences
#
#     count_dist_list = list(zip(counts, codes))
#
#     count_dist_list.sort(key=lambda x: x[0], reverse=True)
#
#     print(count_dist_list)
#
#     hex_colors = map(lambda x: binascii.hexlify(bytearray(int(c) for c in x[1])).decode('ascii'), count_dist_list)
#     hex_colors_url = map(lambda color: "https://www.color-hex.com/color/" + color, hex_colors)
#
#     print("List of most used colors: " + str(list(hex_colors_url)))
