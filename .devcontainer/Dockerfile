FROM mcr.microsoft.com/devcontainers/python:1-3.12-bullseye

ENV POETRY_VERSION=1.8.3
ENV PYTHONUNBUFFERED 1

RUN git clone https://github.com/aws/aws-elastic-beanstalk-cli-setup.git \
    && python ./aws-elastic-beanstalk-cli-setup/scripts/ebcli_installer.py \
        --location /home/vscode/.ebcli-virtual-env \
# Fix for EB CLI incompatibility with Python 3.12+ https://github.com/aws/aws-elastic-beanstalk-cli/issues/493
    && /home/vscode/.ebcli-virtual-env/.ebcli-virtual-env/bin/python -m pip install cement==2.10.14

ENV VIRTUAL_ENV=/home/vscode/.venv
ENV PATH=$VIRTUAL_ENV/bin:/root/.local/bin:/home/vscode/.ebcli-virtual-env/.ebcli-virtual-env/executables:$PATH
ENV POETRY_VIRTUALENVS_CREATE=false

# Required geo spatial library & other tools
RUN apt-get update \
    && export DEBIAN_FRONTEND=noninteractive \
    && apt-get install -y --no-install-recommends gdal-bin

USER vscode
RUN pip install pipx && \
    pipx install poetry==${POETRY_VERSION} && \
    python -m venv ${VIRTUAL_ENV}

WORKDIR /workspaces/python-one
# COPY pyproject.toml poetry.lock jolpica/ ./
# RUN poetry install --no-root
# [Optional] If your requirements rarely change, uncomment this section to add them to the image.
# COPY requirements.txt /tmp/pip-tmp/
# RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
#    && rm -rf /tmp/pip-tmp



