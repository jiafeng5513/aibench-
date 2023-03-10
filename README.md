Ai-benchmark
========
enable openvino for ai-benchmark base on intel dGPU and iGPU.

## references
1. [ai-benchmark](https://ai-benchmark.com/alpha)
2. [openvino-tensorflow](https://github.com/openvinotoolkit/openvino_tensorflow)
3. [openvino](https://github.com/openvinotoolkit/openvino)

## software version
1. python==3.9.16
2. ai-benchmark==0.1.2
3. numpy==1.21.6, ai-benchmark ask for this version
4. openvino_tensorflow==2.3.0
5. tensorflow==2.9.3, openvino_tensorflow ask for this version
6. memory_profiler==0.61.0
7. matplotlib==3.7.1

## results

| model name                | stage                              | i9-10900 CPU              |     |
|---------------------------|------------------------------------|---------------------------|-----|
|                           | Device Inference Score             | 794                       |     |
|                           | Device Training Score              | 928                       |     |
|                           | Device AI Score                    | 1722                      |     |
| 1/19. MobileNet-V2        | inference batch=50, size=224x224   | 337 ± 215 ms              |     |
|                           | training  batch=50, size=224x224   | 1529 ± 9 ms               |     |     
| 2/19. Inception-V3        | inference batch=20, size=346x346   | 734 ± 577 ms              |     | 
|                           | training  batch=20, size=346x346   | 3573 ± 26 ms              |     |     
| 3/19. Inception-V4        | inference batch=10, size=346x346   | 758 ± 603 ms              |     |     
|                           | training  batch=10, size=346x346   | 4333 ± 1725 ms            |     |     
| 4/19. Inception-ResNet-V2 | inference batch=10, size=346x346   | 1429 ± 1354 ms            |     |     
|                           | training  batch=8,  size=346x346   | 2929 ± 22 ms              |     |     
| 5/19. ResNet-V2-50        | inference batch=10, size=346x346   | 515 ± 374 ms              |     |     
|                           | training  batch=10, size=346x346   | 2044 ± 17 ms              |     |     
| 6/19. ResNet-V2-152       | inference batch=10, size=256x256   | 1317 ± 1280 ms            |     |     
|                           | training  batch=10, size=256x256   | 2775 ± 41 ms              |     |     
| 7/19. VGG-16              | inference batch=20, size=224x224   | 1215 ± 1214 ms            |     |     
|                           | training  batch=2,  size=224x224   | 1441 ± 47 ms              |     |     
| 8/19. SRCNN 9-5-5         | inference batch=10, size=512x512   | 1091 ± 757 ms             |     |     
|                           | inference batch=1,  size=1536x1536 | 859 ± 5 ms                |     |
|                           | training  batch=10, size=512x512   | 11819 ± 11 ms             |     |
| 9/19. VGG-19 Super-Res    | inference batch=10, size=256x256   | 2079 ± 1807 ms            |     | 
|                           | inference batch=1,  size=1024x1024 | 2583 ± 2 ms               |     |     
|                           | training  batch=10, size=224x224   | 11114 ± 67 ms             |     |              
| 10/19. ResNet-SRGAN       | inference batch=10, size=512x512   | 2312 ± 1610 ms            |     |     
|                           | inference batch=1,  size=1536x1536 | 1616 ± 12 ms              |     |     
|                           | training  batch=5,  size=512x512   | 4745 ± 13 ms              |     |     
| 11/19. ResNet-DPED        | inference batch=10, size=256x256   | 2958 ± 2158 ms            |     |     
|                           | inference batch=1,  size=1024x1024 | 3425 ± 6 ms               |     |     
|                           | training  batch=15, size=128x128   | 6364 ± 5 ms               |     |     
| 12/19. U-Net              | inference batch=4,  size=512x512   | 7310 ± 6012 ms            |     |     
|                           | inference batch=1,  size=1024x1024 | 3891 ± 7 ms               |     |     
|                           | training                           | error                     |     |
| 13/19. Nvidia-SPADE       | inference batch=5,  size=128x128   | 1750 ± 1651 ms            |     |     
|                           | training  batch=1,  size=128x128   | 1759 ± 64 ms              |     |     
| 14/19. ICNet              | inference batch=5,  size=1024x1536 | 1377 ± 645 ms             |     |     
|                           | training  batch=10, size=1024x1536 | 2850 ± 30 ms              |     |     
| 15/19. PSPNet             | inference batch=5,  size=720x720   | 14040 ± 13070 ms          |     |
|                           | training  batch=1,  size=512x512   | 2709 ± 192 ms             |     |     
| 16/19. DeepLab            | inference batch=2,  size=512x512   | 3066 ± 3126 ms            |     |     
|                           | training  batch=1,  size=384x384   | 1984 ± 35 ms              |     |     
| 17/19. Pixel-RNN          | inference batch=50, size=64x64     | 1913 ± 803 ms             |     |     
|                           | training  batch=10, size=64x64     | 965 ± 7 ms                |     |     
| 18/19. LSTM-Sentiment     | inference batch=100,size=1024x300  | 2750 ± 60 ms              |     |     
|                           | training  batch=10, size=1024x300  | 8256 ± 18 ms              |     |     
| 19/19. GNMT-Translation   | inference batch=1,  size=1x20      | 1395 ± 15 ms (with error) |     |     

