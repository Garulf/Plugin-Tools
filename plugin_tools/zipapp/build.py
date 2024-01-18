import shutil
from pathlib import Path

from ..constants import BUILD_DIR, LIB_DIR, SOURCE_DIR


def build(build_dir: Path = Path(BUILD_DIR), lib_path: Path = Path(LIB_DIR), source_path: Path = Path(SOURCE_DIR)):
    """
    Stages external dependencies with Python program.
    """
    pattern = shutil.ignore_patterns('__pycache__')
    if Path(build_dir).exists():
        shutil.rmtree(build_dir)
    shutil.copytree(source_path, build_dir, dirs_exist_ok=True, ignore=pattern)
    shutil.copytree(lib_path, build_dir, dirs_exist_ok=True)
