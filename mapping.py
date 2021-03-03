def get_customized_mapping(cls):
    return {
	"NAME_0": {
	    "type": "keyword"
	},
	"NAME_1": {
	    "type": "keyword"
	},
	"NAME_2": {
	    "type": "keyword"
	},
	"id": {
	    "type": "integer"
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
