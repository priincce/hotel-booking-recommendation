FROM python:slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONBUFFERED=1


WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    libgomp1 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY . .

RUN python -m pip install --upgrade pip setuptools \
    && pip config set global.break-system-packages true

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir -e .

RUN python pipeline/training_pipeline.py

EXPOSE 5000

CMD [ "python", "application.py"]