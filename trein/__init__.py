import luigi
from docker import Client
from docker.utils import kwargs_from_env
import logging


__version__ = '0.1'

ASSERT_HOSTNAME = False

logger = logging.getLogger(__name__)


class SimMs(luigi.Task):
    pass



def run():
    kwargs = kwargs_from_env()
    if not ASSERT_HOSTNAME:
        kwargs['tls'].assert_hostname = False
    client = Client(**kwargs)
    container = client.create_container(image='ares/simms')
    if container['Warnings']:
        logger.warn(container['Warning'])
    client.start(container['Id'])
    state = client.wait(container['Id'])

