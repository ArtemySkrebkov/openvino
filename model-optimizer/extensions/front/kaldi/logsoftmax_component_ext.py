# Copyright (C) 2018-2021 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from mo.front.extractor import FrontExtractorOp
from mo.ops.log_softmax import LogSoftmax


class LogSoftMaxComponentExtractor(FrontExtractorOp):
    op = 'logsoftmaxcomponent'
    enabled = True

    @classmethod
    def extract(cls, node):
        LogSoftmax.update_node_stat(node, {'axis': 1})
        return cls.enabled
