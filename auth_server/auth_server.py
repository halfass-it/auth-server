from pathlib import Path
from dataclasses import dataclass

from utils.filesystem import CacheDir
from utils.logger import LoggerToFile
from auth_server.auth import Auth


@dataclass
class AuthServer:
  ip: str
  port: int
  buffer_size: int
  timeout: int
  cache_dir: Path = None

  def __post_init__(self) -> None:
    self.cache_dir: Path = self.cache_dir if self.cache_dir else CacheDir().path
    self.logger = LoggerToFile(cache_dir=self.cache_dir)
    self.auth = Auth()
