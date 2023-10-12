# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory within the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Run the Python program when the container launches
CMD ["python", "scramble.py"]
