# from setuptools import setup, find_packages

# setup(name="models", packages=find_packages())
import sys
from pathlib import Path

sys.path.append(Path('modelsbase'))
from models import Account, Address, User
