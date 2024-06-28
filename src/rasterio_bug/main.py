from pathlib import Path
from rasterio.warp import transform_geom
import shapely
import rasterio
import shapely.geometry

DATA = Path(__file__).parent.parent.parent / "data"
TILE_ACROSS_ANTIMERIDIAN = DATA / "tile_across_antimeridian.tif"


def main():
    with rasterio.open(TILE_ACROSS_ANTIMERIDIAN) as dataset:
        crs = dataset.crs
        proj_bbox = dataset.bounds

    geom = shapely.geometry.box(*proj_bbox)
    print(f"CRS agnostic shape: {geom} \n")

    reprojected_shape = transform_geom(crs, "EPSG:4326", geom)
    print(f"Reprojected Shape: {reprojected_shape}")


if __name__ == "__main__":
    main()
