# {{ cookiecutter.slug }}

{{ cookiecutter.description }}

## Installation

Install this tool using `mise` task:

```bash
mise pkg-install
```

## Usage

For help, run:

```bash
{{ cookiecutter.slug }} --help
```

## Development

To contribute to this tool, first checkout the code. If you have `mise`
installed once you `cd` into the repo `mise` should have automatically created
the `venv` and activated it for you.

Alternatively you can manually create the `venv` using `uv`.

```bash
cd {{ cookiecutter.slug }}
uv venv
source .venv/bin/activate
```

To run the tests:

```bash
mise test
```

To lint and fix lint errors where possible:

```bash
mise lint
mise lint-fix
```

## NixOS note

Be aware that if your `NixOS` python version is behind the latest patch `mise`
will try and run the latest patch versus what is in your system. To fix this
you will either need to change `.python-version` to be that specific version
or run `mise install` and let it fail.
