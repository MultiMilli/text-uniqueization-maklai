from itertools import permutations
from json import dumps

from flask import Flask, request, make_response
from nltk.tree import Tree, ParentedTree


app = Flask(__name__)


# A function for finding necessary NP-substrings in a tree
def find_subtrees(tree):
    subtrees = []
    for subtree in tree.subtrees():
        if subtree.label() == 'NP' and len(subtree) > 1 and any(child.label() == ',' or child.label() == 'CC' for child in subtree):
            for elem in subtree.subtrees():
                if elem.label() == 'NP' and any(child.label() == 'NNS' for child in elem):
                    subtrees.append(tree[elem.treeposition()])
    return subtrees


# A function for generating permutations of NNS-elements
def generate_permutation(tree, subtrees):
    positions = [[elem.treeposition() for elem in permutation] for permutation in permutations(subtrees)]
    new_tree = Tree.fromstring(str(tree))       # Formating to "Tree" class for make replacement
    replacement_tree = new_tree.copy(deep=True)
    result = []
    for i in range(1, len(positions)):
        for j in range(len(positions[i])):
            new_tree[positions[0][j]], replacement_tree[positions[i][j]] = replacement_tree[positions[i][j]], new_tree[positions[0][j]]
        replacement_tree = Tree.fromstring(str(tree))
        result.append(new_tree.copy(deep=True))
    return result


# Over-ride Flask.jsonify
def jsonify(status=200, indent=4, sort_keys=True, **kwargs):
    response = make_response(dumps(dict(**kwargs), indent=indent, sort_keys=sort_keys))
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    response.headers['mimetype'] = 'application/json'
    response.status_code = status
    return response


# Request handler for the /paraphrase endpoint
@app.route('/paraphrase', methods=['GET'])
def paraphrase():
    tree_string = request.args.get('tree')
    limit = int(request.args.get('limit', 20))
    tree = ParentedTree.fromstring(tree_string)

    subtrees = find_subtrees(tree=tree)
    result = generate_permutation(tree=tree, subtrees=subtrees)
    paraphrases = [{"tree": i.pformat(margin=float('inf'))} for i in result]

    return jsonify(indent=4, paraphrases=paraphrases[:limit])


if __name__ == '__main__':
    app.run()
