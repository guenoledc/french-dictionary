import connexion
import six

from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.word import Word  # noqa: E501
from swagger_server import util

from domain.usecase import getRandomWord, findByPattern

def random_get():  # noqa: E501
    """random_get

    get one word from the Dictionary choosen randomly # noqa: E501


    :rtype: Word
    """
    return {
        "word": getRandomWord(5, 10)
    }

def one_get():
    print("args = ", connexion.request.args)
    min = int(connexion.request.args["minLength"]) if "minLength" in connexion.request.args else 4
    max = int(connexion.request.args["maxLength"]) if "maxLength" in connexion.request.args else 100
    if min>max:
        min=max
    #print(min, max)
    return {
        "word": getRandomWord(min, max)
    }

def pattern_matcher_get(pattern):
    print("pattern = ", pattern)
    return findByPattern(pattern)