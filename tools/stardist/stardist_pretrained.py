from stardist.models import StarDist2D
from stardist.data import test_image_nuclei_2d
from stardist.plot import render_label
from csbdeep.utils import normalize
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--model')
parser.add_argument('--input',nargs='*')
parser.add_argument('--output')

args = parser.parse_args()
 
# prints a list of available models 
# StarDist2D.from_pretrained() 

# creates a pretrained model
model = StarDist2D.from_pretrained(args.model)

# read user input image(s)
if args.input:
    for image in args.input:
        img = mpimg.imread(image)
# select test image
else:   
    img = test_image_nuclei_2d()

labels, _ = model.predict_instances(normalize(img))

plt.subplot(1,2,1)
plt.imshow(img, cmap="gray")
plt.axis("off")
plt.title("input image")

plt.subplot(1,2,2)
plt.imshow(render_label(labels, img=img))
plt.axis("off")
plt.title("prediction + input overlay")

plt.savefig(args.output)