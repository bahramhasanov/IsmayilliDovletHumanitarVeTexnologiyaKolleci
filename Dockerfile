FROM python:3.9

ENV PYTHONUNBUFFERED 1
ENV APP_ROOT /kollec
ENV DEBUG False

ADD requirements.txt /requirements.txt
RUN pip install virtualenvwrapper
RUN python3 -m venv /venv
RUN /venv/bin/pip install -U pip

RUN /venv/bin/pip install --no-cache-dir -r /requirements.txt
RUN mkdir ${APP_ROOT}
WORKDIR ${APP_ROOT}
ADD . ${APP_ROOT}
RUN if [ -f manage.py ]; then /venv/bin/python manage.py collectstatic --noinput; fi