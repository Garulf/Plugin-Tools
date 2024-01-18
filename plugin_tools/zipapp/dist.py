import shutil
from pathlib import Path
import zipapp

from ..constants import DIST_DIR, BUILD_DIR, SOURCE_DIR
from ..manifest import PluginManifest
from ..utils import convert_name


def create_zipapp(build_dir: Path = Path(BUILD_DIR), dist_dir: Path = Path(DIST_DIR), source_dir: Path = Path(SOURCE_DIR)):
    manifest = PluginManifest.from_path(source_dir)
    slugified_name = convert_name(manifest.Name)
    target_path = Path(dist_dir).joinpath(slugified_name).with_suffix('.pyz')
    zipapp.create_archive(build_dir, target_path)


def dist(source_dir: Path = Path(SOURCE_DIR), dist_dir: Path = Path(DIST_DIR), build_dir: Path = Path(BUILD_DIR)):
    """
    Creates dist directory with zipapp.
    """
    if Path(dist_dir).exists():
        shutil.rmtree(dist_dir)
    pattern = shutil.ignore_patterns('*.py', '__pycache__')
    shutil.copytree(source_dir, dist_dir, dirs_exist_ok=True, ignore=pattern)

    create_zipapp(build_dir, dist_dir, source_dir)

    # remove empty directories from dist
    for directory in Path(dist_dir).iterdir():
        if directory.is_dir() and not any(directory.iterdir()):
            directory.rmdir()
