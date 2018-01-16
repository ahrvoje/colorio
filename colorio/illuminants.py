# -*- coding: utf-8 -*-
#
from __future__ import division

import numpy


def white_point(illuminant):
    '''From <https://en.wikipedia.org/wiki/White_point>:
    The white point of an illuminant is the chromaticity of a white object
    under the illuminant.
    '''
    return


def a():
    '''CIE standard illuminant A is intended to represent typical, domestic,
    tungsten-filament lighting. Its relative spectral power distribution is
    that of a Planckian radiator at a temperature of approximately 2856 K. CIE
    standard illuminant A should be used in all applications of colorimetry
    involving the use of incandescent lighting, unless there are specific
    reasons for using a different illuminant.
    -- CIE Standard Illuminants for Colorimetry, 1999
    '''
    # https://en.wikipedia.org/wiki/Standard_illuminant#Illuminant_A
    lmbda = numpy.arange(300, 831)
    c2 = 1.435e7
    color_temp = 2848
    vals = 100 * (560 / lmbda)**5 * (
        (numpy.exp(c2 / (color_temp * 560)) - 1) /
        (numpy.exp(c2 / (color_temp * lmbda)) - 1)
        )
    return lmbda, vals


def d50():
    # http://www.npsg.uwaterloo.ca/data/illuminant.php
    lmbda = numpy.arange(300, 781, 5)
    vals = numpy.array([
     0.019, 1.035, 2.051, 4.914, 7.778, 11.263, 14.748, 16.348, 17.948, 19.479,
     21.01, 22.476, 23.942, 25.451, 26.961, 25.724, 24.488, 27.179, 29.871,
     39.589, 49.308, 52.91, 56.513, 58.273, 60.034, 58.926, 57.818, 66.321,
     74.825, 81.036, 87.247, 88.93, 90.612, 90.99, 91.368, 93.238, 95.109,
     93.536, 91.963, 93.843, 95.724, 96.169, 96.613, 96.871, 97.129, 99.614,
     102.099, 101.427, 100.755, 101.536, 102.317, 101.159, 100., 98.868,
     97.735, 98.327, 98.918, 96.208, 93.499, 95.593, 97.688, 98.478, 99.269,
     99.155, 99.042, 97.382, 95.722, 97.29, 98.857, 97.262, 95.667, 96.929,
     98.19, 100.597, 103.003, 101.068, 99.133, 93.257, 87.381, 89.492, 91.604,
     92.246, 92.889, 84.872, 76.854, 81.683, 86.511, 89.546, 92.58, 85.405,
     78.23, 67.961, 57.692, 70.307, 82.923, 80.599, 78.274,
     ])
    return lmbda, vals


def d65():
    # See
    #
    # http://www.npsg.uwaterloo.ca/data/illuminant.php
    # https://www.rit.edu/cos/colorscience/rc_useful_data.php
    #
    # for the raw data.
    lmbda = numpy.arange(300, 831)
    vals = numpy.array([
        0.0341, 0.36014, 0.68618, 1.01222, 1.33826, 1.6643, 1.99034, 2.31638,
        2.64242, 2.96846, 3.2945, 4.98865, 6.6828, 8.37695, 10.0711, 11.7652,
        13.4594, 15.1535, 16.8477, 18.5418, 20.236, 21.9177, 23.5995, 25.2812,
        26.963, 28.6447, 30.3265, 32.0082, 33.69, 35.3717, 37.0535, 37.343,
        37.6326, 37.9221, 38.2116, 38.5011, 38.7907, 39.0802, 39.3697, 39.6593,
        39.9488, 40.4451, 40.9414, 41.4377, 41.934, 42.4302, 42.9265, 43.4228,
        43.9191, 44.4154, 44.9117, 45.0844, 45.257, 45.4297, 45.6023, 45.775,
        45.9477, 46.1203, 46.293, 46.4656, 46.6383, 47.1834, 47.7285, 48.2735,
        48.8186, 49.3637, 49.9088, 50.4539, 50.9989, 51.544, 52.0891, 51.8777,
        51.6664, 51.455, 51.2437, 51.0323, 50.8209, 50.6096, 50.3982, 50.1869,
        49.9755, 50.4428, 50.91, 51.3773, 51.8446, 52.3118, 52.7791, 53.2464,
        53.7137, 54.1809, 54.6482, 57.4589, 60.2695, 63.0802, 65.8909, 68.7015,
        71.5122, 74.3229, 77.1336, 79.9442, 82.7549, 83.628, 84.5011, 85.3742,
        86.2473, 87.1204, 87.9936, 88.8667, 89.7398, 90.6129, 91.486, 91.6806,
        91.8752, 92.0697, 92.2643, 92.4589, 92.6535, 92.8481, 93.0426, 93.2372,
        93.4318, 92.7568, 92.0819, 91.4069, 90.732, 90.057, 89.3821, 88.7071,
        88.0322, 87.3572, 86.6823, 88.5006, 90.3188, 92.1371, 93.9554, 95.7736,
        97.5919, 99.4102, 101.228, 103.047, 104.865, 106.079, 107.294, 108.508,
        109.722, 110.936, 112.151, 113.365, 114.579, 115.794, 117.008, 117.088,
        117.169, 117.249, 117.33, 117.41, 117.49, 117.571, 117.651, 117.732,
        117.812, 117.517, 117.222, 116.927, 116.632, 116.336, 116.041, 115.746,
        115.451, 115.156, 114.861, 114.967, 115.073, 115.18, 115.286, 115.392,
        115.498, 115.604, 115.711, 115.817, 115.923, 115.212, 114.501, 113.789,
        113.078, 112.367, 111.656, 110.945, 110.233, 109.522, 108.811, 108.865,
        108.92, 108.974, 109.028, 109.082, 109.137, 109.191, 109.245, 109.3,
        109.354, 109.199, 109.044, 108.888, 108.733, 108.578, 108.423, 108.268,
        108.112, 107.957, 107.802, 107.501, 107.2, 106.898, 106.597, 106.296,
        105.995, 105.694, 105.392, 105.091, 104.79, 105.08, 105.37, 105.66,
        105.95, 106.239, 106.529, 106.819, 107.109, 107.399, 107.689, 107.361,
        107.032, 106.704, 106.375, 106.047, 105.719, 105.39, 105.062, 104.733,
        104.405, 104.369, 104.333, 104.297, 104.261, 104.225, 104.19, 104.154,
        104.118, 104.082, 104.046, 103.641, 103.237, 102.832, 102.428, 102.023,
        101.618, 101.214, 100.809, 100.405, 100., 99.6334, 99.2668, 98.9003,
        98.5337, 98.1671, 97.8005, 97.4339, 97.0674, 96.7008, 96.3342, 96.2796,
        96.225, 96.1703, 96.1157, 96.0611, 96.0065, 95.9519, 95.8972, 95.8426,
        95.788, 95.0778, 94.3675, 93.6573, 92.947, 92.2368, 91.5266, 90.8163,
        90.1061, 89.3958, 88.6856, 88.8177, 88.9497, 89.0818, 89.2138, 89.3459,
        89.478, 89.61, 89.7421, 89.8741, 90.0062, 89.9655, 89.9248, 89.8841,
        89.8434, 89.8026, 89.7619, 89.7212, 89.6805, 89.6398, 89.5991, 89.4091,
        89.219, 89.029, 88.8389, 88.6489, 88.4589, 88.2688, 88.0788, 87.8887,
        87.6987, 87.2577, 86.8167, 86.3757, 85.9347, 85.4936, 85.0526, 84.6116,
        84.1706, 83.7296, 83.2886, 83.3297, 83.3707, 83.4118, 83.4528, 83.4939,
        83.535, 83.576, 83.6171, 83.6581, 83.6992, 83.332, 82.9647, 82.5975,
        82.2302, 81.863, 81.4958, 81.1285, 80.7613, 80.394, 80.0268, 80.0456,
        80.0644, 80.0831, 80.1019, 80.1207, 80.1395, 80.1583, 80.177, 80.1958,
        80.2146, 80.4209, 80.6272, 80.8336, 81.0399, 81.2462, 81.4525, 81.6588,
        81.8652, 82.0715, 82.2778, 81.8784, 81.4791, 81.0797, 80.6804, 80.281,
        79.8816, 79.4823, 79.0829, 78.6836, 78.2842, 77.4279, 76.5716, 75.7153,
        74.859, 74.0027, 73.1465, 72.2902, 71.4339, 70.5776, 69.7213, 69.9101,
        70.0989, 70.2876, 70.4764, 70.6652, 70.854, 71.0428, 71.2315, 71.4203,
        71.6091, 71.8831, 72.1571, 72.4311, 72.7051, 72.979, 73.253, 73.527,
        73.801, 74.075, 74.349, 73.0745, 71.8, 70.5255, 69.251, 67.9765,
        66.702, 65.4275, 64.153, 62.8785, 61.604, 62.4322, 63.2603, 64.0885,
        64.9166, 65.7448, 66.573, 67.4011, 68.2293, 69.0574, 69.8856, 70.4057,
        70.9259, 71.446, 71.9662, 72.4863, 73.0064, 73.5266, 74.0467, 74.5669,
        75.087, 73.9376, 72.7881, 71.6387, 70.4893, 69.3398, 68.1904, 67.041,
        65.8916, 64.7421, 63.5927, 61.8752, 60.1578, 58.4403, 56.7229, 55.0054,
        53.288, 51.5705, 49.8531, 48.1356, 46.4182, 48.4569, 50.4956, 52.5344,
        54.5731, 56.6118, 58.6505, 60.6892, 62.728, 64.7667, 66.8054, 66.4631,
        66.1209, 65.7786, 65.4364, 65.0941, 64.7518, 64.4096, 64.0673, 63.7251,
        63.3828, 63.4749, 63.567, 63.6592, 63.7513, 63.8434, 63.9355, 64.0276,
        64.1198, 64.2119, 64.304, 63.8188, 63.3336, 62.8484, 62.3632, 61.8779,
        61.3927, 60.9075, 60.4223, 59.9371, 59.4519, 58.7026, 57.9533, 57.204,
        56.4547, 55.7054, 54.9562, 54.2069, 53.4576, 52.7083, 51.959, 52.5072,
        53.0553, 53.6035, 54.1516, 54.6998, 55.248, 55.7961, 56.3443, 56.8924,
        57.4406, 57.7278, 58.015, 58.3022, 58.5894, 58.8765, 59.1637, 59.4509,
        59.7381, 60.0253, 60.3125,
        ])
    return lmbda, vals


def f2():
    # http://www.npsg.uwaterloo.ca/data/illuminant.php
    lmbda = numpy.arange(300, 781, 5)
    vals = numpy.array([
        1.18, 1.48, 1.84, 2.15, 3.44, 15.69, 3.85, 3.74, 4.19, 4.62, 5.06,
        34.98, 11.81, 6.27, 6.63, 6.93, 7.19, 7.40, 7.54, 7.62, 7.65, 7.62,
        7.62, 7.45, 7.28, 7.15, 7.05, 7.04, 7.16, 7.47, 8.04, 8.88, 10.01,
        24.88, 16.64, 14.59, 16.16, 17.56, 18.62, 21.47, 22.79, 19.29, 18.66,
        17.73, 16.54, 15.21, 13.80, 12.36, 10.95, 9.65, 8.40, 7.32, 6.31, 5.43,
        4.68, 4.02, 3.45, 2.96, 2.55, 2.19, 1.89, 1.64, 1.53, 1.27, 1.10, 0.99,
        0.88, 0.76, 0.68, 0.61, 0.56, 0.54, 0.51, 0.47, 0.47, 0.43, 0.46, 0.47,
        0.4, 0.33, 0.27,
        ])
    return lmbda, vals
