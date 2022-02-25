FROM tensorflow/tensorflow:2.7.1

RUN apt-get update && apt-get install -y --no-install-recommends \
    ocl-icd-dev \
    gcc \
    ocl-icd-opencl-dev \
    opencl-headers \
    clinfo \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN python3 -m pip install --upgrade pip
RUN pip install stardist tqdm edt