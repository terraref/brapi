def calls_get(datatype=None, pageSize=None, page=None):
    response = {
        "metadata": {
            "datafiles": [],
            "pagination": {
                "currentPage": 0,
                "pageSize": 1000,
                "totalCount": 65,
                "totalPages": 1
            },
            "status": []
        },
        "result": {
            # "data": [
            #     {
            #         "call": "allelematrices",
            #         "datatypes": [
            #             "json"
            #         ],
            #         "methods": [
            #             "GET"
            #         ],
            #         "versions": [
            #             "1.0",
            #             "1.1",
            #             "1.2"
            #         ]
            #     },
            #     {
            #         "call": "allelematrices-search",
            #         "datatypes": [
            #             "json"
            #         ],
            #         "methods": [
            #             "GET",
            #             "POST"
            #         ],
            #         "versions": [
            #             "1.0",
            #             "1.1",
            #             "1.2"
            #         ]
            #     },
            #     {
            #         "call": "allelematrix-search",
            #         "datatypes": [
            #             "json"
            #         ],
            #         "methods": [
            #             "GET",
            #             "POST"
            #         ],
            #         "versions": [
            #             "1.0",
            #             "1.1",
            #             "1.2"
            #         ]
            #     },
            #     {
            #         "call": "attributes",
            #         "datatypes": [
            #             "json"
            #         ],
            #         "methods": [
            #             "GET"
            #         ],
            #         "versions": [
            #             "1.0",
            #             "1.1",
            #             "1.2"
            #         ]
            #     },
            #     {
            #         "call": "attributes/categories",
            #         "datatypes": [
            #             "json"
            #         ],
            #         "methods": [
            #             "GET"
            #         ],
            #         "versions": [
            #             "1.0",
            #             "1.1",
            #             "1.2"
            #         ]
            #     },
            #     {
            #         "call": "breedingmethods",
            #         "datatypes": [
            #             "json"
            #         ],
            #         "methods": [
            #             "GET"
            #         ],
            #         "versions": [
            #             "1.0",
            #             "1.1",
            #             "1.2"
            #         ]
            #     },
            #     {
            #         "call": "breedingmethods/{breedingMethodDbId}",
            #         "datatypes": [
            #             "json"
            #         ],
            #         "methods": [
            #             "GET"
            #         ],
            #         "versions": [
            #             "1.2"
            #         ]
            #     },
            #     {
            #         "call": "calls",
            #         "datatypes": [
            #             "json"
            #         ],
            #         "methods": [
            #             "GET"
            #         ],
            #         "versions": [
            #             "1.2"
            #         ]
            #     },
                {
                    "call": "commonCropNames",
                    "datatypes": [
                        "json"
                    ],
                    "methods": [
                        "GET"
                    ],
                    "versions": [
                        "1.2"
                    ]
                },
                {
                    "call": "crops",
                    "datatypes": [
                        "json"
                    ],
                    "methods": [
                        "GET"
                    ],
                    "versions": [
                        "1.0",
                        "1.1",
                        "1.2"
                    ]
                },
            #     {
            #         "call": "germplasm-search",
            #         "datatypes": [
            #             "json"
            #         ],
            #         "methods": [
            #             "GET",
            #             "POST"
            #         ],
            #         "versions": [
            #             "1.0",
            #             "1.1",
            #             "1.2"
            #         ]
            #     },
            #     {
            #         "call": "germplasm/{germplasmDbId}",
            #         "datatypes": [
            #             "json"
            #         ],
            #         "methods": [
            #             "GET"
            #         ],
            #         "versions": [
            #             "1.0",
            #             "1.1",
            #             "1.2"
            #         ]
            #     },
            #     {
            #         "call": "germplasm/{germplasmDbId}/attributes",
            #         "datatypes": [
            #             "json"
            #         ],
            #         "methods": [
            #             "GET"
            #         ],
            #         "versions": [
            #             "1.0",
            #             "1.1",
            #             "1.2"
            #         ]
            #     },
            #     {
            #         "call": "germplasm/{germplasmDbId}/markerprofiles",
            #         "datatypes": [
            #             "json"
            #         ],
            #         "methods": [
            #             "GET"
            #         ],
            #         "versions": [
            #             "1.0",
            #             "1.1",
            #             "1.2"
            #         ]
            #     },
            #     {
            #         "call": "germplasm/{germplasmDbId}/pedigree",
            #         "datatypes": [
            #             "json"
            #         ],
            #         "methods": [
            #             "GET"
            #         ],
            #         "versions": [
            #             "1.0",
            #             "1.1",
            #             "1.2"
            #         ]
            #     },
            #     {
            #         "call": "germplasm/{germplasmDbId}/progeny",
            #         "datatypes": [
            #             "json"
            #         ],
            #         "methods": [
            #             "GET"
            #         ],
            #         "versions": [
            #             "1.0",
            #             "1.1",
            #             "1.2"
            #         ]
            #     },
            #     {
            #         "call": "locations",
            #         "datatypes": [
            #             "json"
            #         ],
            #         "methods": [
            #             "GET"
            #         ],
            #         "versions": [
            #             "1.0",
            #             "1.1",
            #             "1.2"
            #         ]
            #     },
            #     {
            #         "call": "locations/{locationDbId}",
            #         "datatypes": [
            #             "json"
            #         ],
            #         "methods": [
            #             "GET"
            #         ],
            #         "versions": [
            #             "1.0",
            #             "1.1",
            #             "1.2"
            #         ]
            #     },
            #     {
            #         "call": "maps",
            #         "datatypes": [
            #             "json"
            #         ],
            #         "methods": [
            #             "GET"
            #         ],
            #         "versions": [
            #             "1.0",
            #             "1.1",
            #             "1.2"
            #         ]
            #     },
            #     {
            #         "call": "maps/{mapDbId}",
            #         "datatypes": [
            #             "json"
            #         ],
            #         "methods": [
            #             "GET"
            #         ],
            #         "versions": [
            #             "1.0",
            #             "1.1",
            #             "1.2"
            #         ]
            #     },
            #     {
            #         "call": "maps/{mapDbId}/positions",
            #         "datatypes": [
            #             "json"
            #         ],
            #         "methods": [
            #             "GET"
            #         ],
            #         "versions": [
            #             "1.0",
            #             "1.1",
            #             "1.2"
            #         ]
            #     },
            #     {
            #         "call": "maps/{mapDbId}/positions/{linkageGroupName}",
            #         "datatypes": [
            #             "json"
            #         ],
            #         "methods": [
            #             "GET"
            #         ],
            #         "versions": [
            #             "1.0",
            #             "1.1",
            #             "1.2"
            #         ]
            #     },
            #     {
            #         "call": "markerprofiles",
            #         "datatypes": [
            #             "json"
            #         ],
            #         "methods": [
            #             "GET"
            #         ],
            #         "versions": [
            #             "1.0",
            #             "1.1",
            #             "1.2"
            #         ]
            #     },
            #     {
            #         "call": "markerprofiles/{markerprofileDbId}",
            #         "datatypes": [
            #             "json"
            #         ],
            #         "methods": [
            #             "GET"
            #         ],
            #         "versions": [
            #             "1.0",
            #             "1.1",
            #             "1.2"
            #         ]
            #     },
            #     {
            #         "call": "markers",
            #         "datatypes": [
            #             "json"
            #         ],
            #         "methods": [
            #             "GET"
            #         ],
            #         "versions": [
            #             "1.0",
            #             "1.1",
            #             "1.2"
            #         ]
            #     },
            #     {
            #         "call": "markers-search",
            #         "datatypes": [
            #             "json"
            #         ],
            #         "methods": [
            #             "GET",
            #             "POST"
            #         ],
            #         "versions": [
            #             "1.0",
            #             "1.1",
            #             "1.2"
            #         ]
            #     },
            #     {
            #         "call": "markers/{markerDbId}",
            #         "datatypes": [
            #             "json"
            #         ],
            #         "methods": [
            #             "GET"
            #         ],
            #         "versions": [
            #             "1.0",
            #             "1.1",
            #             "1.2"
            #         ]
            #     },
            #     {
            #         "call": "observationLevels",
            #         "datatypes": [
            #             "json"
            #         ],
            #         "methods": [
            #             "GET"
            #         ],
            #         "versions": [
            #             "1.0",
            #             "1.1",
            #             "1.2"
            #         ]
            #     },
            #     {
            #         "call": "observationlevels",
            #         "datatypes": [
            #             "json"
            #         ],
            #         "methods": [
            #             "GET"
            #         ],
            #         "versions": [
            #             "1.0",
            #             "1.1",
            #             "1.2"
            #         ]
            #     },
            #     {
            #         "call": "ontologies",
            #         "datatypes": [
            #             "json"
            #         ],
            #         "methods": [
            #             "GET"
            #         ],
            #         "versions": [
            #             "1.0",
            #             "1.1",
            #             "1.2"
            #         ]
            #     },
            #     {
            #         "call": "phenotypes",
            #         "datatypes": [
            #             "json"
            #         ],
            #         "methods": [
            #             "POST"
            #         ],
            #         "versions": [
            #             "1.0",
            #             "1.1",
            #             "1.2"
            #         ]
            #     },
                {
                    "call": "phenotypes-search",
                    "datatypes": [
                        "json"
                    ],
                    "methods": [
                        "GET",
            #            "POST"
                    ],
                    "versions": [
                        "1.0",
                        "1.1",
                        "1.2"
                    ]
                },
            #     {
            #         "call": "phenotypes-search/csv",
            #         "datatypes": [
            #             "csv"
            #         ],
            #         "methods": [
            #             "POST"
            #         ],
            #         "versions": [
            #             "1.0",
            #             "1.1",
            #             "1.2"
            #         ]
            #     },
            #     {
            #         "call": "phenotypes-search/table",
            #         "datatypes": [
            #             "json"
            #         ],
            #         "methods": [
            #             "POST"
            #         ],
            #         "versions": [
            #             "1.0",
            #             "1.1",
            #             "1.2"
            #         ]
            #     },
            #     {
            #         "call": "phenotypes-search/tsv",
            #         "datatypes": [
            #             "tsv"
            #         ],
            #         "methods": [
            #             "POST"
            #         ],
            #         "versions": [
            #             "1.0",
            #             "1.1",
            #             "1.2"
            #         ]
            #     },
            #     {
            #         "call": "programs",
            #         "datatypes": [
            #             "json"
            #         ],
            #         "methods": [
            #             "GET"
            #         ],
            #         "versions": [
            #             "1.0",
            #             "1.1",
            #             "1.2"
            #         ]
            #     },
            #     {
            #         "call": "programs-search",
            #         "datatypes": [
            #             "json"
            #         ],
            #         "methods": [
            #             "POST"
            #         ],
            #         "versions": [
            #             "1.0",
            #             "1.1",
            #             "1.2"
            #         ]
            #     },
            #     {
            #         "call": "samples",
            #         "datatypes": [
            #             "json"
            #         ],
            #         "methods": [
            #             "PUT"
            #         ],
            #         "versions": [
            #             "1.0",
            #             "1.1",
            #             "1.2"
            #         ]
            #     },
            #     {
            #         "call": "samples-search",
            #         "datatypes": [
            #             "json"
            #         ],
            #         "methods": [
            #             "GET",
            #             "POST"
            #         ],
            #         "versions": [
            #             "1.0",
            #             "1.1",
            #             "1.2"
            #         ]
            #     },
            #     {
            #         "call": "samples/{sampleDbId}",
            #         "datatypes": [
            #             "json"
            #         ],
            #         "methods": [
            #             "GET"
            #         ],
            #         "versions": [
            #             "1.0",
            #             "1.1",
            #             "1.2"
            #         ]
            #     },
            #     {
            #         "call": "seasons",
            #         "datatypes": [
            #             "json"
            #         ],
            #         "methods": [
            #             "GET"
            #         ],
            #         "versions": [
            #             "1.0",
            #             "1.1",
            #             "1.2"
            #         ]
            #     },
            #     {
            #         "call": "studies-search",
            #         "datatypes": [
            #             "json"
            #         ],
            #         "methods": [
            #             "GET",
            #             "POST"
            #         ],
            #         "versions": [
            #             "1.0",
            #             "1.1",
            #             "1.2"
            #         ]
            #     },
            #     {
            #         "call": "studies/{studyDbId}",
            #         "datatypes": [
            #             "json"
            #         ],
            #         "methods": [
            #             "GET"
            #         ],
            #         "versions": [
            #             "1.0",
            #             "1.1",
            #             "1.2"
            #         ]
            #     },
            #     {
            #         "call": "studies/{studyDbId}/germplasm",
            #         "datatypes": [
            #             "json"
            #         ],
            #         "methods": [
            #             "GET"
            #         ],
            #         "versions": [
            #             "1.0",
            #             "1.1",
            #             "1.2"
            #         ]
            #     },
            #     {
            #         "call": "studies/{studyDbId}/layout",
            #         "datatypes": [
            #             "json"
            #         ],
            #         "methods": [
            #             "GET",
            #             "PUT"
            #         ],
            #         "versions": [
            #             "1.0",
            #             "1.1",
            #             "1.2"
            #         ]
            #     },
            #     {
            #         "call": "studies/{studyDbId}/observationVariables",
            #         "datatypes": [
            #             "json"
            #         ],
            #         "methods": [
            #             "GET"
            #         ],
            #         "versions": [
            #             "1.0",
            #             "1.1",
            #             "1.2"
            #         ]
            #     },
            #     {
            #         "call": "studies/{studyDbId}/observations",
            #         "datatypes": [
            #             "json"
            #         ],
            #         "methods": [
            #             "GET",
            #             "PUT"
            #         ],
            #         "versions": [
            #             "1.0",
            #             "1.1",
            #             "1.2"
            #         ]
            #     },
            #     {
            #         "call": "studies/{studyDbId}/observationunits",
            #         "datatypes": [
            #             "json"
            #         ],
            #         "methods": [
            #             "GET",
            #             "POST",
            #             "PUT"
            #         ],
            #         "versions": [
            #             "1.0",
            #             "1.1",
            #             "1.2"
            #         ]
            #     },
            #     {
            #         "call": "studies/{studyDbId}/observationunits/zip",
            #         "datatypes": [
            #             "json"
            #         ],
            #         "methods": [
            #             "POST"
            #         ],
            #         "versions": [
            #             "1.0",
            #             "1.1",
            #             "1.2"
            #         ]
            #     },
            #     {
            #         "call": "studies/{studyDbId}/observationvariables",
            #         "datatypes": [
            #             "json"
            #         ],
            #         "methods": [
            #             "GET"
            #         ],
            #         "versions": [
            #             "1.0",
            #             "1.1",
            #             "1.2"
            #         ]
            #     },
            #     {
            #         "call": "studies/{studyDbId}/table",
            #         "datatypes": [
            #             "json"
            #         ],
            #         "methods": [
            #             "GET",
            #             "POST"
            #         ],
            #         "versions": [
            #             "1.0",
            #             "1.1",
            #             "1.2"
            #         ]
            #     },
            #     {
            #         "call": "studyTypes",
            #         "datatypes": [
            #             "json"
            #         ],
            #         "methods": [
            #             "GET"
            #         ],
            #         "versions": [
            #             "1.0",
            #             "1.1",
            #             "1.2"
            #         ]
            #     },
            #     {
            #         "call": "studytypes",
            #         "datatypes": [
            #             "json"
            #         ],
            #         "methods": [
            #             "GET"
            #         ],
            #         "versions": [
            #             "1.0",
            #             "1.1",
            #             "1.2"
            #         ]
            #     },
            #     {
            #         "call": "traits",
            #         "datatypes": [
            #             "json"
            #         ],
            #         "methods": [
            #             "GET"
            #         ],
            #         "versions": [
            #             "1.0",
            #             "1.1",
            #             "1.2"
            #         ]
            #     },
            #     {
            #         "call": "traits/{traitDbId}",
            #         "datatypes": [
            #             "json"
            #         ],
            #         "methods": [
            #             "GET"
            #         ],
            #         "versions": [
            #             "1.0",
            #             "1.1",
            #             "1.2"
            #         ]
            #     },
            #     {
            #         "call": "trials",
            #         "datatypes": [
            #             "json"
            #         ],
            #         "methods": [
            #             "GET"
            #         ],
            #         "versions": [
            #             "1.0",
            #             "1.1",
            #             "1.2"
            #         ]
            #     },
            #     {
            #         "call": "trials/{trialDbId}",
            #         "datatypes": [
            #             "json"
            #         ],
            #         "methods": [
            #             "GET"
            #         ],
            #         "versions": [
            #             "1.0",
            #             "1.1",
            #             "1.2"
            #         ]
            #     },
            #     {
            #         "call": "variables",
            #         "datatypes": [
            #             "json"
            #         ],
            #         "methods": [
            #             "GET"
            #         ],
            #         "versions": [
            #             "1.0",
            #             "1.1",
            #             "1.2"
            #         ]
            #     },
            #     {
            #         "call": "variables-search",
            #         "datatypes": [
            #             "json"
            #         ],
            #         "methods": [
            #             "POST"
            #         ],
            #         "versions": [
            #             "1.0",
            #             "1.1",
            #             "1.2"
            #         ]
            #     },
            #     {
            #         "call": "variables/datatypes",
            #         "datatypes": [
            #             "json"
            #         ],
            #         "methods": [
            #             "GET"
            #         ],
            #         "versions": [
            #             "1.0",
            #             "1.1",
            #             "1.2"
            #         ]
            #     },
            #     {
            #         "call": "variables/{observationVariableDbId}",
            #         "datatypes": [
            #             "json"
            #         ],
            #         "methods": [
            #             "GET"
            #         ],
            #         "versions": [
            #             "1.0",
            #             "1.1",
            #             "1.2"
            #         ]
            #     },
            #     {
            #         "call": "vendor/plates",
            #         "datatypes": [
            #             "json"
            #         ],
            #         "methods": [
            #             "POST"
            #         ],
            #         "versions": [
            #             "1.0",
            #             "1.1",
            #             "1.2"
            #         ]
            #     },
            #     {
            #         "call": "vendor/plates-search",
            #         "datatypes": [
            #             "json"
            #         ],
            #         "methods": [
            #             "GET",
            #             "POST"
            #         ],
            #         "versions": [
            #             "1.0",
            #             "1.1",
            #             "1.2"
            #         ]
            #     },
            #     {
            #         "call": "vendor/plates/{vendorPlateDbId}",
            #         "datatypes": [
            #             "json"
            #         ],
            #         "methods": [
            #             "GET"
            #         ],
            #         "versions": [
            #             "1.0",
            #             "1.1",
            #             "1.2"
            #         ]
            #     },
            #     {
            #         "call": "vendor/specifications",
            #         "datatypes": [
            #             "json"
            #         ],
            #         "methods": [
            #             "GET"
            #         ],
            #         "versions": [
            #             "1.0",
            #             "1.1",
            #             "1.2"
            #         ]
            #     }
            # ]
        }
    }

    return response