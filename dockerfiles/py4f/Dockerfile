FROM ubuntu:latest
RUN apt-get update && apt-get -y update
RUN apt-get install -y build-essential python3.6 python3-pip python3-dev
RUN apt-get install -y git
RUN pip3 -q install pip --upgrade

WORKDIR .
COPY . .

RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

RUN mkdir p4f
WORKDIR p4f

RUN git clone https://github.com/yhilpisch/py4fi2nd.git

ENTRYPOINT ["jupyter", "notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0", "--allow-root"]



