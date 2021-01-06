# <h1 align="center">auto theme changer for windows 10</h1>

> automatic theme changing from light mode to dark mode and vice versa based on system time

- only for **windows 10**(1909+) (tested on 1909)


changes the registry values by running reg.exe in windows as a subpprocess using the subprocess module.
registers the runner subcommand as a schedules task to run on an **hourly** basis.

stays light from 7:00 to 18:00 and goes dark in the remaining time.

subcommands set_system_theme and set_app_theme can be used directly by providing a "true" or "false" input as argument.

full help can be obtained by using the --help flag on any sub command or the command itself to reveal all the subcommands.

runner function is the main entry point per-se. the functions are the subcommands too and hence the runner function is the one that runs every hour to be exact.

## installation

#### using pip
```bash
python -m pip install --upgrade autothemewin10
```

#### manual installation
i used flit for this package to manage it's installation and publishing.
hence you need to get flit first
```
python -m pip install --upgrade flit
```

then git clone the repo and in the root of the folder do flit install after making the necessary changes.
