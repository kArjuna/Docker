# Use a lightweight Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /Users/mallikarjuna/Desktop/dockerfile

# Copy the Python script and text files to the container
COPY scripts.py /Users/mallikarjuna/Desktop/dockerfile/scripts.py
COPY IF.txt /Users/mallikarjuna/Desktop/dockerfile/IF.txt
COPY AlwaysRememberUsThisWay.txt /Users/mallikarjuna/Desktop/dockerfile/AlwaysRememberUsThisWay.txt

# Install any necessary dependencies (if any)
RUN pip install --upgrade pip && pip install --no-cache-dir requests

# Run the Python script
CMD ["python", "/Users/mallikarjuna/Desktop/dockerfile/scripts.py"]

