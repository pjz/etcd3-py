from collections import namedtuple

from .base import BaseAPI

EtcdVersion = namedtuple('EtcdVersion', ['etcdserver', 'etcdcluster'])


class ExtraAPI(BaseAPI):
    def version(self):
        """
        get the version of etcdserver and etcdcluster

        :return: EtcdVersion
        """
        resp = self._get(self._url('/version'))
        self._raise_for_status(resp)
        return EtcdVersion(**resp.json())

    def health(self):
        """
        get the health of etcd-server

        :return: EtcdVersion
        """
        resp = self._get(self._url('/health'))
        self._raise_for_status(resp)
        return resp.json()['health']

    def metrics_raw(self):  # pragma: no cover
        """
        get the raw /metrics text

        :return: str
        """
        resp = self._get(self._url('/metrics'))
        self._raise_for_status(resp)
        return resp.content

    def metrics(self):  # pragma: no cover
        """
        get the modelized metrics parsed by prometheus_client
        """
        from prometheus_client.parser import text_string_to_metric_families

        return text_string_to_metric_families(self.metrics_raw())
