from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import nltk
nltk.download('book')
#docker build -t haridasu/nltk-server:1.0 .

# # Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/',)

# Create server
server = SimpleXMLRPCServer(("0.0.0.0", 9000),
                            requestHandler=RequestHandler)
server.register_introspection_functions()


'''
hard code for the following:
    1) skills
    2) learning paths
    3) event
    4) skills
'''
default_functions = ["skills","events","sessions","event","session","skill","questions","question"]
train_sents = nltk.corpus.treebank.tagged_sents()[:3000]
tagger = nltk.UnigramTagger(train_sents)
#nltk functions to be called over rpc
def sessions_pos_tag_and_chunk(string,userName):
    tokenizedSent = nltk.word_tokenize(string)
    posTaggedSent = nltk.pos_tag(tokenizedSent)
    nouns = "NOUNS: {<NN.*>+}"
    conjunctions = "CONJ: {<IN><NN.*>+}"
    possesivePronouns = "PRON: {<PRP.*>}"
    nounParser = nltk.RegexpParser(nouns)
    conjParser = nltk.RegexpParser(conjunctions)
    pronParser = nltk.RegexpParser(possesivePronouns)
    nounTree = nounParser.parse(posTaggedSent)
    conjTree = conjParser.parse(posTaggedSent)
    pronTree = pronParser.parse(posTaggedSent)

    function_name = ""
    func_arg = ""
    nn = ""
    #compare message from user to default_functions list
    #if any word from their message is contained in the list,
    #make this keyword the function to be sent to showdme worker
    tokenizedMessage = nltk.word_tokenize(string)
    print("unitagger")
    print(tagger.tag(tokenizedMessage))
    for w in tokenizedMessage:
        if w.lower() in default_functions: function_name = w.lower()


    #chunking reg ex extractor to identify other key elements
    #to be sent to returning function as args


    for subtree in nounTree.subtrees():
        if subtree.label() =='NOUNS':
            for word,tag in subtree:
                if tag =='NN' or 'NNS' or 'NNP' or 'NNPS': func_arg=word

    for subtree in conjTree.subtrees():
        if subtree.label() =='CONJ':
            for word,tag in subtree:
                if tag != 'IN': func_arg=word

    for subtree in pronTree.subtrees():
        if subtree.label() =='PRON':
            for word,tag in subtree:
                print(word +"####" + tag)
                if tag == 'PRP'or 'PRP$': func_arg=userName

    functionString = function_name + '(' + func_arg + ')'
    return functionString
    #sessions(erlang)


def learning_paths_pos_tag_and_chunk(string,userName):
    tokenizedSent = nltk.word_tokenize(string)
    posTaggedSent = nltk.pos_tag(tokenizedSent)
    nouns = "NOUNS: {<NN.*>+}"
    conjunctions = "CONJ: {<IN><NN.*>+}"
    possesivePronouns = "PRON: {<PRP.*>}"
    nounParser = nltk.RegexpParser(nouns)
    conjParser = nltk.RegexpParser(conjunctions)
    pronParser = nltk.RegexpParser(possesivePronouns)
    nounTree = nounParser.parse(posTaggedSent)
    conjTree = conjParser.parse(posTaggedSent)
    pronTree = pronParser.parse(posTaggedSent)

    function_name = ""
    func_arg = ""
    nn = ""
    #compare message from user to default_functions list
    #if any word from their message is contained in the list,
    #make this keyword the function to be sent to showdme worker
    tokenizedMessage = nltk.word_tokenize(string)
    # print("unitagger")
    # print(tagger.tag(tokenizedMessage))
    function_name="learningPaths"


    #chunking reg ex extractor to identify other key elements
    #to be sent to returning function as args


    for subtree in nounTree.subtrees():
        if subtree.label() =='NOUNS':
            for word,tag in subtree:
                if tag =='NN' or 'NNS' or 'NNP' or 'NNPS': func_arg=word

    for subtree in conjTree.subtrees():
        if subtree.label() =='CONJ':
            for word,tag in subtree:
                if tag != 'IN': func_arg=word

    for subtree in pronTree.subtrees():
        if subtree.label() =='PRON':
            for word,tag in subtree:
                print(word +"####" + tag)
                if tag == 'PRP'or 'PRP$': func_arg=userName

    functionString = function_name + '(' + func_arg + ')'
    return functionString
    #sessions(erlang)

def calendar_pos_tag_and_chunk(string,userName):
    tokenizedSent = nltk.word_tokenize(string)
    posTaggedSent = nltk.pos_tag(tokenizedSent)
    nouns = "NOUNS: {<NN.*>+}"
    conjunctions = "CONJ: {<IN><NN.*>+}"
    possesivePronouns = "PRON: {<PRP.*>}"
    nounParser = nltk.RegexpParser(nouns)
    conjParser = nltk.RegexpParser(conjunctions)
    pronParser = nltk.RegexpParser(possesivePronouns)
    nounTree = nounParser.parse(posTaggedSent)
    conjTree = conjParser.parse(posTaggedSent)
    pronTree = pronParser.parse(posTaggedSent)

    function_name = ""
    func_arg = ""
    nn = ""
    #compare message from user to default_functions list
    #if any word from their message is contained in the list,
    #make this keyword the function to be sent to showdme worker
    tokenizedMessage = nltk.word_tokenize(string)
    print("unitagger")
    print(tagger.tag(tokenizedMessage))
    function_name = "calendar"


    #chunking reg ex extractor to identify other key elements
    #to be sent to returning function as args


    for subtree in nounTree.subtrees():
        if subtree.label() =='NOUNS':
            for word,tag in subtree:
                if tag =='NN' or 'NNS' or 'NNP' or 'NNPS': func_arg=word

    for subtree in conjTree.subtrees():
        if subtree.label() =='CONJ':
            for word,tag in subtree:
                if tag != 'IN': func_arg=word

    for subtree in pronTree.subtrees():
        if subtree.label() =='PRON':
            for word,tag in subtree:
                print(word +"####" + tag)
                if tag == 'PRP'or 'PRP$': func_arg=userName

    functionString = function_name + '(' + func_arg + ')'
    return functionString
    #sessions(erlang)
server.register_function(sessions_pos_tag_and_chunk, 'sessionsPosTagAndChunk')
server.register_function(learning_paths_pos_tag_and_chunk, 'learningPathsPosTagAndChunk')
server.register_function(calendar_pos_tag_and_chunk, 'calendarPosTagAndChunk')
# Run the server's main loop
print('Serving XML-RPC on localhost port 9000')
try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\nKeyboard interrupt received, exiting.")
    server.server_close()
    sys.exit(0)
