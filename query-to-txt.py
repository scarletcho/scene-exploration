from src import ContextDoc
from collections import defaultdict
import pickle as pkl
from tqdm import tqdm
import os
import sys

def collect_sample(sent, query, query_pos):
    lemmas_in_sent = [w.lemma.lower() for w in sent.words]
    try:
        i = lemmas_in_sent.index(query)
    except ValueError:
        return None

    try:
        word_pos = sent.words[i].pos
    except IndexError:
        return None

    if word_pos in query_pos:
        return sent.text
    else:
        return None


query = sys.argv[1]

verbose = False
query_pos = ["NOUN", "PROPN"]  # added PROPN for examples like Christmas
dict_path = "pkl/coca-fiction-dict.pkl"

coca_dict = defaultdict(list)
print('Query:', query)
with open("pkl/coca-fiction-stanza.pkl", "rb") as fr:
    try:
        while True:
            doc = pkl.load(fr)
            for i_sent, sent in enumerate(tqdm(doc.sentences, leave=False)):
                sample = collect_sample(sent, query, query_pos)
                if sample:
                    if verbose:
                        print(sent.text)
                    try:
                        sent_before = doc.sentences[i_sent-1].text
                    except IndexError:
                        sent_before = ''
                    try:
                        sent_next = doc.sentences[i_sent+1].text
                    except IndexError:
                        sent_next = ''
                    sent_curr = sent.text

                    cdoc = ContextDoc(sent_before, sent_curr, sent_next)
                    coca_dict[query].append(cdoc)

                else:
                    continue
    except EOFError:
        pass

if os.path.exists(dict_path):
    with open(dict_path, "rb") as exdict:
        existing_dict = pkl.load(exdict)
        existing_dict[query] = coca_dict[query]

    new_dict = existing_dict
    with open(dict_path, "wb") as f:
        pkl.dump(new_dict, f)
else:
    with open(dict_path, "wb") as f:
        pkl.dump(coca_dict, f)


with open("results/" + query + ".txt", "w") as f:
    for doc in coca_dict[query]:
        line = ' | '.join([doc.sent_before, doc.sent_curr, doc.sent_next])
        f.writelines(line + '\n')


