from benchmark import AIBenchmark
import subprocess
import os
import openvino_tensorflow as ovtf

# 0. detect openvino backend
ovtf.enable()
backends_list = ovtf.list_backends()
for backend in backends_list:
    print("openvino backend : {}".format(backend))

ovtf_backend = ''
if 'GPU.1' in backends_list:
    ovtf_backend = "GPU.1"
elif 'GPU.0' in backends_list:
    ovtf_backend = "GPU.0"
else:
    ovtf_backend = "CPU"

ovtf.set_backend(ovtf_backend)
print("openvino backend set to {}".format(ovtf.get_backend()))

# 1. set json file dump dir
current_path = os.path.split(os.path.realpath(__file__))[0]
json_filename = os.path.join(current_path, 'bench.json')
if os.path.exists(json_filename):
    os.remove(json_filename)

# 2. loop all the case, dump to json bank
for id in range(19):
    python_scripts = "from benchmark import AIBenchmark; " \
                     "import openvino_tensorflow as ovtf; " \
                     "ovtf.enable(); " \
                     "ovtf.set_backend('{}'); " \
                     "print('openvino backend set to '+ str(ovtf.get_backend())); " \
                     "benchmark = AIBenchmark(verbose_level=2); " \
                     "benchmark.run_single_case(case_id={}, json_filename='{}')".format(ovtf_backend, id, json_filename)

    res = subprocess.Popen('python -c "{}"'.format(python_scripts), shell=True, stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)

    while res.poll() is None:
        msg = res.stdout.readline()
        decoded_msg = msg.decode(encoding='utf8')
        print(decoded_msg, end='')

# 3. read json bank, get scores
benchmark = AIBenchmark(verbose_level=2)
result = benchmark.get_result(json_filename=json_filename)