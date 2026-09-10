import json
from pathlib import Path

if "__main__" == __name__:
    config_file = Path("./tools/workdir/config.json").resolve()
    data = json.loads(config_file.read_text())
    print(data.keys())