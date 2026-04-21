# Stage 1: Build stage
FROM node:20-slim AS builder

WORKDIR /app

# Copy package files and install dependencies
COPY package*.json ./
RUN npm install --omit=dev

# Stage 2: Runtime stage
FROM node:20-slim

# Use the built-in 'node' user instead of root
WORKDIR /app
COPY --from=builder /app/node_modules ./node_modules
COPY . .

USER node

# Healthcheck: check if the web server responds
HEALTHCHECK --interval=30s --timeout=3s \
  CMD node -e "require('http').get('http://localhost:3000', (r) => { if (r.statusCode !== 200) throw new Error(); })" || exit 1

EXPOSE 3000

CMD ["npm", "start"]