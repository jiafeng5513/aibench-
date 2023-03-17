import intel_extension_for_tensorflow as itex
from benchmark import AIBenchmark
import tensorflow as tf

backend_cfg = itex.ConfigProto()
backend_cfg.graph_options.onednn_graph = itex.OFF
backend_cfg.graph_options.layout_opt = itex.ON

itex.set_backend('GPU', backend_cfg)
print("itex.get_backend = {}".format(itex.get_backend()))

import logging

logging.basicConfig(filename='debug.log',
                    format='%(message)s',
                    level=logging.INFO)

benchmark = AIBenchmark(verbose_level=2)
results = benchmark.run()
# def add_func(x, y):
#     return x + y
#
#
# with tf.device("/xpu:0"):
#     print(add_func(1, 1))
