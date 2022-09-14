import os
import re
from tqdm import tqdm

def clean_up_minimal(para):
    para = re.sub("^[#@]+\d+ ", "", para) # document number
    para = re.sub("[^\.\!\?\">]+(@ )+[^\.\!\?\"]+[\.\!\?\"]", " ", para)
    para = re.sub("[ ^\.\!\?\">\n]+(@ )+$", " ", para)
    para = re.sub(r"P\d+", " ", para)  # page number
    para = re.sub("/+", "", para)
    para = re.sub("<p> [A-Z]+ <p>", "", para)  # name of the speaker
    para = re.sub("<p>", "", para)
    para = re.sub("\([^\)]+\)", "", para)
    para = re.sub("#", "", para)
    para = re.sub("\*", "", para)
    para = re.sub(" +", " ", para)
    para = re.sub("^ +", "", para)
    return para

fiction_list = [_ for _ in os.listdir("fiction") if _.endswith(".txt")]

for fiction in tqdm(fiction_list):
    with open("fiction/" + fiction, "r") as f:
        corpus = f.readlines()

    text_stack = []
    for para in tqdm(corpus, leave=False):
        para = clean_up_minimal(para)
        if len(para.strip()) > 0:
            text_stack.append(para)

    with open("fiction_refined/" + fiction, "w") as f:
        f.writelines(text_stack)

