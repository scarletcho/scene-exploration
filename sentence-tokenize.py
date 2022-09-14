import os
import stanza
import pickle as pkl
from tqdm import tqdm

def save_objects(objects):
    with open('pkl/coca-fiction-stanza.pkl', 'ab') as output:  # Note: `ab` appends the data
        pkl.dump(objects, output, pkl.HIGHEST_PROTOCOL)

nlp = stanza.Pipeline(lang='en', processors='tokenize,mwt,pos,lemma', logging_level='DEBUG')
fiction_list = [_ for _ in os.listdir("fiction_refined") if _.endswith(".txt")]

for fiction in tqdm(fiction_list):
    with open("fiction_refined/" + fiction, "r") as f:
        documents = f.readlines()

    in_docs = [stanza.Document([], text=d) for d in documents] # Wrap each document with a stanza.Document object
    out_docs = nlp(in_docs) # Call the neural pipeline on this list of documents

    for d in out_docs:
        save_objects(d)

