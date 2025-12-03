FROM node:20-alpine

WORKDIR /app

# Copy dependency files first for caching
COPY package.json package-lock.json ./
RUN npm ci

# Copy the rest of the app
COPY . .

EXPOSE 5173
CMD ["npm", "run", "dev", "--", "--host"]