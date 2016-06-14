#!/usr/bin/python
#coding=utf-8

import logging

from arthas_web.services.core.impala_cli import Impala as impala
from arthas_web.settings import IMPALA_CONF
from impala.util import as_pandas
impala_cli = impala(IMPALA_CONF.get('host'), IMPALA_CONF.get('port'))

logger = logging.getLogger(__name__)


def __parse_data(pd):
    datas = []
    for name in pd.columns.tolist():
        if name == "c_date":
            continue
        data = {
            "name" : name,
            "data" : pd[name].tolist()
        }
        datas.append(data)
    return datas

def _get_normalization_data(sql):
    cur = impala_cli.cursor(sql, True)
    df = as_pandas(cur)

    ret = {}
    ret['time'] = df['c_date'].tolist()
    ret['datas'] = __parse_data(df)
    logger.info('_get_normalization_data data:%s', ret)
    return ret
