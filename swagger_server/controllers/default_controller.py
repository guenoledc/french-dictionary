import connexion
import six

from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.word import Word  # noqa: E501
from swagger_server import util

from domain.usecase import getRandomWord

def random_get():  # noqa: E501
    """random_get

    get one word from the Dictionary choosen randomly # noqa: E501


    :rtype: Word
    """
    return {
        "word": getRandomWord(5, 10)
    }
