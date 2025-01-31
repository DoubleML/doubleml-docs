# Build Documentation with Development Container

This guide shows how to use WSL2 (Windows Subsystem for Linux), Docker Desktop, Visual Studio Code (VS Code), and how to work with Development Containers in VS Code on a Windows machine.

Requirements:
 - [VS Code](https://code.visualstudio.com/)
 - [WSL2](https://learn.microsoft.com/en-us/windows/wsl/install)
 - [Docker Desktop](https://docs.docker.com/desktop/setup/install/windows-install/)

## Verify installations & Setup

You can verify the installations in a terminal:
   
   ```bash
   code --version
   wsl --version
   docker --version
   ```

### Configure Docker to Use WSL2

   See [Docker Desktop Documentation](https://docs.docker.com/desktop/features/wsl/#turn-on-docker-desktop-wsl-2).
   - Open Docker Desktop.
   - Go to **Settings > General** and make sure **Use the WSL 2 based engine** is checked.
   - Under **Settings > Resources > WSL Integration**, ensure that your desired Linux distribution(s) are selected for integration with Docker.

### Install Extensions

   - Open Visual Studio Code.
   - Press `Ctrl+Shift+X` to open the Extensions view.
   - Search and install (includes WSL and Dev Containers Extensions):
      - [Remote Development Extension Pack](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack)

   VS Code Documentations:
   - [Developing in WSL](https://code.visualstudio.com/docs/remote/wsl)
   - [Developing inside a Container](https://code.visualstudio.com/docs/devcontainers/containers)


## Build & Open the Development Container

   - Open the project `doubleml-docs` in VS code:

   ```bash
   code .
   ```

   - Open the Command Palette (`Ctrl+Shift+P`).
   - Type `Remote-Containers: Reopen Folder in Container`.
   - VS Code will build the new container(this may take some time) and open the project in it.


## Build the documentation

You can build the documentation via

   ```bash
   cd doc
   make html
   ```

   Open the directory in WSL with
   ```bash
   explorer.exe .
   ```