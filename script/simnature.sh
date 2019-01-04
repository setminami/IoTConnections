#!/usr/bin/env bash
RUNNABLE_PREFIX=/usr/local
DEFAULT_VENV_NAME=Simnature
SIMNATURE_PRJ_PATH=~/${DEFAULT_VENV_NAME}
PRJ_NAME=IoTConnections
PYVERSION=3.7
PRJ_PATH=${SIMNATURE_PRJ_PATH}/${PRJ_NAME}
SWAGGER_GENERATED_SERVER=${PRJ_PATH}/swagger/python-flask-server-generated/swagger_server

export PYTHONPATH=${RUNNABLE_PREFIX}/lib/python${PYVERSION}:${PRJ_PATH}/script/rpc_server:${SWAGGER_GENERATED_SERVER}