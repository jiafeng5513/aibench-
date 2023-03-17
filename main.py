from benchmark import AIBenchmark
import subprocess
import os


benchmark = AIBenchmark(verbose_level=2)
# results = benchmark.run()


json_filename = 'bench.json'
if os.path.exists(json_filename):
    os.remove(json_filename)


for id in range(19):
    python_scripts = "from benchmark import AIBenchmark; " \
                     "benchmark = AIBenchmark(verbose_level=2); " \
                     "benchmark.run_single_case(case_id={}, json_filename='{}')".format(id, json_filename)

    res = subprocess.Popen('python -c "{}"'.format(python_scripts), shell=True, stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)

    while res.poll() is None:
        msg = res.stdout.readline()
        decoded_msg = msg.decode(encoding='utf8')
        print(decoded_msg, end='')


result = benchmark.get_result(json_filename=json_filename)