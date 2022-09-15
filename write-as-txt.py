import pickle as pkl

dict_path = "pkl/coca-fiction-dict.pkl"

with open(dict_path, "rb") as f:
    d = pkl.load(f)

for query in d:
    print('query:', query)
    with open("results/" + query + ".txt", "w") as f:
        for doc in d[query]:
            line = ' | '.join([doc.sent_before, doc.sent_curr, doc.sent_next])
            f.writelines(line + '\n')
