from utils.filesystem import CacheDir
from auth_server.auth import Auth


class AuthServer:
  def __init__(self) -> None:
    self.cache_dir = CacheDir()
    self.auth = Auth()
