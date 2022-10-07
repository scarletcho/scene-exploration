import pickle as pkl

# stat
doc_cnt = 0
sent_cnt = 0
word_cnt = 0
token_cnt = 0

with open("pkl/coca-fiction-stanza.pkl", "rb") as fr:
    try:
        while True:
            doc = pkl.load(fr)
            doc_cnt += 1
            sent_cnt += len(doc.sentences)
            word_cnt += doc.num_words
            token_cnt += doc.num_tokens
    except EOFError:
        pass

print("Total # of documents: {}".format(str(doc_cnt)))
print("Total # of sentences: {}".format(str(sent_cnt)))
print("Total # of words: {}".format(str(word_cnt)))
print("Total # of tokens: {}".format(str(token_cnt)))

