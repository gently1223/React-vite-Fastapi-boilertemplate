# Use the official Node.js image as the base image
FROM node:14-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the package.json and package-lock.json files
COPY package*.json ./

# Install the project dependencies
RUN npm install

# Copy the application code
COPY . .

# Build the application
RUN npm run build

# Set the command to run the application as development mode
CMD ["npm", "run", "dev"]
