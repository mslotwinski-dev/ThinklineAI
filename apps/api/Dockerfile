# --- ETAP 1: Budowanie dla Produkcji (builder) ---
FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# --- ETAP 2: Środowisko Deweloperskie (development) ---
FROM node:18-alpine AS development
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
ENV NODE_ENV=development
EXPOSE 5000
CMD ["npm", "run", "start:dev"]

# --- ETAP 3: Środowisko Produkcyjne (production) ---
FROM node:18-alpine AS production
WORKDIR /app
COPY package*.json ./
RUN npm install --production
COPY --from=builder /app/dist ./dist
ENV NODE_ENV=production
EXPOSE 8080
CMD ["node", "dist/main.js"]