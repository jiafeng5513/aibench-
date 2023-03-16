# import os
# os.environ['OPENVINO_TF_LOG_PLACEMENT'] = '1'

import openvino_tensorflow as ovtf
ovtf.enable()
backends_list = ovtf.list_backends()
for backend in backends_list:
    print("openvino backend : {}".format(backend))
ovtf.set_backend("GPU.1")


from benchmark import AIBenchmark
benchmark = AIBenchmark(verbose_level=2)
results = benchmark.run()

