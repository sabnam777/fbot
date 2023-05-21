#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @Bae_wafaaaFROM python:3.9

WORKDIR /app

COPY . /app/

RUN pip install -r requirements.txt

CMD python main.py
