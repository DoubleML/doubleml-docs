# Build Documentation with Development Container

This guide shows how to use WSL2 (Windows Subsystem for Linux), Docker Desktop, Visual Studio Code (VS Code), and how to work with Development Containers in VS Code on a Windows machine.

Requirements:
 - [VS Code](https://code.visualstudio.com/)
 - [WSL2](https://learn.microsoft.com/en-us/windows/wsl/install)
 - [Docker Desktop](https://docs.docker.com/desktop/setup/install/windows-install/)

## Step 1: Verify installations & Setup

You can verify the installations in a terminal:
   
   ```bash
   code --version
   wsl --version
   docker --version
   ```

### Configure Docker to Use WSL2

   See [Docker Desktop Documentation](https://docs.docker.com/desktop/features/wsl/#turn-on-docker-desktop-wsl-2).
   1. Open Docker Desktop.
   2. Go to **Settings > General** and make sure **Use the WSL 2 based engine** is checked.
   3. Under **Settings > Resources > WSL Integration**, ensure that your desired Linux distribution(s) are selected for integration with Docker.

### Install Extensions

   1. Open Visual Studio Code.
   2. Press `Ctrl+Shift+X` to open the Extensions view.
   3. Search and install (includes WSL and Dev Containers Extensions):
      - [Remote Development Extension Pack](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack)

   Helpful VS Code Documentations:
   - [Developing in WSL](https://code.visualstudio.com/docs/remote/wsl)
   - [Developing inside a Container](https://code.visualstudio.com/docs/devcontainers/containers)


## Step 2: Open the Development Container (Using Pre-built Image)

For faster setup, we'll use a pre-built Docker image:

1. Open the `doubleml-docs` repository in VS Code:

   ```bash
   code /path/to/doubleml-docs
   ```

2. Open the Command Palette (`Ctrl+Shift+P`).
3. Type `Dev Containers: Reopen in Container`.

VS Code will pull the `svenklaassen/doubleml-docs:latest` image (if needed) based on `devcontainer.json` and open the project in the container.<br>
This approach is much faster than building the container from scratch. VS Code automatically downloads the image from Docker Hub if it's not already on your system.


## Step 3: Build the documentation

1. Open a terminal in VS Code (`Terminal > New Terminal`)

2. Build the documentation:

   ```bash
   cd doc
   make html
   ```

3. View the built documentation by opening the output files:

   ```bash
   # On Windows
   explorer.exe _build/html
   
   # On Linux
   xdg-open _build/html
   
   # On macOS
   open _build/html
   ```
