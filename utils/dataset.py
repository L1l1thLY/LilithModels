from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import gzip
import os
import shutil  # Prove some functions for file op
import tempfile

import numpy as np
from six.moves import urllib
import tensorflow as tf

base_url = 'https://storage.googleapis.com/cvdf-datasets/mnist/'

def read32(bytestream):
    """Read 4 bytes from bytestream as an unsigned 32-bit integer."""
    pass


def check_image_file_header(filename):
    """Validate that filename corresponds to images for the MNIST dataset."""
    pass


def check_labels_file_header(filename):
    """Validate that filename corresponds to labels for the MNIST dataset."""
    pass


def download(directory, filename):
    """Download (and unzip) a file from the MNIST dataset if not already done."""
    pass


def dataset(directory, images_file, labels_file):
    """Download and parse MNIST dataset."""
    pass


def train(directory):
    """tf.data.Dataset object for MNIST training data."""
    pass


def test(directory):
    """tf.data.Dataset object for MNIST test data."""
    pass
