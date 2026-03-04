FROM python:3.11-slim
WORKDIR /app
RUN pip install --no-cache-dir pyyaml
COPY tiering.py .
COPY policy ./policy
CMD ["python","tiering.py"]
