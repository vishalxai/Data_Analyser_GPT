# 1. Use an official lightweight Python image
FROM python:3.11-slim

# 2. Set the working directory inside the cloud container
WORKDIR /app

# 3. Copy your requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy all your project files into the container
COPY . .

# 5. Create the temp directory so the local executor has a place to work
RUN mkdir -p temp

# 6. Expose the port Streamlit uses
EXPOSE 8501

# 7. Tell the container how to run your app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]