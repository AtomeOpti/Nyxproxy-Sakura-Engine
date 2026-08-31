# 🌸 Nyxproxy Sakura Engine

Nyxproxy Sakura Engine is a high-performance, animated Command-Line Interface (CLI) application built for real-time proxy scraping, testing, and management. Designed with a custom dark/neon Sakura aesthetic using Python's `rich` ecosystem, it aggregates free proxies from multiple sources, validates their latency, anonymity levels, and protocols concurrently, and presents live updates via a dynamic terminal interface.

---

## ⚡ Key Features

* **Multi-Source Scraping:** Aggregates proxy feeds concurrently across dozens of public and private sources.
* **Real-Time Latency & Anonymity Checking:** Tests HTTP/SOCKS proxies on the fly with custom multi-threading workers.
* **Interactive Terminal UI:** Features dynamic tables, live hit-counters, animated indicators, and custom ascii art visuals.
* **Export Options:** Easily save working proxy hits straight to clean `.txt` or `.csv` files.

---

## 🚧 Development Status & Downloads

> **Note:** Nyxproxy Sakura Engine is currently under **active development**. 

* **Source Preview:** The code in this repository serves as an architectural preview. Core engine components and private provider modules are stripped in this public repository.
* **Executables & Binaries:** Compiled binaries (`.exe`) are **not available for download on GitHub** at this time. 

### 🌐 Upcoming Release Platform
All official releases, compiled executables, and documentation will be hosted exclusively on our upcoming official website once the beta testing phase finishes. 

Stay tuned for the official domain announcement!

---

## 📁 Repository Structure

```text
├── cli_app.py        # CLI interface and layout engine (Preview)
├── scraper.py        # Scraping and checking core thread pool (Preview)
├── providers.py      # Provider list and feed endpoints (Preview)
├── image_0.png       # Terminal ASCII banner asset
└── README.md         # Project documentation
