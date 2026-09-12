<div align="center">
  <video src="./nyxproxy-demo.mp4" controls muted loop playsinline width="760"></video>

  <a href="./nyxproxy-demo.mp4">▶ Open the Nyxproxy Sakura Engine demo video</a>

  # Nyxproxy Sakura Engine

  **A high-performance proxy discovery and routing engine.**  
  A transparent public preview of the Sakura network stack by **AtomeOpti**.

  <p>
    <a href="https://atomeopti.github.io/Nyxproxy-Sakura-Engine/"><strong>Launch the official experience →</strong></a>
  </p>

  <p>
    <img src="https://img.shields.io/badge/status-active-3fb950?style=flat-square" alt="Active" />
    <img src="https://img.shields.io/badge/license-MIT-8b5cf6?style=flat-square" alt="MIT License" />
    <img src="https://img.shields.io/badge/python-3.x-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python 3" />
    <img src="https://img.shields.io/badge/source-preview-f472b6?style=flat-square" alt="Source preview" />
  </p>
</div>

---

## Overview

Nyxproxy Sakura Engine is a network and proxy-routing project focused on **provider management, node discovery and traffic tooling**.

This repository is the **public source preview**: it documents the project’s structure and interface while keeping the production scraping and build components private.

> [!IMPORTANT]
> This repository is **not intended to be compiled or executed as a complete production build**. For the supported, up-to-date version, use the official website below.

<div align="center">

### [Download / discover the official version](https://atomeopti.github.io/Nyxproxy-Sakura-Engine/)

</div>

## What the project showcases

| Area | Description |
| :--- | :--- |
| **Provider management** | Organises active proxy sources and network endpoints. |
| **Node discovery** | Provides the structure used to retrieve and process proxy nodes. |
| **CLI experience** | Presents a clear terminal interface with Sakura branding and runtime notices. |
| **Web presentation** | Includes a dedicated dark interface for product documentation and discovery. |

## Architecture at a glance

```text
┌──────────────────────┐
│      CLI / UI         │  cli_app.py · index.html
└──────────┬───────────┘
           │
┌──────────▼───────────┐
│   Provider Manager    │  providers.py
└──────────┬───────────┘
           │
┌──────────▼───────────┐
│   Sakura Scraper      │  scraper.py
└──────────┬───────────┘
           │
┌──────────▼───────────┐
│  Proxy validation     │  private production layer
└──────────────────────┘
```

## Repository map

| File | Role |
| :--- | :--- |
| [`cli_app.py`](./cli_app.py) | Terminal entry point and branded CLI preview. |
| [`providers.py`](./providers.py) | Provider endpoint management structure. |
| [`scraper.py`](./scraper.py) | Public interface of the proxy discovery layer. |
| [`index.html`](./index.html) | Product landing page and developer-facing presentation. |
| [`image_0.png`](./image_0.png) | Visual asset used by the project interface. |
| [`nyxproxy-demo.mp4`](./nyxproxy-demo.mp4) | Product demo video. |
| [`LICENSE`](./LICENSE) | MIT license for this repository. |

## Running the public preview

The preview intentionally stops before the private production layer is loaded:

```bash
python cli_app.py
```

Expected behaviour: the CLI displays the Nyxproxy Sakura Engine banner and explains that the complete engine is distributed through the official release channel.

## Why is the engine partially stripped?

The production build relies on private server-side and build-side verification components. Keeping those components out of the public repository helps protect the official distribution and prevents unauthorised modified builds.

This repository is therefore best understood as a **transparent technical preview**, not as a standalone replacement for the official application.

## Roadmap

- [x] Public project overview
- [x] CLI preview and provider abstraction
- [x] Dedicated product landing page
- [ ] Expanded public API documentation
- [ ] More architecture and integration examples

## Official links

- **Website:** [atomeopti.github.io/Nyxproxy-Sakura-Engine](https://atomeopti.github.io/Nyxproxy-Sakura-Engine/)
- **Organisation:** [github.com/AtomeOpti](https://github.com/AtomeOpti)

<div align="center">
  <sub>Built and maintained by <a href="https://github.com/AtomeOpti">AtomeOpti</a> · Nyxproxy Sakura Engine</sub>
</div>
