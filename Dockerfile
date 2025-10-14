FROM python:3.9-slim
RUN useradd --create-home --shell /bin/bash appuser
WORKDIR /home/appuser/app
COPY app/requeriments.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app/ .
RUN chown -R appuser:appuser /home/appuser
USER appuser
EXPOSE 5000
ENV FLASK_APP=app.py
ENV FLASK_ENV=production
CMD ["python", "app.py"]
