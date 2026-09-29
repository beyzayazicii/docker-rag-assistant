# Common Docker CLI commands

Source: https://github.com/docker/docs/tree/main/data/cli

## docker container run

Create and run a new container from an image

Aliases: docker container run, docker run

Usage:

```console
docker container run [OPTIONS] IMAGE [COMMAND] [ARG...]
```

### Description of docker container run

The `docker run` command runs a command in a new container, pulling the image if needed and starting the container.

You can restart a stopped container with all its previous changes intact using `docker start`.
Use `docker ps -a` to view a list of all containers, including those that are stopped.

### Options of docker container run

- `--add-host`: Add a custom host-to-IP mapping (host:ip)
- `--annotation`: Add an annotation to the container (passed through to the OCI runtime)
- `--attach`, `-a`: Attach to STDIN, STDOUT or STDERR
- `--blkio-weight`: Block IO (relative weight), between 10 and 1000, or 0 to disable (default 0)
- `--blkio-weight-device`: Block IO weight (relative device weight)
- `--cap-add`: Add Linux capabilities
- `--cap-drop`: Drop Linux capabilities
- `--cgroup-parent`: Optional parent cgroup for the container
- `--cgroupns`: Cgroup namespace to use (host|private) 'host': Run the container in the Docker host's cgroup namespace 'private': Run the container in its own private cgroup namespace '': Use the cgroup namespace as configured by the default-cgroupns-mode option on the daemon (default)
- `--cidfile`: Write the container ID to the file
- `--cpu-count`: CPU count (Windows only)
- `--cpu-percent`: CPU percent (Windows only)
- `--cpu-period`: Limit CPU CFS (Completely Fair Scheduler) period
- `--cpu-quota`: Limit CPU CFS (Completely Fair Scheduler) quota
- `--cpu-rt-period`: Limit CPU real-time period in microseconds
- `--cpu-rt-runtime`: Limit CPU real-time runtime in microseconds
- `--cpu-shares`, `-c`: CPU shares (relative weight)
- `--cpus`: Number of CPUs
- `--cpuset-cpus`: CPUs in which to allow execution (0-3, 0,1)
- `--cpuset-mems`: MEMs in which to allow execution (0-3, 0,1)
- `--detach`, `-d`: Run container in background and print container ID
- `--detach-keys`: Override the key sequence for detaching a container
- `--device`: Add a host device to the container
- `--device-cgroup-rule`: Add a rule to the cgroup allowed devices list
- `--device-read-bps`: Limit read rate (bytes per second) from a device
- `--device-read-iops`: Limit read rate (IO per second) from a device
- `--device-write-bps`: Limit write rate (bytes per second) to a device
- `--device-write-iops`: Limit write rate (IO per second) to a device
- `--dns`: Set custom DNS servers
- `--dns-option`: Set DNS options
- `--dns-search`: Set custom DNS search domains
- `--domainname`: Container NIS domain name
- `--entrypoint`: Overwrite the default ENTRYPOINT of the image
- `--env`, `-e`: Set environment variables
- `--env-file`: Read in a file of environment variables
- `--expose`: Expose a port or a range of ports
- `--gpus`: GPU devices to add to the container ('all' to pass all GPUs)
- `--group-add`: Add additional groups to join
- `--health-cmd`: Command to run to check health
- `--health-interval`: Time between running the check (ms|s|m|h) (default 0s)
- `--health-retries`: Consecutive failures needed to report unhealthy
- `--health-start-interval`: Time between running the check during the start period (ms|s|m|h) (default 0s)
- `--health-start-period`: Start period for the container to initialize before starting health-retries countdown (ms|s|m|h) (default 0s)
- `--health-timeout`: Maximum time to allow one check to run (ms|s|m|h) (default 0s)
- `--help`: Print usage
- `--hostname`, `-h`: Container host name
- `--init`: Run an init inside the container that forwards signals and reaps processes
- `--interactive`, `-i`: Keep STDIN open even if not attached
- `--io-maxbandwidth`: Maximum IO bandwidth limit for the system drive (Windows only)
- `--io-maxiops`: Maximum IOps limit for the system drive (Windows only)
- `--ip`: IPv4 address (e.g., 172.30.100.104)
- `--ip6`: IPv6 address (e.g., 2001:db8::33)
- `--ipc`: IPC mode to use
- `--isolation`: Container isolation technology
- `--label`, `-l`: Set meta data on a container
- `--label-file`: Read in a line delimited file of labels
- `--link`: Add link to another container
- `--link-local-ip`: Container IPv4/IPv6 link-local addresses
- `--log-driver`: Logging driver for the container
- `--log-opt`: Log driver options
- `--mac-address`: Container MAC address (e.g., 92:d0:c6:0a:29:33)
- `--memory`, `-m`: Memory limit
- `--memory-reservation`: Memory soft limit
- `--memory-swap`: Swap limit equal to memory plus swap: '-1' to enable unlimited swap
- `--memory-swappiness`: Tune container memory swappiness (0 to 100)
- `--mount`: Attach a filesystem mount to the container
- `--name`: Assign a name to the container
- `--network`: Connect a container to a network
- `--network-alias`: Add network-scoped alias for the container
- `--no-healthcheck`: Disable any container-specified HEALTHCHECK
- `--oom-kill-disable`: Disable OOM Killer
- `--oom-score-adj`: Tune host's OOM preferences (-1000 to 1000)
- `--pid`: PID namespace to use
- `--pids-limit`: Tune container pids limit (set -1 for unlimited)
- `--platform`: Set platform if server is multi-platform capable
- `--privileged`: Give extended privileges to this container
- `--publish`, `-p`: Publish a container's port(s) to the host
- `--publish-all`, `-P`: Publish all exposed ports to random ports
- `--pull`: Pull image before running (`always`, `missing`, `never`)
- `--quiet`, `-q`: Suppress the pull output
- `--read-only`: Mount the container's root filesystem as read only
- `--restart`: Restart policy to apply when a container exits
- `--rm`: Automatically remove the container and its associated anonymous volumes when it exits
- `--runtime`: Runtime to use for this container
- `--security-opt`: Security Options
- `--shm-size`: Size of /dev/shm
- `--sig-proxy`: Proxy received signals to the process
- `--stop-signal`: Signal to stop the container
- `--stop-timeout`: Timeout (in seconds) to stop a container
- `--storage-opt`: Storage driver options for the container
- `--sysctl`: Sysctl options
- `--tmpfs`: Mount a tmpfs directory
- `--tty`, `-t`: Allocate a pseudo-TTY
- `--ulimit`: Ulimit options
- `--umask`: Set umask for the container
- `--use-api-socket`: Bind mount Docker API socket and required auth
- `--user`, `-u`: Username or UID (format: <name|uid>[:<group|gid>])
- `--userns`: User namespace to use
- `--uts`: UTS namespace to use
- `--volume`, `-v`: Bind mount a volume
- `--volume-driver`: Optional volume driver for the container
- `--volumes-from`: Mount volumes from the specified container(s)
- `--workdir`, `-w`: Working directory inside the container

### Examples of docker container run

#### Assign name (--name)

The `--name` flag lets you specify a custom identifier for a container. The
following example runs a container named `test` using the `nginx:alpine` image
in detached mode.

```console
$ docker run --name test -d nginx:alpine
4bed76d3ad428b889c56c1ecc2bf2ed95cb08256db22dc5ef5863e1d03252a19
$ docker ps
CONTAINER ID   IMAGE          COMMAND                  CREATED        STATUS                  PORTS     NAMES
4bed76d3ad42   nginx:alpine   "/docker-entrypoint.…"   1 second ago   Up Less than a second   80/tcp    test
```

You can reference the container by name with other commands. For example, the
following commands stop and remove a container named `test`:

```console
$ docker stop test
test
$ docker rm test
test
```

If you don't specify a custom name using the `--name` flag, the daemon assigns
a randomly generated name, such as `vibrant_cannon`, to the container. Using a
custom-defined name provides the benefit of having an easy-to-remember ID for a
container.

Moreover, if you connect the container to a user-defined bridge network, other
containers on the same network can refer to the container by name via DNS.

```console
$ docker network create mynet
cb79f45948d87e389e12013fa4d969689ed2c3316985dd832a43aaec9a0fe394
$ docker run --name test --net mynet -d nginx:alpine
58df6ecfbc2ad7c42d088ed028d367f9e22a5f834d7c74c66c0ab0485626c32a
$ docker run --net mynet busybox:latest ping test
PING test (172.18.0.2): 56 data bytes
64 bytes from 172.18.0.2: seq=0 ttl=64 time=0.073 ms
64 bytes from 172.18.0.2: seq=1 ttl=64 time=0.411 ms
64 bytes from 172.18.0.2: seq=2 ttl=64 time=0.319 ms
64 bytes from 172.18.0.2: seq=3 ttl=64 time=0.383 ms
...
```

#### Set working directory (-w, --workdir)

```console
$ docker run -w /path/to/dir/ ubuntu pwd
```

The `-w` option runs the command executed inside the directory specified, in this example,
`/path/to/dir/`. If the path doesn't exist, Docker creates it inside the container.

#### Mount volume (-v)

```console
$ docker  run  -v $(pwd):$(pwd) -w $(pwd) -i -t  ubuntu pwd
```

The example above mounts the current directory into the container at the same path
using the `-v` flag, sets it as the working directory, and then runs the `pwd` command inside the container.

As of Docker Engine version 23, you can use relative paths on the host.

```console
$ docker  run  -v ./content:/content -w /content -i -t  ubuntu pwd
```

The example above mounts the `content` directory in the current directory into the container at the
`/content` path using the `-v` flag, sets it as the working directory, and then
runs the `pwd` command inside the container.

```console
$ docker run -v /doesnt/exist:/foo -w /foo -i -t ubuntu bash
```

When the host directory of a bind-mounted volume doesn't exist, Docker
automatically creates this directory on the host for you. In the
example above, Docker creates the `/doesnt/exist`
folder before starting your container.

#### Add bind mounts or volumes using the --mount flag

The `--mount` flag allows you to mount volumes, host-directories, and `tmpfs`
mounts in a container.

The `--mount` flag supports most options supported by the `-v` or the
`--volume` flag, but uses a different syntax. For in-depth information on the
`--mount` flag, and a comparison between `--volume` and `--mount`, refer to
Bind mounts.

Even though there is no plan to deprecate `--volume`, usage of `--mount` is recommended.

Examples:

```console
$ docker run --read-only --mount type=volume,target=/icanwrite busybox touch /icanwrite/here
```

```console
$ docker run -t -i --mount type=bind,src=/data,dst=/data busybox sh
```

#### Publish or expose port (-p, --expose)

```console
$ docker run -p 127.0.0.1:80:8080/tcp nginx:alpine
```

This binds port `8080` of the container to TCP port `80` on `127.0.0.1` of the
host. You can also specify `udp` and `sctp` ports. The [Networking overview
page](/network/) explains in detail how to publish ports
with Docker.

> [!NOTE]
> If you don't specify an IP address (i.e., `-p 80:80` instead of `-p
> 127.0.0.1:80:80`) when publishing a container's ports, Docker publishes the
> port on all interfaces (address `0.0.0.0`) by default. These ports are
> externally accessible. This also applies if you configured UFW to block this
> specific port, as Docker manages its own iptables rules. [Read
> more](/network/packet-filtering-firewalls/)

```console
$ docker run --expose 80 nginx:alpine
```

This exposes port `80` of the container without publishing the port to the host
system's interfaces.

#### Set environment variables (-e, --env, --env-file)

```console
$ docker run -e MYVAR1 --env MYVAR2=foo --env-file ./env.list ubuntu bash
```

Use the `-e`, `--env`, and `--env-file` flags to set simple (non-array)
environment variables in the container you're running, or overwrite variables
defined in the Dockerfile of the image you're running.

You can define the variable and its value when running the container:

```console
$ docker run --env VAR1=value1 --env VAR2=value2 ubuntu env | grep VAR
VAR1=value1
VAR2=value2
```

You can also use variables exported to your local environment:

```console
export VAR1=value1
export VAR2=value2

$ docker run --env VAR1 --env VAR2 ubuntu env | grep VAR
VAR1=value1
VAR2=value2
```

When running the command, the Docker CLI client checks the value the variable
has in your local environment and passes it to the container.
If no `=` is provided and that variable isn't exported in your local
environment, the variable is unset in the container.

You can also load the environment variables from a file. This file should use
the syntax `<variable>=value` (which sets the variable to the given value) or
`<variable>` (which takes the value from the local environment), and `#` for
comments. Lines beginning with `#` are treated as line comments and are
ignored, whereas a `#` appearing anywhere else in a line is treated as part of
the variable value.

```console
$ cat env.list
# This is a comment
VAR1=value1
VAR2=value2
USER

$ docker run --env-file env.list ubuntu env | grep -E 'VAR|USER'
VAR1=value1
VAR2=value2
USER=jonzeolla
```

#### Connect a container to a network (--network)

To start a container and connect it to a network, use the `--network` option.

If you want to add a running container to a network use the `docker network connect` subcommand.

You can connect multiple containers to the same network. Once connected, the
containers can communicate using only another container's IP address
or name. For `overlay` networks or custom plugins that support multi-host
connectivity, containers connected to the same multi-host network but launched
from different Engines can also communicate in this way.

> [!NOTE]
> The default bridge network only allows containers to communicate with each other using
> internal IP addresses. User-created bridge networks provide DNS resolution between
> containers using container names.

You can disconnect a container from a network using the `docker network
disconnect` command.

The following commands create a network named `my-net` and add a `busybox` container
to the `my-net` network.

```console
$ docker network create my-net
$ docker run -itd --network=my-net busybox
```

You can also choose the IP addresses for the container with `--ip` and `--ip6`
flags when you start the container on a user-defined network. To assign a
static IP to containers, you must specify subnet block for the network.

```console
$ docker network create --subnet 192.0.2.0/24 my-net
$ docker run -itd --network=my-net --ip=192.0.2.69 busybox
```

To connect the container to more than one network, repeat the `--network` option.

```console
$ docker network create --subnet 192.0.2.0/24 my-net1
$ docker network create --subnet 192.0.3.0/24 my-net2
$ docker run -itd --network=my-net1 --network=my-net2 busybox
```

To specify options when connecting to more than one network, use the extended syntax
for the `--network` flag. Comma-separated options that can be specified in the extended
`--network` syntax are:

| Option          | Top-level Equivalent                  | Description                                                                             |
|-----------------|---------------------------------------|-----------------------------------------------------------------------------------------|
| `name`          |                                       | The name of the network (mandatory)                                                     |
| `alias`         | `--network-alias`                     | Add network-scoped alias for the container                                              |
| `ip`            | `--ip`                                | IPv4 address (e.g., 172.30.100.104)                                                     |
| `ip6`           | `--ip6`                               | IPv6 address (e.g., 2001:db8::33)                                                       |
| `mac-address`   | `--mac-address`                       | Container MAC address (e.g., 92:d0:c6:0a:29:33)                                         |
| `link-local-ip` | `--link-local-ip`                     | Container IPv4/IPv6 link-local addresses                                                |
| `driver-opt`    | `docker network connect --driver-opt` | Network driver options                                                                  |
| `gw-priority`   |                                       | Highest gw-priority provides the default gateway. Accepts positive and negative values. |

```console
$ docker network create --subnet 192.0.2.0/24 my-net1
$ docker network create --subnet 192.0.3.0/24 my-net2
$ docker run -itd --network=name=my-net1,ip=192.0.2.42 --network=name=my-net2,ip=192.0.3.42 busybox
```

`sysctl` settings that start with `net.ipv4.`, `net.ipv6.` or `net.mpls.` can be
set per-interface using `driver-opt` label `com.docker.network.endpoint.sysctls`.
The interface name must be the string `IFNAME`.

To set more than one `sysctl` for an interface, quote the whole `driver-opt` field,
remembering to escape the quotes for the shell if necessary. For example, if the
interface to `my-net` is given name `eth0`, the following example sets sysctls
`net.ipv4.conf.eth0.log_martians=1` and `net.ipv4.conf.eth0.forwarding=0`, and
assigns the IPv4 address `192.0.2.42`.

```console
$ docker network create --subnet 192.0.2.0/24 my-net
$ docker run -itd --network=name=my-net,\"driver-opt=com.docker.network.endpoint.sysctls=net.ipv4.conf.IFNAME.log_martians=1,net.ipv4.conf.IFNAME.forwarding=0\",ip=192.0.2.42 busybox
```

> [!NOTE]
> Network drivers may restrict the sysctl settings that can be modified and, to protect
> the operation of the network, new restrictions may be added in the future.

For more information on connecting a container to a network when using the `run` command,
see the Docker network overview.

#### Keep STDIN open (-i, --interactive)

The `--interactive` (or `-i`) flag keeps the container's `STDIN` open, and lets
you send input to the container through standard input.

```console
$ echo hello | docker run --rm -i busybox cat
hello
```

The `-i` flag is most often used together with the `--tty` flag to bind the I/O
streams of the container to a pseudo terminal, creating an interactive terminal
session for the container. See Allocate a pseudo-TTY for more examples.

```console
$ docker run -it debian
root@10a3e71492b0:/# factor 90
90: 2 3 3 5
root@10a3e71492b0:/# exit
exit
```

Using the `-i` flag on its own allows for composition, such as piping input to
containers:

```console
$ docker run --rm -i busybox echo "foo bar baz" \
  | docker run --rm -i busybox awk '{ print $2 }' \
  | docker run --rm -i busybox rev
rab
```

## docker container ls

List containers

Aliases: docker container ls, docker container list, docker container ps, docker ps

Usage:

```console
docker container ls [OPTIONS]
```

### Description of docker container ls

List containers

### Options of docker container ls

- `--all`, `-a`: Show all containers (default shows just running)
- `--filter`, `-f`: Filter output based on conditions provided
- `--format`: Format output using a custom template: 'table': Print output in table format with column headers (default) 'table TEMPLATE': Print output in table format using the given Go template 'json': Print in JSON format 'TEMPLATE': Print output using the given Go template. Refer to https://docs.docker.com/go/formatting/ for more information about formatting output with templates
- `--last`, `-n`: Show n last created containers (includes all states)
- `--latest`, `-l`: Show the latest created container (includes all states)
- `--no-trunc`: Don't truncate output
- `--quiet`, `-q`: Only display container IDs
- `--size`, `-s`: Display total file sizes

### Examples of docker container ls

#### Do not truncate output (--no-trunc)

Running `docker ps --no-trunc` showing 2 linked containers.

```console
$ docker ps --no-trunc

CONTAINER ID                                                     IMAGE                        COMMAND                CREATED              STATUS              PORTS               NAMES
ca5534a51dd04bbcebe9b23ba05f389466cf0c190f1f8f182d7eea92a9671d00 ubuntu:24.04                 bash                   17 seconds ago       Up 16 seconds       3300-3310/tcp       webapp
9ca9747b233100676a48cc7806131586213fa5dab86dd1972d6a8732e3a84a4d crosbymichael/redis:latest   /redis-server --dir    33 minutes ago       Up 33 minutes       6379/tcp            redis,webapp/db
```

#### Show both running and stopped containers (-a, --all)

The `docker ps` command only shows running containers by default. To see all
containers, use the `--all` (or `-a`) flag:

```console
$ docker ps -a
```

`docker ps` groups exposed ports into a single range if possible. E.g., a
container that exposes TCP ports `100, 101, 102` displays `100-102/tcp` in
the `PORTS` column.

#### Show disk usage by container (--size)

The `docker ps --size` (or `-s`) command displays two different on-disk-sizes for each container:

```console
$ docker ps --size

CONTAINER ID   IMAGE          COMMAND                  CREATED        STATUS       PORTS   NAMES        SIZE
e90b8831a4b8   nginx          "/bin/bash -c 'mkdir "   11 weeks ago   Up 4 hours           my_nginx     35.58 kB (virtual 109.2 MB)
00c6131c5e30   telegraf:1.5   "/entrypoint.sh"         11 weeks ago   Up 11 weeks          my_telegraf  0 B (virtual 209.5 MB)
```
  * The "size" information shows the amount of data (on disk) that is used for the _writable_ layer of each container
  * The "virtual size" is the total amount of disk-space used for the read-only _image_ data used by the container and the writable layer.

For more information, refer to the container size on disk section.

#### Filtering (--filter)

The `--filter` (or `-f`) flag format is a `key=value` pair. If there is more
than one filter, then pass multiple flags (e.g. `--filter "foo=bar" --filter "bif=baz"`).

The currently supported filters are:

| Filter                | Description                                                                                                                          |
|:----------------------|:-------------------------------------------------------------------------------------------------------------------------------------|
| `id`                  | Container's ID                                                                                                                       |
| `name`                | Container's name                                                                                                                     |
| `label`               | An arbitrary string representing either a key or a key-value pair. Expressed as `<key>` or `<key>=<value>`                           |
| `exited`              | An integer representing the container's exit code. Only useful with `--all`.                                                         |
| `status`              | One of `created`, `restarting`, `running`, `removing`, `paused`, `exited`, or `dead`                                                 |
| `ancestor`            | Filters containers which share a given image as an ancestor. Expressed as `<image-name>[:<tag>]`,  `<image id>`, or `<image@digest>` |
| `before` or `since`   | Filters containers created before or after a given container ID or name                                                              |
| `volume`              | Filters running containers which have mounted a given volume or bind mount.                                                          |
| `network`             | Filters running containers connected to a given network.                                                                             |
| `publish` or `expose` | Filters containers which publish or expose a given port. Expressed as `<port>[/<proto>]` or `<startport-endport>/[<proto>]`          |
| `health`              | Filters containers based on their healthcheck status. One of `starting`, `healthy`, `unhealthy` or `none`.                           |
| `isolation`           | Windows daemon only. One of `default`, `process`, or `hyperv`.                                                                       |
| `is-task`             | Filters containers that are a "task" for a service. Boolean option (`true` or `false`)                                               |

## docker container exec

Execute a command in a running container

Aliases: docker container exec, docker exec

Usage:

```console
docker container exec [OPTIONS] CONTAINER COMMAND [ARG...]
```

### Description of docker container exec

The `docker exec` command runs a new command in a running container.

The command you specify with `docker exec` only runs while the container's
primary process (`PID 1`) is running, and it isn't restarted if the container
is restarted.

The command runs in the default working directory of the container.

The command must be an executable. A chained or a quoted command doesn't work.

- This works: `docker exec -it my_container sh -c "echo a && echo b"`
- This doesn't work: `docker exec -it my_container "echo a && echo b"`

### Options of docker container exec

- `--detach`, `-d`: Detached mode: run command in the background
- `--detach-keys`: Override the key sequence for detaching a container
- `--env`, `-e`: Set environment variables
- `--env-file`: Read in a file of environment variables
- `--interactive`, `-i`: Keep STDIN open even if not attached
- `--privileged`: Give extended privileges to the command
- `--tty`, `-t`: Allocate a pseudo-TTY
- `--user`, `-u`: Username or UID (format: `<name|uid>[:<group|gid>]`)
- `--workdir`, `-w`: Working directory inside the container

### Examples of docker container exec

#### Run `docker exec` on a running container

First, start a container.

```console
$ docker run --name mycontainer -d -i -t alpine /bin/sh
```

This creates and starts a container named `mycontainer` from an `alpine` image
with an `sh` shell as its main process. The `-d` option (shorthand for `--detach`)
sets the container to run in the background, in detached mode, with a pseudo-TTY
attached (`-t`). The `-i` option is set to keep `STDIN` attached (`-i`), which
prevents the `sh` process from exiting immediately.

Next, execute a command on the container.

```console
$ docker exec -d mycontainer touch /tmp/execWorks
```

This creates a new file `/tmp/execWorks` inside the running container
`mycontainer`, in the background.

Next, execute an interactive `sh` shell on the container.

```console
$ docker exec -it mycontainer sh
```

This starts a new shell session in the container `mycontainer`.

#### Set environment variables for the exec process (--env, -e)

Next, set environment variables in the current bash session.

The `docker exec` command inherits the environment variables that are set at the
time the container is created. Use the `--env` (or the `-e` shorthand) to
override global environment variables, or to set additional environment
variables for the process started by `docker exec`.

The following example creates a new shell session in the container `mycontainer`,
with environment variables `$VAR_A` set to `1`, and `$VAR_B` set to `2`.
These environment variables are only valid for the `sh` process started by that
`docker exec` command, and aren't available to other processes running inside
the container.

```console
$ docker exec -e VAR_A=1 -e VAR_B=2 mycontainer env
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
HOSTNAME=f64a4851eb71
VAR_A=1
VAR_B=2
HOME=/root
```

#### Escalate container privileges (--privileged)

See `docker run --privileged`.

#### Set the working directory for the exec process (--workdir, -w)

By default `docker exec` command runs in the same working directory set when
the container was created.

```console
$ docker exec -it mycontainer pwd
/
```

You can specify an alternative working directory for the command to execute
using the `--workdir` option (or the `-w` shorthand):

```console
$ docker exec -it -w /root mycontainer pwd
/root
```

#### Try to run `docker exec` on a paused container

If the container is paused, then the `docker exec` command fails with an error:

```console
$ docker pause mycontainer
mycontainer

$ docker ps

CONTAINER ID   IMAGE     COMMAND     CREATED          STATUS                   PORTS     NAMES
482efdf39fac   alpine    "/bin/sh"   17 seconds ago   Up 16 seconds (Paused)             mycontainer

$ docker exec mycontainer sh

Error response from daemon: Container mycontainer is paused, unpause the container before exec

$ echo $?
1
```

## docker container logs

Fetch the logs of a container

Aliases: docker container logs, docker logs

Usage:

```console
docker container logs [OPTIONS] CONTAINER
```

### Description of docker container logs

The `docker logs` command batch-retrieves logs present at the time of execution.

For more information about selecting and configuring logging drivers, refer to
Configure logging drivers.

### Options of docker container logs

- `--details`: Show extra details provided to logs
- `--follow`, `-f`: Follow log output
- `--since`: Show logs since timestamp (e.g. `2013-01-02T13:23:37Z`) or relative (e.g. `42m` for 42 minutes)
- `--tail`, `-n`: Number of lines to show from the end of the logs
- `--timestamps`, `-t`: Show timestamps
- `--until`: Show logs before a timestamp (e.g. `2013-01-02T13:23:37Z`) or relative (e.g. `42m` for 42 minutes)

### Examples of docker container logs

#### Stream log output  (-f, --follow)

The `docker logs --follow` command will continue streaming the new output from
the container's `STDOUT` and `STDERR`.

#### Retrieve the last logs (-n, --tail)

Passing a negative number or a non-integer to `--tail` is invalid and the
value is set to `all` in that case.

#### Retrieve logs with timestamps (-t, --timestamps)

The `docker logs --timestamps` command will add an RFC3339Nano timestamp
, for example `2014-09-16T06:17:46.000000000Z`, to each
log entry. To ensure that the timestamps are aligned the
nano-second part of the timestamp will be padded with zero when necessary.

#### Retrieve logs with additional attributes (--details)

The `docker logs --details` command will add on extra attributes, such as
environment variables and labels, provided to `--log-opt` when creating the
container.

#### Retrieve logs generated since a specific point in time (--since)

The `--since` option shows only the container logs generated after
a given date. You can specify the date as an RFC 3339 date, a UNIX
timestamp, or a Go duration string (e.g. `1m30s`, `3h`). Besides RFC3339 date
format you may also use RFC3339Nano, `2006-01-02T15:04:05`,
`2006-01-02T15:04:05.999999999`, `2006-01-02T07:00`, and `2006-01-02`. The local
timezone on the client will be used if you do not provide either a `Z` or a
`+-00:00` timezone offset at the end of the timestamp. When providing Unix
timestamps enter seconds[.nanoseconds], where seconds is the number of seconds
that have elapsed since January 1, 1970 (midnight UTC/GMT), not counting leap
seconds (aka Unix epoch or Unix time), and the optional .nanoseconds field is a
fraction of a second no more than nine digits long. You can combine the
`--since` option with either or both of the `--follow` or `--tail` options.

#### Retrieve logs until a specific point in time (--until)

In order to retrieve logs before a specific point in time, run:

```console
$ docker run --name test -d busybox sh -c "while true; do $(echo date); sleep 1; done"
$ date
Tue 14 Nov 2017 16:40:00 CET
$ docker logs -f --until=2s test
Tue 14 Nov 2017 16:40:00 CET
Tue 14 Nov 2017 16:40:01 CET
Tue 14 Nov 2017 16:40:02 CET
```

## docker container stop

Stop one or more running containers

Aliases: docker container stop, docker stop

Usage:

```console
docker container stop [OPTIONS] CONTAINER [CONTAINER...]
```

### Description of docker container stop

The main process inside the container will receive `SIGTERM`, and after a grace
period, `SIGKILL`. The first signal can be changed with the `STOPSIGNAL`
instruction in the container's Dockerfile, or the `--stop-signal` option to
`docker run` and `docker create`.

### Options of docker container stop

- `--signal`, `-s`: Signal to send to the container
- `--timeout`, `-t`: Seconds to wait before killing the container

### Examples of docker container stop

```console
$ docker stop my_container
```

#### Stop container with signal (-s, --signal)

The `--signal` flag sends the system call signal to the container to exit.
This signal can be a signal name in the format `SIG<NAME>`, for instance
`SIGKILL`, or an unsigned number that matches a position in the kernel's
syscall table, for instance `9`. Refer to signal(7)
for available signals.

The default signal to use is defined by the image's `StopSignal`,
which can be set through the `STOPSIGNAL`
Dockerfile instruction when building the image, or configured using the
`--stop-signal`
option when creating the container. If no signal is configured for the
container, `SIGTERM` is used as default.

#### Stop container with timeout (-t, --timeout)

The `--timeout` flag sets the number of seconds to wait for the container
to stop after sending the pre-defined (see [`--signal`]{#signal)) system call signal.
If the container does not exit after the timeout elapses, it's forcibly killed
with a `SIGKILL` signal.

If you set `--timeout` to `-1`, no timeout is applied, and the daemon
waits indefinitely for the container to exit.

The default timeout can be specified using the `--stop-timeout`
option when creating the container. If no default is configured for the container,
the Daemon determines the default, and is 10 seconds for Linux containers, and
30 seconds for Windows containers.

## docker container rm

Remove one or more containers

Aliases: docker container rm, docker container remove, docker rm

Usage:

```console
docker container rm [OPTIONS] CONTAINER [CONTAINER...]
```

### Description of docker container rm

Remove one or more containers

### Options of docker container rm

- `--force`, `-f`: Force the removal of a running container (uses SIGKILL)
- `--link`, `-l`: Remove the specified link
- `--volumes`, `-v`: Remove anonymous volumes associated with the container

### Examples of docker container rm

#### Remove a container

This removes the container referenced under the link `/redis`.

```console
$ docker rm /redis

/redis
```

#### Remove a link specified with `--link` on the default bridge network (--link)

This removes the underlying link between `/webapp` and the `/redis`
containers on the default bridge network, removing all network communication
between the two containers. This does not apply when `--link` is used with
user-specified networks.

```console
$ docker rm --link /webapp/redis

/webapp/redis
```

#### Force-remove a running container (--force)

This command force-removes a running container.

```console
$ docker rm --force redis

redis
```

The main process inside the container referenced under the link `redis` will receive
`SIGKILL`, then the container will be removed.

#### Remove all stopped containers

Use the `docker container prune` command to remove all
stopped containers, or refer to the `docker system prune`
command to remove unused containers in addition to other Docker resources, such
as (unused) images and networks.

Alternatively, you can use the `docker ps` with the `-q` / `--quiet` option to
generate a list of container IDs to remove, and use that list as argument for
the `docker rm` command.

Combining commands can be more flexible, but is less portable as it depends
on features provided by the shell, and the exact syntax may differ depending on
what shell is used. To use this approach on Windows, consider using PowerShell
or Bash.

The example below uses `docker ps -q` to print the IDs of all containers that
have exited (`--filter status=exited`), and removes those containers with
the `docker rm` command:

```console
$ docker rm $(docker ps --filter status=exited -q)
```

Or, using the `xargs` Linux utility:

```console
$ docker ps --filter status=exited -q | xargs docker rm
```

#### Remove a container and its volumes (-v, --volumes)

```console
$ docker rm --volumes redis
redis
```

This command removes the container and any volumes associated with it.
Note that if a volume was specified with a name, it will not be removed.

#### Remove a container and selectively remove volumes

```console
$ docker create -v awesome:/foo -v /bar --name hello redis
hello

$ docker rm -v hello
```

In this example, the volume for `/foo` remains intact, but the volume for
`/bar` is removed. The same behavior holds for volumes inherited with
`--volumes-from`.

## docker buildx build

Start a build

Aliases: docker build, docker builder build, docker image build, docker buildx b

Usage:

```console
docker buildx build [OPTIONS] PATH | URL | -
```

### Description of docker buildx build

The `docker buildx build` command starts a build using BuildKit.

### Options of docker buildx build

- `--add-host`: Add a custom host-to-IP mapping (format: `host:ip`)
- `--allow`: Allow extra privileged entitlement (e.g., `network.host`, `security.insecure`, `device`, `buildx.local.delete`)
- `--annotation`: Add annotation to the image
- `--attest`: Attestation parameters (format: `type=sbom,generator=image`)
- `--build-arg`: Set build-time variables
- `--build-context`: Additional build contexts (e.g., name=path)
- `--cache-from`: External cache sources (e.g., `user/app:cache`, `type=local,src=path/to/dir`)
- `--cache-to`: Cache export destinations (e.g., `user/app:cache`, `type=local,dest=path/to/dir`)
- `--call`: Set method for evaluating build (`check`, `outline`, `targets`)
- `--cgroup-parent`: Set the parent cgroup for the `RUN` instructions during build
- `--check`: Shorthand for `--call=check`
- `--file`, `-f`: Name of the Dockerfile (default: `PATH/Dockerfile`)
- `--iidfile`: Write the image ID to a file
- `--label`: Set metadata for an image
- `--load`: Shorthand for `--output=type=docker`
- `--metadata-file`: Write build result metadata to a file
- `--network`: Set the networking mode for the `RUN` instructions during build
- `--no-cache`: Do not use cache when building the image
- `--no-cache-filter`: Do not cache specified stages
- `--output`, `-o`: Output destination (format: `type=local,dest=path`)
- `--platform`: Set target platform for build
- `--policy`: Policy configuration (format: `filename=path,filename=path,disabled=true|false[,log-level=level]`)
- `--progress`: Set type of progress output (`auto`, `none`, `plain`, `quiet`, `rawjson`, `tty`). Use plain to show container output
- `--provenance`: Shorthand for `--attest=type=provenance`
- `--pull`: Always attempt to pull all referenced images
- `--push`: Shorthand for `--output=type=registry,unpack=false`
- `--quiet`, `-q`: Suppress the build output and print image ID on success
- `--resource`: Resource limits for build containers (format: `memory=2g`, `cpu-quota=50000`)
- `--sbom`: Shorthand for `--attest=type=sbom`
- `--secret`: Secret to expose to the build (format: `id=mysecret[,src=/local/secret]`)
- `--shm-size`: Shared memory size for build containers
- `--ssh`: SSH agent socket or keys to expose to the build (format: `default|<id>[=<socket>|<key>[,<key>]]`)
- `--tag`, `-t`: Image identifier (format: `[registry/]repository[:tag]`)
- `--target`: Set the target build stage to build
- `--ulimit`: Ulimit options

### Examples of docker buildx build

#### Create attestations (--attest)

```text
--attest=type=sbom,...
--attest=type=provenance,...
```

Create image attestations.
BuildKit currently supports:

- `sbom` - Software Bill of Materials.

  Use `--attest=type=sbom` to generate an SBOM for an image at build-time.
  Alternatively, you can use the `--sbom` shorthand.

  For more information, see here.

- `provenance` - SLSA Provenance

  Use `--attest=type=provenance` to generate provenance for an image at
  build-time. Alternatively, you can use the `--provenance` shorthand.

  By default, a minimal provenance attestation will be created for the build
  result, which will only be attached for images pushed to registries.

  For more information, see here.

#### Set build-time variables (--build-arg)

You can use `ENV` instructions in a Dockerfile to define variable values. These
values persist in the built image. Often persistence isn't what you want. Users
want to specify variables differently depending on which host they build an
image on.

A good example is `http_proxy` or source versions for pulling intermediate
files. The `ARG` instruction lets Dockerfile authors define values that users
can set at build-time using the  `--build-arg` flag:

```console
$ docker buildx build --build-arg HTTP_PROXY=http://10.20.30.2:1234 --build-arg FTP_PROXY=http://40.50.60.5:4567 .
```

This flag allows you to pass the build-time variables that are
accessed like regular environment variables in the `RUN` instruction of the
Dockerfile. These values don't persist in the intermediate or final images
like `ENV` values do. You must add `--build-arg` for each build argument.

Using this flag doesn't alter the output you see when the build process echoes the`ARG` lines from the
Dockerfile.

For detailed information on using `ARG` and `ENV` instructions, see the
Dockerfile reference.

You can also use the `--build-arg` flag without a value, in which case the daemon
propagates the value from the local environment into the Docker container it's building:

```console
$ export HTTP_PROXY=http://10.20.30.2:1234
$ docker buildx build --build-arg HTTP_PROXY .
```

This example is similar to how `docker run -e` works. Refer to the `docker run` documentation
for more information.

There are also useful built-in build arguments, such as:

* `BUILDKIT_CONTEXT_KEEP_GIT_DIR=<bool>`: trigger git context to keep the `.git` directory
* `BUILDKIT_INLINE_CACHE=<bool>`: inline cache metadata to image config or not
* `BUILDKIT_MULTI_PLATFORM=<bool>`: opt into deterministic output regardless of multi-platform output or not

```console
$ docker buildx build --build-arg BUILDKIT_MULTI_PLATFORM=1 .
```

Learn more about the built-in build arguments in the Dockerfile reference docs.

#### Specify a Dockerfile (-f, --file)

```console
$ docker buildx build -f [PATH|URL|-] .
```

Specifies the location of the Dockerfile to use.
If unspecified, a file named `Dockerfile` at the root of the build context is used by default.

The supported inputs formats are:

- `Local file path`
- `Remote URL`
- `Standard input`

#### Set the networking mode for the RUN instructions during build (--network)

Available options for the networking mode are:

- `default` (default): Run in the default network.
- `none`: Run with no network access.
- `host`: Run in the host’s network environment.

Find more details in the Dockerfile reference.

#### Tag an image (-t, --tag)

```console
$ docker buildx build -t docker/apache:2.0 .
```

This examples builds in the same way as the previous example, but it then tags the resulting
image. The repository name will be `docker/apache` and the tag `2.0`.

Read more about valid tags.

You can apply multiple tags to an image. For example, you can apply the `latest`
tag to a newly built image and add another tag that references a specific
version.

For example, to tag an image both as `docker/fedora-jboss:latest` and
`docker/fedora-jboss:v2.1`, use the following:

```console
$ docker buildx build -t docker/fedora-jboss:latest -t docker/fedora-jboss:v2.1 .
```

#### Specifying target build stage (--target)

When building a Dockerfile with multiple build stages, use the `--target`
option to specify an intermediate build stage by name as a final stage for the
resulting image. The builder skips commands after the target stage.

```dockerfile
FROM debian AS build-env
# ...

FROM alpine AS production-env
# ...
```

```console
$ docker buildx build -t mybuildimage --target build-env .
```

## docker image ls

List images

Aliases: docker image ls, docker image list, docker images

Usage:

```console
docker image ls [OPTIONS] [REPOSITORY[:TAG]]
```

### Description of docker image ls

The default `docker images` will show all top level
images, their repository and tags, and their size.

Docker images have intermediate layers that increase reusability,
decrease disk usage, and speed up `docker build` by
allowing each step to be cached. These intermediate layers are not shown
by default.

Untagged (dangling) images are also hidden by default. Use the `-a` (`--all`)
flag to show intermediate layers and dangling images.

The `SIZE` is the cumulative space taken up by the image and all
its parent images. This is also the disk space used by the contents of the
Tar file created when you `docker save` an image.

An image will be listed more than once if it has multiple repository names
or tags. This single image (identifiable by its matching `IMAGE ID`)
uses up the `SIZE` listed only once.

### Options of docker image ls

- `--all`, `-a`: Show all images (default hides intermediate and dangling images)
- `--digests`: Show digests
- `--filter`, `-f`: Filter output based on conditions provided
- `--format`: Format output using a custom template: 'table': Print output in table format with column headers (default) 'table TEMPLATE': Print output in table format using the given Go template 'json': Print in JSON format 'TEMPLATE': Print output using the given Go template. Refer to https://docs.docker.com/go/formatting/ for more information about formatting output with templates
- `--no-trunc`: Don't truncate output
- `--quiet`, `-q`: Only show image IDs
- `--tree`: List multi-platform images as a tree (EXPERIMENTAL)

### Examples of docker image ls

#### List the most recently created images

```console
$ docker images

REPOSITORY                TAG                 IMAGE ID            CREATED             SIZE
<none>                    <none>              77af4d6b9913        19 hours ago        1.089 GB
committ                   latest              b6fa739cedf5        19 hours ago        1.089 GB
<none>                    <none>              78a85c484f71        19 hours ago        1.089 GB
docker                    latest              30557a29d5ab        20 hours ago        1.089 GB
<none>                    <none>              5ed6274db6ce        24 hours ago        1.089 GB
postgres                  9                   746b819f315e        4 days ago          213.4 MB
postgres                  9.3                 746b819f315e        4 days ago          213.4 MB
postgres                  9.3.5               746b819f315e        4 days ago          213.4 MB
postgres                  latest              746b819f315e        4 days ago          213.4 MB
```

#### List images by name and tag

The `docker images` command takes an optional `[REPOSITORY[:TAG]]` argument
that restricts the list to images that match the argument. If you specify
`REPOSITORY`but no `TAG`, the `docker images` command lists all images in the
given repository.

For example, to list all images in the `java` repository, run the following command:

```console
$ docker images java

REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
java                8                   308e519aac60        6 days ago          824.5 MB
java                7                   493d82594c15        3 months ago        656.3 MB
java                latest              2711b1d6f3aa        5 months ago        603.9 MB
```

The `[REPOSITORY[:TAG]]` value must be an exact match. This means that, for example,
`docker images jav` does not match the image `java`.

If both `REPOSITORY` and `TAG` are provided, only images matching that
repository and tag are listed.  To find all local images in the `java`
repository with tag `8` you can use:

```console
$ docker images java:8

REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
java                8                   308e519aac60        6 days ago          824.5 MB
```

If nothing matches `REPOSITORY[:TAG]`, the list is empty.

```console
$ docker images java:0

REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
```

#### List the full length image IDs (--no-trunc)

```console
$ docker images --no-trunc

REPOSITORY                    TAG                 IMAGE ID                                                                  CREATED             SIZE
<none>                        <none>              sha256:77af4d6b9913e693e8d0b4b294fa62ade6054e6b2f1ffb617ac955dd63fb0182   19 hours ago        1.089 GB
committest                    latest              sha256:b6fa739cedf5ea12a620a439402b6004d057da800f91c7524b5086a5e4749c9f   19 hours ago        1.089 GB
<none>                        <none>              sha256:78a85c484f71509adeaace20e72e941f6bdd2b25b4c75da8693efd9f61a37921   19 hours ago        1.089 GB
docker                        latest              sha256:30557a29d5abc51e5f1d5b472e79b7e296f595abcf19fe6b9199dbbc809c6ff4   20 hours ago        1.089 GB
<none>                        <none>              sha256:0124422dd9f9cf7ef15c0617cda3931ee68346455441d66ab8bdc5b05e9fdce5   20 hours ago        1.089 GB
<none>                        <none>              sha256:18ad6fad340262ac2a636efd98a6d1f0ea775ae3d45240d3418466495a19a81b   22 hours ago        1.082 GB
<none>                        <none>              sha256:f9f1e26352f0a3ba6a0ff68167559f64f3e21ff7ada60366e2d44a04befd1d3a   23 hours ago        1.089 GB
tryout                        latest              sha256:2629d1fa0b81b222fca63371ca16cbf6a0772d07759ff80e8d1369b926940074   23 hours ago        131.5 MB
<none>                        <none>              sha256:5ed6274db6ceb2397844896966ea239290555e74ef307030ebb01ff91b1914df   24 hours ago        1.089 GB
```

#### Filtering (--filter)

The filtering flag (`-f` or `--filter`) format is of "key=value". If there is more
than one filter, then pass multiple flags (e.g., `--filter "foo=bar" --filter "bif=baz"`).

The currently supported filters are:

* dangling (boolean - true or false)
* label (`label=<key>` or `label=<key>=<value>`)
* before (`<image-name>[:<tag>]`,  `<image id>` or `<image@digest>`) - filter images created before given id or references
* since (`<image-name>[:<tag>]`,  `<image id>` or `<image@digest>`) - filter images created since given id or references
* reference (pattern of an image reference) - filter images whose reference matches the specified pattern

## docker image pull

Download an image from a registry

Aliases: docker image pull, docker pull

Usage:

```console
docker image pull [OPTIONS] NAME[:TAG|@DIGEST]
```

### Description of docker image pull

Most of your images will be created on top of a base image from the
Docker Hub registry.

Docker Hub contains many pre-built images that you
can `pull` and try without needing to define and configure your own.

To download a particular image, or set of images (i.e., a repository),
use `docker pull`.

### Proxy configuration

If you are behind an HTTP proxy server, for example in corporate settings,
you may have to configure the Docker daemon to use the proxy server for
operations such as pulling and pushing images. Refer to the
dockerd command-line reference for details.

### Concurrent downloads

By default the Docker daemon downloads three layers of an image at a time.
If you are on a low bandwidth connection this may cause timeout issues and you may want to lower
this via the `--max-concurrent-downloads` daemon option. See the
daemon documentation for more details.

### Options of docker image pull

- `--all-tags`, `-a`: Download all tagged images in the repository
- `--platform`: Set platform if server is multi-platform capable
- `--quiet`, `-q`: Suppress verbose output

### Examples of docker image pull

#### Pull an image from Docker Hub

To download a particular image, or set of images (i.e., a repository), use
`docker image pull` (or the `docker pull` shorthand). If no tag is provided,
Docker Engine uses the `:latest` tag as a default. This example pulls the
`debian:latest` image:

```console
$ docker image pull debian

Using default tag: latest
latest: Pulling from library/debian
e756f3fdd6a3: Pull complete
Digest: sha256:3f1d6c17773a45c97bd8f158d665c9709d7b29ed7917ac934086ad96f92e4510
Status: Downloaded newer image for debian:latest
docker.io/library/debian:latest
```

Docker images can consist of multiple layers. In the example above, the image
consists of a single layer; `e756f3fdd6a3`.

Layers can be reused by images. For example, the `debian:bookworm` image shares
its layer with the `debian:latest`. Pulling the `debian:bookworm` image therefore
only pulls its metadata, but not its layers, because the layer is already present
locally:

```console
$ docker image pull debian:bookworm

bookworm: Pulling from library/debian
Digest: sha256:3f1d6c17773a45c97bd8f158d665c9709d7b29ed7917ac934086ad96f92e4510
Status: Downloaded newer image for debian:bookworm
docker.io/library/debian:bookworm
```

To see which images are present locally, use the `docker images`
command:

```console
$ docker images

REPOSITORY   TAG        IMAGE ID       CREATED        SIZE
debian       bookworm   4eacea30377a   8 days ago     124MB
debian       latest     4eacea30377a   8 days ago     124MB
```

Docker uses a content-addressable image store, and the image ID is a SHA256
digest covering the image's configuration and layers. In the example above,
`debian:bookworm` and `debian:latest` have the same image ID because they are
the same image tagged with different names. Because they are the same image,
their layers are stored only once and do not consume extra disk space.

For more information about images, layers, and the content-addressable store,
refer to understand images, containers, and storage drivers.

#### Pull from a different registry

By default, `docker pull` pulls images from Docker Hub. It is also possible to
manually specify the path of a registry to pull from. For example, if you have
set up a local registry, you can specify its path to pull from it. A registry
path is similar to a URL, but does not contain a protocol specifier (`https://`).

The following command pulls the `testing/test-image` image from a local registry
listening on port 5000 (`myregistry.local:5000`):

```console
$ docker image pull myregistry.local:5000/testing/test-image
```

Registry credentials are managed by docker login.

Docker uses the `https://` protocol to communicate with a registry, unless the
registry is allowed to be accessed over an insecure connection. Refer to the
insecure registries section for more information.

#### Pull a repository with multiple images (-a, --all-tags)

By default, `docker pull` pulls a single image from the registry. A repository
can contain multiple images. To pull all images from a repository, provide the
`-a` (or `--all-tags`) option when using `docker pull`.

This command pulls all images from the `ubuntu` repository:

```console
$ docker image pull --all-tags ubuntu

Pulling repository ubuntu
ad57ef8d78d7: Download complete
105182bb5e8b: Download complete
511136ea3c5a: Download complete
73bd853d2ea5: Download complete
....

Status: Downloaded newer image for ubuntu
```

After the pull has completed use the `docker image ls` command (or the `docker images`
shorthand) to see the images that were pulled. The example below shows all the
`ubuntu` images that are present locally:

```console
$ docker image ls --filter reference=ubuntu
REPOSITORY   TAG       IMAGE ID       CREATED        SIZE
ubuntu       22.04     8a3cdc4d1ad3   3 weeks ago    77.9MB
ubuntu       jammy     8a3cdc4d1ad3   3 weeks ago    77.9MB
ubuntu       24.04     35a88802559d   6 weeks ago    78.1MB
ubuntu       latest    35a88802559d   6 weeks ago    78.1MB
ubuntu       noble     35a88802559d   6 weeks ago    78.1MB
```

#### Cancel a pull

Killing the `docker pull` process, for example by pressing `CTRL-c` while it is
running in a terminal, will terminate the pull operation.

```console
$ docker pull ubuntu

Using default tag: latest
latest: Pulling from library/ubuntu
a3ed95caeb02: Pulling fs layer
236608c7b546: Pulling fs layer
^C
```

The Engine terminates a pull operation when the connection between the daemon
and the client (initiating the pull) is cut or lost for any reason or the
command is manually terminated.

## docker volume create

Create a volume

Usage:

```console
docker volume create [OPTIONS] [VOLUME]
```

### Description of docker volume create

Creates a new volume that containers can consume and store data in. If a name is
not specified, Docker generates a random name.

### Options of docker volume create

- `--availability`: Cluster Volume availability (`active`, `pause`, `drain`)
- `--driver`, `-d`: Specify volume driver name
- `--group`: Cluster Volume group (cluster volumes)
- `--label`: Set metadata for a volume
- `--limit-bytes`: Minimum size of the Cluster Volume in bytes
- `--opt`, `-o`: Set driver specific options
- `--required-bytes`: Maximum size of the Cluster Volume in bytes
- `--scope`: Cluster Volume access scope (`single`, `multi`)
- `--secret`: Cluster Volume secrets
- `--sharing`: Cluster Volume access sharing (`none`, `readonly`, `onewriter`, `all`)
- `--topology-preferred`: A topology that the Cluster Volume would be preferred in
- `--topology-required`: A topology that the Cluster Volume must be accessible from
- `--type`: Cluster Volume access type (`mount`, `block`)

### Examples of docker volume create

Create a volume and then configure the container to use it:

```console
$ docker volume create hello

hello

$ docker run -d -v hello:/world busybox ls /world
```

The mount is created inside the container's `/world` directory. Docker doesn't
support relative paths for mount points inside the container.

Multiple containers can use the same volume. This is useful if two containers
need access to shared data. For example, if one container writes and the other
reads the data.

Volume names must be unique among drivers. This means you can't use the same
volume name with two different drivers. Attempting to create two volumes with
the same name results in an error:

```console
A volume named  "hello"  already exists with the "some-other" driver. Choose a different volume name.
```

If you specify a volume name already in use on the current driver, Docker
assumes you want to reuse the existing volume and doesn't return an error.

#### Driver-specific options (-o, --opt)

Some volume drivers may take options to customize the volume creation. Use the
`-o` or `--opt` flags to pass driver options:

```console
$ docker volume create --driver fake \
    --opt tardis=blue \
    --opt timey=wimey \
    foo
```

These options are passed directly to the volume driver. Options for
different volume drivers may do different things (or nothing at all).

The built-in `local` driver accepts no options on Windows. On Linux and with
Docker Desktop, the `local` driver accepts options similar to the Linux `mount`
command. You can provide multiple options by passing the `--opt` flag multiple
times. Some `mount` options (such as the `o` option) can take a comma-separated
list of options. Complete list of available mount options can be found
here.

For example, the following creates a `tmpfs` volume called `foo` with a size of
100 megabyte and `uid` of 1000.

```console
$ docker volume create --driver local \
    --opt type=tmpfs \
    --opt device=tmpfs \
    --opt o=size=100m,uid=1000 \
    foo
```

Another example that uses `btrfs`:

```console
$ docker volume create --driver local \
    --opt type=btrfs \
    --opt device=/dev/sda2 \
    foo
```

Another example that uses `nfs` to mount the `/path/to/dir` in `rw` mode from
`192.168.1.1`:

```console
$ docker volume create --driver local \
    --opt type=nfs \
    --opt o=addr=192.168.1.1,rw \
    --opt device=:/path/to/dir \
    foo
```

## docker network create

Create a network

Usage:

```console
docker network create [OPTIONS] NETWORK
```

### Description of docker network create

Creates a new network. The `DRIVER` accepts `bridge` or `overlay` which are the
built-in network drivers. If you have installed a third party or your own custom
network driver you can specify that `DRIVER` here also. If you don't specify the
`--driver` option, the command automatically creates a `bridge` network for you.
When you install Docker Engine it creates a `bridge` network automatically. This
network corresponds to the `docker0` bridge that Docker Engine has traditionally relied
on. When you launch a new container with  `docker run` it automatically connects to
this bridge network. You cannot remove this default bridge network, but you can
create new ones using the `network create` command.

```console
$ docker network create -d bridge my-bridge-network
```

Bridge networks are isolated networks on a single Docker Engine installation. If you
want to create a network that spans multiple Docker hosts each running Docker
Engine, you must enable Swarm mode, and create an `overlay` network. To read more
about overlay networks with Swarm mode, see "*use overlay networks*".

Once you have enabled swarm mode, you can create a swarm-scoped overlay network:

```console
$ docker network create --scope=swarm --attachable -d overlay my-multihost-network
```

By default, swarm-scoped networks do not allow manually started containers to
be attached. This restriction is added to prevent someone that has access to
a non-manager node in the swarm cluster from running a container that is able
to access the network stack of a swarm service.

The `--attachable` option used in the example above disables this restriction,
and allows for both swarm services and manually started containers to attach to
the overlay network.

Network names must be unique. The Docker daemon attempts to identify naming
conflicts but this is not guaranteed. It is the user's responsibility to avoid
name conflicts.

### Overlay network limitations

You should create overlay networks with `/24` blocks (the default), which limits
you to 256 IP addresses, when you create networks using the default VIP-based
endpoint-mode. This recommendation addresses
limitations with swarm mode. If you
need more than 256 IP addresses, do not increase the IP block size. You can
either use `dnsrr` endpoint mode with an external load balancer, or use multiple
smaller overlay networks. See
Configure service discovery
for more information about different endpoint modes.

### Options of docker network create

- `--attachable`: Enable manual container attachment
- `--aux-address`: Auxiliary IPv4 or IPv6 addresses used by Network driver
- `--config-from`: The network from which to copy the configuration
- `--config-only`: Create a configuration only network
- `--driver`, `-d`: Driver to manage the Network
- `--gateway`: IPv4 or IPv6 Gateway for the master subnet
- `--ingress`: Create swarm routing-mesh network
- `--internal`: Restrict external access to the network
- `--ip-range`: Allocate container ip from a sub-range
- `--ipam-driver`: IP Address Management Driver
- `--ipam-opt`: Set IPAM driver specific options
- `--ipv4`: Enable or disable IPv4 address assignment
- `--ipv6`: Enable or disable IPv6 address assignment
- `--label`: Set metadata on a network
- `--opt`, `-o`: Set driver specific options
- `--scope`: Control the network's scope
- `--subnet`: Subnet in CIDR format that represents a network segment

### Examples of docker network create

#### Connect containers

When you start a container, use the `--network` flag to connect it to a network.
This example adds the `busybox` container to the `mynet` network:

```console
$ docker run -itd --network=mynet busybox
```

If you want to add a container to a network after the container is already
running, use the `docker network connect` subcommand.

You can connect multiple containers to the same network. Once connected, the
containers can communicate using only another container's IP address or name.
For `overlay` networks or custom plugins that support multi-host connectivity,
containers connected to the same multi-host network but launched from different
daemons can also communicate in this way.

You can disconnect a container from a network using the `docker network
disconnect` command.

#### Specify advanced options

When you create a network, Docker Engine creates a non-overlapping subnetwork
for the network by default. This subnetwork is not a subdivision of an existing
network. It is purely for ip-addressing purposes. You can override this default
and specify subnetwork values directly using the `--subnet` option. On a
`bridge` network you can only create a single subnet:

```console
$ docker network create --driver=bridge --subnet=192.168.0.0/16 br0
```

Additionally, you also specify the `--gateway` `--ip-range` and `--aux-address`
options.

```console
$ docker network create \
  --driver=bridge \
  --subnet=172.28.0.0/16 \
  --ip-range=172.28.5.0/24 \
  --gateway=172.28.5.254 \
  br0
```

If you omit the `--gateway` flag, Docker Engine selects one for you from inside
a preferred pool. For `overlay` networks and for network driver plugins that
support it you can create multiple subnetworks. This example uses two `/25`
subnet mask to adhere to the current guidance of not having more than 256 IPs in
a single overlay network. Each of the subnetworks has 126 usable addresses.

```console
$ docker network create -d overlay \
  --subnet=192.168.10.0/25 \
  --subnet=192.168.20.0/25 \
  --gateway=192.168.10.100 \
  --gateway=192.168.20.100 \
  --aux-address="my-router=192.168.10.5" --aux-address="my-switch=192.168.10.6" \
  --aux-address="my-printer=192.168.20.5" --aux-address="my-nas=192.168.20.6" \
  my-multihost-network
```

Be sure that your subnetworks do not overlap. If they do, the network create
fails and Docker Engine returns an error.

#### Network internal mode (--internal)

Containers on an internal network may communicate between each other, but not
with any other network, as no default route is configured and firewall rules
are set up to drop all traffic to or from other networks. Communication with
the gateway IP  address (and thus appropriately configured host services) is
possible, and the host may communicate with any container IP directly.

By default, when you connect a container to an `overlay` network, Docker also
connects a bridge network to it to provide external connectivity. If you want
to create an externally isolated `overlay` network, you can specify the
`--internal` option.

#### Network ingress mode (--ingress)

You can create the network which will be used to provide the routing-mesh in the
swarm cluster. You do so by specifying `--ingress` when creating the network. Only
one ingress network can be created at the time. The network can be removed only
if no services depend on it. Any option available when creating an overlay network
is also available when creating the ingress network, besides the `--attachable` option.

```console
$ docker network create -d overlay \
  --subnet=10.11.0.0/16 \
  --ingress \
  --opt com.docker.network.driver.mtu=9216 \
  --opt encrypted=true \
  my-ingress-network
```

#### Run services on predefined networks

You can create services on the predefined Docker networks `bridge` and `host`.

```console
$ docker service create --name my-service \
  --network host \
  --replicas 2 \
  busybox top
```
