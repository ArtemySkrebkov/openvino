# Copyright (C) 2018-2021 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from extensions.ops.hard_sigmoid import HardSigmoid
from mo.front.common.partial_infer.utils import mo_array
from mo.front.common.replacement import FrontReplacementOp
from mo.front.onnx.extractors.utils import onnx_attr
from mo.front.tf.graph_utils import create_op_with_const_inputs
from mo.graph.graph import Node, Graph


class HardSigmoidFrontExtractor(FrontReplacementOp):
    op = 'HardSigmoid'
    enabled = True

    def replace_op(self, graph: Graph, node: Node):
        alpha = onnx_attr(node, 'alpha', 'f', default=0.2)
        beta = onnx_attr(node, 'beta', 'f', default=0.5)

        hard_sigmoid = create_op_with_const_inputs(graph, HardSigmoid, {1: mo_array(alpha), 2: mo_array(beta)},
                                                   {'name': node.name + '/HardSigmoid_'})

        node.in_port(0).get_connection().set_destination(hard_sigmoid.in_port(0))
        return [hard_sigmoid.id]
