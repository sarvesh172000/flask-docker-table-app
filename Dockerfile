# Step 1: Use an official Python runtime as a parent image
FROM python:3.11-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the requirements file and install dependencies
# This is done in a separate step to leverage Docker's layer caching.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Step 4: Copy the rest of the application code into the container
COPY . .

# Step 5: Expose the port the app will run on
EXPOSE 8000

# Step 6: Define the command to run the application using Gunicorn
# Binds the server to 0.0.0.0 to be accessible from outside the container
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]