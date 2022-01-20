FROM ubuntu:bionic
COPY /code /code/
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENV DEBIAN_FRONTEND=nonintercative
RUN \
  apt-get update && \
  apt-get install software-properties-common -y && \
  add-apt-repository ppa:deadsnakes/ppa && \
  apt-get update && \
  apt-get install python3.9 python3-pip python3.9-distutils -y && \
  python3.9 -m pip install --upgrade setuptools && \
  python3.9 -m pip install --upgrade pip && \
  python3.9 -m pip install --upgrade distlib && \
  python3.9 -m pip install -r /code/requirements.txt
WORKDIR /code
CMD ["/bin/bash"]