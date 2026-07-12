# typer cookiecutter template

Cookiecutter template for creating new [Typer](https://typer.tiangolo.com/)
command-line tools.

## Installation

You need to have [cookiecutter](https://cookiecutter.readthedocs.io/) installed.
You can use [uv](https://docs.astral.sh/uv/) (if you have it and you should) for
this:

```bash
uv tool run cookiecutter
```

You can fallback to regular `pip` if you prefer.

It is highly recommended to use `mise` to ease tool management. Follow the
[install documentation](https://mise.jdx.dev/getting-started.html).

## Usage

Run `cookiecutter gh:bedecarroll/typer-app` and then answer the prompts. Here's
an example run:

```bash
$ cookiecutter gh:bedecarroll/typer-app
name []: click app template demo
description []: Demonstration
author []: Bede Carroll
```

This will create a directory called `click-app-template-demo` based on the name
you provided. The name will be automatically converted to dashes and underscores
as needed.

## Developing your command-line tool

If your tool is called `my-new-tool`, you can start working on it as per this example:

```bash
cd my-new-tool
# Trust the folder for mise
mise trust
# The venv should be created for you, check like so
which python
# Confirm your tool can be run from the command-line
my-new-tool version
```

You should see the following:

```bash
0.0.1
```

You can run the default test for your tool like so:

```bash
mise test
```

This will execute the test in the `tests` folder.

Now you can open the `src/my_new_tool/main.py` file and start adding commands
as per the examples.

## Creating a Git repository for your tool

You can initialize a Git repository for your tool like this:

```bash
cd my-new-tool
git init
git add .
git commit -m "Initial structure from template"
```

## Reference links

- Inspiration is Simon Willison's [Click cookiecutter template](https://github.com/simonw/click-app)
- [Typer](https://typer.tiangolo.com/)
- [UV](https://docs.astral.sh/uv/)
- [Loguru](https://github.com/Delgan/loguru)
- [Icecream](https://github.com/gruns/icecream)
- [Rich](https://github.com/Textualize/rich)
- [Mise](https://mise.jdx.dev/)
- [12 Factor CLI Apps](https://medium.com/@jdxcode/12-factor-cli-apps-dd3c227a0e46)
