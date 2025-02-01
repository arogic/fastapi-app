FROM python:3.9-slim

WORKDIR /app

COPY app/requirements.txt /app/

# Add /home/ubuntu/.local/bin to the PATH
ENV PATH="/home/ubuntu/.local/bin:${PATH}"

# Create a non-root user and group
RUN groupadd -r ubuntu && useradd -r -g ubuntu -m ubuntu

# Set the working directory
WORKDIR /app

COPY app /app/

# Change ownership of the application files to the non-root user
RUN chown -R ubuntu:ubuntu /app

# Switch to the non-root user
USER ubuntu

RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app will run on
EXPOSE 8000

# Run the FastAPI app using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

