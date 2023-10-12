# Pepperstone Data Team Code Challenge
Solved by Jitendra Gehlot as part of Data Engineer Role Interview process.

Steps to Execute the program.

1. Build the Docker image:
Open a terminal, navigate to the directory containing your Dockerfile and Python program, and run the following command to build the Docker image. Make sure you have Docker installed on your system.

`docker build -t scramble-app .`

This command will build a Docker image named scramble-app based on the Dockerfile in the current directory. The . at the end indicates the current directory as the build context.

2. Run the Docker container:
You can now run the Docker container based on the image you created.

`docker run scramble-app`

Now, your Python program will run in a Docker container with the specified input and dictionary files. Make sure to adapt the paths and file names to your specific setup.

