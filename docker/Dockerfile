FROM python:3.9-bullseye

# Metadata
LABEL MAINTAINERS="chimera (chimera@chimera.website)"
LABEL VERSION="1.0"

# Creating virtual enviroment
ENV VIRTUAL_ENV=/opt/venv
RUN python -m venv $VIRTUAL_ENV
# Some magic: next line also activates venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip -r requirements.txt

# Switching to an unpriviliged user
RUN useradd --create-home sorokin-hvost
USER sorokin-hvost
WORKDIR /home/sorokin-hvost/bot
COPY . /home/sorokin-hvost/bot

# Running a bot
CMD python -u game.py
