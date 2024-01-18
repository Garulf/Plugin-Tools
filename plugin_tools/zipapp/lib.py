import sys
import subprocess
from pathlib import Path

import typer

from ..constants import LIB_DIR, REQUIREMENTS


# @app.command()
def lib(lib_path: Path = Path(LIB_DIR), requirements: Path = Path(REQUIREMENTS)):
    """
    Install external dependencies to lib directory for caching.
    """
    if Path(lib_path).exists():
        typer.echo(f'Lib path {lib_path} already exists. Using cached dependencies.')
        return
    subprocess.check_output((sys.executable, '-m', 'pip', 'install', '-r',
                             requirements, '-t', lib_path))
