1. `docker attach <container-id>`
	1. attach stdin, stdout and stderr to your shell.
2. `docker exec -it <container-name> /bin/bash`
	1. `-i`: keep STDIN open even if not attached
	2. `-t` alloc a psuedo-tty
3. `docker image build`: assembles the container
4. `docker image inspect`: view labels