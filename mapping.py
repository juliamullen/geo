def get_customized_mapping(cls):
    return {
	    "country": {
		"type": "keyword"
	    },
	    "country_id": {
		"type": "keyword"
	    },
	    "division": {
		"type": "keyword"
	    },
	    "division_id": {
		"type": "integer"
	    },
	    "location": {
		"type": "keyword"
	    },
	    "location_id": {
		"type": "keyword"
	    },
	    "id": {
		"type": "keyword"
	    },
	    "type": {
		"type": "keyword"
	    },
	    "geometry": {
		"properties": {
		    "type": {
			"normalizer": "keyword_lowercase_normalizer",
			"type": "keyword"
		    },
		    "coordinates": {
			"type": "float"
		    },
		}
	    }
	}
