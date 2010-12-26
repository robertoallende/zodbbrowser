$(function () {
	$("#tree").jstree({ 
		"json_data" : {
			"ajax" : { "url" : "tree",
                       "dataType" : "json"
                   },
            "error": this.onError,
            "success": this.onSuccess
		},
		"plugins" : [ "themes", "json_data" ]
	});
});

