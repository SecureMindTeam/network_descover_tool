# 🛡️ SecureMind Network Discover Tool

<div align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Scapy-Security-red?style=for-the-badge" alt="Scapy">
  <img src="https://img.shields.io/badge/Blue_Team-SecureMind-blue?style=for-the-badge" alt="Blue Team">
</div>

## 📖 Overview
The **Network Discover Tool** is a fast, efficient, and lightweight utility developed by the **SecureMind (Blue Team)**. Operating on the **ARP (Address Resolution Protocol)**, this tool is designed to actively discover live hosts connected to a Local Area Network (LAN).

As a foundational step in network security, asset discovery is crucial for Security Operations Center (SOC) analysts and system administrators to identify active machines and detect unauthorized or rogue devices within the network environment.

## ✨ Features
* **Active Host Discovery:** Broadcasts ARP requests to identify live devices on the network.
* **Detailed Output:** Extracts and displays both the IP Address and the Hardware (MAC) Address of responding hosts.
* **Professional CLI:** Features a styled, easy-to-read command-line interface powered by `rich` and `pyfiglet`.
* **Lightweight:** Minimal dependencies and rapid execution.

## 🛠️ Prerequisites
Before running this tool, ensure you have the following:
* **Python 3.x** installed on your system.
* **Root/Administrator Privileges:** Operating on the network layer to craft and send raw packets via `scapy` requires elevated permissions.

## ⚙️ Installation

1. Clone the repository to your local machine:
   ```bash
   git clone [https://github.com/YourUsername/network-discover-tool.git](https://github.com/YourUsername/network-discover-tool.git)
   cd network-discover-tool
2. pip install -r requirements.txt

## 🚀 Usage
sudo python main.py

## 📊 Example Output
------------------------------ Live Host Machine ------------------------------
*******************************************************************************
   _____                            __  __ _           _ 
  / ____|                          |  \/  (_)         | |
 | (___   ___  ___ _   _ _ __ ___  | \  / |_ _ __   __| |
  \___ \ / _ \/ __| | | | '__/ _ \ | |\/| | | '_ \ / _` |
  ____) |  __/ (__| |_| | | |  __/ | |  | | | | | | (_| |
 |_____/ \___|\___|\__,_|_|  \___| |_|  |_|_|_| |_|\__,_|
                                                         
*******************************************************************************
src Ip Is > 192.168.1.1   src Mac Is >  00:1A:2B:3C:4D:5E
src Ip Is > 192.168.1.5   src Mac Is >  AA:BB:CC:DD:EE:FF

