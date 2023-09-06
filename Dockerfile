# Use an official Nginx image as the base image
FROM nginx:alpine

# Copy the contents of the local 'frontend' directory to the Nginx document root
COPY ./ /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Start Nginx in the foreground
CMD ["nginx", "-g", "daemon off;"]
