import sys
import distance, operator
import networkx as nx
from pattern.en import tokenize
from pattern.vector import Document,LEMMA
import re
import wikipedia_content_fetch

def summarize(text_to_summarize):
    stokens = tokenize(text_to_summarize)

    # STEP 1
    # pattern.vector's Document is a nifty bag-o-words structure,
    # with a TF weighting scheme
    docs = [Document(string= s, name=e,stemmer=LEMMA)
            for e,s in enumerate(stokens) if len(s.split(" ")) > 7]
    
    linkgraph = []
    # STEP 2 and 3 happen interwovenly
    for doc in docs:
        for doc_copy in docs:
            if doc.name != doc_copy.name:
                # STEP 2 happens here
                wordset_a = [x[1] for x in doc.keywords()]
                wordset_b = [y[1] for y in doc_copy.keywords()]
                jacc_dist = distance.jaccard(wordset_a, wordset_b)
                if jacc_dist < 1:
                    linkgraph.append((str(doc.name), #index to sentence
                                      str(doc_copy.name),1-jacc_dist)) #dist. score
    # By the time we reach here, we'd have completed STEP 3
    
    # STEP 4
    #I referenced this SO post for help with pagerank'ing
    #http://stackoverflow.com/questions/9136539/how-to-weighted-edges-affect-pagerank-in-networkx
    D=nx.DiGraph()
    D.add_weighted_edges_from(linkgraph)
    pagerank = nx.pagerank(D)
    sort_pagerank = sorted(pagerank.items(),key=operator.itemgetter(1))
    sort_pagerank.reverse()
    top2 = sort_pagerank[:2]
    orderedtop2 = [int(x[0]) for x in top2]
    orderedtop2 = sorted(orderedtop2)
    return " ".join([ stokens[i] for i in orderedtop2 ])

if __name__ == "__main__":
	if sys.argv[1] == re.compile(r"((https?):((//)|(\\\\))+[\w\d:#@%/;$()~_?\+-=\\\.&]*)") :
	    text = wikipedia_content_fetch.wikipedia_content_fetching(sys.argv[1])
	    print summarize(text)

	elif sys.argv[1] == re.compile(r"''"):
		file = open("text.txt", "r+")
		text = tokenize_file.read()
		print summarize(text)
		file.close()
	else :
		print "Incorrect parameters :", sys.argv[1], "!!! Try Again."