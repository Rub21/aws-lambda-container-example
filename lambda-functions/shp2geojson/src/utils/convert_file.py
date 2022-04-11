import os
import geopandas
from smart_open import open


def read_shapefile(zip_file: str):
    """Read zip file and return as geojson file

    Args:
        zip_file (str): Shapefile as zip file

    Returns:
        dict: geojson file
    """
    gdf = geopandas.read_file(zip_file)
    geojson_dict = gdf.to_json()
    return geojson_dict


def save_json_files(json_obj: dict, s3_path: str):
    try:
        with open(s3_path, "w") as out_geo:
            out_geo.write(json_obj)
        return True
    except:
        print("No s3 bucket access...")
        return False




