# Use an official Python runtime as a parent image
FROM python:3.11

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
WORKDIR /tanxfi_task

# Copy the current directory contents into the container at /tanxfi_task
COPY . /tanxfi_task

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install Redis server
RUN apt-get update && apt-get install -y redis-server

# Apply database migrations
RUN python manage.py makemigrations
RUN python manage.py migrate

# Expose port 8000
EXPOSE 8000

# Copy the entrypoint script into the container
COPY entrypoint.sh /tanxfi_task/entrypoint.sh

# Give execute permissions to the script
RUN chmod +x /tanxfi_task/entrypoint.sh

# Run the entrypoint script
CMD ["/tanxfi_task/entrypoint.sh"]
