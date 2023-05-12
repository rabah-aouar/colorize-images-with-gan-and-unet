import argparse
from .colorizers import *

def colorize(path):
    # load colorizers
    colorizer_eccv16 = eccv16(pretrained=True).eval()
    #colorizer_siggraph17 = siggraph17(pretrained=True).eval()
    img = load_img(path)
    # default size to process images is 256x256# grab L channel in both original ("orig") and resized ("rs") resolutions
    (tens_l_orig, tens_l_rs) = preprocess_img(img, HW=(256,256))
    # colorizer outputs 256x256 ab map
    # resize and concatenate to original L channelimg_bw = postprocess_tens(tens_l_orig, torch.cat((0*tens_l_orig,0*tens_l_orig),dim=1))
    out_img_eccv16 = postprocess_tens(tens_l_orig, colorizer_eccv16(tens_l_rs).cpu())
    #out_img_siggraph17 = postprocess_tens(tens_l_orig, colorizer_siggraph17(tens_l_rs).cpu())
    return out_img_eccv16
