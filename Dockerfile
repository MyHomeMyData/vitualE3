FROM python:3-alpine

WORKDIR /virtuale3

COPY . .
RUN pip3 install -r requirements.txt
RUN echo -e '#!/bin/sh \n exec python3 /virtuale3/virtualE3.py "$@"' > /usr/bin/virtualE3 && \
    chmod +x /usr/bin/virtualE3

ENV PYTHONUNBUFFERED=1

ENTRYPOINT ["virtualE3"]