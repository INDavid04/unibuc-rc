FROM python:3.9-slim

RUN apt-get update && apt-get install -y curl && pip install flask

# Pentru a treia cerinta, cea cu docker compose, avem nevoie de scapy
RUN pip install scapy
