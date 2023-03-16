Ai-benchmark
========
enable openvino for ai-benchmark base on intel dGPU and iGPU.

## references
1. [ai-benchmark](https://ai-benchmark.com/alpha)
2. [openvino-tensorflow](https://github.com/openvinotoolkit/openvino_tensorflow)
3. [openvino](https://github.com/openvinotoolkit/openvino)

## env setup (common)
1. [Ubuntu 22.04 jammy](https://cn.ubuntu.com/download)
2. [Arc Deiver](https://dgpu-docs.intel.com/installation-guides/ubuntu/ubuntu-jammy-dc.html)
3. [Miniconda](https://mirrors.bfsu.edu.cn/anaconda/miniconda/)
4. [TsinghuaOpenSource](https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/)

## env setup (for openvino_tensorflow)
1. python==3.9.16
2. ai-benchmark==0.1.2
3. numpy==1.21.6, ai-benchmark ask for this version
4. openvino_tensorflow==2.3.0
5. tensorflow==2.9.3, openvino_tensorflow ask for this version
6. memory_profiler==0.61.0
7. matplotlib==3.7.1

## env setup (for oneAPI)
1. [install itex for arc GPU](https://github.com/intel/intel-extension-for-tensorflow/blob/main/docs/install/experimental/install_for_arc_gpu.md)

## results
* i9-10900  CPU: avx, openvino_tensorflow
* i9-12900K CPU: openvino_tensorflow
* A770(0)      : openvino_tensorflow
* A770(1)      : oneAPI, itex

| model name                | stage                              | i9-10900 CPU              | i9-12700K CPU           | A770(0)        | A770(1)        |
|---------------------------|------------------------------------|---------------------------|-------------------------|----------------|----------------|
|                           | Device Inference Score             | 794                       | 330                     | 4869           | 11100          |
|                           | Device Training Score              | 928                       | 698                     | 1979           | 11758          |
|                           | Device AI Score                    | 1722                      | 1028                    | 6848           | 22858          |
| 1/19. MobileNet-V2        | inference batch=50, size=224x224   | 337 ± 215 ms              | 522 ± 142 ms            | 36.3 ± 1.8 ms  | 52.6 ± 6.0 ms  |
|                           | training  batch=50, size=224x224   | 1529 ± 9 ms               | 1224 ± 13 ms            | 648 ± 9 ms     | 130 ± 7 ms     |
| 2/19. Inception-V3        | inference batch=20, size=346x346   | 734 ± 577 ms              | 2373 ± 662 ms           | 102 ± 2 ms     | 77.7 ± 8.9 ms  |
|                           | training  batch=20, size=346x346   | 3573 ± 26 ms              | 4751 ± 560 ms           | 1373 ± 11 ms   | 240 ± 10 ms    |
| 3/19. Inception-V4        | inference batch=10, size=346x346   | 758 ± 603 ms              | 2585 ± 818 ms           | 152 ± 2 ms     | 55.0 ± 8.3 ms  |
|                           | training  batch=10, size=346x346   | 4333 ± 1725 ms            | 5552 ± 1297 ms          | 1376 ± 9 ms    | 219 ± 8 ms     |
| 4/19. Inception-ResNet-V2 | inference batch=10, size=346x346   | 1429 ± 1354 ms            | 3120 ± 1169 ms          | 200 ± 1 ms     | 73.1 ± 3.9 ms  |
|                           | training  batch=8,  size=346x346   | 2929 ± 22 ms              | 4663 ± 306 ms           | 1309 ± 5 ms    | 200 ± 8 ms     |
| 5/19. ResNet-V2-50        | inference batch=10, size=346x346   | 515 ± 374 ms              | 1300 ± 305 ms           | 73.3 ± 1.4 ms  | 30.3 ± 7.6 ms  |
|                           | training  batch=10, size=346x346   | 2044 ± 17 ms              | 3095 ± 96 ms            | 923 ± 7 ms     | 116 ± 10 ms    |
| 6/19. ResNet-V2-152       | inference batch=10, size=256x256   | 1317 ± 1280 ms            | 2366 ± 859 ms           | 176 ± 1 ms     | 42.8 ± 7.9 ms  |
|                           | training  batch=10, size=256x256   | 2775 ± 41 ms              | 4691 ± 139 ms           | 1348 ± 9 ms    | 162 ± 9 ms     |
| 7/19. VGG-16              | inference batch=20, size=224x224   | 1215 ± 1214 ms            | 5489 ± 2105 ms          | 1264 ± 5 ms    | 87.3 ± 3.2 ms  |
|                           | training  batch=2,  size=224x224   | 1441 ± 47 ms              | 2018 ± 176 ms           | 1657 ± 5 ms    | 59.3 ± 8.5 ms  |
| 8/19. SRCNN 9-5-5         | inference batch=10, size=512x512   | 1091 ± 757 ms             | 3922 ± 1554 ms          | 49.7 ± 5.6 ms  | 45.6 ± 4.5 ms  |
|                           | inference batch=1,  size=1536x1536 | 859 ± 5 ms                | 3269 ± 21 ms            | 37.7 ± 0.6 ms  | 36.3 ± 1.3 ms  |
|                           | training  batch=10, size=512x512   | 11819 ± 11 ms             | 10125 ± 12 ms           | 1586 ± 35 ms   | 270 ± 2 ms     |
| 9/19. VGG-19 Super-Res    | inference batch=10, size=256x256   | 2079 ± 1807 ms            | 7117 ± 2474 ms          | 88.1 ± 4.0 ms  | 71.6 ± 7.9 ms  |
|                           | inference batch=1,  size=1024x1024 | 2583 ± 2 ms               | 9133 ± 5 ms             | 114 ± 4 ms     | 120 ± 1 ms     |
|                           | training  batch=10, size=224x224   | 11114 ± 67 ms             | 16749 ± 1824 ms         | 3093 ± 83 ms   | 298.4 ± 0.6 ms |
| 10/19. ResNet-SRGAN       | inference batch=10, size=512x512   | 2312 ± 1610 ms            | 5395 ± 1821 ms          | 92.9 ± 0.9 ms  | 115.8 ± 0.8 ms |
|                           | inference batch=1,  size=1536x1536 | 1616 ± 12 ms              | 4048 ± 12 ms            | 76.0 ± 1.3 ms  | 109.5 ± 0.7 ms |
|                           | training  batch=5,  size=512x512   | 4745 ± 13 ms              | 7591 ± 1060 ms          | 1839 ± 35 ms   | 196 ± 6 ms     |
| 11/19. ResNet-DPED        | inference batch=10, size=256x256   | 2958 ± 2158 ms            | 23784 ± 18709 ms        | 99.9 ± 2.1 ms  | 133.1 ± 0.3 ms |
|                           | inference batch=1,  size=1024x1024 | 3425 ± 6 ms               | 9788 ± 10 ms            | 412.5 ± 0.9 ms | 222.1 ± 0.3 ms |
|                           | training  batch=15, size=128x128   | 6364 ± 5 ms               | 12817 ± 168 ms          | 1500 ± 30 ms   | 166 ± 2 ms     |
| 12/19. U-Net              | inference batch=4,  size=512x512   | 7310 ± 6012 ms            | 14069 ± 5021 ms         | 745 ± 3 ms     | 259.4 ± 0.8 ms |
|                           | inference batch=1,  size=1024x1024 | 3891 ± 7 ms               | 11783 ± 133 ms          | 1732 ± 3 ms    | 274.8 ± 0.7 ms |
|                           | training  batch=4, size=256x25     | error                     | error                   | 2547 ± 24 ms   | 216 ± 10 ms    |
| 13/19. Nvidia-SPADE       | inference batch=5,  size=128x128   | 1750 ± 1651 ms            | 6419 ± 2376 ms          | 582 ± 2 ms     | error          |
|                           | training  batch=1,  size=128x128   | 1759 ± 64 ms              | 2052 ± 62 ms            | 1071 ± 41 ms   | error          |
| 14/19. ICNet              | inference batch=5,  size=1024x1536 | 1377 ± 645 ms             | 1900 ± 554 ms           | 654 ± 8 ms     | 95.0 ± 27.9 ms |
|                           | training  batch=10, size=1024x1536 | 2850 ± 30 ms              | 3670 ± 8 ms             | 1427 ± 37 ms   | 259 ± 21 ms    |
| 15/19. PSPNet             | inference batch=5,  size=720x720   | 14040 ± 13070 ms          | 43956 ± 13270 ms        | 6437 ± 73 ms   | 724 ± 3 ms     |
|                           | training  batch=1,  size=512x512   | 2709 ± 192 ms             | 10584 ± 371 ms          | 1845 ± 31 ms   | 185 ± 11 ms    |
| 16/19. DeepLab            | inference batch=2,  size=512x512   | 3066 ± 3126 ms            | 9231 ± 3816 ms          | 1437 ± 15 ms   | 123 ± 17 ms    |
|                           | training  batch=1,  size=384x384   | 1984 ± 35 ms              | 4244 ± 734 ms           | 1040 ± 4 ms    | 137 ± 7 ms     |
| 17/19. Pixel-RNN          | inference batch=50, size=64x64     | 1913 ± 803 ms             | 1486 ± 451 ms           | 1136 ± 153 ms  | 1361 ± 11 ms   |
|                           | training  batch=10, size=64x64     | 965 ± 7 ms                | 693 ± 13 ms             | 574 ± 4 ms     | 6601 ± 28 ms   |
| 18/19. LSTM-Sentiment     | inference batch=100,size=1024x300  | 2750 ± 60 ms              | 2031 ± 34 ms            | 3079 ± 5 ms    | 862 ± 7 ms     |
|                           | training  batch=10, size=1024x300  | 8256 ± 18 ms              | 3585 ± 100 ms           | 7838 ± 59 ms   | 2766 ± 10 ms   |
| 19/19. GNMT-Translation   | inference batch=1,  size=1x20      | 1395 ± 15 ms (with error) | 723 ± 8 ms (with error) | 717 ± 5 ms     | 424 ± 2 ms     |

