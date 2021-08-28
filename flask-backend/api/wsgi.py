import logging
import sys
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/opt/api/')
from app import create_app
application = create_app()
