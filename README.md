# :globe_with_meridians: Unique Geohash :globe_with_meridians:

Your task is to transform the set of longitude, latitude coordinates provided in the `test_points.txt.gz` file
into corresponding [GeoHash](https://en.wikipedia.org/wiki/Geohash) codes.
For each pair of coordinates only the shortest geohash prefix that uniquely identifies this point must be stored.
For instance, this 3 points dataset will store these unique prefixes:

|latitude        | longitude       | geohash      | unique_prefix |
|----------------|-----------------|--------------|---------------|
|41.388828145321 | 2.1689976634898 | sp3e3qe7mkcb | sp3e3         |
|41.390743       | 2.138067        | sp3e2wuys9dr | sp3e2wuy      |
|41.390853       | 2.138177        | sp3e2wuzpnhr | sp3e2wuz      |

The solution must be coded in `Python` and you can use any public domain libraries.
It should work with any file respecting the same schema as the one provided.
The executable must output the solution on `stdout` in [CSV format](https://tools.ietf.org/html/rfc4180)
with 4 columns following the structure of the example, *ie*:

```csv
lat,lng,geohash,uniq
41.388828145321,2.1689976634898,sp3e3qe7mkcb,sp3e3
41.390743,2.138067,sp3e2wuys9dr,sp3e2wuy
41.390853,2.138177,sp3e2wuzpnhr,sp3e2wuz
```

## :nerd_face: We value in the solution

- Good software design
- Proper documentation
- Compliance to Python standards and modern usages (*eg.*: [PEP8](https://www.python.org/dev/peps/pep-0008/))
- Proper use of data structures
- Ergonomy of the command line interface
- Setup/Launch instructions if required
