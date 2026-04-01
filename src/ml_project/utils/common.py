import os
from box.exceptions import BoxValueError
import yaml
from ml_project import logger
import json
import joblib
from ensure import ensure_annotations
from box import Box, ConfigBox
from pathlib import Path
from typing import Any



@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a yaml file and returns
    
    Args:
        path_to_yaml (str): Path like input
        
    Raises:
        ValueError: If the yaml file is empty
        e: empty yaml file error
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError(f"yaml file: {path_to_yaml} is empty")
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories: list[Path], verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories to be created
        ignore_log (bool, optional): ignore if multiple directories are created. Defaults to False.
    """
    
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")
            
            
@ensure_annotations
def save_json(path: Path, data: dict):
    """Saves json data

    Args:
        path (Path): path to the json file
        data (dict): data to be saved in json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"json file saved at: {path}")
    
    
@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """Loads a json files data

    Args:
        path (Path): path to the json file

    Returns:
        ConfigBox: data as class attributes instead of dictionary  
    """
    with open(path) as f:
        data = json.load(f)
    logger.info(f"json file loaded Successfully from: {path}")
    return ConfigBox(data)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """Saves binary data

    Args:
        data (Any): data to be saved in binary format
        path (Path): path to the binary file
    """
    joblib.dump(value = data, filename = path)
    logger.info(f"binary file saved at: {path}")
    

@ensure_annotations
def load_bin(path: Path) -> Any:
    """Loads binary data

    Args:
        path (Path): path to the binary file

    Returns:
        Any: data loaded from the binary file
    """
    data = joblib.load(filename = path)
    logger.info(f"binary file loaded successfully from: {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """Returns the size of a file in KB

    Args:
        path (Path): path to the file

    Returns:
        str: size of the file in KB
    """
    size_in_kb = round(os.path.getsize(path) / 1024, 2)
    return f"{size_in_kb} KB"