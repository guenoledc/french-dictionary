import connexion
import six

from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.word import Word  # noqa: E501
from swagger_server import util


def random_get():  # noqa: E501
    """random_get

    get one word from the dictionnary choosen randomly # noqa: E501


    :rtype: Word
    """
    return 'do some magic!'
