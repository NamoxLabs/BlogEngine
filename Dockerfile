### Build and install packages
FROM python:3.7 as build-python

RUN \
  apt-get -y update && \
  apt-get install -y gettext && \
  # Cleanup apt cache
  apt-get clean && \
  rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install pipenv
ADD Pipfile /app/
ADD Pipfile.lock /app/
WORKDIR /app
RUN pipenv install --system --deploy --dev

### Build static assets
FROM node:10 as build-nodejs

ARG STATIC_URL
ENV STATIC_URL ${STATIC_URL:-/static/}

# Install node_modules
ADD webpack.config.js app.json package.json package-lock.json tsconfig.json webpack.d.ts /app/
WORKDIR /app
RUN npm install

# Build static
ADD ./engine/static /app/engine/static/
ADD ./templates /app/templates/
RUN \
  STATIC_URL=${STATIC_URL} \
  npm run build-assets --production 
  #&& \
  #npm run build-emails --production

### Final image
FROM python:3.7-slim

ARG STATIC_URL
ENV STATIC_URL ${STATIC_URL:-/static/}

RUN \
  apt-get update && \
  apt-get install -y libxml2 libssl1.1 libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 shared-mime-info mime-support && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/*

ADD . /app
COPY --from=build-python /usr/local/lib/python3.7/site-packages/ /usr/local/lib/python3.7/site-packages/
COPY --from=build-python /usr/local/bin/ /usr/local/bin/
COPY --from=build-nodejs /app/engine/static /app/engine/static
COPY --from=build-nodejs /app/webpack-bundle.json /app/
COPY --from=build-nodejs /app/templates /app/templates
WORKDIR /app

RUN SECRET_KEY=dummy \
    STATIC_URL=${STATIC_URL} \
    python3 manage.py collectstatic --no-input

RUN useradd --system engine && \
    mkdir -p /app/media /app/static && \
    chown -R engine:engine /app/

USER engine

EXPOSE 9999
ENV PORT 9999

ENV PYTHONUNBUFFERED 1
ENV PROCESSES 4
CMD ["uwsgi", "/app/engine/wsgi/uwsgi.ini"]

#FROM python:3
#ENV PYTHONUNBUFFERED 1
#RUN mkdir /app
#WORKDIR /app
#ADD requirements.txt /app/
#RUN pip install -r requirements.txt
#ADD . /app/