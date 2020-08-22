# Base on offical Node.js Alpine image
FROM node:alpine

# Set working directory
WORKDIR /usr/src/app

# # Install PM2 globally
# RUN npm install --global pm2

# Copy package.json and package-lock.json before other files
# Utilise Docker cache to save re-installing dependencies if unchanged
COPY ./package*.json /usr/src/app/

# Install all dependencies
RUN npm install

# Copy all files
COPY ./ /usr/src/app

# Build nextjs files for production.
RUN npm run build