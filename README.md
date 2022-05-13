# tele2nies

# todo: 
* frontend stuff
* integration stuff
* backend to do: check if "dangerous item" close to edge, (other possible dangerous scenarios)

## hackfestBE API endpoints
* **URL: ** /get_labels/
* **Method: ** `GET`
* **Required Params: ** `image encoded in base64 format`
* **Sample Response: **  returns a json with code and features in the picture
```
{
    "code": 200,
    "data": {
        "Cat": {
            "bottom_left": [
                0.2858941853046417,
                0.17550413310527802
            ],
            "botton_right": [
                0.7382640838623047,
                0.17550413310527802
            ],
            "name": "Cat",
            "top_left": [
                0.2858941853046417,
                0.9805750250816345
            ],
            "top_right": [
                0.7382640838623047,
                0.9805750250816345
            ]
        },
        "Furniture": {
            "bottom_left": [
                0.8298903107643127,
                0.08395647257566452
            ],
            "botton_right": [
                0.9973958134651184,
                0.08395647257566452
            ],
            "name": "Furniture",
            "top_left": [
                0.8298903107643127,
                0.9858327507972717
            ],
            "top_right": [
                0.9973958134651184,
                0.9858327507972717
            ]
        }
    }
}
```

