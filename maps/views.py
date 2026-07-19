from django.conf import settings

from django.http import JsonResponse

import requests


def reverse_geocode(request):

    lat = request.GET.get("lat")

    lon = request.GET.get("lon")


    if not lat or not lon:

        return JsonResponse(

            {
                "error":
                "Latitude and Longitude required."
            },

            status=400

        )


    url = (

        "https://nominatim.openstreetmap.org/reverse"

        f"?format=jsonv2&lat={lat}&lon={lon}"

    )


    try:

        response = requests.get(

            url,

            headers={

                "User-Agent":
                "Rydoo/1.0"

            },

            timeout=10

        )


        response.raise_for_status()


        data = response.json()


        return JsonResponse(
            data
        )


    except requests.RequestException as error:


        return JsonResponse(

            {

                "error":
                str(error)

            },

            status=500

        )


def route(request):

    start = request.GET.get(
        "start"
    )


    end = request.GET.get(
        "end"
    )


    if not start or not end:

        return JsonResponse(

            {

                "error":
                "start and end are required."

            },

            status=400

        )


    try:


        start_lon, start_lat = map(

            float,

            start.split(",")

        )


        end_lon, end_lat = map(

            float,

            end.split(",")

        )


    except (

        ValueError,

        TypeError

    ):


        return JsonResponse(

            {

                "error":
                "Invalid coordinates."

            },

            status=400

        )


    url = (

        "https://api.openrouteservice.org"

        "/v2/directions/driving-car"

    )


    headers = {

        "Authorization":
        settings.ORS_API_KEY,

        "Content-Type":
        "application/json"

    }


    body = {

        "coordinates":

        [

            [

                start_lon,

                start_lat

            ],

            [

                end_lon,

                end_lat

            ]

        ]

    }


    try:


        response = requests.post(

            url,

            headers=headers,

            json=body,

            timeout=20

        )


        data = response.json()


        print(
            "ORS STATUS:",
            response.status_code
        )


        print(
            "ORS RESPONSE:",
            data
        )


        if not response.ok:


            return JsonResponse(

                data,

                status=response.status_code

            )


        if "routes" not in data:


            return JsonResponse(

                {

                    "error":

                    {

                        "message":
                        "No driving route found."

                    },

                    "ors_response":
                    data

                },

                status=400

            )


        return JsonResponse(
            data
        )


    except requests.RequestException as error:


        return JsonResponse(

            {

                "error":

                {

                    "message":
                    str(error)

                }

            },

            status=500

        )