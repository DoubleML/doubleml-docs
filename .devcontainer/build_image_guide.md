# Building and Publishing the Docker Image

This guide shows how to build the DoubleML documentation development container locally and publish it to Docker Hub.

## Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running
- Access to the `svenklaassen` [Docker Hub](https://www.docker.com/products/docker-hub/) account
- [doubleml-docs](https://github.com/DoubleML/doubleml-docs) repository cloned to your local machine

## Step 1: Login to Docker Hub

Open a terminal and login to Docker Hub:

```bash
docker login
```

Enter the Docker Hub username (`svenklaassen`) and password (or token) when prompted.

## Step 2: Build the Docker Image

Navigate to your project root directory and build the image (using the `latest`-tag):

```bash
docker build -t svenklaassen/doubleml-docs:latest -f .devcontainer/Dockerfile.dev .
```

To force a complete rebuild without using cache:

```bash
docker build --no-cache -t yourusername/doubleml-docs:latest -f .devcontainer/Dockerfile.dev .
```

## Step 3 (Optional): Verify the image

### Open the repository in VS Code

1. Ensure your `.devcontainer/devcontainer.json` is configured to use your local image:

    ```json
    "image": "svenklaassen/doubleml-docs:latest"
    ```

2. Open your repository in VS Code:

   ```bash
   code /path/to/doubleml-docs
   ```

3. Open the Command Palette (`Ctrl+Shift+P`) and select `Remote-Containers: Reopen in Container`.
   VS Code will use your locally built image.

### Build the documentation

Once inside the container, verify that you can successfully build the documentation:

1. Open a terminal in VS Code (`Terminal > New Terminal`)

2. Build the documentation:

   ```bash
   cd doc
   make html
   ```

3. Check the output for any errors or warnings

4. View the built documentation by opening the output files:

   ```bash
   # On Windows
   explorer.exe _build/html
   
   # On Linux
   xdg-open _build/html
   
   # On macOS
   open _build/html
   ```

If the documentation builds successfully and looks correct, your Docker image is working properly and ready to be pushed to Docker Hub.

## Step 4: Push to Docker Hub

Push your built image to Docker Hub:

```bash
docker push svenklaassen/doubleml-docs:latest
```

## Step 5: Using the Published Image

After publishing, there are two ways to use the image:

### Option 1: Manual Container Management
Pull and run the container manually:

```bash
docker pull svenklaassen/doubleml-docs:latest
# Then run commands to create a container from this image
```

### Option 2: VS Code Integration (Recommended)
Simply reference the image in your `devcontainer.json` file:

```json
"image": "svenklaassen/doubleml-docs:latest"
```

VS Code will automatically pull the image when opening the project in a container - no separate `docker pull` command needed.

## Troubleshooting

### Clear Docker Cache

If you're experiencing issues with cached layers:

```bash
# Remove build cache
docker builder prune

# For a more thorough cleanup
docker system prune -a
```

### Check Image Size

To verify the image size before pushing:

```bash
docker images svenklaassen/doubleml-docs
```