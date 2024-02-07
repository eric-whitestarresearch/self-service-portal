FROM python:3.10.13-slim-bookworm
RUN mkdir /code
COPY code /code
RUN pip install -r /code/requirements.txt
ENTRYPOINT ["python3", "/code/runner.py"]