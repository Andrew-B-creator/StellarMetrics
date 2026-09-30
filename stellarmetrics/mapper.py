import pandas as pd

HYG_convertor = {"id":"star_id",
"ra":"ra",
"dec":"dec",
"dist": "distance_parsec",
"mag": "apparent_magnitude",
"absmag": "absolute_magnitude",
"ci":"color_index"
}

GAIA_convertor = {"source_id":"star_id",
"ra":"ra",
"dec": "dec",
"parallax":"parallax_mas",
"parallax_error":"parallax_error_mas",
"phot_g_mean_mag":"apparent_magnitude",
"bp_rp":"color_index"
}

KEPLER_convertor = {"kepid": "star_id",
"ra":"ra",
"dec":"dec",
"teff": "temperature",
"radius":"radius"
}



MAPS = {"HYG" : HYG_convertor,
"GAIA" : GAIA_convertor,
"KEPLER" : KEPLER_convertor,
}


def unify_map_columns(df, map_name):
    mapping = MAPS.get(map_name.upper())
    if mapping is None:
        raise ValueError(f"Mapping for {map_name} not found")
    else:
        universal_df = df.rename(columns=mapping)
    return universal_df

