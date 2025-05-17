#!/bin/sh
kaggle kernels output nguyenbnguyen/dog-breed-classification-mobilenet -p ./classification/dog_breeds

find . -name '*.log' -delete

find . -name '*.csv' -delete