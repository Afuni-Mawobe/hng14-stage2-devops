# Stage 1: builder
FROM node:20-slim AS builder
WORKDIR /app
COPY package*.json ./
RUN npm install --omit=dev

# Stage 2: production
FROM node:20-slim AS production
RUN groupadd -r nodeuser && useradd -r -g nodeuser nodeuser
WORKDIR /app
COPY --from=builder /app/node_modules ./node_modules
COPY . .
RUN chown -R nodeuser:nodeuser /app
USER nodeuser
HEALTHCHECK --interval=30s --timeout=3s CMD node -e "require('http').get('http://localhost:3000', (r) => { if (r.statusCode !== 200) throw new Error(); })" || exit 1
EXPOSE 3000
CMD ["npm", "start"]