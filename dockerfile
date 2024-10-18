# Use a lightweight Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /home/data/dockerfile

# Copy the Python script and text files to the container
COPY scripts.py /home/data/dockerfile/scripts.py
COPY IF.txt /home/data/dockerfile/IF.txt
COPY AlwaysRememberUsThisWay.txt /home/data/dockerfile/AlwaysRememberUsThisWay.txt

# Install any necessary dependencies (if any)
RUN pip install --upgrade pip && pip install --no-cache-dir requests

# Run the Python script
CMD ["python", "/home/data/dockerfile/scripts.py"]
