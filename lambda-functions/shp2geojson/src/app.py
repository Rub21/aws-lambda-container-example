import os

from utils import convert_file


def handler(event, context):
    shapefile_zip_url = os.environ["SHAPEFILE_ZIP_URL"]
    s3_path = os.environ["S3_PATH"]
    country = os.environ["COUNTRY"]

    geojson_dict = convert_file.read_shapefile(shapefile_zip_url)
    geojson_file=f"{s3_path}/{country}.geojson"
    print(f"Geojson file:{geojson_file}")
    status = convert_file.save_json_files(geojson_dict, geojson_file)
    return {"statusCode": 200 if status else 500, "body":{"file":geojson_file}}


if __name__ == "__main__":
    handler(None, None)
