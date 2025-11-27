# DurasAGV Product

Welcome to the `product-duras-agv` flagship product.

This is a standalone application that *consumes* services from the NovaEco, primarily the `NovaAgro` sector and `NovaSapien` enabler, to provide.

This is a monorepo that contains the three core components of the `product-duras-agv` product:

  * **`/api`**: The "Backend-for-Frontend" (BFF) API service.
  * **`/app`**: The frontend web application (e.g., React/Node.js).
  * **`/website`**: The Docusaurus-based marketing and support site for this product.
  * **`/tests`**: The intra-repo integration tests that verify `/api` and `/app` work together.

## 🚀 Getting Started (Local Development)

This repository is configured to use **DevContainers** for a one-click setup, powered by our centralized `ecosystem-devtools` images.

1.  Make sure you have([https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/)) installed and running.
2.  Install the([https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)) in VS Code.
3.  Clone this repository: `git clone https://github.com/novaeco-tech/product-duras-agv.git`
4.  Open the cloned folder in VS Code.
5.  A pop-up will appear: "Folder contains a Dev Container... Reopen in Container?". Click **"Reopen in Container"**.

This will instantly download the pre-built `dev-python` and `dev-node` images and start all three `product-duras-agv` services (`api`, `app`, `website`) in an integrated environment.

**Note:** This environment does *not* run other enablers (like `NovaAgro` or `NovaSapien`). You must write unit tests in `/api/tests` that *mock* any external API calls.