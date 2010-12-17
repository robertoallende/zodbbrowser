$(function () {
	$("#tree").jstree({ 
		"json_data" : {
			"ajax" : { "url" : "tree",
                        "dataType" : "json",
                     }
		},
		"plugins" : [ "themes", "json_data" ]
	});
});
