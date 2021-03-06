# BuildBetter by tele2nies
<p align="center">
  <img src='ui/fe/img/BuildBetter.png' width = '200px' height = '200px'>
</p>

# Project Overview:
Poor housing in developing countries can lead to severe consequences, and this is due to the lack of information regarding safe housekeeping. BuildBetter aims to help families in developing countries identify potential house hazards to create a safe, resilient and sustainable environment for them. By keeping them informed of dangerous hazards and allowing them to contact contracters to help them, our users will be equipped with the necessary knowledge on safe housekeeping, improving their health and well-being in the long run. We hope to address the following Sustainable Development Goals with our application.
<br>

<img src = 'https://sustainabledevelopment.un.org/content/sdgsummit/images/E_SDG%20goals_icons-individual-rgb-03.png' width = '120px' height = '120px'>
<img src = 'https://sustainabledevelopment.un.org/content/sdgsummit/images/E_SDG%20goals_icons-individual-rgb-07.png' width = '120px' height = '120px' >
<img src = 'https://sustainabledevelopment.un.org/content/sdgsummit/images/E_SDG%20goals_icons-individual-rgb-11.png' width = '120px' height = '120px'>

# What it does:
BuildBetter is a mobile application that uses Visual Object Recognition to “diagnose and fix” possible causes of injury at/around home. Users can identify potential hazards and  risks by simply scanning their house using their mobile device. Once the scan is completed, users will be notified of the risk level and can contact the relevant contracters for assistance. They are also able get an overview of their on-going jobs with contracters.
<br>
<img src = 'ui/fe/img/screen1.png'  width = '150px'>
<img src = 'ui/fe/img/screen2.png'  width = '150px'>
<img src = 'ui/fe/img/screen3.png' width = '150px'>
<img src = 'ui/fe/img/screen4.png' width = '150px'>
<img src = 'ui/fe/img/screen6.png'  width = '150px'>


# Technologies used:
* Firebase
  * Track analytics to find recurring incidents
* Google Meet
  * Set up calls with contractors for improvement consultations
* Cloud Vision API
    * Object recognition to identify problems

# Future Plans
We hope to implement the following in the future:
* Google Cloud Machine Learning
* Recommender
* Google Cloud IoT


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

